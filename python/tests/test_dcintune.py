import mdedevicecontrol.dcintune as intune

import os
import asyncio
import pytest

from tests import hash, root_dir
    
pytest_plugins = ('pytest_asyncio',)

class DcIntuneArgs: 

    def __init__(self):

        self.tenantId = os.environ["TENANT_ID"]
        self.clientId = os.environ["CLIENT_ID"]
        self.clientSecret = os.environ["CLIENT_SECRET"]

        

        self.loggingConf = intune.file("logging.conf")


        self.command = "export"

        self.dest = os.path.join(str(root_dir),"export")
        self.package_name = hash(self.tenantId)

        self.templates_path = intune.path_array("templates")
        self.template = "dcutil.j2"
        self.readme_template = "readme.j2"
        self.description_template = "description.j2"
        self.readme_file = "readme.md"

@pytest.mark.asyncio
async def test_intune_export():
        
    args = DcIntuneArgs()
    
    result = await intune.process_args(args)
    

