#!/usr/bin/env python



__all__ = ['convert_dc_policy','dcdoc','dcgraph','dcintune']



import argparse
import argcomplete
from configparser import SafeConfigParser, ConfigParser
import asyncio
import json
import copy
import os
import urllib.parse
import pathlib
import xml.etree.ElementTree as ET
from json import JSONEncoder
import uuid
import pandas

import logging

import jinja2
logger = logging.getLogger(__name__)

class Util:

    def xml_safe_text(text):

        try:

            ET.fromstring("<test>"+text+"</test>")
            return text
        except Exception as e:
            out = str(text).replace("&","&amp;")
            out = str(out).replace("<","&lt;")
            out = str(out).replace(">","&gt;")
            out = str(out).replace("'","&apos;")
            out = str(out).replace("\"","&quot;")
            return out

    # from  https://stackoverflow.com/questions/2556108/rreplace-how-to-replace-the-last-occurrence-of-an-expression-in-a-string
    def rreplace(s, old, new, occurrence):
        li = s.rsplit(old, occurrence)
        return new.join(li)

class DCJSONEncoder(JSONEncoder):
    def default(self, obj):
        try:
            return obj.toJSON()  # Call a custom method if available
        except AttributeError:
            return super().default(obj)

    
class Format:

    Mac = "mac"
    OMA_URI = "oma-uri"
    GPO = "gpo"

class Setting: 

    class Data:

        def fromDictionary(dict):

            name = "default name"
            description = "default description"

            if "name" in dict.keys():
                name = dict["name"]

            if "description" in dict.keys():
                description = dict["description"]

            data = Setting.Data(name,description)

            if Format.OMA_URI in dict.keys():
                oma_uri = dict[Format.OMA_URI]
                if "supported" in oma_uri.keys():
                    data.set_supported(Format.OMA_URI,oma_uri["supported"])
                if "documenation" in oma_uri.keys():
                    data.set_documentation(Format.OMA_URI,oma_uri["documentation"])
                if "value_map" in oma_uri.keys():
                    data.set_value_map(Format.OMA_URI,oma_uri["value_map"])
                if "type" in oma_uri.keys():
                    data.set_oma_uri_type(Format.OMA_URI,oma_uri["type"])
                if "oma-uri" in oma_uri.keys():
                    data.set_oma_uri(Format.OMA_URI,oma_uri["oma-uri"])

            if Format.Mac in dict.keys():
                mac = dict[Format.Mac]
                if "supported" in mac.keys():
                    data.set_supported(Format.Mac,mac["supported"])
                if "documenation" in mac.keys():
                    data.set_documentation(Format.Mac,mac["documentation"])
                if "value_map" in mac.keys():
                    data.set_value_map(Format.Mac,mac["value_map"])
                if "mac_setting" in mac.keys():
                    mac_setting = mac["mac_setting"]
                    if "name" in mac_setting.keys():
                        data.set_mac_setting_name(mac_setting["name"])
                    if "category" in mac_setting.keys():
                        data.set_mac_setting_category(mac_setting["category"])

            if Format.GPO in dict.keys():
                gpo = dict["gpo"]
                if "supported" in gpo.keys():
                    data.set_supported(Format.GPO,gpo["supported"])
                if "documenation" in gpo.keys():
                    data.set_documentation(Format.GPO,gpo["documentation"])
                if "value_map" in gpo.keys():
                    data.set_value_map(Format.GPO,gpo["value_map"])

                    
                
                    


        def __init__(self,name,description):
            self.name = name
            self.description = description
            self.data = {
                "name": name,
                "description": description,
                "oma-uri":{
                    "supported": False

                },
                "gpo":{
                    "supported": False
                },
                "mac":{
                    "supported": False
                }
            }

        def set_supported(self,format,supported):
            self.data[format]["supported"] = supported

        def set_documentation(self,format,documentation):
            self.data[format]["documentation"] = documentation

        def set_value_map(self,format,value_map):
            self.data[format]["value_map"] = value_map

        def set_oma_uri(self,oma_uri):
            self.data["oma-uri"]["oma-uri"] = oma_uri

        def set_oma_uri_type(self,oma_uri_type):
            self.data["oma-uri"]["type"] = oma_uri_type

        
        def set_mac_setting_name(self,name):
            if "mac_setting" in self.data["mac"].keys():
                mac_setting = self.data["mac"]["mac_setting"]
                mac_setting["name"] = name
            else:
                mac_setting = {
                    "name":name
                }
                self.data["mac"]["mac_setting"] = mac_setting

        def set_mac_setting_category(self,category):
            if "mac_setting" in self.data["mac"].keys():
                mac_setting = self.data["mac"]["mac_setting"]
                mac_setting["category"] = category
            else:
                mac_setting = {
                    "category":category
                }
                self.data["mac"]["mac_setting"] = mac_setting
        
        
        def get_data(self):
            return self.data
        
        
            
            
    OMA_URI_Integer_DataType = "Integer"
    OMA_URI_XML_DataType = "String (XML File)"
    OMA_URI_String_DataType = "String"

    DeviceControlEnabled = "DeviceControlEnabled"
    DefaultEnforcement = "DefaultEnforcement"
    DataDuplicationDirectory = "DataDuplicationDirectory"
    SecuredDevicesConfiguration = "SecuredDevicesConfiguration"
    DataDuplicationMaximumQuota = "DataDuplicationMaximumQuota"
    DataDuplicationRemoteLocation = "DataDuplicationRemoteLocation"
    UXNavigationTarget = "UXNavigationTarget"

    data = {
        DeviceControlEnabled:{
            "description":"Enables/disables device control",
            "name": "Device Control Enabled",
            "oma-uri": {
                "supported": True,
                "oma-uri": "./Vendor/MSFT/Defender/Configuration/DeviceControlEnabled",
                "documentation": "https://learn.microsoft.com/en-us/windows/client-management/mdm/defender-csp#configurationdevicecontrolenabled",
                "type": OMA_URI_Integer_DataType,
                "value_map": {
                    True: 1,
                    False: 0
                }
            },
            "gpo":{
                "supported":True

            },
            "mac":{
                "supported":False

            }
        },
        DefaultEnforcement:{
            "name": "Default Enforcement",
            "description": "Control Device Control default enforcement. This is the enforcement applied if there are no policy rules present or at the end of the policy rules evaluation none were matched.",
            "oma-uri": {
                "supported":True,
                "oma-uri":"./Vendor/MSFT/Defender/Configuration/DefaultEnforcement",
                "documentation": "https://learn.microsoft.com/en-us/windows/client-management/mdm/defender-csp#configurationdefaultenforcement",
                "type": OMA_URI_Integer_DataType,
                "value_map":{
                    "Allow": 1,
                    "Deny": 2
                }
            },
            "gpo": {
                "supported":True
            },
            "mac": {
                "supported":True,
                "documentation": "https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/mac-device-control-overview?view=o365-worldwide#settings",
                "value_map":{
                    "Allow":"allow",
                    "Deny":"deny"
                },
                "mac_setting": {
                    "category": "global",
                    "name": "defaultEnforcement",  
                }
                
            }
        },
        DataDuplicationDirectory:{
            "name": "File Evidence Directory",
            "description": "Define data duplication directory for device control.",
            "oma-uri": {
                "supported":True,
                "oma-uri":"./Device/Vendor/MSFT/Defender/Configuration/DataDuplicationDirectory",
                "documentation": "https://learn.microsoft.com/en-us/windows/client-management/mdm/defender-csp#configurationdataduplicationdirectory",
                "type": OMA_URI_String_DataType
            },
            "mac":{
                "supported":False
            }
        },
        SecuredDevicesConfiguration: {
            "name": "Secured Devices",
            "description":"Defines which device's primary ids should be secured by Defender Device Control. If this configuration isn't set the default value will be applied, meaning all supported devices will be secured.",
            "oma-uri": {
                "supported": True,
                "documentation": "https://learn.microsoft.com/en-us/windows/client-management/mdm/defender-csp#configurationsecureddevicesconfiguration",
                "oma-uri": "./Vendor/MSFT/Defender/Configuration/SecuredDevicesConfiguration",
                "type": OMA_URI_String_DataType
            },
            "mac": {
                "supported": True,
                "documentation": "https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/mac-device-control-overview?view=o365-worldwide#settings",
                "mac_setting": {
                    "category":"features"
                },
                "documentation": "https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/mac-device-control-overview?view=o365-worldwide#settings",
                
            }

        },
        DataDuplicationMaximumQuota:{
            "name": "File Evidence Quota",
            "description":"Defines the maximum data duplication quota in MB that can be collected. When the quota is reached the filter will stop duplicating any data until the service manages to dispatch the existing collected data, thus decreasing the quota again below the maximum. The valid interval is [5-5000] MB. By default, the maximum quota will be 500 MB.",
            "oma-uri":{
                "supported":True,
                "documentation": "https://learn.microsoft.com/en-us/windows/client-management/mdm/defender-csp#configurationdataduplicationmaximumquota",
                "oma-uri": "./Device/Vendor/MSFT/Defender/Configuration/DataDuplicationMaximumQuota",
                "type": OMA_URI_Integer_DataType
            },
            "mac":{
                "supported":False
            }
        },
        DataDuplicationRemoteLocation:{
            "name": "File Evidence Remote Location",
            "description":"Define data duplication remote location for Device Control. When configuring this setting, ensure that Device Control is Enabled and that the provided path is a remote path the user can access.",
            "oma-uri":{
                "supported": True,
                "oma-uri": "./Device/Vendor/MSFT/Defender/Configuration/DataDuplicationRemoteLocation",
                "documentation": "https://learn.microsoft.com/en-us/windows/client-management/mdm/defender-csp#configurationdataduplicationremotelocation",
                "type": OMA_URI_String_DataType
            },
            "mac":{
                "supported": False
            }
        },
        UXNavigationTarget: {
            "name":"UX Navigation Target",
            "description":"Notification hyperlink",
            "oma-uri":{
                "supported":False
            },
            "gpo":{
                "supported":False
            },
            "mac":{
                "supported":True,
                "mac_setting":{
                    "category": "UX",
                    "name": "navigationTarget",
                },
                "documentation": "https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/mac-device-control-overview?view=o365-worldwide#settings",
                
            }
        }
    
    }

    def getSettingNameFor(oma_uri):

        for key in Setting.data:
            setting_data = Setting.data[key]
            if setting_data["oma-uri"]["supported"]:
                if oma_uri == setting_data["oma-uri"]["oma-uri"]:
                    return key
                
        return None
    
    def getOMAURIFor(name):

        setting_data = Setting.data[name]

        if setting_data == None:
            return None

        if "oma-uri" in setting_data.keys():
            return setting_data["oma-uri"]["oma-uri"]
        else:
            return None
    

    def addSettingData(name,data):
        Setting.data[name] = data

    


    
    def __init__(self,name,value):
        self.name = name
        self.value = value
        

        if name not in Setting.data.keys():
            raise Exception("Unknown Setting "+name)
        

    def get_data_type(self, format = "oma-uri"):
         supported = Setting.data[self.name][format]["supported"]
         if supported:
            return Setting.data[self.name][format]["type"]
         else:
            return ""
    
    def get_documentation(self, format="oma-uri"):
        supported = Setting.data[self.name][format]["supported"]
        if supported:
            return Setting.data[self.name][format]["documentation"]
        return ""
    
    def get_description(self):
        return Setting.data[self.name]["description"]
        
    def get_oma_uri(self):

        supported = Setting.data[self.name]["oma-uri"]["supported"]

        if supported:
            return Setting.data[self.name]["oma-uri"]["oma-uri"]
        else:
            return ""

    def get_value(self,format = "oma-uri"):

        if not Setting.data[self.name][format]["supported"]:
            return ""
        
        elif format == "oma-uri":
            oma_uri = Setting.data[self.name]["oma-uri"]
            if not "type" in oma_uri.keys():
                return self.value
            
            if oma_uri["type"] == Setting.OMA_URI_String_DataType:
                return self.value
            elif oma_uri["type"] == Setting.OMA_URI_Integer_DataType:
                if "value_map" in oma_uri.keys():
                    return int(oma_uri["value_map"][self.value])
                else:
                    return self.value
            else:
                return self.value
            
        else:
            return self.value

