import asyncio
import os
import base64
from msgraph_beta.generated.models.o_data_errors.o_data_error import ODataError
from dcgraph import Graph
import plistlib
import argparse
import json
import pathlib
import yaml

import xml.etree.ElementTree as ET

import devicecontrol as dc


class Package:

    layout = [
        "macOS",
        "macOS.devicecontrol",
        "macOS.devicecontrol.policies",
        "windows",
        "windows.devicecontrol",
        "windows.devicecontrol.groups",
        "windows.devicecontrol.rules"
    ]

    MAC_PATH = "macOS.devicecontrol.policies"
    WINDOWS_GROUPS_PATH = "windows.devicecontrol.groups"
    WINDOWS_RULES_PATH = "windows.devicecontrol.rules"

    class IntuneSetting:

        def __init__(self,dc_setting,name = None,description = None):
            self.setting = dc_setting
            self.name = name
            self.description = description
            pass
        
    class IntuneAssignment:

        class TargetGroup:

            def __init__(self,group):

                self.name = group.display_name
                self.id = group.id
                self.odata_type = group.odata_type
                self.security_enabled = group.security_enabled
                self.security_identifier = group.security_identifier


            def toJSON(self):

                return {
                    "name": self.name,
                    "id": self.id
                }
                


        def __init__(self,assignments):

            self.data = {
                "include":[],
                "exclude":[]
            }

            for assignment in assignments.value:

                target = assignment.target
                target_type = target.odata_type

                print(target_type)

                if target_type == "#microsoft.graph.allDevicesAssignmentTarget":
                    self.data["include"].append("all machines")
                elif target_type == "#microsoft.graph.allLicensedUsersAssignmentTarget":
                    self.data["include"].append("all users")
                elif target_type == "#microsoft.graph.exclusionGroupAssignmentTarget":
                    excluded_group_id = target.group_id
                    self.data["exclude"].append(excluded_group_id)
                elif target_type == "#microsoft.graph.groupAssignmentTarget":
                    included_group_id = target.group_id
                    self.data["include"].append(included_group_id)

            
    class Policy:

        WINDOWS_OS = "Windows"
        MAC_OS = "MacOS"

        def __init__(self, graph):
            self.name = "A Windows Policy"
            self.description = "A default description for the policy"
            self.rules = []
            self.groups = []
            self.settings = []
            self.os = self.WINDOWS_OS
            self.id = None
            self.assignments = {}

            self.graph = graph

        async def setAssignments(self,assignments):

            intune_assignment = Package.IntuneAssignment(assignments)

            target_types = ["include","exclude"]
            for target_type in target_types:
                targets = intune_assignment.data[target_type]
                index = 0
                for target in targets:
                    if not str(target).startswith("all"):
                        group = await self.graph.get_group_by_id(target)
                        intune_assignment.data[target_type][index] = \
                            Package.IntuneAssignment.TargetGroup(group).toJSON()
                    index=index+1
 
            self.assignments = intune_assignment.data

        def addGroup(self,group):
            self.groups.append(group)

        def addRule(self,rule):
            self.rules.append(rule)

        def addSetting(self,setting):
            self.settings.append(setting)

        def setPayload(self,payload):
            if self.os == self.MAC_OS:
                mac_policy = json.loads(payload)

                if "groups" in mac_policy.keys():
                    for group in mac_policy["groups"]:
                        self.groups.append(dc.Group(group,"mac"))

                if "rules" in mac_policy.keys():
                    for rule in mac_policy["rules"]:
                        self.rules.append(dc.PolicyRule(rule,"mac"))

                
                dc_settings = dc.Settings.generate_settings_from_mac_policy(mac_policy)
                for dc_setting in dc_settings:
                    self.settings.append(Package.IntuneSetting(dc_setting))

        def getPolicyJSON(self):

            json = {}

            if self.os == Package.Policy.MAC_OS:
                json["groups"] = self.groups
                json["rules"] = self.rules

            return json


    def __init__(self,name):
        self.name = name
        self.policies = []



    def addPolicy(self,policy):
        self.policies.append(policy)

    def save(self,destination):

        package_path = pathlib.PurePath(os.path.join(destination,self.name))
        if not os.path.isdir(package_path):
            os.mkdir(package_path)

        path_map = {}

        for layout_path in Package.layout:
            orig_path = str(layout_path)

            layout_path = layout_path.replace(".",os.sep)
            layout_path = pathlib.PurePath(os.path.join(package_path,layout_path)) 
            if not os.path.isdir(layout_path):
                os.mkdir(layout_path)

            path_map[orig_path] = layout_path

        policy_data = {}

        for policy in self.policies:
            name = policy.name
            if policy.os == Package.Policy.MAC_OS:
                policy_json = policy.getPolicyJSON()

                policy_file_path = pathlib.PurePath(os.path.join(path_map[Package.MAC_PATH],name+".json"))
                policy_file = open(policy_file_path,"w")
                json.dump(policy_json,policy_file,cls=dc.DCJSONEncoder,indent=5)
                policy_file.close()

                policy_data[name] = {
                    "os":"mac",
                    "description": policy.description,
                    "assignments": policy.assignments
                }

            elif policy.os == Package.Policy.WINDOWS_OS:

                groups_data = {}
                rules_data = {}
                settings_data = {}

                for group in policy.groups:
                    group_file_path = pathlib.PurePath(os.path.join(path_map[Package.WINDOWS_GROUPS_PATH],group.name+".xml"))
                    group_file = open(group_file_path,"w")
                    group_file.write(str(group))
                    group_file.close()

                    groups_data [group.name] = {
                        "groupId":group.id,
                        "description": group.description
                    }

                for rule in policy.rules:
                    rule_file_path = pathlib.PurePath(os.path.join(path_map[Package.WINDOWS_RULES_PATH],group.name+".xml"))
                    rule_file = open(rule_file_path,"w")
                    rule_file.write(str(group))
                    rule_file.close()

                    rules_data [rule.name] = {
                        "ruleId":rule.id,
                        "description": rule.description
                    }

                for setting in policy.settings:

                    dc_setting = setting.setting

                    settings_data[dc_setting.name] = {
                        "value" : dc_setting.value,
                        "name": setting.name,
                        "description": setting.description
                    }

                policy_data[name] = {
                    "os":"Windows",
                    "description": policy.description,
                    "assignments": policy.assignments,
                    "groups": groups_data,
                    "rules": rules_data,
                    "settings": settings_data
                }



        package_file_path = pathlib.PurePath(os.path.join(package_path,"package.yaml"))
        package_file = open(package_file_path,"w")    

        package_data = {
            "policies":policy_data
        }

        yaml.dump(package_data,package_file)
        package_file.close()

        
        


