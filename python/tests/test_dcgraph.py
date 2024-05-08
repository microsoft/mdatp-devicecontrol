import os

import mdedevicecontrol.dcgraph as dcgraph
import asyncio

from msgraph_beta.generated.device_management.configuration_settings.configuration_settings_request_builder import ConfigurationSettingsRequestBuilder
from msgraph_beta.generated.models.device_management_configuration_setting_definition import DeviceManagementConfigurationSettingDefinition
from msgraph_beta.generated.models.windows10_custom_configuration import Windows10CustomConfiguration, OmaSetting
from msgraph_beta.generated.models.oma_setting_string_xml import OmaSettingStringXml

def get_graph():

        tenantId = os.environ["TENANT_ID"]
        clientId = os.environ["CLIENT_ID"]
        clientSecret = os.environ["CLIENT_SECRET"]

        graph = asyncio.run(dcgraph.Graph(tenantId,clientId,clientSecret))

        return graph
       


def test_intune_oma():

    graph = get_graph()
    
    win10config = Windows10CustomConfiguration()
    win10config.display_name = "This is imported"
    win10config.description = "This is the description"
        
    f1 = OmaSettingStringXml()
    test = "<PolicyRule></PolicyRule>"
    f1.value(str(test).encode("utf-8"))
    f1.file_name = "test_file.xml"

    win10config.oma_settings = [f1]

    result = asyncio.run(graph.create_device_configuration(win10config))

    print("Result="+str(result))
    print("Result Class="+result.__class__.name)