class Settings:

    default_enforcement_map = {
        "allow":"Allow",
        "deny": "Deny"
    }

    default_features = {
        "appleDevice": {
            "disable": True
        },
        "removableMedia":{
            "disable": True
        },
        "portableDevice": {
            "disable": True
        },
        "bluetoothDevice":{
            "disable":True
        }
    }

    mac_default_enforcement = "allow"

    def generate_settings_from_mac_policy(json):
        settings = None

        
        

        if "settings" in json.keys():

            settings_dict = {}
            settings_json = json["settings"]

            if "features" in settings_json:
                features = Settings.default_features
                for features_key in settings_json["features"]:
                     features[features_key] = settings_json["features"][features_key]
                settings_dict[Setting.SecuredDevicesConfiguration] = features
            else:
                settings_dict[Setting.SecuredDevicesConfiguration] = Settings.default_features

            if "global" in settings_json:
                global_json = settings_json["global"]
                mac_default_enforcement = global_json["defaultEnforcement"]
                if mac_default_enforcement not in Settings.default_enforcement_map.values():
                    default_enforcement = Settings.default_enforcement_map[mac_default_enforcement]
                else:
                    default_enforcement = mac_default_enforcement

                settings_dict[Setting.DefaultEnforcement] = default_enforcement
            else:
                settings_dict[Setting.DefaultEnforcement] = Settings.mac_default_enforcement

            if "ux" in settings_json:
                ux_json = settings_json["ux"]
                settings_dict[Setting.UXNavigationTarget] = ux_json["navigationTarget"]

            if len(settings_dict) > 0:
                settings = Settings(settings_dict)

        return settings


    def __init__(self, setting_dict=None):
        self.settings = []
        if setting_dict is None:
            return
        else: 
            for name in setting_dict:
                value = setting_dict[name]
                if isinstance(value,dict):
                    if "value" in value.keys():
                        #this is loaded from Intune
                        self.settings.append(Setting(name,value["value"]))
                    else:
                        #this is mac settings
                        self.settings.append(Setting(name,value))    
                else:
                    self.settings.append(Setting(name,value))

    def addSetting(self,setting):
        self.settings.append(setting)


    def getIntuneCustomValues(self):
        custom_rows = {}

        for setting in self.settings:
            row = IntuneCustomRow(setting)
            custom_rows[row.OMA_URI] = row

        return custom_rows
    
    def __iter__(self):
        return self.settings.__iter__()

    def __next__(self): 
        return self.settings.__next__()
    

    def get_mac_settings(self):

        mac_settings = {

        }

        for setting in self.settings:

            if setting.name == Setting.SecuredDevicesConfiguration: 
                mac_settings["features"] = setting.value
            
            if Setting.DefaultEnforcement == setting.name:
                mac_settings["global"] = {
                    "defaultEnforcement": str(setting.value).lower()
                }
            
            if Setting.UXNavigationTarget == setting.name:
                mac_settings["ux"] = {
                    "navigationTarget":setting.value
                }
        return mac_settings

class IntuneCustomRow:


    def __init__(self,object):
        self.name = ""
        self.description = ""
        self.OMA_URI = ""
        self.data_type = Setting.OMA_URI_XML_DataType
        self.value = ""
        self.object = object

        match object.__class__.__name__:

            case "Group":
                self.name = object.name
                self.OMA_URI = object.get_oma_uri()
                self.value = object.path
            case "PolicyRule":
                self.name = object.name
                self.OMA_URI = object.get_oma_uri()
                self.value = object.path
            case "Setting":
                self.name = object.name
                self.OMA_URI = object.get_oma_uri()
                self.value = object.get_value("oma-uri")
                self.data_type = object.get_data_type("oma-uri")
            case other:
                print ("Unknown object class "+str(object.__class__.__name__))

class Property:

    def __init__(self, group_property, property_value):
        self.name = group_property.name

        self.allowed_values = group_property.allowed_values
        if self.allowed_values is not None and property_value not in self.allowed_values:
            raise Exception("Invalid value "+property_value+" for group property "+group_property.name)
        self.value = property_value
        self.label = group_property.label

class Clause:

    def __init__(self,clause, group_type, clause_type = None):
        self._properties = []
        self.group_type = group_type
        self.clause_type = clause_type
        self.sub_clauses = []
        self.sub_clause_type = None

        property = None
        value = None
        if "$type" in clause:
            property = clause.get("$type")
            if property == "and" or property == "or":
                self.sub_clause_type = property
                if "clauses" in clause:
                    self.has_sub_clauses = True
                    clauses = clause.get("clauses")
                    for subclause in clauses:
                        sc = Clause(subclause,self.group_type,self.sub_clause_type)
                        self.sub_clauses.append(sc)

            if "value" in clause:
                value = clause.get("value")

            if property is not None and value is not None:
                group_property = self.group_type.get_property_by_name(property)
                self._properties.append(Property(group_property, value))
            elif self.sub_clause_type is None:
                logger.warn("Unknown Clause")
                return
            
class GroupProperty:

    #Reference to group
    WindowsGroupId = "GroupId"
    
    #Windows Device
    WindowsDeviceFriendlyName = "FriendlyNameId"
    
    WindowsRemovableMediaDevices = "RemovableMediaDevices"
    WindowsCdRomDevices = "CdRomDevices"
    WindowsPortableDevices = "WpdDevices"
    WindowsPrinterDevices = "PrinterDevices"

    WindowsDeviceVendorProduct = "VID_PID"
    WindowsDeviceVendor = "VID"
    WindowsDeviceProduct = "PID"
    WindowsDeviceInstancePath = "InstancePathId"
    WindowsDeviceId = "DeviceId"
    WindowsDeviceHardwareId = "HardwareId"
    WindowsDeviceBus = "BusId"
    WindowsDeviceSerialNumber = "SerialNumberId"
    WindowsDeviceFamily = "PrimaryId"

    #Encryption state
    WindowsDeviceEncryptedState = "DeviceEncryptionStateId"
    WindowsDeviceBitlockerEncrypted = "BitlockerEncrypted"
    WindowsDeviceNotEncrypted = "Plain"


    #Network
    NetworkCategory = "NetworkCategoryId"
    NetworkCategoryPublic = "Public"
    NetworkCategoryPrivate = "Private"
    NetworkCategoryDomainAuthenticated = "DomainAuthenticated"
    
    NetworkName = "NameId"

    NetworkDomain = "NetworkDomainId"
    NonDomain = "NonDomain"
    Domain = "Domain"
    DomainAuthenticated = "DomainAuthenticated"

    #VPN Connection
    VPNConnectionStatus = "VPNConnectionStatusId"
    VPNConnectionStatusConnected = "Connected"
    VPNConnectionStatusDisconnected = "Disconnected"
    VPNServerAddress = "VPNServerAddressId"
    VPNDnsSuffix = "VPNDnsSuffixId"
    VPNConnectionName = "NameId"

    #PrinterConnection
    WindowsPrinterConnection = "PrinterConnectionId"
    USBPrinterConnection = "USB"
    CorporatePrinterConnection = "Corporate"
    NetworkPrinterConnection = "Network"
    UniversalPrinterConnection = "Universal"
    FilePrinterConnection = "File"
    CustomPrinterConnection = "Custom"
    LocalPrinterConnection = "Local"

    #File
    FilePath = "PathId"

    #PrintJob
    PrintOutputFileName = "PrintOutputFileNameId"
    PrintDocumentName = "PrintDocumentNameId"

    #AppleDevice
    MacDeviceFamily = "primaryId"

    MacAppleDevices = "apple_devices"
    MacRemovableMediaDevices = "removable_media_devices"
    MacPortableDevices = "portable_devices"
    MacBluetoothDevices = "bluetooth_devices"

    MacVendorId = "vendorId"
    MacProductId = "productId"
    MacSerialNumber = "serialNumber"

    MacEncryption = "encryption"
    MacEncryptionAPFS = "apfs"
    MacGroupId = "groupId"

    #MacFile
    MacFileType = "fileType"


    properties_by_name = {}

    def __init__(self,name,label,description,allowed_values = None):
        self.name = name
        self.label = label
        self.description = description
        self.allowed_values = allowed_values

        GroupProperty.properties_by_name[name] = self

class GroupType:

    

    WindowsDeviceGroupType = "Device"
    WindowsPrinterGroupType = "Device"
    
    FileGroupType = "File"
    NetworkGroupType = "Network"
    VPNConnectionGroupType = "VPNConnection"

    PrintJobType = "PrintJob"

    MacDeviceGroupType = "device"
    MacFileGroupType = "file"

    


    def __init__(self,name, label, group_properties, format = Format.OMA_URI):
        self.name = name
        self.group_properties = group_properties
        self.name_map = {}
        self.label = label
        self.format = format

        for group_property in group_properties:
            self.name_map[group_property.name] = group_property

    def isWindows(self):
        return self.format is not Format.Mac
    
    def get_property_by_name(self, property_name):
        if property_name in self.name_map.keys():
            return self.name_map[property_name]
        else:
            return None


class MatchType:

    All = "MatchAll"
    Any = "MatchAny"

