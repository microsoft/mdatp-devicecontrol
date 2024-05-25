import os

import mdedevicecontrol.dcgraph as dcgraph
import mdedevicecontrol as dc
import mdedevicecontrol.dcintune as intune
import asyncio
import pytest


from msgraph_beta.generated.device_management.configuration_settings.configuration_settings_request_builder import ConfigurationSettingsRequestBuilder
from msgraph_beta.generated.models.device_management_configuration_setting_definition import DeviceManagementConfigurationSettingDefinition
from msgraph_beta.generated.models.windows10_custom_configuration import Windows10CustomConfiguration
from msgraph_beta.generated.models.oma_setting_string_xml import OmaSettingStringXml



from msgraph_beta.generated.models.device_management_configuration_group_setting_collection_instance import DeviceManagementConfigurationGroupSettingCollectionInstance
from msgraph_beta.generated.models.device_management_configuration_group_setting_value import DeviceManagementConfigurationGroupSettingValue
from msgraph_beta.generated.models.device_management_configuration_simple_setting_instance import DeviceManagementConfigurationSimpleSettingInstance
from msgraph_beta.generated.models.device_management_configuration_string_setting_value import DeviceManagementConfigurationStringSettingValue
from msgraph_beta.generated.models.device_management_configuration_choice_setting_instance import DeviceManagementConfigurationChoiceSettingInstance
from msgraph_beta.generated.models.device_management_configuration_choice_setting_value import DeviceManagementConfigurationChoiceSettingValue
from msgraph_beta.generated.models.device_management_configuration_reference_setting_value import DeviceManagementConfigurationReferenceSettingValue
from msgraph_beta.generated.models.device_management_configuration_choice_setting_collection_instance import DeviceManagementConfigurationChoiceSettingCollectionInstance
from msgraph_beta.generated.models.device_management_configuration_setting_instance_template_reference import DeviceManagementConfigurationSettingInstanceTemplateReference
from msgraph_beta.generated.models.device_management_configuration_simple_setting_instance import DeviceManagementConfigurationSimpleSettingInstance

pytest_plugins = ('pytest_asyncio',)

def get_graph():

        tenantId = os.environ["TENANT_ID"]
        clientId = os.environ["CLIENT_ID"]
        clientSecret = os.environ["CLIENT_SECRET"]

        graph = dcgraph.Graph(tenantId,clientId,clientSecret)
        


        return graph
       

@pytest.mark.asyncio(scope="session")
async def test_v2_group():

       import logging.config
       logging.config.fileConfig("logging.conf")

       logger = logging.getLogger("mdedevicecontrol")
      
       graph = get_graph()

       #https://graph.microsoft.com/beta/deviceManagement/reusablePolicySettings/260025de-b493-4b31-abf9-0c310854657f?$select=settingInstance

       groupdata = DeviceManagementConfigurationGroupSettingCollectionInstance()
       groupdata.setting_definition_id = "device_vendor_msft_defender_configuration_devicecontrol_policygroups_{groupid}_groupdata"
       groupdata.group_setting_collection_value = []

       groupdata_group_setting_value = DeviceManagementConfigurationGroupSettingValue()
       groupdata.group_setting_collection_value.append(groupdata_group_setting_value)
 
       groupdata_group_setting_value.children = []

       #group id
       groupdata_id_setting = DeviceManagementConfigurationSimpleSettingInstance()
       groupdata_id_setting.setting_definition_id = "device_vendor_msft_defender_configuration_devicecontrol_policygroups_{groupid}_groupdata_id"

       groupdata_id_value = DeviceManagementConfigurationStringSettingValue()
       groupdata_id_value.value = "{9d8c5f1a-8171-4aed-80da-e2703cca37c5}"

       groupdata_id_setting.simple_setting_value = groupdata_id_value
       groupdata_group_setting_value.children.append(groupdata_id_setting)

       #id list
       groupdata_list = DeviceManagementConfigurationGroupSettingCollectionInstance()
       groupdata_list.setting_instance_template_reference = "device_vendor_msft_defender_configuration_devicecontrol_policygroups_{groupid}_groupdata_printerdevicesidlist"

       groupdata_list_value = DeviceManagementConfigurationGroupSettingValue()
       groupdata_list.group_setting_collection_value = groupdata_list_value

       groupdata_list_value.children = []

       #printer name
       printer_name_setting = DeviceManagementConfigurationSimpleSettingInstance()
       printer_name_setting.setting_definition_id = "device_vendor_msft_defender_configuration_devicecontrol_policygroups_{groupid}_groupdata_printerdevicesidlist_name"

       printer_name_setting_value = DeviceManagementConfigurationStringSettingValue()
       printer_name_setting_value.value = "Test 4"

       groupdata_list_value.children.append(printer_name_setting)

       printer_connection_id_setting = DeviceManagementConfigurationChoiceSettingInstance()
       printer_connection_id_setting.setting_definition_id = "device_vendor_msft_defender_configuration_devicecontrol_policygroups_{groupid}_groupdata_printerdevicesidlist_printerconnectionid"
       printer_connection_id_setting_choice_setting_value = DeviceManagementConfigurationChoiceSettingValue 
       printer_connection_id_setting.choice_setting_value = printer_connection_id_setting_choice_setting_value

       printer_connection_id_setting_choice_setting_value.value = "device_vendor_msft_defender_configuration_devicecontrol_policygroups_{groupid}_groupdata_printerdevicesidlist_printerconnectionid_2"
       groupdata_list_value.children.append(printer_connection_id_setting)

       groupdata_group_setting_value.children.append(groupdata_list)

       #match type
       match_type_setting = DeviceManagementConfigurationChoiceSettingInstance()
       match_type_setting.setting_definition_id = "device_vendor_msft_defender_configuration_devicecontrol_policygroups_{groupid}_groupdata_matchtype"
       match_type_setting.choice_setting_value = DeviceManagementConfigurationChoiceSettingValue()
       match_type_setting.choice_setting_value.value = "device_vendor_msft_defender_configuration_devicecontrol_policygroups_{groupid}_groupdata_matchtype_matchany"

       groupdata_group_setting_value.children.append(match_type_setting)


