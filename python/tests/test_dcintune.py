import mdedevicecontrol.dcintune as intune

import os
import asyncio

    

class DcIntuneArgs: 

    def __init__(self):

        self.tenantId = os.environ["TENANT_ID"]
        self.clientId = os.environ["CLIENT_ID"]
        self.clientSecret = os.environ["CLIENT_SECRET"]

        

        self.loggingConf = intune.file("logging.conf")


        self.command = "export"

        self.dest = os.getcwd()
        self.package_name = "Test1"

        self.templates_path = intune.path_array("templates")
        self.template = "dcutil.j2"
        self.readme_template = "readme.j2"
        self.description_template = "description.j2"
        self.readme_file = "readme.md"


def test_intune_export():
        
    args = DcIntuneArgs()
    
    asyncio.run(intune.process_args(args))
    