class Group:

    Types = {
        
    }

    

    MacDeviceFamilyProperty = GroupProperty(
        GroupProperty.MacDeviceFamily,
        "Mac Device Family",
        "One of apple_devices, removable_media_devices, portable_devices, bluetooth_devices",
        [
            GroupProperty.MacAppleDevices,
            GroupProperty.MacBluetoothDevices,
            GroupProperty.MacRemovableMediaDevices,
            GroupProperty.MacPortableDevices
        ]
    )

    MacDeviceVendorProperty = GroupProperty(
        GroupProperty.MacVendorId,
        "Vendor Id (VID)",
        "Matches a device's vendor ID"
    )

    MacDeviceProductProperty = GroupProperty(
        GroupProperty.MacProductId,
        "Product Id (PID)",
        "Matches a device's product ID"
    )

    MacDeviceSerialNumber = GroupProperty(
        GroupProperty.MacSerialNumber,
        "Mac Device Serial Number",
        "Matches a device's serial number"
    )

    MacDeviceEncryptedProperty = GroupProperty(
        GroupProperty.MacEncryption,
        "Mac Encrypted",
        "Match if a device is apfs-encrypted.",
        [
            GroupProperty.MacEncryptionAPFS
        ]
    )

    MacGroupProperty = GroupProperty(
        GroupProperty.MacGroupId,
        "Device Control Group",
        "Match if a device is a member of a group. The value represents the UUID of the group to match against."
    )

    AppleDeviceGroupProperties = [
        MacDeviceFamilyProperty,
        MacDeviceVendorProperty,
        MacDeviceProductProperty,
        MacDeviceSerialNumber,
        MacDeviceEncryptedProperty,
        MacGroupProperty
    ]

    AppleDeviceGroupType = GroupType(
        GroupType.MacDeviceGroupType,
        "Apple Devices",
        AppleDeviceGroupProperties,
        Format.Mac
    )

    Types[GroupType.MacDeviceGroupType] = AppleDeviceGroupType


    WindowsGroupProperty = GroupProperty(
        GroupProperty.WindowsGroupId,
        "Device Control Group",
        "Match if a device is a member of a group. The value represents the UUID of the group to match against."
    )

    WindowsDeviceFamilyProperty = GroupProperty(
        GroupProperty.WindowsDeviceFamily,
        "Windows Device Family",
        "The Primary ID includes RemovableMediaDevices, CdRomDevices, WpdDevices, PrinterDevices.",
        [
            GroupProperty.WindowsCdRomDevices,
            GroupProperty.WindowsRemovableMediaDevices,
            GroupProperty.WindowsPrinterDevices,
            GroupProperty.WindowsPortableDevices
        ]
    )

    WindowsDeviceFriendlyNameProperty = GroupProperty(
        GroupProperty.WindowsDeviceFriendlyName,
        "Windows Device Friendly Name",
        "It's a string attached to the device, for example, Generic Flash Disk USB Device. It's the Friendly name in the Device Manager."
    )

    WindowsDeviceVendorProductProperty = GroupProperty(
        GroupProperty.WindowsDeviceVendorProduct,
        "Vendor Product Id (VID/PID)",
        "Vendor ID is the four-digit vendor code that the USB committee assigns to the vendor. Product ID is the four-digit product code that the vendor assigns to the device. It supports wildcard."
    )

    WindowsDeviceVendorProperty = GroupProperty(
        GroupProperty.WindowsDeviceVendor,
        "Vendor Id (VID)",
        "Vendor ID is the four-digit vendor code that the USB committee assigns to the vendor"
    )

    WindowsDeviceProductProperty = GroupProperty(
        GroupProperty.WindowsDeviceProduct,
        "Product Id (PID)",
        "Product ID is the four-digit product code that the vendor assigns to the device. It supports wildcard."
    )

    WindowsDeviceInstancePathProperty = GroupProperty(
        GroupProperty.WindowsDeviceInstancePath,
        "Windows Device Instance Path",
        "InstancePathId is a string that uniquely identifies the device in the system, for example, USBSTOR\\DISK&VEN_GENERIC&PROD_FLASH_DISK&REV_8.07\\8735B611&0. It's the Device instance path in the Device Manager. The number at the end (for example &0) represents the available slot and may change from device to device. For best results, use a wildcard at the end. For example, USBSTOR\\DISK&VEN_GENERIC&PROD_FLASH_DISK&REV_8.07\\8735B611*"
    )

    WindowsDeviceIdProperty = GroupProperty(
        GroupProperty.WindowsDeviceId,
        "Windows Device Id",
        "To transform Device instance path to Device ID format, see Standard USB Identifiers, for example, USBSTOR\\DISK&VEN_GENERIC&PROD_FLASH_DISK&REV_8.07",
    )

    WindowsDeviceHardwareIdProperty = GroupProperty(
        GroupProperty.WindowsDeviceHardwareId,
        "Windows Device Hardware",
        "A string that identifies the device in the system, for example, USBSTOR\\DiskGeneric_Flash_Disk___8.07. It's Hardware Ids in the Device Manager."
    )

    WindowsDeviceBusProperty = GroupProperty(
        GroupProperty.WindowsDeviceBus,
        "Windows Device Bus",
        "For example, USB, SCSI"
    )

    WindowsDeviceSerialNumberProperty = GroupProperty(
        GroupProperty.WindowsDeviceSerialNumber,
        "Windows Device Serial Number",
        "You can find SerialNumberId from Device instance path in the Device Manager, for example, 03003324080520232521 is SerialNumberId in USBSTOR\\DISK&VEN__USB&PROD__SANDISK_3.2GEN1&REV_1.00\\03003324080520232521&0"
    )

    WindowsDeviceEncryptionStateProperty = GroupProperty(
        GroupProperty.WindowsDeviceEncryptedState,
        "Windows Device Encryption State",
        "Checks the encryption state (e.g. Bitlocker) of a device",
        [
            GroupProperty.WindowsDeviceBitlockerEncrypted,
            GroupProperty.WindowsDeviceNotEncrypted
        ]
    )

    WinodwsPrinterConnectionProperty = GroupProperty(
        GroupProperty.WindowsPrinterConnection,
        "Windows Printer Connection",
        [
            GroupProperty.USBPrinterConnection,
            GroupProperty.CorporatePrinterConnection,
            GroupProperty.NetworkPrinterConnection,
            GroupProperty.UniversalPrinterConnection,
            GroupProperty.FilePrinterConnection,
            GroupProperty.CustomPrinterConnection,
            GroupProperty.LocalPrinterConnection
        ]

    )


    WindowsPrinterGroupProperties = [
        WindowsDeviceFamilyProperty,
        WindowsDeviceFriendlyNameProperty,
        WindowsDeviceVendorProductProperty,   
        WinodwsPrinterConnectionProperty,
        WindowsGroupProperty
    ]

    WindowsDeviceGroupProperties = [
        WindowsDeviceFamilyProperty,
        WindowsDeviceFriendlyNameProperty,
        WindowsDeviceVendorProductProperty,
        WindowsDeviceVendorProperty,
        WindowsDeviceProductProperty,
        WindowsDeviceInstancePathProperty,
        WindowsDeviceIdProperty,
        WindowsDeviceHardwareIdProperty,
        WindowsDeviceBusProperty,
        WindowsDeviceSerialNumberProperty,
        WindowsDeviceEncryptionStateProperty,
        WindowsGroupProperty
    ]

    WindowsDeviceGroupType = GroupType(
        GroupType.WindowsDeviceGroupType,
        "Windows Devices",
        WindowsDeviceGroupProperties
    )

    WindowsPrinterGroupType = GroupType(
        GroupType.WindowsPrinterGroupType,
        "Windows Printers",
        WindowsPrinterGroupProperties
    )

    Types[GroupType.WindowsDeviceGroupType] = WindowsDeviceGroupType
    
    NetworkNameProperty = GroupProperty(
        GroupProperty.NetworkName,
        "Network Name",
        "The name of the network"
    )

    NetworkCategoryProperty = GroupProperty(
        GroupProperty.NetworkCategory,
        "Network Category",
        "Only applicable for Network type Group",
        [
            GroupProperty.NetworkCategoryDomainAuthenticated,
            GroupProperty.NetworkCategoryPrivate,
            GroupProperty.NetworkCategoryPublic
        ]
    )

    NetworkDomainProperty = GroupProperty(
        GroupProperty.NetworkDomain,
        "Network Domain",
        "Domain property of the network",
        [
            GroupProperty.NonDomain,
            GroupProperty.DomainAuthenticated,
            GroupProperty.Domain
        ]
    )

    NetworkGroupProperties = [
        NetworkNameProperty,
        NetworkDomainProperty,
        NetworkCategoryProperty,
        WindowsGroupProperty
    ]

    NetworkGroupType = GroupType(
        GroupType.NetworkGroupType,
        "Windows Network",
        NetworkGroupProperties
    )

    Types[GroupType.NetworkGroupType] = NetworkGroupType

    VPNConnectionNameProperty = GroupProperty(
        GroupProperty.VPNConnectionName,
        "VPN Connection Name",
        "The name of the VPN Connection, supports wildcards"
    )

    VPNDnsSuffixProperty = GroupProperty (
        GroupProperty.VPNDnsSuffix,
        "VPN Connection DNS Suffix",
        "The value of VPN DNS Suffix, supports wildcards"
    )

    VPNServerAddressProperty = GroupProperty(
        GroupProperty.VPNServerAddress,
        "VPN Connection Server Address",
        "The value of the VPN server address, supports wildcards"
    )

    VPNConnectionStatusProperty = GroupProperty(
        GroupProperty.VPNConnectionStatus,
        "VPN Connection Status",
        "The status of the VPN Connection",
        [
            GroupProperty.VPNConnectionStatusConnected,
            GroupProperty.VPNConnectionStatusDisconnected
        ]
    )

    VPNConnectionProperties = [
        VPNConnectionNameProperty,
        VPNConnectionStatusProperty,
        VPNDnsSuffixProperty,
        VPNServerAddressProperty,
        WindowsGroupProperty
    ]

    VPNConnectionGroupType = GroupType(
        GroupType.VPNConnectionGroupType,
        "Windows VPN Connection",
        VPNConnectionProperties
    )

    Types[GroupType.VPNConnectionGroupType] = VPNConnectionGroupType

    FilePathProperty = GroupProperty(
        GroupProperty.FilePath,
        "File Path",
        "value of file path or name, supports wildcard"
    )

    MacFileTypeProperty = GroupProperty(
        GroupProperty.MacFileType,
        "File Type",
        "The type of file on Mac"
    )

    FileGroupProperties = [
        FilePathProperty,
        WindowsGroupProperty
    ]

    MacFileGroupProperties = [
        MacFileTypeProperty
    ]

    

    FileGroupType = GroupType(
        GroupType.FileGroupType,
        "Windows File",
        FileGroupProperties
    )

    Types[GroupType.FileGroupType] = FileGroupType

    MacFileGroupType = GroupType(
        GroupType.MacFileGroupType,
        "Mac File",
        MacFileGroupProperties,
        Format.Mac
    )

    Types[GroupType.MacFileGroupType] = MacFileGroupType

    PrintOutputFileNameProperty = GroupProperty(
        GroupProperty.PrintOutputFileName,
        "Print Job File Name",
        "The output destination file path for print to file. Wildcards are supported. For example, C:\\*\\Test.pdf"
    )

    PrintDocumentNameProperty = GroupProperty(
        GroupProperty.PrintDocumentName,
        "Print Job Document Name",
        "The source file path. Wildcards are supported. This path might not exist. For example, add text to a new file in Notepad, and then print without saving the file."
    )

    PrintJobGroupProperties = [
        PrintDocumentNameProperty,
        PrintOutputFileNameProperty,
        WindowsGroupProperty
    ]

    PrintJobGroupType = GroupType(
        GroupType.PrintJobType,
        "Windows Print Job",
        PrintJobGroupProperties
    )
    
    Types[GroupType.PrintJobType] = PrintJobGroupType

    supported_match_types = [
        MatchType.Any,
        MatchType.All
    ]

    AllGroupTypes = [
        WindowsDeviceGroupType,
        WindowsPrinterGroupType,
        NetworkGroupType,
        VPNConnectionGroupType,
        FileGroupType,
        MacFileGroupType,
        PrintJobGroupType,
        AppleDeviceGroupType
    ]

    

    def __init__(self,root,format,path=None):

        self.format = format
        self.set_path(path)
        self._properties = []
        self.clauses = []
        self.root = root
        self.conditions = {}

        self.group_type = None
        self.group_properties = {}

        self.description = ""

        if format == "gpo" or format =="oma-uri":

            self.id = root.attrib["Id"]
            if "Type" in root.attrib.keys():
                self.type = root.attrib["Type"]
            else:
                self.type = "Device"

            self.group_type = Group.Types[self.type]

            name_node = root.find(".//Name")
            if name_node is None:
                self.name = "?"
            else:
                self.name = name_node.text

            match_node = root.find(".//MatchType")
            if match_node is None:
                if "MatchType" in root.attrib.keys():
                    self.match_type = root.attrib["MatchType"]
                else:
                    self.match_type = "?"
            else:
                self.match_type = match_node.text
            
            descriptors = root.findall("./DescriptorIdList//")
            for descriptor in descriptors:

                if descriptor.tag == ET.Comment:
                    logger.debug("Skipping comment "+str(descriptor.text))
                    continue

                logger.debug("Getting group property for "+str(descriptor.tag))
                group_property = self.group_type.get_property_by_name(descriptor.tag)
                if group_property is None:
                    #This is the special case where they have the same group type (device),
                    #but different properties
                    if self.group_type.name == GroupType.WindowsDeviceGroupType and descriptor.tag == GroupProperty.WindowsPrinterConnection:
                        self.group_type = Group.WindowsPrinterGroupType
                        group_property = self.group_type.get_property_by_name(descriptor.tag)
                
                    else:
                        raise Exception("Unknown group property"+str(descriptor.tag)+" for "+self.group_type.label)
                

                self._properties.append(Property(group_property, descriptor.text))
                self.conditions[descriptor.tag] = descriptor.text


            
            

        elif format == "mac":
            if "id" in root.keys():
                self.id = root["id"]

            if "name" in root.keys():
                self.name = root["name"]

            if "$type" in root.keys():
                self.type = root["$type"]
                self.group_type = Group.Types[self.type]

            if "query" in root.keys():
                query = root["query"]

                if "$type" in query.keys():
                    self.match_type = query["$type"]

                if "clauses" in query.keys():
                    clauses = query["clauses"]
                    for clause in clauses:
                        self.clauses.append(Clause(clause, self.group_type, self.match_type))

                self.conditions = clauses

    
    def set_path(self,path):
        if path is not None:
            p = pathlib.Path(path)
            p = p.resolve()
            self.path = str(p)

    def get_oma_uri(self):
        return "./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/"+urllib.parse.quote_plus(self.id)+"/GroupData"
        
    def get_conditions(self):
        return self.conditions

    def toXML(self,indent = "\t"):

        out = indent + "<Group Id=\""+self.id+"\" Type=\""+self.type+"\">\n"
        out +=indent + "\t<!-- "+self.get_oma_uri()+" -->\n"
        out +=indent + "\t<Name>"+Util.xml_safe_text(self.name)+"</Name>\n"
        out +=indent + "\t<MatchType>"+self.match_type+"</MatchType>\n"
        out +=indent + "\t<DescriptorIdList>\n"
        
        for property in self._properties:
            tag = property.name
            text = property.value

            out += indent +"\t\t<"+tag+">"+Util.xml_safe_text(text)+"</"+tag+">\n"

        out += indent +"\t</DescriptorIdList>\n"
        out += indent +"</Group>"

        return out
    
    def toJSON(self,i=0):
        if i==0:
            return self.root
        else:
            return json.dumps(self.root,indent=i)
    
    def __str__(self):
        if self.format != "mac":
            return self.toXML()
        else:
            return self.toJSON(1)
    
    def __eq__(self,other):
        if self.match_type == other.match_type and len(self._properties) == len(other._properties):
            for property in self._properties:
                if property in other._properties:
                    continue
                else:
                    return False
            return True
        return self.id == other.id
    
    def __hash__(self):
        hashList = []
        for property in self._properties:
            key = property.name
            value = property.value
            hashList.append(key+"="+value)
            
        hashList.append("id="+self.id)    
        hashList.append ("type="+self.match_type)

        hashList.sort()
        return hash(str(hashList))

