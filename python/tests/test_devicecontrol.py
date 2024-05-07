import mdedevicecontrol as dc

from tests import root_dir
import os

def test_create_api():

    api = dc.api()


def test_create_group():

    api = dc.api()

    vid_pid = api.createProperty(dc.Group.WindowsDeviceVendorProductProperty,"05AC_12AB")
    properties = [vid_pid]

    g1 = api.createGroup(name="Allowed Devices",
                         group_type=dc.Group.WindowsDeviceGroupType,
                         match_type=dc.MatchType.Any,
                         properties=properties)

    print(str(g1))


def test_create_entry():

    api = dc.api()

    entry = api.createEntry()

def test_create_rule():

    api = dc.api()

    rule = api.createRule("Test Rule")

def test_create_rule_1():

    api = dc.api()

    removable_media_devices_family = api.createProperty(dc.Group.WindowsDeviceFamilyProperty,dc.GroupProperty.WindowsRemovableMediaDevices)
    properties = [removable_media_devices_family]

    all_removable_media_devices = api.createGroup(name="All Removable Media Devices",
            group_type=dc.Group.WindowsDeviceGroupType,
            match_type=dc.MatchType.Any,
            properties=properties)
    
    allow_read_entry = api.createEntry()

    rule = api.createRule("Test Rule 2",
                          included_groups=[all_removable_media_devices],
                          entries=[allow_read_entry])
    

def test_save():

    api = dc.api()
    removable_media_devices_family = api.createProperty(dc.Group.WindowsDeviceFamilyProperty,dc.GroupProperty.WindowsRemovableMediaDevices)
    properties = [removable_media_devices_family]

    all_removable_media_devices = api.createGroup(name="All Removable Media Devices",
            group_type=dc.Group.WindowsDeviceGroupType,
            match_type=dc.MatchType.Any,
            properties=properties)
    
    allow_read_entry = api.createEntry()

    rule = api.createRule("Test Rule 2",
                          included_groups=[all_removable_media_devices],
                          entries=[allow_read_entry])
    

    api.save(os.path.join(str(root_dir),"export"),"Test Package 0")
