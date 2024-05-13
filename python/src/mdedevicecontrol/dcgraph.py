from configparser import SectionProxy
from azure.identity import DeviceCodeCredential
from azure.identity.aio import ClientSecretCredential

from msgraph_beta import GraphServiceClient, GraphRequestAdapter
from msgraph_core import GraphClientFactory
from kiota_authentication_azure.azure_identity_authentication_provider import (
    AzureIdentityAuthenticationProvider
)

import asyncio

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

from msgraph_beta.generated.models.device_management_configuration_policy import DeviceManagementConfigurationPolicy
from msgraph_beta.generated.models.device_management_configuration_setting import DeviceManagementConfigurationSetting
from msgraph_beta.generated.models.device_management_configuration_policy_template_reference import DeviceManagementConfigurationPolicyTemplateReference
from msgraph_beta.generated.models.device_management_configuration_technologies import DeviceManagementConfigurationTechnologies
from msgraph_beta.generated.models.device_management_configuration_platforms import DeviceManagementConfigurationPlatforms
from msgraph_beta.generated.models.device_management_reusable_policy_setting import DeviceManagementReusablePolicySetting
from msgraph_beta.generated.models.device_management_configuration_group_setting_collection_instance import DeviceManagementConfigurationGroupSettingCollectionInstance
from msgraph_beta.generated.models.device_management_configuration_group_setting_value import DeviceManagementConfigurationGroupSettingValue
from msgraph_beta.generated.models.device_management_configuration_setting_instance_template_reference import DeviceManagementConfigurationSettingInstanceTemplateReference
scopes = "DeviceManagementConfiguration.Read.All DeviceManagementConfiguration.ReadWrite.All Directory.Read.All"

'''
https://graph.microsoft.com/beta/deviceManagement/configurationPolicyTemplates?$filter=displayName eq 'Device Control'

https://graph.microsoft.com/beta/deviceManagement/reusablePolicySettings
'''

import logging
logger = logging.getLogger(__name__)

from kiota_http.middleware import BaseMiddleware
import httpx

class DebugHandler(BaseMiddleware):

    async def send(
        self, request: httpx.Request, transport: httpx.AsyncBaseTransport
    ) -> httpx.Response:
        print()
        print(f"{request.method} {request.url}")
        for key, value in request.headers.items():
            print(f"{key}: {value}")
        if request.content:
            print()
            print("Request body:")
            print(request.content.decode())
            logger.debug("BODY="+request.content.decode())

        response: httpx.Response = await super().send(request, transport)

        print()
        print(f"Response: {response.status_code} {response.reason_phrase}")
        print("Response headers:")
        for key, value in response.headers.items():
            print(f"{key}: {value}")

        print()
        print("Response body:")
        response_content = await response.aread()
        print(f"Response content: {response_content.decode()}")

        return response



