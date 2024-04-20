from configparser import SectionProxy
from azure.identity import DeviceCodeCredential

from msgraph_beta import GraphServiceClient
from msgraph_beta.generated.users.item.user_item_request_builder import UserItemRequestBuilder
from msgraph_beta.generated.users.item.mail_folders.item.messages.messages_request_builder import (
    MessagesRequestBuilder)
from msgraph_beta.generated.users.item.send_mail.send_mail_post_request_body import (
    SendMailPostRequestBody)
from msgraph_beta.generated.models.message import Message
from msgraph_beta.generated.models.item_body import ItemBody
from msgraph_beta.generated.models.body_type import BodyType
from msgraph_beta.generated.models.recipient import Recipient
from msgraph_beta.generated.models.email_address import EmailAddress

from msgraph_beta.generated.device_management.configuration_policy_templates.configuration_policy_templates_request_builder import ConfigurationPolicyTemplatesRequestBuilder
from msgraph_beta.generated.device_management.configuration_policies.configuration_policies_request_builder import ConfigurationPoliciesRequestBuilder
from msgraph_beta.generated.device_management.configuration_settings.item.device_management_configuration_setting_definition_item_request_builder import DeviceManagementConfigurationSettingDefinitionItemRequestBuilder 
from msgraph_beta.generated.device_management.reusable_policy_settings.item.device_management_reusable_policy_setting_item_request_builder import DeviceManagementReusablePolicySettingItemRequestBuilder
from msgraph_beta.generated.device_management.reusable_settings.reusable_settings_request_builder import ReusableSettingsRequestBuilder


scopes = "DeviceManagementConfiguration.Read.All DeviceManagementConfiguration.ReadWrite.All Directory.Read.All"

'''
https://graph.microsoft.com/beta/deviceManagement/configurationPolicyTemplates?$filter=displayName eq 'Device Control'

https://graph.microsoft.com/beta/deviceManagement/reusablePolicySettings
'''

import logging
logger = logging.getLogger(__name__)