class Enforcement:

    Allow = "allow"
    Deny = "deny"
    AuditAllowed = "auditAllowed"
    AuditDenied = "auditDeny"

    def __init__(self,name,label,variations):
        self.name = name
        self.label = label
        self.variations = variations

    def __str__(self):
        return self.name
    
    def __eq__(self,other):
        return str(self) == str(other)
    
    def __hash__(self):
        return hash(str(self))
    
class PolicyRule:

    def read_device_properties(device_properties_node,device_properties_list,groups_list):
        for device_property in device_properties_node:
            device_property_name = device_property.tag
            device_property_value = device_property.text
            device_property_type = GroupType.get_property_by_name(
                Group.WindowsDeviceGroupType,device_property_name)
            
            if device_property_type is None:
                device_property_type = GroupType.get_property_by_name(
                    Group.WindowsPrinterGroupType,device_property_name)
                
            if device_property_type is None:
                raise Exception("Unknown Windows Device Property "+device_property_name)
            
            device_property =  Property(device_property_type,device_property_value)          

            device_properties_list.append(device_property)

            if device_property_type.name == GroupProperty.WindowsGroupId:
                groups_list.append(device_property_value)

    def add_mac_group(groupId,device_properties_list,groups_list):
        device_property =  Property(Group.MacGroupProperty,groupId)          
        device_properties_list.append(device_property)
        groups_list.append(groupId)


    Allow = Enforcement(Enforcement.Allow,"Allow",{
        "mac":"allow",
        "gpo":"Allow",
        "oma-uri":"Allow"
    })

    AuditAllowed = Enforcement(Enforcement.AuditAllowed,"Audit Allowed",{
        "mac":"auditAllow",
        "gpo":"AuditAllowed",
        "oma-uri":"AuditAllowed"
    })

    Deny = Enforcement(Enforcement.Deny,"Deny",{
        "mac":"deny",
        "gpo":"Deny",
        "oma-uri":"Deny"
    })

    AuditDenied = Enforcement(Enforcement.AuditDenied,"Audit Denied",{
        "mac":"auditDeny",
        "gpo":"AuditDenied",
        "oma-uri":"AuditDenied"
    })

    Enforcements = [
        Allow,Deny,AuditAllowed,AuditDenied
    ]


    def __init__(self,root, format, path=None, rule_index = 1):

                            
        self.root = root

        self.format = format
        self.set_path(path)

        self.rule_index = rule_index
        self.id = None
        self.name = None
        self.description = None
        self.included_device_properties = []
        self.included_groups = []

        self.excluded_groups = []
        self.excluded_device_properties = []

        self.entries = []

        self.entry_type = None

        if format == "gpo" or format =="oma-uri":

            self.id = root.attrib["Id"]
            name_node = root.find(".//Name")
            if name_node is None:
                self.name = "?"
            else:
                self.name = name_node.text

            included_device_properties_node = root.find(".//IncludedIdList")
            if not included_device_properties_node is None:
                included_device_properties = included_device_properties_node.findall(".//")
                PolicyRule.read_device_properties(
                    included_device_properties,
                    self.included_device_properties,
                    self.included_groups)

            excluded_device_properties_node = root.find(".//ExcludedIdList")
            if not excluded_device_properties_node is None:
                excluded_device_properties = excluded_device_properties_node.findall(".//")
                PolicyRule.read_device_properties(
                    excluded_device_properties,
                    self.excluded_device_properties,
                    self.excluded_groups)

            for entry in root.findall(".//Entry"):
                self.add_entry(Entry(entry,self.format))     

        elif format == "mac":
            if "id" in root.keys():
                self.id = root["id"]

            if "name" in root.keys():
                self.name = root["name"]

            if "includeGroups" in root.keys():
                for groupId in root["includeGroups"]:
                    PolicyRule.add_mac_group(groupId,self.included_device_properties,self.included_groups)
                
            
            
            if "excludeGroups" in root.keys():
                for groupId in root["excludeGroups"]:
                    PolicyRule.add_mac_group(groupId,self.excluded_device_properties,self.excluded_groups)
                
                
            if "entries" in root.keys():
                entries = root["entries"]
                for entry in entries:
                    self.add_entry(Entry(entry,self.format))

        #set the entry_type for the rule
        # if there is more than 1 make it a generic device
        for entry in self.entries:
            if self.entry_type is None:
                self.entry_type = entry.entry_type
            elif self.entry_type is not entry.entry_type:
                if self.format == "mac":
                    self.entry_type = Entry.AppleGeneric
                else:
                    self.entry_type = Entry.WindowsGeneric
                break
        

    def add_entry(self,entry):
        entry.rule = self
        self.entries.append(entry)
    
    def set_path(self,path):
        if path is not None:
            p = pathlib.Path(path)
            p = p.resolve()
            self.path = str(p)
        
    def get_oma_uri(self):
        return "./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/"+urllib.parse.quote_plus(self.id)+"/RuleData"
    
    def toXML(self,indent = "\t"):

        out = indent + "<PolicyRule Id=\""+self.id+"\" >\n"
        out +=indent + "\t<!-- "+self.get_oma_uri()+" -->\n"
        out +=indent + "\t<Name>"+Util.xml_safe_text(self.name)+"</Name>\n"
        
        out +=indent + "\t<IncludedIdList>\n"
        for device_property in self.included_device_properties:
            out += indent +"\t\t<"+device_property.name+">"+device_property.value+"</"+device_property.name+">\n"

        out +=indent + "\t</IncludedIdList>\n"

        out += indent +"\t<ExcludedIdList>\n"
        for device_property in self.excluded_device_properties:
            out += indent +"\t\t<"+device_property.name+">"+device_property.value+"</"+device_property.name+">\n"

        out += indent +"\t</ExcludedIdList>\n"

        for entry in self.entries:

            out += entry.toXML(indent+"\t")


        out += indent +"</PolicyRule>"

        #This should clean out any strange encodings
        encoded_btyes = str(out).encode(errors="ignore")
        return encoded_btyes.decode("utf-8")
    
    def toJSON(self,i=0):
        if i==0:
            return self.root
        else:
            return json.dumps(self.root,indent=i)
    
    def __eq__(self,other):
        return str(self) == str(other)
    
    def __hash__(self):
        if self.format == "mac":
            return hash(self.toJSON(1))
        else:
            return hash(self.toXML())
        
    def __str__(self):
        if self.format == "mac":
            return self.toJSON(4)
        else:
            return self.toXML()


class Option:

    def __init__(self,name,label,variations):
        self.name = name
        self.label = label
        self.variations = variations

    def __str__(self):
        return self.label

class Notifications:

    Nothing = Option("nothing","None",{
        "mac":[],
        "gpo": 0,
        "oma-uri":0
    })

    ShowNotification = Option("show_notification","Show notification",{
        "mac":"show_notification",
        "gpo": 1,
        "oma-uri":1
    })

    CreatePolicyTriggeredEvent = Option("send_event","Send event",{
        "mac":"send_event",
        "gpo": 2,
        "oma-uri":2
    })

    
    DontTriggerAudit = Option("disable","Disable",{
        "mac": "disable",
        "gpo": 4,
        "oma-uri": 4
    })

    CreateFileEventWithFile = Option("fileEvidenceWithFile","Create file evidence with file",{
        "mac": None,
        "gpo": 8,
        "oma-uri": 8
    })
        
    CreateFileEventNoFile = Option("fileEvidenceWithoutFile","Create file evidence without file",{
        "mac": None,
        "gpo": 16,
        "oma-uri": 16
    })


    def __init__(self,options,format):

        self.notifications = []

        if format == "mac" and options is None:
            self.notifications.append(Notifications.Nothing)
        elif options == 0:
            self.notifications.append(Notifications.Nothing)
        else:
            all_notifications = [
                Notifications.ShowNotification,
                Notifications.CreatePolicyTriggeredEvent,
                Notifications.DontTriggerAudit,
                Notifications.CreateFileEventWithFile,
                Notifications.CreateFileEventNoFile
            ]

            if format == "mac":
                for option in options:
                    for notification in all_notifications:
                        if notification.variations["mac"] == option:
                            self.notifications.append(notification)

            else:
                #On windows the options are a bit mask
                for notification in all_notifications:
                    if notification.variations[format] & options:
                        self.notifications.append(notification)

    def __str__(self):
        out = ""
        if len(self.notifications) == 0:
            out = "None"
        elif len(self.notifications) == 1:
            out = str(self.notifications[0])
        else:
            out = str(self.notifications[0])+" and "+str(self.notifications[1])

        return out
    
    def __int__(self):
        out = 0
        for notification in self.notifications:
            out = out + notification.variations["gpo"]

        return out


    def __iter__(self):
        return self.notifications.__iter__()
    
    def __next__(self):
        return self.notifications.__next__()

