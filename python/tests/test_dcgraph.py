import os

import mdedevicecontrol.dcgraph as dcgraph
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

pytest_plugins = ('pytest_asyncio',)

def get_graph():

        tenantId = os.environ["TENANT_ID"]
        clientId = os.environ["CLIENT_ID"]
        clientSecret = os.environ["CLIENT_SECRET"]

        graph = dcgraph.Graph(tenantId,clientId,clientSecret)

        return graph
       

@pytest.mark.asyncio
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

@pytest.mark.asyncio
async def test_v2_group():
      
      graph = get_graph()

      #This is the template for dcv2 https://graph.microsoft.com/beta/deviceManagement/configurationPolicyTemplates/0f2034c6-3cd6-4ee1-bd37-f3c0693e9548_1?$expand=settingTemplates

      #This is an example rule for dcv2 https://graph.microsoft.com/beta/deviceManagement/configurationPolicies/4f633fc5-0e54-45bd-ba81-f81d88c1ddc2?$expand=settings

      rule = DeviceManagementConfigurationGroupSettingCollectionInstance()
      rule.definition_id = "device_vendor_msft_defender_configuration_devicecontrol_policyrules_{ruleid}"
      
      rule_group_setting_collection_value = []
      rule.group_setting_collection_value = rule_group_setting_collection_value

      rule_value = DeviceManagementConfigurationGroupSettingValue() 
      rule_value_children = []
      rule_value.children = rule_value_children

      rule_group_setting_collection_value.append(rule_value)

      rule_data = DeviceManagementConfigurationGroupSettingCollectionInstance()
      rule_data.setting_definition_id = "device_vendor_msft_defender_configuration_devicecontrol_policyrules_{ruleid}_ruledata"


      rule_data_group_setting_value = DeviceManagementConfigurationGroupSettingValue()
      rule_data.group_setting_collection_value = [rule_data_group_setting_value]

      rule_data_group_setting_value_children = []

      #Create the rule id
      rule_id_simple_setting_instance = DeviceManagementConfigurationSimpleSettingInstance()
      rule_id_simple_setting_instance.setting_definition_id = "device_vendor_msft_defender_configuration_devicecontrol_policyrules_{ruleid}_ruledata_id"

      rule_id_simple_setting_instance_value = DeviceManagementConfigurationStringSettingValue()
      rule_id_simple_setting_instance.simple_setting_value = rule_id_simple_setting_instance_value

      #This is the rule id value
      rule_id_simple_setting_instance_value.value = "{f1a6460e-e3ff-4e54-a878-3e4e02ec19d7}"
      
      rule_data_group_setting_value_children.append(rule_id_simple_setting_instance)
      
      print(str(rule))
      
