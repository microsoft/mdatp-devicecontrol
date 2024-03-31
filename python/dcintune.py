import asyncio
import os
import base64
import jinja2
from msgraph_beta.generated.models.o_data_errors.o_data_error import ODataError
from dcgraph import Graph
import plistlib
import argparse
import json
import pathlib
import yaml

import xml.etree.ElementTree as ET

import devicecontrol as dc
from dcdoc import Inventory, Description


class DeviceControlPolicyTemplate:

    async def getTemplate(graph):
        template = DeviceControlPolicyTemplate()
        await template.load_data(graph)
        return template

    def __init__(self):
        self.dc_setting_instance_templates = {}
    
    async def load_data(self,graph):

        #configuration_settings = await graph.get_configuration_settings()

        dc_policy_template = await graph.get_device_control_policy_template()
        dc_policy_template_id = dc_policy_template.value[0].id

        dc_policy_template_settings_instance_templates = await graph.get_configuration_policy_settings_templates_by_id(dc_policy_template_id)
        

        #create a map of the settings in the device control template by their id
        for dc_policy_template_setting_instance_template in dc_policy_template_settings_instance_templates.value:
            setting_instance_template = dc_policy_template_setting_instance_template.setting_instance_template
            details = await graph.get_configuration_settings_for_definition(setting_instance_template.setting_definition_id)
            self.dc_setting_instance_templates[setting_instance_template.setting_definition_id] = details



    def get_value(self,setting):
        setting_instance = setting.setting_instance
        setting_definition_id = setting_instance.setting_definition_id

        setting_instance_template = self.dc_setting_instance_templates[setting_definition_id]
            
        if setting_instance.odata_type == "#microsoft.graph.deviceManagementConfigurationChoiceSettingInstance":
            return self.get_choice_value(setting_instance,setting_instance_template)
        else:
            print(setting_instance.odata_type)

    def get_choice_value(self,setting_instance,setting_instance_template):
        
        
        print("choice_value > setting_instance > setting_definition_id="+setting_instance.setting_definition_id)
        choice_setting_value = setting_instance.choice_setting_value
        print("choice_value > setting_instance > choice_setting_value="+choice_setting_value.odata_type)

        if choice_setting_value.odata_type == "#microsoft.graph.deviceManagementConfigurationChoiceSettingValue":
            print("choice_value > setting_instance > choice_setting_value > value ="+choice_setting_value.value)
            for child in choice_setting_value.children:
                value = None
                
                if child.odata_type == "#microsoft.graph.deviceManagementConfigurationSimpleSettingCollectionInstance":
                    value = self.get_simple_setting_collection_value(child,setting_instance_template)
                elif child.odata_type == "#microsoft.graph.deviceManagementConfigurationChoiceSettingInstance":
                    value = self.get_choice_setting_value(child,setting_instance_template)
                else:
                    print("choice_value > setting_instance > choice_setting_value > child > odata_type="+child.odata_type)


    def get_simple_setting_collection_value(self,simple_setting_collection_instance,template):
        print(simple_setting_collection_instance)
        collection = []
        for value in simple_setting_collection_instance.simple_setting_collection_value:
            if value.odata_type == "#microsoft.graph.deviceManagementConfigurationStringSettingValue":
                collection.append(str(value.value))
            else:
                print(value.odata_type)

        return collection


    def get_choice_setting_value(self,choice_setting_instance,template):
        value = choice_setting_instance.choice_setting_value.value

        setting_value = None
        options = template.options
        for option in options:
            if option.item_id == value:
                setting_value = option

        return setting_value
                    



        

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

    MAC_DEVICE_CONTROL = "macOS.devicecontrol"
    MAC_DEVICE_CONTROL_POLICIES = "macOS.devicecontrol.policies"

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

        def getMacOSSettings(self):

            settings_dict = {}
            if self.os == Package.Policy.MAC_OS:
                for setting in self.settings:
                    dc_setting = setting.setting

                    mac_settings_data = dc_setting.data[dc_setting.name]["mac"]["mac_setting"]
                    
                    category = mac_settings_data["category"]

                    settings_for_category = {}

                    if category in settings_dict.keys():
                        settings_for_category = settings_dict[category]

                    if "name" in mac_settings_data:
                        setting_name = mac_settings_data["name"]
                        settings_for_category[setting_name] = dc_setting.value
                    else:    
                        settings_for_category = dc_setting.value

                    settings_dict[category] = settings_for_category

            return settings_dict
        
        def getPolicyJSON(self):

            json = {}

            if self.os == Package.Policy.MAC_OS:
                json["groups"] = self.groups
                json["rules"] = self.rules
                json["settings"] = self.getMacOSSettings()

            return json


    def __init__(self,name,templateEnv=None):

        self.name = name
        self.policies = []
        self.templateEnv = templateEnv
        if templateEnv is None:
            templateLoader = jinja2.FileSystemLoader("templates")
            self.templateEnv = jinja2.Environment(loader=templateLoader)


        


    def addPolicy(self,policy):
        self.policies.append(policy)

    def save(self,destination,rule_template_name,readme_template_name,description_template_name):

        
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

        mac_policy_file_paths = []
        windows_policy_file_paths = []

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

                mac_policy_file_paths.append(policy_file_path)


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

                    windows_policy_file_paths.append(rule_file_path)

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

        #load_templates
        rule_template = self.templateEnv.get_template(rule_template_name)
        readme_template = self.templateEnv.get_template(readme_template_name)
        description_template = self.templateEnv.get_template(description_template_name)


        #generate documentation for mac
        mac_src_paths = [str(path_map[Package.MAC_DEVICE_CONTROL_POLICIES])]
        mac_dest_paths = str(path_map[Package.MAC_DEVICE_CONTROL])
        
        mac_inventory = Inventory(mac_src_paths,None,mac_dest_paths)
        mac_inventory.load_inventory()

        for mac_policy_file_path in mac_policy_file_paths:

            mac_policy_file_name = str(mac_policy_file_path).split(os.sep)[-1]

            query = "path.str.contains('"+str(mac_policy_file_name)+"',regex=False)"
            title = mac_policy_file_name.split(".")[0]
            outfile = title+".md"

            result = mac_inventory.process_query(query)

            result["description"] = Description(result,self.templateEnv,description_template_name)

            with open(mac_policy_file_path,"r") as json_file:
                mac_policy = json.loads(json_file.read())
                mac_settings = dc.Settings.generate_settings_from_mac_policy(mac_policy)
            
            json_file.close()
            

            mac_inventory.generate_text(result,rule_template,str(path_map[Package.MAC_DEVICE_CONTROL]),outfile,title,mac_settings)
            
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
    
