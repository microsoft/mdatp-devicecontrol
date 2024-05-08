import mdedevicecontrol as dc

from tests import root_dir
import os
import asyncio

def test_create_api():

    api = dc.api()

def test_create_api_with_graph():

    api = dc.api(
        clientId=os.environ["CLIENT_ID"],
        tenantId=os.environ["TENANT_ID"],
        clientSecret=os.environ["CLIENT_SECRET"]
    )

    asyncio.run(api.connectToGraph())


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


def test_copy_group():

    api = dc.api()
    removable_media_devices_family = api.createProperty(dc.Group.WindowsDeviceFamilyProperty,dc.GroupProperty.WindowsRemovableMediaDevices)
    properties = [removable_media_devices_family]

    all_removable_media_devices = api.createGroup(name="All Removable Media Devices",
            group_type=dc.Group.WindowsDeviceGroupType,
            match_type=dc.MatchType.Any,
            properties=properties)
    
    all_removable_media_devices_2 = api.copy(all_removable_media_devices)
    if all_removable_media_devices.id == all_removable_media_devices_2.id:
        raise AssertionError("Copy has the same id")

     
def test_large_setup():

    api = dc.api(
        clientId=os.environ["CLIENT_ID"],
        tenantId=os.environ["TENANT_ID"],
        clientSecret=os.environ["CLIENT_SECRET"]
    )

    asyncio.run(api.connectToGraph())

    from mdedevicecontrol import WindowsEntryType, PolicyRule, Notifications, Format
    
    printers_devices_family = api.createProperty(dc.Group.WindowsDeviceFamilyProperty,dc.GroupProperty.WindowsPrinterDevices)
    removable_media_devices_family = api.createProperty(dc.Group.WindowsDeviceFamilyProperty,dc.GroupProperty.WindowsRemovableMediaDevices)
    wpd_devices_family  = api.createProperty(dc.Group.WindowsDeviceFamilyProperty,dc.GroupProperty.WindowsPortableDevices)
    cd_dvd_family = api.createProperty(dc.Group.WindowsDeviceFamilyProperty,dc.GroupProperty.WindowsCdRomDevices)


    printers_group = api.createGroup(name="All Printers",
        group_type=dc.Group.WindowsPrinterGroupType,
        match_type=dc.MatchType.Any,
        properties=[printers_devices_family])
    
    all_devices_group = api.createGroup(name="All Devices",
        group_type=dc.Group.WindowsDeviceGroupType,
        match_type=dc.MatchType.Any,
        properties=[
            printers_devices_family,
            removable_media_devices_family,
            wpd_devices_family,
            cd_dvd_family]
        )
    

    
    bitlocker_encrypted = api.createProperty(dc.Group.WindowsDeviceEncryptionStateProperty, dc.GroupProperty.WindowsDeviceBitlockerEncrypted)
    
    bitlocker_group_properties = [bitlocker_encrypted]
    bitlocker_group = api.createGroup(name="BitLocker Encrypted",
            group_type=dc.Group.WindowsDeviceGroupType,
            match_type=dc.MatchType.Any,
            properties=bitlocker_group_properties)
    
    bitlocker_unencrypted = api.createProperty(dc.Group.WindowsDeviceEncryptionStateProperty, dc.GroupProperty.WindowsDeviceNotEncrypted)
    
    plain_group_properties = [bitlocker_unencrypted]
    plain_group = api.createGroup(name="Not Bitlocker Encrypted",
            group_type=dc.Group.WindowsDeviceGroupType,
            match_type=dc.MatchType.Any,
            properties=plain_group_properties)
    

    vid_pid_group_data = {
        "Not BitLocker encrypted but has internal encryption": ["2D9B-8004"],
        "Smartphones": ["05AC-12AB","18D1-4EE1"],
        "Other Trusted Devices":["0E8D-1887"]

    }
    
    vid_pid_groups ={}
    for vid_pid_group_name in vid_pid_group_data:

        vid_pid_group_properties = []
        for vid_pid in vid_pid_group_data[vid_pid_group_name]:
            vid_pid_property = api.createProperty(dc.Group.WindowsDeviceVendorProductProperty, vid_pid)
            vid_pid_group_properties.append(vid_pid_property)

        vid_pid_group = api.createGroup(name=vid_pid_group_name,
            group_type=dc.Group.WindowsDeviceGroupType,
            match_type=dc.MatchType.Any,
            properties=vid_pid_group_properties)
        
        vid_pid_groups[vid_pid_group_name] = vid_pid_group
    

    friendly_names_for_trusted_images = [
        "PNY USB 2.0 FD USB Device"
    ]

    trusted_images_group_properties = []

    for friendly_name in friendly_names_for_trusted_images:
        friendly_name_property = api.createProperty(dc.Group.WindowsDeviceFriendlyNameProperty, friendly_name)
        trusted_images_group_properties.append(friendly_name_property)

    trusted_images_group = api.createGroup(name="Trusted Images",
            group_type=dc.Group.WindowsDeviceGroupType,
            match_type=dc.MatchType.Any,
            properties=trusted_images_group_properties)


    rwx_except_for_smartphones = {
        "ro":[
            vid_pid_groups["Smartphones"]
        ],
        "rwx":[ 
            bitlocker_group,
            plain_group,
            trusted_images_group,
            printers_group,
            vid_pid_groups["Not BitLocker encrypted but has internal encryption"],
            vid_pid_groups["Other Trusted Devices"]
        ],
        "description": "Allow full access to allowed devices and read-only access to  Smartphones"
    }
    rwx_except_for_smartphones_and_unencrypted = {
        "ro":[
            vid_pid_groups["Smartphones"],
            plain_group
        ],
        "rwx":[ 
            bitlocker_group,
            trusted_images_group,
            printers_group,
            vid_pid_groups["Not BitLocker encrypted but has internal encryption"],
            vid_pid_groups["Other Trusted Devices"]
        ],
        "description":"Allow full access to allowed devices and read-only to Smartphones and un-encrypted devices "
    }
    rwx_except_for_unencrypted =  {
        "ro":[
            vid_pid_groups["Smartphones"],
            plain_group
        ],
        "rwx":[ 
            bitlocker_group,
            trusted_images_group,
            printers_group,
            vid_pid_groups["Not BitLocker encrypted but has internal encryption"],
            vid_pid_groups["Other Trusted Devices"]
        ],
        "description": "Allow full access to allowed devices and read-only to un-encrypted devices"
    }

    rules_data = {
        "Regular User": rwx_except_for_smartphones_and_unencrypted,
        "Smartphone User": rwx_except_for_unencrypted,
        "Special User": rwx_except_for_smartphones
    }

    full_access_permissions = {
        WindowsEntryType.DiskReadMask : True,
        WindowsEntryType.DiskExecuteMask: True,
        WindowsEntryType.DiskWriteMask: True,
        WindowsEntryType.FileExecuteMask: True,
        WindowsEntryType.FileReadMask: True,
        WindowsEntryType.FileWriteMask: True,
        WindowsEntryType.PrintMask: True
    }

    read_only_permissions = {
        WindowsEntryType.DiskReadMask: True,
        WindowsEntryType.FileReadMask: True
    }

    write_and_execute_permissions = {
        WindowsEntryType.DiskExecuteMask: True,
        WindowsEntryType.DiskWriteMask: True,
        WindowsEntryType.FileExecuteMask: True,
        WindowsEntryType.FileWriteMask: True,
        WindowsEntryType.PrintMask: True
    }

    for rule_name in rules_data:

        rule_data = rules_data[rule_name]
        read_only = rule_data["ro"]
        full_access = rule_data["rwx"]

        #create a rule which is allow full access unless ro

        full_access_entry = api.createEntry(permissions=full_access_permissions)

        full_access_rule = api.createRule(
            rule_name="Allow Full Access for "+rule_name,
            included_groups=[all_devices_group],
            excluded_groups=read_only,
            entries=[full_access_entry]
        )

        #create a rule which is deny write and execute unless full_access

        deny_write_entry = api.createEntry(permissions=write_and_execute_permissions,enforcement=PolicyRule.Deny)
        audit_deny_write_entry = api.createEntry(permissions=write_and_execute_permissions,enforcement=PolicyRule.AuditDenied,notifications=Notifications(3,format=Format.OMA_URI))
        allow_read_entry = api.createEntry()

        read_only_rule = api.createRule(
            rule_name="Allow Read Only for "+rule_name,
            included_groups=read_only,
            excluded_groups=full_access,
            entries=[deny_write_entry,audit_deny_write_entry,allow_read_entry]
        )

        policy = api.createPolicy("Policy for "+rule_name,
                                  description=rule_data["description"],
                                  rules = [read_only_rule,full_access_rule],
                                  groups= read_only + full_access)

    api.save(os.path.join(str(root_dir),"export"),"Test Package 1")

    

    
