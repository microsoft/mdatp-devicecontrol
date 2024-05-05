import mdedevicecontrol.dcintune as intune

import os

class DcIntuneArgs: 

    def __init__(self):

        self.tenantId = os.environ["AAD_TENANT_ID"]
        self.clientId = os.environ["AAD_CLIENT_ID"]
        self.loggingConf = doc.file("logging.conf")


        self.command = "export"

        self.dest = os.getcwd()
        self.package_name = "Test1"

        self.templates_path = intune.path_array("templates")
        self.template = "dcutil.j2"
        self.readme_template = "readme.j2"
        self.description_template = "description.j2"
        self.readme_file = "readme.md"
        
        

def test_rule_xml_1():

    rule = intune.DeviceControlPolicyTemplate.DeviceControlRule()
    rule.id = "12345"
    rule.name = "Test"
    #rule.included_groups = ["group1","group2"]
    
    out =str(rule)
    print(out)