class WindowsEntryType:

    DiskReadMask = 0x01
    DiskWriteMask = 0x02
    DiskExecuteMask = 0x04
    FileReadMask = 0x08
    FileWriteMask = 0x10
    FileExecuteMask = 0x20
    PrintMask = 0x40

    access_masks = {
        DiskReadMask: "Disk Read",
        DiskWriteMask: "Disk Write",
        DiskExecuteMask: "Disk Execute",
        FileReadMask: "File Read",
        FileWriteMask: "File Write",
        FileExecuteMask: "File Execute",
        PrintMask: "Print"
    }

    access_mask_text_labels = {
        DiskReadMask: "Read",
        DiskWriteMask: "Write",
        DiskExecuteMask: "Execute",
        PrintMask: "Print"
    }

    allow_notification_masks = {
        0x04: "Disable",
        0x08: "Create File Evidence",
        0x10: "Create File Evidence withouy File"
    }

    deny_notification_masks = {
        0x04: "Disable"
    }

    audit_allowed_notification_masks = {
        0x01: "None",
        0x02: "Send event"
    }

    audit_denied_notification_masks = {
        0x01: "Show notification",
        0x02: "Send event"
    }

    notification_masks = {
        PolicyRule.Allow: allow_notification_masks,
        PolicyRule.AuditAllowed: audit_allowed_notification_masks,
        PolicyRule.Deny: deny_notification_masks,
        PolicyRule.AuditDenied: audit_denied_notification_masks
    }


    def getAccessMaskForPermissions(permissions):

        access_mask = 0
        for permission in permissions:
            if permissions[permission]:
                access_mask = access_mask + permission

        return access_mask


    def __init__(self,name, label,access_masks):
        self.name = name
        self.access_masks = access_masks

        self.access_types = {

        }

        for mask in self.access_masks:
            self.access_types[WindowsEntryType.access_masks[mask]] = {
                "label":WindowsEntryType.access_masks[mask]
            }
            

        self.label = label


    def __str__(self):
        return self.label

class MacEntryType:

    GenericRead = "generic_read"
    GenericWrite = "generic_write"
    GenericExecute = "generic_execute"

    notification_masks = {
        PolicyRule.Allow: ["disable_audit_allow"],
        PolicyRule.AuditAllowed: ["send_event"],
        PolicyRule.Deny: ["disable_audit_allow"],
        PolicyRule.AuditDenied: ["send_event","send_notification"]
    }


    def __init__(self,name, label, access_types):
        self.name = name
        self.access_types = access_types
        self.label = label

    def get_generic_access(self,permission):
        if permission in [MacEntryType.GenericRead, MacEntryType.GenericWrite, MacEntryType.GenericExecute]:
            return permission
         
        if permission in self.access_types.keys():
            return self.access_types[permission]["generic_access"]
        else:
            return None

    def __str__(self):
        return self.label

class Entry:

    #SID is case insensitive
    def getSID(entry):
        sid = entry.find("./Sid")
        if sid is not None:
            return sid.text
        
        sid = entry.find("./SID")
        if sid is not None:
            return sid.text
        
        return "All Users"
        

    
    WindowsPrinter = WindowsEntryType("windows_printer","Windows Printer",
        [0x40]
    )
    WindowsDevice  = WindowsEntryType("windows_device","Windows Removable Device",
        [0x01,0x02,0x04,0x08,0x10,0x20]
    )
    WindowsGeneric  = WindowsEntryType("windows_generic","Windows Generic Device",
        [0x01,0x02,0x04,0x08,0x10,0x20,0x40]
    )
    AppleDevice = MacEntryType("appleDevice","Apple Device",
        {
            "backup_device": {
                "generic_access": MacEntryType.GenericRead,
                "description": "",
                "label": "Backup device"
            },
            "update_device":{
                "generic_access": MacEntryType.GenericWrite,
                "description": "",
                "label": "Update device"
            },
            "download_photos_from_device":{
                "generic_access": MacEntryType.GenericRead,
                "description": "download photo(s) from the specific iOS device to local machine",
                "label": "Download photos"
            },
            "download_files_from_device":{ 
                "generic_access": MacEntryType.GenericRead,
                "description": "download file(s) from the specific iOS device to local machine",
                "label": "Download files"
            },
            "sync_content_to_device":{
                "generic_access": MacEntryType.GenericWrite,
                "description": "sync content from local machine to specific iOS device",
                "label": "Synch device"
            }
        }
    )
    AppleRemovableMedia = MacEntryType("removableMedia","Apple Removable Media",
        {
            "read":{
                "generic_access":MacEntryType.GenericRead,
                "label": "Read",
                "description":""
            },
            "write":{
                "generic_access":MacEntryType.GenericWrite,
                "label": "Write",
                "description":""
            },
            "execute":{
                "generic_access":MacEntryType.GenericExecute,
                "label": "Execute",
                "description":""
            }
        }
    )
    AppleGeneric = MacEntryType("generic", "Apple Generic Device", {
        MacEntryType.GenericRead: {
            "label": "Read",
            "description": "Equivalent to setting all access values denoted in this table that map to generic_read."
        },
        MacEntryType.GenericWrite:{
            "label": "Write",
            "description": "Equivalent to setting all access values denoted in this table that map to generic_write.",
        },
        MacEntryType.GenericExecute:{
            "label": "Execute",
            "description": "Equivalent to setting all access values denoted in this table that map to generic_execute."
        }
    })
    AppleBluetoothDevice = MacEntryType("bluetoothDevice","Apple Bluetooth Device",
        {
            "download_files_from_device": {
                "generic_access": MacEntryType.GenericRead,
                "label": "Download files",
                "description":""
            },
            "send_files_to_device": {
                "generic_access": MacEntryType.GenericWrite,
                "label": "Send files",
                "description":""
            }
        }
    )
    ApplePortableDevice = MacEntryType("portableDevice","Apple Portable Device",
        {
            "download_files_from_device": {
                "label": "Download files",
                "generic_access": MacEntryType.GenericRead,
                "description":""
            },
            "send_files_to_device":{
                "label": "Send files",
                "generic_access": MacEntryType.GenericWrite,
                "description":""
            },
            "download_photos_from_device": {
                "label": "Download photos",
                "generic_access": MacEntryType.GenericRead,
                "description":""
            },
            "debug": {
                "label": "Debug",
                "generic_access": MacEntryType.GenericExecute,
                "description": "ADB tool control"
            }

        }
    )

    WindowsEntryTypes = [
        WindowsPrinter,
        WindowsDevice,
        WindowsGeneric
    ]

    MacEntryTypes = [
        AppleBluetoothDevice,
        AppleDevice,
        AppleGeneric,
        ApplePortableDevice,
        AppleRemovableMedia
    ]

    AllEntryTypes = [
        WindowsPrinter,
        WindowsDevice,
        WindowsGeneric,
        AppleBluetoothDevice,
        AppleDevice,
        AppleGeneric,
        ApplePortableDevice,
        AppleRemovableMedia
    ]

    def get_enforcement(variation,format): 
        for enforcement in PolicyRule.Enforcements:
            variations = enforcement.variations
            variation_for_format = variations[format]
            if variation == variation_for_format:
                return enforcement
            
        print ("No enforcement for "+variation+" in format "+format)

    def __init__(self,entry,format = "gpo"):

        self.entry_type = None
        self.format = format

        self.parameters = None
        self.sid = "All Users"
        self.computersid = "All Computers"

        self.rule = None

        if format == "gpo" or format == "oma-uri":

            self.permissions = {
                WindowsEntryType.DiskReadMask: False,
                WindowsEntryType.DiskWriteMask: False,
                WindowsEntryType.DiskExecuteMask: False,
                WindowsEntryType.FileReadMask: False,
                WindowsEntryType.FileWriteMask: False,
                WindowsEntryType.FileExecuteMask: False,
                WindowsEntryType.PrintMask: False
            }

            

            self.id = entry.attrib["Id"]
            self.enforcement_type = entry.find("./Type").text
            self.enforcement = Entry.get_enforcement(self.enforcement_type,format)
            
            
            self.options_mask = entry.find("./Options").text
            
            self.notifications = Notifications(int(self.options_mask),format)
            self.options_text = str(self.notifications)
            
            self.access_mask = entry.find("./AccessMask").text
            
            has_mixed_entry_type = False

            
            

        
            
            self.access_mask_text = ""
            

            for mask in WindowsEntryType.access_masks.keys():
                if int(self.access_mask) & mask:
                    self.permissions[mask] = True
                    if mask in WindowsEntryType.access_mask_text_labels:
                        self.access_mask_text = self.access_mask_text+", "+WindowsEntryType.access_mask_text_labels[mask]

                    if self.entry_type is None:
                        if mask == 64:
                            self.entry_type = Entry.WindowsPrinter
                        else:
                            self.entry_type = Entry.WindowsDevice

                    elif mask ==64:
                        has_mixed_entry_type = True
                            


            # The entry type determins the layout of the report
            if has_mixed_entry_type:
                self.entry_type = Entry.WindowsGeneric

            #replaces last , with and
            self.access_mask_text = self.access_mask_text[2:]
            self.access_mask_text = Util.rreplace(self.access_mask_text,","," and",1)


            #notification_masks = WindowsEntryType.notification_masks[self.enforcement_type]
            #for mask in notification_masks:
            #    if int(self.options_mask) & mask:
            #        self.notifications.append(notification_masks[mask])

           
            self.sid = Entry.getSID(entry)

            computersid = entry.find("./ComputerSid")
            if computersid is not None:
                self.computersid = computersid
            else:
                self.computersid = "All Computers"

            parameters = entry.find("./Parameters")
            if parameters is not None:
                self.parameters = Parameters(parameters)
            
        
        elif format == "mac":

            self.permissions = {}
            self.generic_windows_permissions = {
                WindowsEntryType.DiskReadMask: False,
                WindowsEntryType.DiskWriteMask: False,
                WindowsEntryType.DiskExecuteMask: False,
                WindowsEntryType.FileReadMask: False,
                WindowsEntryType.FileWriteMask: False,
                WindowsEntryType.FileExecuteMask: False,
                WindowsEntryType.PrintMask: False
            }
            self.generic_mac_permissions = {
                MacEntryType.GenericRead:False,
                MacEntryType.GenericWrite:False,
                MacEntryType.GenericExecute:False 
            }

            self.id = entry["id"]
            
            

            if "$type" in entry.keys():
                type = entry["$type"]

                if type == "appleDevice":
                    self.entry_type = Entry.AppleDevice
                elif type == "removableMedia":
                    self.entry_type = Entry.AppleRemovableMedia
                elif type == "generic":
                    self.entry_type = Entry.AppleGeneric
                elif type == "bluetoothDevice":
                    self.entry_type = Entry.AppleBluetoothDevice
                elif type == "portableDevice":
                    self.entry_type = Entry.ApplePortableDevice
                else:
                    logger.warn("Unknown type "+self.entry_type)
                    self.entry_type = Entry.AppleGeneric

                
                read_permissions = []
                write_permissions = []
                execute_permissions = []
                
                for access_type in self.entry_type.access_types:
                    generic_access = self.entry_type.get_generic_access(access_type)

                    if generic_access == MacEntryType.GenericRead:
                        read_permissions.append(access_type)
                    elif generic_access == MacEntryType.GenericWrite:
                        write_permissions.append(access_type)
                    else:
                        execute_permissions.append(access_type)

                #order the permissions rwx
                self.all_permissions = read_permissions + write_permissions + execute_permissions        

                if "enforcement" in entry.keys():
                    enforcement_obj = entry["enforcement"]
                    self.enforcement = Entry.get_enforcement(enforcement_obj["$type"],"mac")

                    if "options" in enforcement_obj.keys():
                        self.notifications = Notifications(enforcement_obj["options"],"mac")
                    else:
                        self.notifications = Notifications(None,"mac")
                    

                self.access_mask = 0

                if "access" in entry.keys():
                    self.access = entry["access"]
                    for permission in self.all_permissions:
                        enabled = permission in self.access
                        generic_access = self.entry_type.get_generic_access(permission)

                        if generic_access is MacEntryType.GenericRead:
                            self.generic_windows_permissions[WindowsEntryType.DiskReadMask] = enabled
                            self.generic_windows_permissions[WindowsEntryType.FileReadMask] = enabled
                            self.access_mask = self.access_mask + WindowsEntryType.DiskReadMask + WindowsEntryType.FileReadMask
                            self.generic_mac_permissions[MacEntryType.GenericRead] = enabled
                         
                        elif generic_access is MacEntryType.GenericWrite:
                            self.generic_windows_permissions[WindowsEntryType.DiskWriteMask] = enabled
                            self.generic_windows_permissions[WindowsEntryType.FileWriteMask] = enabled
                            self.access_mask = self.access_mask + WindowsEntryType.DiskWriteMask + WindowsEntryType.FileWriteMask
                            self.generic_mac_permissions[MacEntryType.GenericWrite] = enabled

                        elif generic_access is MacEntryType.GenericExecute:
                            self.generic_windows_permissions[WindowsEntryType.DiskExecuteMask] = enabled
                            self.generic_windows_permissions[WindowsEntryType.FileExecuteMask] = enabled
                            self.access_mask = self.access_mask + WindowsEntryType.DiskExecuteMask + WindowsEntryType.FileExecuteMask
                            self.generic_mac_permissions[MacEntryType.GenericExecute] = enabled
                            


    def has_conditions(self):
        return self.parameters is not None or self.sid != "All Users" or self.computersid != "All Computers"

    def has_user_condition(self):
        return self.sid != "All Users"
    
    def has_computer_condition(self):
        return self.computersid != "All Computers"
    
    def has_parameters(self):
        return self.parameters is not None
    
    def get_condition_match_type(self):
        condition_match_type = None

        if self.has_conditions():
            if self.parameters is not None:
                condition_match_type = self.parameters.match_type
            else:
                #This is if there is a user or computer condition
                condition_match_type = MatchType.All
        
        return condition_match_type
    
    def get_group_ids(self):
        if self.parameters is not None:
            return self.parameters.get_group_ids()
        else:
            return []
    

    def getElementTree(self):

        logger.debug("Returning Element Tree for entry")

        entry_xml = ET.Element("Entry", Id=self.id)

        logger.debug("Id="+self.id)

        type_xml = ET.SubElement(entry_xml,"Type")
        type_xml.text = self.enforcement.variations["gpo"]
        logger.debug("Set type text to "+type_xml.text)

        access_mask_xml = ET.SubElement(entry_xml,"AccessMask")

        access_mask_xml.text = str(self.access_mask)
        logger.debug("Set access mask text to "+access_mask_xml.text)

        options_xml = ET.SubElement(entry_xml,"Options")
        options_xml.text = str(int(self.notifications))

        logger.debug("Set options text to "+options_xml.text)

        logger.debug("Creating an entry with xml="+ET.tostring(entry_xml,method="xml").decode("utf-8"))        
     
        return entry_xml

    def toXML(self,indent):

        out = indent + "<Entry Id=\""+self.id+"\">\n"
        out += indent +"\t<Type>"+self.enforcement.variations["gpo"]+"</Type>\n"
        out += indent +"\t<AccessMask>"+str(self.access_mask)+"</AccessMask>\n"
        out += indent +"\t<Options>"+str(int(self.notifications))+"</Options>\n"

        if self.sid != "All Users":
            out += indent +"\t<Sid>"+self.sid+"</Sid>\n"

        if self.parameters is not None:
            out += self.parameters.toXML(indent+"\t")
            

        out += indent +"</Entry>\n"

        return out
    
    def validateSupport(self,feature_data,support):

        unsupported_access_masks = feature_data["unsupported_access_masks"]

        for mask in self.permissions.keys():
            enabled = self.permissions[mask]
            if enabled: 
                if unsupported_access_masks[mask]:
                    if mask not in WindowsEntryType.access_masks:
                        support.issues.append(mask+" is an unsupported access mask")
                    else:
                        support.issues.append(WindowsEntryType.access_masks[mask]+" ("+str(mask)+") is an unsupported access mask")
                
                

        if self.enforcement not in feature_data["supported_notifications"]:
            support.issues.append("Unsupported type of entry "+self.enforcement)
        else:
            supported_notifications = feature_data["supported_notifications"][self.enforcement]["notifications"]
            #notification_masks_for_type = WindowsEntryType.notification_masks[self.enforcement]
            
            for notification in self.notifications:
                if notification not in supported_notifications:
                    support.issues.append(notification.label+" is an unsupported notification.")

        if self.parameters is not None:
            if "parameters" not in feature_data.keys():
                support.issues.append("Parameters are not supported")

        
