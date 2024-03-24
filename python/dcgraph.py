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

from msgraph_beta.generated.device_management.configuration_policies.item.assignments.assignments_request_builder import (AssignmentsRequestBuilder)

class Graph:
    settings: SectionProxy
    device_code_credential: DeviceCodeCredential
    user_client: GraphServiceClient

    def __init__(self, config: SectionProxy):
        self.settings = config
        client_id = self.settings['clientId']
        tenant_id = self.settings['tenantId']
        graph_scopes = self.settings['graphUserScopes'].split(' ')

        self.device_code_credential = DeviceCodeCredential(client_id, tenant_id = tenant_id)
        self.user_client = GraphServiceClient(self.device_code_credential, graph_scopes)


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

        
        user = await self.user_client.me().get(request_configuration=request_config)
        return user

    async def make_graph_call(self):
        # INSERT YOUR CODE HERE

        #self.user_client.device_
        #configs = await self.user_client.device_management.device_configurations.get_targeted_users_and_devices
        
        configs = await self.user_client.device_management.device_configurations.get()
        return configs
    
    async def get_assignments(self,id):
        # INSERT YOUR CODE HERE
 
        assignments = await self.user_client.device_management.device_configurations.by_device_configuration_id(id).assignments.get()
        return assignments
