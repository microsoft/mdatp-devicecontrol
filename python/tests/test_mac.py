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

    sn1 = api.createProperty(dc.GroupProperty.WindowsDeviceSerialNumber,"11111111111")
    sn2 = api.createProperty(dc.GroupProperty.WindowsDeviceSerialNumber,"11111111111")
    
    allowedSerialNumbersGroup = api.createGroup(properties=[sn1,sn2])

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

    convert.convert_rule(allowReadToAllowedSerialNumbers)