class Parameters:

    def __init__(self,parameters):
        self.match_type = parameters.attrib['MatchType']
        self.conditions = []
        for condition in parameters.findall("./"):
            match condition.tag:
                case "Network":
                    self.conditions.append(Condition(condition))
                case "VPNConnection":
                    self.conditions.append(Condition(condition))
                case "File":
                    self.conditions.append(Condition(condition))
                case "Parameters":
                    self.conditions.append(Parameters(condition))
                case other:
                    raise Exception('Unknown condition '+condition.tag)

    def get_group_ids(self):
        groups = []
        for condition in self.conditions:
            group_ids = condition.get_group_ids()
            for group_id in group_ids:
                groups.append(group_id)

        return groups

    def toXML(self,indent):

        out = indent + "<Parameters MatchType=\""+self.match_type+"\">\n"

        for condition in self.conditions:
            out += condition.toXML(indent+"\t")

        out += indent + "</Parameters>\n"

        return out

class Condition:
        
    
    def __init__(self,condition):
        self.match_type = condition.attrib['MatchType']
        
        self.groups = []
        self.properties = []

        self.tag = condition.tag
        self.condition_type = condition.tag
        self.read_condition_properties(condition.findall(".//"))


    def get_group_ids(self):
        return self.groups
    
    def toXML(self,indent):
        out = indent + "<"+self.tag+" MatchType=\""+self.match_type+"\">\n"

        for group in self.groups:
            out += indent +"\t<GroupId>"+group+"</GroupId>\n"

        out += indent + "</"+self.tag+">\n"

        return out
    
    def read_condition_properties(self,condition_properties):
        
        for condition_property in condition_properties:

            condition_property_name = condition_property.tag
            condition_property_value = condition_property.text

            self.condition_type = Group.Types[self.tag]

            condition_property_type = GroupType.get_property_by_name(
                self.condition_type,condition_property_name)
                
            if condition_property_type is None:
                raise Exception("Unknown "+self.condition_type.label+" property "+condition_property_name)
            
            condition_property =  Property(condition_property_type,condition_property_value)          

            self.properties.append(condition_property)

            if condition_property_type.name == GroupProperty.WindowsGroupId:
                self.groups.append(condition_property_value)


class Support:

    def __init__(self):
        self.issues = []

    def isValid(self):
        return len(self.issues) == 0
    
    def __add__(self,other):
        result = copy.copy(self)
        result.issues = list(set(other.issues+self.issues))

        return result
    
class Feature:

    def get_unsupported_dictionary(supported_values=None):

        if supported_values is None:
            return {
                1: False,
                2: False,
                4: False,
                8: False,
                16:False,
                32:False,
                64: False
            }
        
        unsupported_access_masks = {
            1: True,
            2: True,
            4: True,
            8: True,
            16: True,
            32: True,
            64: True
        } 

        for value in supported_values:
            unsupported_access_masks[value] = False

        return unsupported_access_masks

    def __init__(self, feature_data):
        self.feature_data = feature_data
        self.support_data = {}
        entry_data = self.feature_data["entry"]
        if "access_masks" in entry_data.keys():
            entry_data["unsupported_access_masks"] = Feature.get_unsupported_dictionary(entry_data["access_masks"])
        else:
            entry_data["unsupported_access_masks"] = Feature.get_unsupported_dictionary()

        for type in entry_data["supported_notifications"]:
            notifications = entry_data["supported_notifications"][type]["notifications"]
            #entry_data["supported_notifications"][type]["unsupported_notifications"] = Feature.get_unsupported_dictionary(notifications)



    def get_support_for(self,object):

        if object.id in self.support_data.keys():
            return self.support_data[object.id]
        
        support = Support()
        self.support_data[object.id] = support

        match object.__class__.__name__:
            case "Group":
                group_support = self.feature_data["group"]
                supported_group_types = group_support["supported_types"]
                if object.group_type not in supported_group_types:
                    support.issues.append(object.group_type.label+" groups not supported.")
                elif "unsupported_descriptors" in self.feature_data["group"].keys():
                    unsupported_descriptors = self.feature_data["group"]["unsupported_descriptors"]
                    if object.group_type in unsupported_descriptors.keys():
                        unsupported_descriptors_for_group = unsupported_descriptors[object.group_type]
                        if hasattr(object,"_properties"):
                            for property in object._properties:
                                for unsupported_descriptor_for_group in unsupported_descriptors_for_group:
                                    logger.debug("Checking "+str(property.name)+" for unsupported descriptors "+unsupported_descriptor_for_group.name)
                                    if property.name == unsupported_descriptor_for_group.name:
                                        support.issues.append(property.name+" not supported" )
                    

                supported_match_types = group_support["match_types"]
                if object.match_type not in supported_match_types:
                    support.issues.append(object.match_type+" not supported.")

            case "PolicyRule":
                
                entry_support = self.feature_data["entry"]
                for entry in object.entries:
                    entry.validateSupport(entry_support,support)


        return support


WindowsFeature = Feature(
        {
            "group": {
               "supported_types": [
                    Group.WindowsDeviceGroupType,
                    Group.WindowsPrinterGroupType,
                    Group.FileGroupType,
                    Group.NetworkGroupType,
                    Group.VPNConnectionGroupType,
                    Group.PrintJobGroupType
               ],
                "match_types": [MatchType.All,MatchType.Any]
            },   
            "entry":{
                "supported_types":{
                    "windows_printer": Entry.WindowsPrinter,
                    "windows_device": Entry.WindowsDevice
                },
                "supported_notifications":{
                    PolicyRule.Allow:{
                        "notifications":[
                            Notifications.Nothing,
                            Notifications.DontTriggerAudit,
                            Notifications.CreateFileEventNoFile,
                            Notifications.CreateFileEventWithFile]
                    },
                    PolicyRule.AuditAllowed:{
                        "notifications":[
                            Notifications.Nothing,
                            Notifications.CreatePolicyTriggeredEvent]
                    },
                    PolicyRule.Deny:{
                        "notifications":[
                            Notifications.Nothing,
                            Notifications.DontTriggerAudit
                        ]
                    },
                    PolicyRule.AuditDenied:{
                        "notifications":[
                            Notifications.Nothing,
                            Notifications.ShowNotification,
                            Notifications.CreatePolicyTriggeredEvent
                        ]
                    }
                }
            }
        }
    )
    