@pytest.mark.asyncio(scope="session")
async def get_v1_polices():

       import logging.config
       logging.config.fileConfig("logging.conf")

       logger = logging.getLogger("mdedevicecontrol")
      
       graph = get_graph()

       result = graph.get_v1_policies_by_name('Policy for Special User')

       logger.debug(result)



@pytest.mark.asyncio(scope="session")
async def test_v2_rule():

       import logging.config
       logging.config.fileConfig("logging.conf")

       logger = logging.getLogger("mdedevicecontrol")
      
       graph = get_graph()

       #This is the template for dcv2 https://graph.microsoft.com/beta/deviceManagement/configurationPolicyTemplates/0f2034c6-3cd6-4ee1-bd37-f3c0693e9548_1?$expand=settingTemplates

       #This is an example rule for dcv2 https://graph.microsoft.com/beta/deviceManagement/configurationPolicies/4f633fc5-0e54-45bd-ba81-f81d88c1ddc2?$expand=settings

       api = dc.api(
              clientId=os.environ["CLIENT_ID"],
              clientSecret=os.environ["CLIENT_SECRET"],
              tenantId=os.environ["TENANT_ID"]
       )

       api.setMode(dc.api.MODE_WINDOWS_V2)

       g1 = api.createGroupOfWindowsDevicesBySerialNumber("allowed USBs",["1111111"])

       group_setting = intune.DeviceControlPolicyTemplate.DeviceControlGroup.createSettingFromGroup(g1)

       group_result = await graph.create_group_v2(group_setting,"g1")
       group_id = group_result.id

       group_maps = {}
       group_maps[g1.id] = group_id

       e1 = api.createReadOnlyEntry()
       r1 = api.createRule(rule_name="r1",included_groups=[g1],entries=[e1])

       rule = intune.DeviceControlPolicyTemplate.DeviceControlRule.createSettingsFromRule(r1,group_maps)



      
       logger.info(str(rule))

       try:
              result = await graph.create_policy_v2("test","test rule",[rule])
       except RuntimeError as e:
              logger.error(e)

@pytest.mark.asyncio(scope="session")
async def test_intune_oma():

    graph = get_graph()
    
    win10config = Windows10CustomConfiguration()
    win10config.display_name = "This is imported"
    win10config.description = "This is the description"
        
    f1 = OmaSettingStringXml()
    test = "<PolicyRule></PolicyRule>"
    f1.value = str(test).encode("utf-8")
    f1.file_name = "test_file.xml"
    f1.display_name = "Test XML"
    f1.description = "This is the description of the file"
    f1.oma_uri = "./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7b783b7807-4516-41cb-b5ad-b460f91629fe%7d/RuleData"

    win10config.oma_settings = [f1]

    result = await graph.create_device_configuration(win10config)

    print("Result="+str(result))
    print("Result Class="+result.__class__.__name__)


@pytest.mark.asyncio(scope="session")
async def test_ah_1():

       import logging.config
       logging.config.fileConfig("logging.conf")

       logger = logging.getLogger("mdedevicecontrol")

       graph = get_graph()

       query = '''
DeviceRegistryEvents
| where RegistryKey == "HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows Defender\\Policy Manager"
| where RegistryValueName == "PolicyRules"
| where RegistryValueData  !=  PreviousRegistryValueData
| project ReportId, DeviceName ,RegistryValueData, Timestamp
               '''
              

       result = await graph.query_ah(query)
       logger.debug("ah1 result=result")