class Graph:
    
    device_code_credential: DeviceCodeCredential
    user_client: GraphServiceClient

    def __init__(self, tenantId, clientId):
        
        client_id = clientId
        tenant_id = tenantId
        graph_scopes = scopes.split(' ')

        logger.debug("scopes: "+str(graph_scopes))
        self.device_code_credential = DeviceCodeCredential(client_id, tenant_id = tenant_id)
        self.graph_client = GraphServiceClient(self.device_code_credential, graph_scopes)


    async def get_user_token(self):
        graph_scopes = self.settings['graphUserScopes']
        access_token = self.device_code_credential.get_token(graph_scopes)
        return access_token.token
    

    async def get_user(self):
        # Only request specific properties using $select
        query_params = UserItemRequestBuilder.UserItemRequestBuilderGetQueryParameters(
            select=['displayName', 'mail', 'userPrincipalName']
        )

        request_config = UserItemRequestBuilder.UserItemRequestBuilderGetRequestConfiguration(
            query_parameters=query_params
        )

        
        user = await self.graph_client.me().get(request_configuration=request_config)
        return user

    async def export_device_configurations(self):
        
        configs = await self.graph_client.device_management.device_configurations.get()
        return configs
    

    

    async def get_xml(self,id,secret_reference):

        logger.debug(">>>> get_xml id="+id+" secret_reference="+secret_reference)
        xml = await self.graph_client.device_management.device_configurations.by_device_configuration_id(id).get_oma_setting_plain_text_value_with_secret_reference_value_id(secret_reference_value_id=secret_reference).get()
        logger.debug("<<<< get_xml "+str(xml))
        return xml
    
    async def get_group_by_id(self,group_id):

        group = await self.graph_client.groups.by_group_id(group_id=group_id).get()
        return group
    
    async def get_device_control_policy_template(self):

        query_params = ConfigurationPolicyTemplatesRequestBuilder.ConfigurationPolicyTemplatesRequestBuilderGetQueryParameters(
		filter = "displayName eq 'Device Control'",
)

        request_configuration = ConfigurationPolicyTemplatesRequestBuilder.ConfigurationPolicyTemplatesRequestBuilderGetRequestConfiguration(
            query_parameters = query_params,
        )

        result = await self.graph_client.device_management.configuration_policy_templates.get(request_configuration = request_configuration)
        return result
    

    async def get_device_control_policies(self):

        query_params = ConfigurationPoliciesRequestBuilder.ConfigurationPoliciesRequestBuilderGetQueryParameters(
		filter = "templateReference/templateDisplayName eq 'Device Control'",
)

        request_configuration = ConfigurationPoliciesRequestBuilder.ConfigurationPoliciesRequestBuilderGetRequestConfiguration(
            query_parameters = query_params,
        )

        result = await self.graph_client.device_management.configuration_policies.get(request_configuration = request_configuration)
        return result
    
    async def get_device_control_policy_settings(self,id):
        result = await self.graph_client.device_management.configuration_policies.by_device_management_configuration_policy_id(id).settings.get()
        return result
    
    async def get_configuration_policy_settings_templates_by_id(self,id):

        result = await self.graph_client.device_management.configuration_policy_templates.by_device_management_configuration_policy_template_id(id).setting_templates.get()
        return result
    
    async def get_configuration_settings_for_definition(self,deviceManagementConfigurationSettingDefinitionid):

        query_params = DeviceManagementConfigurationSettingDefinitionItemRequestBuilder.DeviceManagementConfigurationSettingDefinitionItemRequestBuilderGetQueryParameters(
		select = ["baseUri","description","displayName","infoUrls","occurrence","offsetUri","settingUsage","uxBehavior","options"],
)

        request_configuration = DeviceManagementConfigurationSettingDefinitionItemRequestBuilder.DeviceManagementConfigurationSettingDefinitionItemRequestBuilderGetRequestConfiguration(
            query_parameters = query_params,
        )

        result = await self.graph_client.device_management.configuration_settings.by_device_management_configuration_setting_definition_id(deviceManagementConfigurationSettingDefinitionid).get()

        return result

    async def get_configuration_settings(self):
        result = await self.graph_client.device_management.configuration_settings.get()
        return result
    
    async def get_assignments_for_policy(self,policy_id):
        result = await self.graph_client.device_management.configuration_policies.by_device_management_configuration_policy_id(policy_id).assignments.get()
        
        return result
    
    async def get_assignments_for_configuration(self,id):
 
        assignments = await self.graph_client.device_management.device_configurations.by_device_configuration_id(id).assignments.get()
        return assignments
    
    async def get_group_details(self,id):

        query_params = DeviceManagementReusablePolicySettingItemRequestBuilder.DeviceManagementReusablePolicySettingItemRequestBuilderGetQueryParameters(
		    select = ["settingInstance","displayName","description"],
        )

        request_configuration = DeviceManagementReusablePolicySettingItemRequestBuilder.DeviceManagementReusablePolicySettingItemRequestBuilderGetRequestConfiguration(
            query_parameters = query_params,
        )

        result = await self.graph_client.device_management.reusable_policy_settings.by_device_management_reusable_policy_setting_id(id).get(request_configuration = request_configuration)
        return result
    
    async def get_reusable_settings_for_groups(self):
        query_params = ReusableSettingsRequestBuilder.ReusableSettingsRequestBuilderGetQueryParameters(
		    filter = "offsetUri eq '/configuration/devicecontrol/policygroups/{0}/groupdata'",
        )

        request_configuration = ReusableSettingsRequestBuilder.ReusableSettingsRequestBuilderGetRequestConfiguration(
            query_parameters = query_params,
        )

        result = await self.graph_client.device_management.reusable_settings.get(request_configuration = request_configuration)
        return result