IntuneUXFeature = Feature(
    {
        "group": {
            "supported_types": [
                Group.WindowsDeviceGroupType,
                Group.WindowsPrinterGroupType
            ],
            "match_types": [MatchType.All,MatchType.Any],
            "unsupported_descriptors": {
                Group.WindowsDeviceGroupType: [
                    Group.WindowsDeviceEncryptionStateProperty
                ]
            }
        },
        "entry":{
            "access_masks":[1,2,4,64],
             "supported_notifications":{
                    PolicyRule.Allow:{
                        "notifications":[
                            Notifications.Nothing,
                            Notifications.DontTriggerAudit]
                    },
                    PolicyRule.AuditAllowed:{
                        "notifications":[
                            Notifications.Nothing,
                            Notifications.CreatePolicyTriggeredEvent]
                    },
                    PolicyRule.Deny:{
                        "notifications":[
                            Notifications.Nothing,
                            Notifications.DontTriggerAudit
                        ]
                    },
                    PolicyRule.AuditDenied:{
                        "notifications":[
                            Notifications.Nothing,
                            Notifications.ShowNotification,
                            Notifications.CreatePolicyTriggeredEvent
                        ]
                    }
                }
            }
        }
    )
    
class api:

    '''
                    entry_type=Entry.WindowsDevice,
                    enforcement=PolicyRule.Allow,
                    permissions={
                        WindowsEntryType.DiskReadMask: True,
                        WindowsEntryType.FileReadMask: True
                    },
                    notifications=Notifications(0,Format.OMA_URI),
    '''

    entriesByName = {
        "Allow full access":{
            "entry_type": Enforcement.Allow,
            "permissions": {
                WindowsEntryType.DiskReadMask: True,
                WindowsEntryType.DiskWriteMask: True,
                WindowsEntryType.DiskExecuteMask: True,
                WindowsEntryType.FileReadMask: True,
                WindowsEntryType.FileWriteMask: True,
                WindowsEntryType.FileExecuteMask: True
            },
            "notifications": Notifications(0,Format.OMA_URI)
        },
        "Audit write access":{
            "entry_type":Enforcement.AuditAllowed,
            "AccessMask":18,
            "Options": 2
        },
        "Allow read access":
        {
            "Type":Enforcement.Allow,
            "AccessMask":9,
            "Options":0
        },
        "Deny write and execute access":{
            "Type":Enforcement.Deny,
            "AccessMask":54,
            "Options":3
        }
    }

    def newGUID():
        return "{"+str(uuid.uuid4())+"}"


    def __init__(self,path=os.getcwd(),
                 clientId=None,
                 tenantId=None,
                 clientSecret=None, 
                 templates_path = "templates"):
        
        logger.debug("Created instance of device control api")

        logger.debug("localpath="+path)
        logger.debug("Templates Path="+templates_path)
        templateLoader = jinja2.FileSystemLoader(searchpath=templates_path)
        self.templateEnv = jinja2.Environment(loader=templateLoader)



        self.groups = {}
        self.rules = {}

        self.clientId = clientId
        self.tenantId = tenantId
        self.clientSecret = clientSecret

        self.graph = None

        self.path = path
        
        self.policies = {}

            
        pass

    async def connectToGraph(self):

        if self.clientId is not None and self.tenantId is not None and self.clientSecret is not None:
            from mdedevicecontrol.dcgraph import Graph

            self.graph = Graph(self.tenantId,self.clientId,self.clientSecret)

        else:
            raise Exception("No credentials to connect to graph")
        
    def createProperty(self,groupProperty,value):
        logger.debug("Creating property for "+str(groupProperty.name)+" value="+value)
        return Property(groupProperty,value)

    def createGroup(self,name, 
                    group_type = Group.WindowsDeviceGroupType, 
                    match_type = MatchType.Any,
                    properties = [],
                    id = None):
        
        if id is None:
            id = api.newGUID()
            logger.debug("Generating UUID="+id+" for group")

        logger.debug("Creating a group name="+name+" match_type="+match_type+" id="+id)
        
        '''
            <Group Id="{33e06f08-8787-4219-9dca-5872854f9d79}" Type="Device">
		        <!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B33e06f08-8787-4219-9dca-5872854f9d79%7D/GroupData -->
		        <Name>bitlocker encrypted USBs</Name>
		        <MatchType>MatchAll</MatchType>
		        <DescriptorIdList>
			        <PrimaryId>RemovableMediaDevices</PrimaryId>
			        <DeviceEncryptionStateId>BitlockerEncrypted</DeviceEncryptionStateId>
		        </DescriptorIdList>
	        </Group>
        '''

        
        group_xml = ET.Element("Group", Id=id, Type=group_type.name)
            
        oma_uri_comment = ET.Comment("./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/"+urllib.parse.quote(id)+"/GroupData")
        group_xml.append(oma_uri_comment)

        name_xml = ET.SubElement(group_xml,"Name")
        name_xml.text = name

        match_type_xml = ET.SubElement(group_xml,"MatchType")
        match match_type:
            case MatchType.Any:
                match_type_xml.text = MatchType.Any
            case MatchType.All:
                match_type_xml.text = MatchType.All
            case _:
                logger.warn("Unknown MatchType "+match_type)
        
        descriptorId_list = ET.SubElement(group_xml,"DescriptorIdList")
        for property in properties:
            comment = property.label
            tag_name = property.name
            tag_text = property.value

            logger.debug("Adding property "+str(property))
            
            if comment is not None:
                descriptorId_list.append(ET.Comment(comment))

            if tag_name is not None:
                tag = ET.SubElement(descriptorId_list,tag_name)
                tag.text = tag_text

        logger.debug("Creating a group with xml="+ET.tostring(group_xml,method="xml").decode("utf-8"))
        group = Group(group_xml,Format.OMA_URI)
        self.groups[group.id] = group

        return group
    

    def createGroupOfWindowsDevicesBySerialNumber(self,name,values = [], id=None):
        return self.createGroupOfWindowsDevices(name,property=Group.WindowsDeviceSerialNumberProperty, values=values,id=id)


    def createGroupOfWindowsDevices(self,name, 
                    property = Group.WindowsDeviceVendorProductProperty,
                    values = [],
                    id = None):
        
        group_type = Group.WindowsDeviceGroupType
        match_type = MatchType.Any

        properties = []

        for value in values:
            property = self.createProperty(property,value)
            properties.append(property)

        return self.createGroup(name,properties=properties,group_type=group_type,match_type=match_type,id=id)


    def createEntryByName(self,entry_name):
        pass

    def createEntry(self,
                    entry_type=Entry.WindowsDevice,
                    enforcement=PolicyRule.Allow,
                    permissions={
                        WindowsEntryType.DiskReadMask: True,
                        WindowsEntryType.FileReadMask: True
                    },
                    notifications=Notifications(0,Format.OMA_URI),
                    id=None):
        '''
        <Entry Id="{467726b6-a548-4f09-80d0-e8a0efc90bce}">
		    <Type>Allow</Type>
		    <AccessMask>63</AccessMask>
		    <Options>0</Options>
	    </Entry>
        '''

        if id is None:
            id = api.newGUID()
            logger.debug("Generating UUID="+id+" for entry")

        logger.debug("Creating an entry with properties type="+entry_type.label+" enforcement="+enforcement.label+" permissions="+str(permissions)+" notifications="+str(notifications)+" id="+id)
        
        entry_xml = ET.Element("Entry", Id=id)

        type_xml = ET.SubElement(entry_xml,"Type")
        type_xml.text = enforcement.variations[Format.OMA_URI]

        access_mask_xml = ET.SubElement(entry_xml,"AccessMask")

        if entry_type in Entry.WindowsEntryTypes:
            access_mask_xml.text = str(WindowsEntryType.getAccessMaskForPermissions(permissions))
            logger.debug("Set access mask text to "+access_mask_xml.text)

        options_xml = ET.SubElement(entry_xml,"Options")
        options_xml.text = str(int(notifications))

        logger.debug("Set options text to "+options_xml.text)

        logger.debug("Creating an entry with xml="+ET.tostring(entry_xml,method="xml").decode("utf-8"))        
        
        return Entry(entry_xml)


    def createRule(self,rule_name,
                   included_groups = [], 
                   excluded_groups = [], 
                   entries = [], 
                   id = None):
        

        '''
        <PolicyRule Id="{f7e75634-7eec-4e67-bec5-5e7750cb9e02}"> 
<!-- Allow Any Read activity -->
<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7bf7e75634-7eec-4e67-bec5-5e7750cb9e02%7d/RuleData -->
   <Name>Allow Read Activity</Name>
   <IncludedIdList>
		<GroupId>{9b28fae8-72f7-4267-a1a5-685f747a7146}</GroupId>
   </IncludedIdList>
   <ExcludedIdList>
   </ExcludedIdList>
   <Entry Id="{27c79875-25d2-4765-aec2-cb2d1000613f}">
      <Type>Allow</Type>
      <Options>0</Options>
      <AccessMask>9</AccessMask>
   </Entry>
    <Entry Id="{b280c2bf-ca5d-46a1-afc9-7e34d8098ca7}">
      <Type>AuditAllowed</Type>
      <Options>2</Options>
      <AccessMask>9</AccessMask>
   </Entry>
</PolicyRule>
        '''
        
        if id is None:
            id = api.newGUID()
            logger.debug("Generating UUID="+id+" for rule")

        rule_xml = ET.Element("PolicyRule", Id=id)
        oma_uri_comment = ET.Comment("./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/"+urllib.parse.quote(id)+"/RulesData")
        rule_xml.append(oma_uri_comment)

        name_xml = ET.SubElement(rule_xml,"Name")
        name_xml.text = rule_name

        included_xml = ET.SubElement(rule_xml,"IncludedIdList")

        for included_group in included_groups:

            group_xml = ET.SubElement(included_xml,"GroupId")
            group_xml.text = included_group.id

        excluded_xml = ET.SubElement(rule_xml,"ExcludedIdList")

        for excluded_group in excluded_groups:

            group_xml = ET.SubElement(excluded_xml,"GroupId")
            group_xml.text = excluded_group.id

        for entry in entries:

            entry_xml = entry.getElementTree()
            rule_xml.append(entry_xml)


        logger.debug("Creating rule with xml="+ET.tostring(rule_xml,method="xml").decode("utf-8"))        
        rule = PolicyRule(rule_xml,Format.OMA_URI)
        self.rules[rule.id] = rule

        return rule
            


    def createPolicy(self,name, 
                     version = "v1", 
                     os = "windows",
                     description = None,
                     rules = [],
                     groups = []):

        import mdedevicecontrol.dcintune as intune

        policy = intune.Package.Policy(self.graph)
        policy.name = name
        policy.version = version
        policy.os = os
        policy.description = "A policy"

        if description is not None:
            policy.description = description

        for rule in rules:
            policy.addRule(rule)

        for group in groups:
            policy.addGroup(group)

        self.policies[policy.name] = policy
        return policy
        

    def save(self,name="package"):

        import mdedevicecontrol.dcintune as intune

        
        if len(self.policies) > 0:
            self.package = intune.Package(name,self.templateEnv)

            for policy_name in self.policies:
                policy = self.policies[policy_name]
                self.package.addPolicy(policy)


            self.package.save(self.path,
                 rule_template_name="dcutil.j2",
                 readme_template_name="readme.j2",
                 description_template_name="description.j2")

            return


        package_path = pathlib.PurePath(os.path.join(self.path,name))
        if not os.path.isdir(package_path):
            os.mkdir(package_path)

        path_map = {}

        for layout_path in intune.Package.layout:
            orig_path = str(layout_path)

            layout_path = layout_path.replace(".",os.sep)
            layout_path = pathlib.PurePath(os.path.join(package_path,layout_path)) 
            if not os.path.isdir(layout_path):
                os.mkdir(layout_path)

            path_map[orig_path] = layout_path

        for group_id in self.groups:

            group = self.groups[group_id]
            logger.debug("Saving group "+str(group_id)+" class="+str(group.__class__))
            logger.debug("Name Class="+str(group.name.__class__))
            logger.debug("Group Name="+str(group.name)) 
            group_file_path = pathlib.PurePath(os.path.join(path_map[intune.Package.WINDOWS_GROUPS_PATH],group.name+".xml"))
            group_file = open(group_file_path,"w")
            group_file.write(str(group))
            group_file.close()

            logger.info("Exporting group "+group.name+" to "+str(group_file_path))

        for rule_id in self.rules:
                
            rule = self.rules[rule_id]    
            rule_file_path = pathlib.PurePath(os.path.join(path_map[intune.Package.WINDOWS_RULES_PATH],rule.name+".xml"))
            rule_file = open(rule_file_path,"w")
            rule_file.write(str(rule))
            rule_file.close()

            logger.info("Exporting rule "+rule.name+" to "+str(rule_file_path))

    def copy(self,object):

        logger.debug("Creating a copy of "+str(object.__class__.__name__))

        match str(object.__class__.__name__):
            case "Entry":
                new_entry = copy.deepcopy(object)
                logger.debug("Changing id of copy id="+object.id)
                new_entry.id = api.newGUID()
                logger.debug("New id is "+new_entry.id)
                return new_entry
            case "Group":
                new_group = copy.deepcopy(object)
                logger.debug("Changing id of copy id="+object.id)
                new_group.id = api.newGUID()
                logger.debug("New id is "+new_group.id)
                self.groups[new_group.id] = new_group
                return new_group
            case _:
                logger.warning("Can't copy "+str(object.__class__.__name__))
                return object

    async def deploy(self):

        if self.package is None:
            logger.info("No package to deploy.")
            return
        
        await self.package.deploy(self.graph)
        self.package.save_metadata(self.path)


