import asyncio
import configparser
import os
import base64
from msgraph_beta.generated.models.o_data_errors.o_data_error import ODataError
from dcgraph import Graph
import plistlib
import argparse

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
            await export(graph)
            
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

async def export(graph: Graph):
    configs = await graph.export_device_configurations()
    for device_config in configs.value:
        if device_config.odata_type == "#microsoft.graph.macOSCustomConfiguration":
            payload_bytes = device_config.payload
            payload = base64.b64decode(payload_bytes)
            plist = plistlib.loads(payload,fmt=plistlib.FMT_XML)
            if 'deviceControl' in plist['PayloadContent'][0]:
                deviceControl = plist['PayloadContent'][0]['deviceControl']
                print(deviceControl)

                id = device_config.id
                assignments = await graph.get_assignments(id)

        if device_config.odata_type == "#microsoft.graph.windows10CustomConfiguration":
            id = device_config.id
            for oma_setting in device_config.oma_settings:
                value = None
                if oma_setting.odata_type == "#microsoft.graph.omaSettingInteger":
                    value = int(oma_setting.value)
                elif oma_setting.odata_type == "#microsoft.graph.omaSettingStringXml":
                    secret_reference_value_id = oma_setting.secret_reference_value_id
                    xml = await graph.get_xml(id,secret_reference_value_id)
                    print (xml.value)
                
            



# Run main
asyncio.run(main())