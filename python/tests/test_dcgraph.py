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
from msgraph_beta.generated.models.device_management_configuration_choice_setting_instance import DeviceManagementConfigurationChoiceSettingInstance
from msgraph_beta.generated.models.device_management_configuration_choice_setting_value import DeviceManagementConfigurationChoiceSettingValue

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

        #This is the template for dcv2 https://graph.microsoft.com/beta/deviceManagement/configurationPolicyTemplates/0f2034c6-3cd6-4ee1-bd37-f3c0693e9548_1?$expand=settingTemplates

        #This is an example rule for dcv2 https://graph.microsoft.com/beta/deviceManagement/configurationPolicies/4f633fc5-0e54-45bd-ba81-f81d88c1ddc2?$expand=settings

        rule = DeviceManagementConfigurationGroupSettingCollectionInstance()
        rule.setting_definition_id = "device_vendor_msft_defender_configuration_devicecontrol_policyrules_{ruleid}"
      
        rule_group_setting_collection_value = []
        rule.group_setting_collection_value = rule_group_setting_collection_value

        rule_value = DeviceManagementConfigurationGroupSettingValue() 
        rule_value_children = []
        rule_value.children = rule_value_children

        rule_group_setting_collection_value.append(rule_value)

        rule_data = DeviceManagementConfigurationGroupSettingCollectionInstance()
        rule_data.setting_definition_id = "device_vendor_msft_defender_configuration_devicecontrol_policyrules_{ruleid}_ruledata"

        rule_value_children.append(rule_data)

        rule_data_group_setting_value = DeviceManagementConfigurationGroupSettingValue()
        rule_data.group_setting_collection_value = [rule_data_group_setting_value]

        rule_data_group_setting_value_children = []
        rule_data_group_setting_value.children = rule_data_group_setting_value_children

        #Create the rule id
        rule_id_simple_setting_instance = DeviceManagementConfigurationSimpleSettingInstance()
        rule_id_simple_setting_instance.setting_definition_id = "device_vendor_msft_defender_configuration_devicecontrol_policyrules_{ruleid}_ruledata_id"

        rule_id_simple_setting_instance_value = DeviceManagementConfigurationStringSettingValue()
        rule_id_simple_setting_instance.simple_setting_value = rule_id_simple_setting_instance_value
        #This is the rule id value
        rule_id_simple_setting_instance_value.value = "{f1a6460e-e3ff-4e54-a878-3e4e02ec19d7}"
      
        #Add it to the list
        rule_data_group_setting_value_children.append(rule_id_simple_setting_instance)

        #Create the name
        rule_name_simple_setting_instance = DeviceManagementConfigurationSimpleSettingInstance()
        rule_name_simple_setting_instance.setting_definition_id = "device_vendor_msft_defender_configuration_devicecontrol_policyrules_{ruleid}_ruledata_name"
        
        rule_name_simple_setting_instance_value = DeviceManagementConfigurationStringSettingValue()
        rule_name_simple_setting_instance.simple_setting_value = rule_name_simple_setting_instance_value

        #This is the rule name
        rule_name_simple_setting_instance_value.value = "Deny All Removable Media"
      
        #Add it to the list
        rule_data_group_setting_value_children.append(rule_name_simple_setting_instance)

        #Create the included groups
        included_groups_configuration_group_setting_collection_instance = DeviceManagementConfigurationGroupSettingCollectionInstance()
        included_groups_configuration_group_setting_collection_instance.setting_definition_id = "device_vendor_msft_defender_configuration_devicecontrol_policyrules_{ruleid}_ruledata_includedidlist"

        included_groups_configuration_group_setting_collection_instance_value = DeviceManagementConfigurationGroupSettingValue()
        included_groups_configuration_group_setting_collection_instance_group_setting_collection_value = [included_groups_configuration_group_setting_collection_instance_value]
        
        included_groups_configuration_group_setting_collection_instance.group_setting_collection_value = included_groups_configuration_group_setting_collection_instance_group_setting_collection_value

        included_groups_configuration_group_setting_collection_instance_value.children = []

        included_group_ids = ["0c1529ef-6565-4441-a6d3-afb66709f66b"]

        for included_group_id in included_group_ids:
               
                included_group_id_configuration_simple_setting_instance = DeviceManagementConfigurationSimpleSettingInstance()
                included_group_id_configuration_simple_setting_instance.setting_definition_id = "device_vendor_msft_defender_configuration_devicecontrol_policyrules_{ruleid}_ruledata_includedidlist_groupid"

                included_group_id_configuration_simple_setting_instance_value = DeviceManagementConfigurationStringSettingValue()
                included_group_id_configuration_simple_setting_instance.simple_setting_value = included_group_id_configuration_simple_setting_instance_value
                included_group_id_configuration_simple_setting_instance_value.value = included_group_id

                included_groups_configuration_group_setting_collection_instance_value.children.append(
                       included_group_id_configuration_simple_setting_instance
                )


         #Add it to the list
        rule_data_group_setting_value_children.append(included_groups_configuration_group_setting_collection_instance)
        

        #This is an entry
        rule_data_entry = DeviceManagementConfigurationGroupSettingCollectionInstance()
        rule_data_entry.setting_definition_id = "device_vendor_msft_defender_configuration_devicecontrol_policyrules_{ruleid}_ruledata_entry"
        
        #Add it to the list
        rule_data_group_setting_value_children.append(rule_data_entry)
        
        rule_data_group_setting_collection_value = DeviceManagementConfigurationGroupSettingValue()
        rule_data_entry.group_setting_collection_value = [rule_data_group_setting_collection_value]

        rule_data_group_setting_collection_value.children = []

        rule_data_entry_type = DeviceManagementConfigurationChoiceSettingInstance()
        rule_data_entry_type.setting_definition_id = "device_vendor_msft_defender_configuration_devicecontrol_policyrules_{ruleid}_ruledata_entry_type"

        rule_data_group_setting_collection_value.children.append(rule_data_entry_type) 
        
        rule_data_entry_type_value = DeviceManagementConfigurationChoiceSettingValue()
        rule_data_entry_type.choice_setting_value = rule_data_entry_type_value
        rule_data_entry_type_value.value = "device_vendor_msft_defender_configuration_devicecontrol_policyrules_{ruleid}_ruledata_entry_type_deny"
        rule_data_entry_type_value.children = []

        rule_data_entry_options = DeviceManagementConfigurationChoiceSettingInstance()
        rule_data_entry_options.setting_definition_id = "device_vendor_msft_defender_configuration_devicecontrol_policyrules_{ruleid}_ruledata_entry_options"

        rule_data_entry_options_value = DeviceManagementConfigurationChoiceSettingValue()
        rule_data_entry_options.choice_setting_value = rule_data_entry_options_value
        rule_data_entry_options_value.value = "device_vendor_msft_defender_configuration_devicecontrol_policyrules_{ruleid}_ruledata_entry_options_0"

        # The options are a child to the allow/deny
        rule_data_entry_type_value.children.append(rule_data_entry_options)


        rule_data_entry_access_mask = DeviceManagementConfigurationChoiceSettingInstance()
        rule_data_entry_access_mask.setting_definition_id = "device_vendor_msft_defender_configuration_devicecontrol_policyrules_{ruleid}_ruledata_entry_accesmask"

        #Add it to the list
        rule_data_group_setting_collection_value.children.append(rule_data_entry_access_mask)
        rule_data_entry_access_mask_choice_setting_value = DeviceManagementConfigurationChoiceSettingValue()

        rule_data_entry_access_mask.choice_setting_value = rule_data_entry_access_mask_choice_setting_value


        masks = [
               "device_vendor_msft_defender_configuration_devicecontrol_policyrules_{ruleid}_ruledata_entry_accesmask_1",
               "device_vendor_msft_defender_configuration_devicecontrol_policyrules_{ruleid}_ruledata_entry_accesmask_2",
               "device_vendor_msft_defender_configuration_devicecontrol_policyrules_{ruleid}_ruledata_entry_accesmask_4"
        ]

        rule_data_entry_access_mask_choice_setting_value.value = []
        for mask in masks:
               
               mask_value = DeviceManagementConfigurationChoiceSettingValue()
               mask_value.value = mask

               rule_data_entry_access_mask_choice_setting_value.value.append(mask_value)


        entry_id_setting = DeviceManagementConfigurationSimpleSettingInstance()
        entry_id_setting.setting_definition_id = "device_vendor_msft_defender_configuration_devicecontrol_policyrules_{ruleid}_ruledata_entry_id"

        entry_id_setting_value = DeviceManagementConfigurationStringSettingValue()
        entry_id_setting_value.value = "{6f9df57a-aadb-4b41-9e35-3634dc3857e6}"

        entry_id_setting.simple_setting_value = entry_id_setting_value

        #Add it to the list
        rule_data_group_setting_collection_value.children.append(entry_id_setting)

        logger.info(str(rule))

        try:
              result = await graph.create_rule_v2(rule)
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