class CommandLine:

    async def process_args(args):     
        print(str(args))
        if not "operation" in args or args.operation is None:
            return
    
        if "DC_CONFIG_PATH" in os.environ:
            dc_config_path = os.environ["DC_CONFIG_PATH"]
        else: 
            dc_config_path = str(pathlib.Path(os.path.join(os.getcwd(),"mdedevicecontrol.conf")).resolve())

        if not os.path.exists(dc_config_path):
            print("Error: No DC Config found at "+dc_config_path)
            return
    

        if "DC_LOG_PATH" in os.environ:
            dc_log_path = os.environ["DC_LOG_PATH"]
        else:
            dc_log_path = "dc.log"
        
        config = ConfigParser()
        config.read(dc_config_path)

        import logging.config
        logging.config.fileConfig(dc_config_path,defaults={
            "args":"('"+dc_log_path+"',)"
        })

        #set up templat env
        templates_path=os.path.join(pathlib.Path(__file__).parent,"templates")
        templateLoader = jinja2.FileSystemLoader(templates_path)
        CommandLine.templateEnv = jinja2.Environment(loader=templateLoader)
        CommandLine.rule_template_name = config["templates"]["rule"]
        CommandLine.readme_template_name = config["templates"]["readme"]
        CommandLine.description_template_name = config["templates"]["description"]


        logger.info("Operation="+args.operation)

        match args.operation:
            case "init":
                if args.init_source is None:
                    CommandLine.init(args)
                elif args.init_source == "xlsx":
                    CommandLine.init_with_xlsx(args,config)
            case "validate":
                if args.validate_options == "graph":
                    token = await CommandLine.validate_graph(args,config)


        pass

    def init(args):
        
        from mdedevicecontrol.dcintune import Package

        cwd = pathlib.Path(os.getcwd())
        
        p = Package(cwd.name,templateEnv=CommandLine.templateEnv)

        

        p.save(str(cwd.parent),
               CommandLine.rule_template_name,
               CommandLine.readme_template_name,
               CommandLine.description_template_name)



        pass

    async def validate_graph(args,config):

        cred_type = "user"
        if args.authentication_type is not None:
            logger.debug("authentication_type="+args.authentication_type)
            cred_type = args.authentication_type

        from mdedevicecontrol.dcintune import Graph

        tenantId = None
        clientId = None
        clientSecret = None


        if "DC_TENANT_ID" in os.environ:
            tenantId = os.environ["DC_TENANT_ID"]

        if "DC_CLIENT_ID" in os.environ:
            clientId = os.environ["DC_CLIENT_ID"]

        if "DC_CLIENT_SECRET" in os.environ:
            clientSecret = os.environ["DC_CLIENT_SECRET"]

        
        scopes = config["graph"]["scopes"]

        if cred_type == "user":
            graph = Graph(tenantId=tenantId,clientId=clientId,clientSecret=None,scopes=scopes)
            token = await graph.get_user_token()
        else:
            graph = Graph(tenantId=tenantId,clientId=clientId,clientSecret=clientSecret,scopes=scopes)
            token = await graph.get_app_only_token()

    def init_with_xlsx(args,config):

        xlsx_file_path = str(pathlib.Path(args.file).resolve())
        if os.path.exists(xlsx_file_path):
            logger.info("file="+xlsx_file_path)
        else:
            logger.error(xlsx_file_path+" not found")
            return
        
        import pandas as pd

        xslx_entries =pd.read_excel(xlsx_file_path,sheet_name="Entries")

        logger.debug(str(xslx_entries))

        entries = {}

        dc = api()

        for index,row in xslx_entries.iterrows():

            name = str(row["Name"]).strip()
            type = row["Type"]
            notification = row["Notification"]

            permissions = {

            }

            permissions[WindowsEntryType.DiskReadMask] = (row["Disk Read"] == "X")
            permissions[WindowsEntryType.DiskWriteMask] = (row["Disk Write"] == "X")
            permissions[WindowsEntryType.DiskExecuteMask] = (row["Disk Execute"] == "X")
            permissions[WindowsEntryType.FileReadMask] = (row["File Read"] == "X")
            permissions[WindowsEntryType.FileWriteMask] = (row["File Write"] == "X")
            permissions[WindowsEntryType.FileExecuteMask] = (row["File Execute"] == "X")

            enforcement = None

            match type:
                case "Allow":
                    enforcement = PolicyRule.Allow
                case "Deny":
                    enforcement = PolicyRule.Deny
                case "AuditAllowed":
                    enforcement = PolicyRule.AuditAllowed
                case "AuditDenied":
                    enforcement = PolicyRule.AuditDenied

            entries[name] = api.createEntry(
                Entry.WindowsDevice,
                enforcement=enforcement,
                permissions=permissions,
                notifications=Notifications(notification,Format.OMA_URI)
            )

        xslx_groups = pd.read_excel(xlsx_file_path,sheet_name="Groups")
        logger.debug(str(xslx_groups))

        

        groups = {}
        for index, row in xslx_groups.iterrows():
            group_name = row['Name']
            group_type = row['Type']
            group_match = row['Match']

            xslx_group = pd.read_excel(xlsx_file_path,sheet_name=group_name)
            logger.debug(str(xslx_group))

            property_name = list(xslx_group.columns)[0]
            logger.debug("Property="+property_name)

            group_property = GroupProperty.properties_by_name[property_name]

            property_values = list(xslx_group[property_name])
            logger.debug("Property_Values="+str(property_values))
            
            group = dc.createGroupOfWindowsDevices(
                name=group_name,
                property=group_property,
                values=property_values)
            
            groups[group_name] = group


        xslx_rules =pd.read_excel(xlsx_file_path,sheet_name="Rules")

        rules = {}
        for index,row in xslx_rules.iterrows():

            rule_name = row["Name"]
            rule_description = row["Description"]

            included_group_names = str(row["Included Groups"]).split(",")
            excluded_group_names = str(row["Excluded Groups"]).split(",")

            entry_names = str(row["Entries"]).split(",")

            included_groups = []
            for included_group_name in included_group_names:
                if included_group_name in groups:
                    included_groups.append(groups[included_group_name])
                else:
                    raise RuntimeError(included_group_name+" not found.")
                
            excluded_groups = []
            for excluded_group_name in excluded_group_names:
                if excluded_group_name in groups:
                    excluded_groups.append(groups[excluded_group_name])
                elif excluded_group_name != "nan":
                    raise RuntimeError(excluded_group_name+" not found.")
                

            entries_for_rule = []
            for entry_name in entry_names:

                entry_name = str(entry_name).strip()
                if entry_name not in entries:
                    raise RuntimeError("No entry named "+str(entry_name)+" found.")
                
                entry_with_new_id = dc.copy(object=entries[entry_name])
                entries_for_rule.append(entry_with_new_id)

            rule = dc.createRule(rule_name=rule_name,
                          included_groups=included_groups,
                          excluded_groups=excluded_groups,
                          entries=entries_for_rule)

            rule.description = rule_description

            rules[rule_name] = rule

        policy = dc.createPolicy(
            os=args.os,
            name=args.name,
            version=args.version,
            rules=list(rules.values()),
            groups=list(groups.values())
        )
         
        from mdedevicecontrol.dcintune import Package

        cwd = pathlib.Path(os.getcwd())
        
        p = Package(cwd.name,templateEnv=CommandLine.templateEnv)
        p.addPolicy(policy)

        p.save(str(cwd.parent),
               CommandLine.rule_template_name,
               CommandLine.readme_template_name,
               CommandLine.description_template_name)



def main():
    
   
    arg_parser = argparse.ArgumentParser(
    description='Utility for device control')
    subparsers = arg_parser.add_subparsers(help='The operation',dest="operation")
    init_arg_parser = subparsers.add_parser('init',help="Initialize the directory")
    init_arg_parser.add_argument("-n","--name",dest="name",help="The name of the package")
    
    init_sources_parser = init_arg_parser.add_subparsers(help='source',required=False, dest="init_source")
    intune_source_parser = init_sources_parser.add_parser('intune')
    intune_source_parser.add_argument("-p","--policies",dest="policies",help="comma separated list of policies")

    xlsx_source_parser = init_sources_parser.add_parser('xlsx')
    xlsx_source_parser.add_argument("-f","--file",dest="file",help="xlsx file to import",required=True)
    xlsx_source_parser.add_argument("-n","--name",dest="name",help="name of the policy",required=True)
    xlsx_source_parser.add_argument("-d","--description",dest="description",help="description of the policy",required=False)
    xlsx_source_parser.add_argument("-o","--os",dest="os",default="windows",required=True)
    xlsx_source_parser.add_argument("-v","--version",dest="version",default="v1",required=True)

    
    
    update_arg_parser = subparsers.add_parser('update', help='Update the configuration from the source')
    
    deploy_arg_parser = subparsers.add_parser('apply', help='Apply the configuraion to Intune')
    
    validate_arg_parser = subparsers.add_parser('validate', help='Validate the configuration')
    validate_options_sub_parser = validate_arg_parser.add_subparsers(help='options',dest="validate_options")
    validate_graph_options = validate_options_sub_parser.add_parser('graph')
    validate_graph_options_auth_type = validate_graph_options.add_subparsers(help="The type of authentication to the graph",dest="authentication_type")
    validate_graph_options_auth_type.add_parser("user")
    validate_graph_options_auth_type.add_parser("application")
    



    
    
    args = arg_parser.parse_args()


    asyncio.run(CommandLine.process_args(args))

if __name__ == "main":
    main()