def client_id_type(value):
    return value

def tenant_id_type(value):
    return value

def dir_type(path):
    if os.path.isdir(path):
        return path
    else:
        raise NotADirectoryError(path)
    



async def main():
    
    arg_parser = argparse.ArgumentParser(
    description='Utility for importing and exporting device control settings to/from Intune.')

    arg_parser.add_argument('-t', '--tenantId', type=tenant_id_type, dest="tenantId", help='tenantId for the tenant',required=True)
    arg_parser.add_argument('-c', '--clientId', type=client_id_type, dest="clientId", help='clientId of the application',required=True)
 
    subparsers = arg_parser.add_subparsers(help='sub-command help')
    parser_export = subparsers.add_parser('export', help='export help')
    parser_export.add_argument("command",action="store_const",const="export")
    parser_export.add_argument('-d','--dest',dest="dest",type=dir_type,help="The output directory.  Defaults to current working directory.",default=".")
    parser_export.add_argument('-n','--name',dest="package_name",help="The name of the package")
    
   

    parser_import = subparsers.add_parser('import', help='export help')
    parser_import.add_argument("command",action="store_const",const="import")
    
    args = arg_parser.parse_args()

    graph: Graph = Graph(args.tenantId,args.clientId)

    try:
        if args.command == "export":
            await export(graph,args.dest,args.package_name)
            
    except ODataError as odata_error:
        print('Error:')
        if odata_error.error:
            print(odata_error.error.code, odata_error.error.message)




async def export(graph: Graph, destination,name):

    package = Package(name)

    configs = await graph.export_device_configurations()
    for device_config in configs.value:
        if device_config.odata_type == "#microsoft.graph.macOSCustomConfiguration":
            payload_bytes = device_config.payload
            payload = base64.b64decode(payload_bytes)
            plist = plistlib.loads(payload,fmt=plistlib.FMT_XML)
            if 'deviceControl' in plist['PayloadContent'][0]:

                policy = Package.Policy(graph)

                id = device_config.id

                package.addPolicy(policy)
                policy.os = policy.MAC_OS
                policy.id = id
                policy.name = device_config.display_name
                policy.description = device_config.description

                deviceControl = plist['PayloadContent'][0]['deviceControl']
                
                policy.setPayload(deviceControl['policy'])

                assignments = await graph.get_assignments(id)

                await policy.setAssignments(assignments)

        if device_config.odata_type == "#microsoft.graph.windows10CustomConfiguration":
            
            policy = Package.Policy(graph)

            id = device_config.id

            package.addPolicy(policy)
            policy.id = id
            policy.name = device_config.display_name
            policy.description = device_config.description

            
            assignments = await graph.get_assignments(id)

            await policy.setAssignments(assignments)


            for oma_setting in device_config.oma_settings:
                
                name = oma_setting.display_name
                description = oma_setting.description
                oma_uri = oma_setting.oma_uri

                
                if oma_setting.odata_type == "#microsoft.graph.omaSettingStringXml":
                    secret_reference_value_id = oma_setting.secret_reference_value_id
                    xml = await graph.get_xml(id,secret_reference_value_id)
                    root = ET.fromstring(xml.value)

                    #file name without .xml
                    name = str(oma_setting.file_name).split(".")[0]
                    if root.tag == "PolicyRule":
                        rule = dc.PolicyRule(root,dc.Format.OMA_URI)
                        policy.addRule(rule)
                        policy.name = name
                        policy.description = oma_setting.description
                    elif root.tag == "Group":
                        group = dc.Group(root,dc.Format.OMA_URI)
                        policy.addGroup(group)
                        group.name = name
                        group.description = oma_setting.description
            
                else:
                    dc_setting_name = dc.Setting.getSettingNameFor(oma_uri)
                    if dc_setting_name is not None:
                        setting_value = oma_setting.value
                        dc_setting = dc.Setting(dc_setting_name,setting_value)
                        intune_settings = Package.IntuneSetting(dc_setting,oma_setting.display_name,oma_setting.description)
                        policy.addSetting(intune_settings)

    package.save(destination)


# Run main
asyncio.run(main())