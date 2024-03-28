import asyncio
import os
import base64
from msgraph_beta.generated.models.o_data_errors.o_data_error import ODataError
from dcgraph import Graph
import plistlib
import argparse
import json

import xml.etree.ElementTree as ET

import devicecontrol as dc

class Package:

    class IntuneSetting:

        def __init__(self,dc_setting,name = None,description = None):
            self.setting = dc_setting
            self.name = name
            self.description = description
            pass
        

    class Policy:

        WINDOWS_OS = "Windows"
        MAC_OS = "MacOS"

        def __init__(self):
            self.name = "A Windows Policy"
            self.description = "A default description for the policy"
            self.rules = []
            self.groups = []
            self.settings = []
            self.os = self.WINDOWS_OS
            self.id = None
            self.assignments = {}

        def setAssignments(self,assignments):
            print(assignments)

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




    def __init__(self):
        self.policies = []

    def addPolicy(self,policy):
        self.policies.append(policy)

    def save(self,destination):
        print(destination)

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
   

    parser_import = subparsers.add_parser('import', help='export help')
    parser_import.add_argument("command",action="store_const",const="import")
    
    args = arg_parser.parse_args()

    graph: Graph = Graph(args.tenantId,args.clientId)

    await greet_user(graph)

    
    
    try:
        if args.command == "export":
            await export(graph,args.dest)
            
    except ODataError as odata_error:
        print('Error:')
        if odata_error.error:
            print(odata_error.error.code, odata_error.error.message)



async def greet_user(graph: Graph):
    user = await graph.get_user()
    if user:
        print('Hello,', user.display_name)
        # For Work/school accounts, email is in mail property
        # Personal accounts, email is in userPrincipalName
        print('Email:', user.mail or user.user_principal_name, '\n')

async def display_access_token(graph: Graph):
    token = await graph.get_user_token()
    print('User token:', token, '\n')

async def export(graph: Graph, destination):

    package = Package()

    configs = await graph.export_device_configurations()
    for device_config in configs.value:
        if device_config.odata_type == "#microsoft.graph.macOSCustomConfiguration":
            payload_bytes = device_config.payload
            payload = base64.b64decode(payload_bytes)
            plist = plistlib.loads(payload,fmt=plistlib.FMT_XML)
            if 'deviceControl' in plist['PayloadContent'][0]:

                policy = Package.Policy()

                id = device_config.id

                package.addPolicy(policy)
                policy.os = policy.MAC_OS
                policy.id = id

                deviceControl = plist['PayloadContent'][0]['deviceControl']
                
                policy.setPayload(deviceControl['policy'])

                assignments = await graph.get_assignments(id)

                policy.setAssignments(assignments)

        if device_config.odata_type == "#microsoft.graph.windows10CustomConfiguration":
            
            policy = Package.Policy()

            id = device_config.id

            package.addPolicy(policy)
            policy.id = id

            
            assignments = await graph.get_assignments(id)

            policy.setAssignments(assignments)


            for oma_setting in device_config.oma_settings:
                
                name = oma_setting.display_name
                description = oma_setting.description
                oma_uri = oma_setting.oma_uri

                
                if oma_setting.odata_type == "#microsoft.graph.omaSettingStringXml":
                    secret_reference_value_id = oma_setting.secret_reference_value_id
                    xml = await graph.get_xml(id,secret_reference_value_id)
                    root = ET.fromstring(xml.value)   
                    if root.tag == "PolicyRule":
                        rule = dc.PolicyRule(root,dc.Format.OMA_URI)
                        policy.addRule(rule)
                    elif root.tag == "Group":
                        group = dc.Group(root,dc.Format.OMA_URI)
                        policy.addGroup(group)
            
                else:
                    dc_setting_name = dc.Setting.getSettingNameFor(oma_uri)
                    if dc_setting_name is not None:
                        setting_value = oma_setting.value
                        dc_setting = dc.Setting(dc_setting_name,setting_value,description)
                        policy.addSetting(Package.IntuneSetting(dc_setting),name,description)

    package.save(destination)


# Run main
asyncio.run(main())