class Graph:
    
    device_code_credential: DeviceCodeCredential
    user_client: GraphServiceClient

    def __init__(self, tenantId, clientId, clientSecret, scopes = None):
        
        client_id = clientId
        self.tenant_id = tenantId
        client_secret = clientSecret

        if self.tenant_id is not None:
            logger.debug("TenantId=...."+self.tenant_id[:4])

        if client_id is not None:
            logger.debug("ClientId=...."+client_id[:4])

        if client_secret is not None:
            logger.debug("ClientSecret=...."+client_secret[:4])

        self.graph_scopes = scopes.split(' ')

        if self.graph_scopes is not None:
            logger.debug("scopes: "+str(self.graph_scopes))

        
        _middleware = GraphClientFactory.get_default_middleware(None)
        _middleware.append(DebugHandler())
        _http_client = GraphClientFactory.create_with_custom_middleware(
            _middleware
        )

        if client_secret is not None:
            self.client_credential = ClientSecretCredential(self.tenant_id, client_id, client_secret)
            self.graph_scopes = ["https://graph.microsoft.com/.default"]
        else:
            self.client_credential = DeviceCodeCredential(client_id, tenant_id = self.tenant_id)

        _auth_provider = AzureIdentityAuthenticationProvider(self.client_credential)

        _adapter = GraphRequestAdapter(_auth_provider, _http_client)

        logger.debug("Client credential created.")
        self.graph_client =  GraphServiceClient(
            self.client_credential,
            scopes=self.graph_scopes,
            request_adapter=_adapter,
)
        logger.debug("Graph client created.")

    async def get_app_only_token(self):
        logger.debug("get_app_only_token")
        graph_scope = 'https://graph.microsoft.com/.default'
        access_token = await self.client_credential.get_token(graph_scope)
        logger.debug("access token "+str(access_token.token))
        return access_token.token
    

    async def get_user_token(self):
        access_token = self.client_credential.get_token(' '.join(self.graph_scopes))
        return access_token.token
    

    def get_client(self):
        return self.graph_client
    
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
    

    async def create_device_configuration(self,device_configuration):

        logger.debug("configuration="+str(device_configuration))
        loop = asyncio.get_event_loop()
        logger.debug("loop="+str(loop))
        try:
            result = await self.graph_client.device_management.device_configurations.post(device_configuration)
            logger.debug("result="+str(result))
            return result
        except RuntimeError as e:
            logger.error(str(e))   
             

    async def update_device_configuration(self,device_configuration,id):
        logger.debug("configuration="+str(device_configuration)+" id="+id)
        loop = asyncio.get_event_loop()
        logger.debug("loop="+str(loop))
        try:
            result = await self.graph_client.device_management.device_configurations.by_device_configuration_id(id).patch(device_configuration)
            logger.debug("result="+str(result))
            return result
        except RuntimeError as e:
            logger.error(str(e))   
            return e 


    

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
		    select = ["settingInstance","displayName","description","id"],
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
    

    async def create_group_v2(self,group,name):

        setting = DeviceManagementReusablePolicySetting()
        setting.setting_instance = group
        setting.display_name = name
        setting.setting_definition_id = "device_vendor_msft_defender_configuration_devicecontrol_policygroups_{groupid}_groupdata"
        
        logger.debug("Create Group v2 "+str(group))
        result = await self.graph_client.device_management.reusable_policy_settings.post(setting)
        logger.debug(str(result))
        return result



    async def create_policy_v2(self,name,description,rules):

        policy = DeviceManagementConfigurationPolicy()
        policy.name = name
        policy.description = description
        policy.platforms = DeviceManagementConfigurationPlatforms.Windows10
        policy.role_scope_tag_ids = ["0"]
    

        policy.technologies = DeviceManagementConfigurationTechnologies.Mdm
        policy.template_reference = DeviceManagementConfigurationPolicyTemplateReference()
        policy.template_reference.template_display_name = "Device Control"
        policy.template_reference.template_display_version = "Version 1"
        policy.template_reference.template_family = "endpointSecurityAttackSurfaceReduction"
        policy.template_reference.template_id = "0f2034c6-3cd6-4ee1-bd37-f3c0693e9548_1"

        setting = DeviceManagementConfigurationSetting()
        setting.setting_instance = DeviceManagementConfigurationGroupSettingCollectionInstance()
        setting.setting_instance.setting_definition_id =  "device_vendor_msft_defender_configuration_devicecontrol_policyrules_{ruleid}"
        setting.setting_instance.setting_instance_template_reference = DeviceManagementConfigurationSettingInstanceTemplateReference()
        setting.setting_instance.setting_instance_template_reference.setting_instance_template_id = "a5c5409c-886a-4909-81c7-28156aee9419"

        rules_settings = []

        setting.setting_instance.group_setting_collection_value = rules_settings

        
        for rule in rules:
            
            rule_setting = DeviceManagementConfigurationGroupSettingValue()
            rule_setting.children = [rule]

            rules_settings.append(rule_setting)
            
        policy.settings = [setting]
        
        result = await self.graph_client.device_management.configuration_policies.post(policy)
        return result