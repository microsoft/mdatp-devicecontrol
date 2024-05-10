import mdedevicecontrol as dc
import mdedevicecontrol.convert_dc_policy as convert
import os

from tests import root_dir

import logging.config
logging.config.fileConfig("logging.conf")

logger = logging.getLogger("mdedevicecontrol")

def test_mac_convert():

    api = dc.api(
        path=os.path.join(str(root_dir),"export")
    )

    serialNumbers = ["111111111","222222222"]
    
    allowedSerialNumbersGroup = api.createGroupOfWindowsDevicesBySerialNumber("Allowed USBs",serialNumbers)
    

    permissions = {
        dc.WindowsEntryType.DiskReadMask: True,
        dc.WindowsEntryType.DiskWriteMask: True,
        dc.WindowsEntryType.DiskExecuteMask: True
    }

    fullAccess = api.createEntry(permissions=permissions)

    allowReadToAllowedSerialNumbers = api.createRule("Allow Read access to serial numbers",
                                                     entries= [fullAccess],
                                                     included_groups=[allowedSerialNumbersGroup])

    logger.info(str(allowReadToAllowedSerialNumbers))

    convert.convert_group(allowReadToAllowedSerialNumbers,True)