def path_array(path):
    paths = []
    path_strs = str.split(path,os.pathsep)
    for path_str in path_strs:
        
        path = pathlib.Path(path_str)
        if path.is_absolute():
            paths.append(path)
        else:
            parent_path = pathlib.Path(__file__ ).parent.resolve() 
            path = pathlib.Path(str(parent_path)+ os.sep + path_str).resolve()
            paths.append(path)

    return paths


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
    parser_export.add_argument('-t','--template',dest="template",help="Jinja2 template to use to generate output.  Defaults to dcutil.j2.",default="dcutil.j2")
    parser_export.add_argument('-rt','--readme_template',dest="readme_template",help="Jinja2 template to use for the readme.  Defaults to readme.j2.",default="readme.j2")
    parser_export.add_argument('-dt','--description_template',dest="description_template",help="Jinja2 template to use for the description.  Defaults to description.j2.",default="description.j2")
    parser_export.add_argument('-r','--readme',dest="readme_file",help="The readme file to generate.  Defaults to readme.md.",default="readme.md")
    parser_export.add_argument('-tp','--templates_path',dest="templates_path",help="path to Jinja2 templates.  Defaults to templates.",default="templates",type=path_array)
    
   

    parser_import = subparsers.add_parser('import', help='export help')
    parser_import.add_argument("command",action="store_const",const="import")
    


    args = arg_parser.parse_args()

    graph: Graph = Graph(args.tenantId,args.clientId)

    try:
        if args.command == "export":

            templateLoader = jinja2.FileSystemLoader(searchpath=args.templates_path)
            templateEnv = jinja2.Environment(loader=templateLoader)

            
            await export(graph,args.dest,args.package_name,
                         templateEnv,
                         args.template,
                         args.readme_template,
                         args.description_template)
            
    except ODataError as odata_error:
        print('Error:')
        if odata_error.error:
            print(odata_error.error.code, odata_error.error.message)




async def export(graph: Graph, destination,name, 
                 templateEnv, 
                 rule_template="dcutil.j2",
                 readme_template="readme.j2",
                 description_template="description.j2"):

    package = Package(name,templateEnv)

    dc_policy_template = await DeviceControlPolicyTemplate.getTemplate(graph)

    #get the device control configuration policies
    dc_policies = await graph.get_device_control_policies()
    for dc_policy in dc_policies.value:

        id = dc_policy.id

        settings = await graph.get_device_control_policy_settings(id)

        for setting in settings.value:

            settings_value = dc_policy_template.get_value(setting)


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


    

    package.save(destination,rule_template,readme_template,description_template)


# Run main
asyncio.run(main())