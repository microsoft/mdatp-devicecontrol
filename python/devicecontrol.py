
import json
import copy
import urllib.parse
import xml.etree.ElementTree as ET

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

    
class Setting: 

    
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
                }
                
            }
        },
        DataDuplicationDirectory:{
            "name": "File Evidence Directory",
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
            "oma-uri": {
                "supported": True,
                "documentation": "https://learn.microsoft.com/en-us/windows/client-management/mdm/defender-csp#configurationsecureddevicesconfiguration",
                "oma-uri": "./Vendor/MSFT/Defender/Configuration/SecuredDevicesConfiguration",
                "type": OMA_URI_String_DataType
            },
            "mac": {
                "supported": True,
                "documentation": "https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/mac-device-control-overview?view=o365-worldwide#settings"
            }

        },
        DataDuplicationMaximumQuota:{
            "name": "File Evidence Quota",
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
            "oma-uri":{
                "supported":False
            },
            "gpo":{
                "supported":False
            },
            "mac":{
                "supported":True
            }
        }
    
    }
    
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
                default_enforcement = Settings.default_enforcement_map[mac_default_enforcement]

                settings_dict[Setting.DefaultEnforcement] = default_enforcement
            else:
                settings_dict[Setting.DefaultEnforcement] = Settings.mac_default_enforcement

            if "ux" in settings_json:
                ux_json = settings_json["ux"]
                settings_dict[Setting.UXNavigationTarget] = ux_json["navigationTarget"]

        if len(settings_dict) > 0:
            settings = Settings(settings_dict)

        return settings


    def __init__(self, setting_dict):
        self.settings = []
        for name in setting_dict:
            value = setting_dict[name]
            self.settings.append(Setting(name,value))

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

    def __init__(self, property_name, property_value):
        self.name = property_name
        self.value = property_value

class Clause:

    def __init__(self,clause, clause_type = None):
        self._properties = []
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
                        sc = Clause(subclause,self.sub_clause_type)
                        self.sub_clauses.append(sc)

            if "value" in clause:
                value = clause.get("value")

            if property is not None and value is not None:
                self._properties.append(Property(property, value))
            elif self.sub_clause_type is None:
                print("Unknown Clause")
                return
            
class GroupProperty:

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

    def __init__(self,name,label,description,allowed_values = None):
        self.name = name
        self.label = label
        self.description = description
        self.allowed_values = allowed_values

class GroupType:

    WindowsDeviceGroupType = "Device"
    WindowsPrinterGroupType = "Device"
    
    FileGroupType = "File"
    NetworkGroupType = "Network"
    VPNConnectionGroupType = "VPNConnection"

    PrintJobType = "PrintJob"


    def __init__(self,name, group_properties):
        self.name = name
        self.group_properties = group_properties

    


class Group:

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
        "InstancePathId is a string that uniquely identifies the device in the system, for example, USBSTOR\\DISK&VEN_GENERIC&PROD_FLASH_DISK&REV_8.07\\8735B611&0. It's the Device instance path in the Device Manager. The number at the end (for example &0) represents the available slot and may change from device to device. For best results, use a wildcard at the end. For example, USBSTOR\DISK&VEN_GENERIC&PROD_FLASH_DISK&REV_8.07\8735B611*"
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
        WinodwsPrinterConnectionProperty
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
        WindowsDeviceSerialNumberProperty
    ]

    WindowsDeviceGroupType = GroupType(
        GroupType.WindowsDeviceGroupType,
        WindowsDeviceGroupProperties
    )

    WindowsPrinterGroupType = GroupType(
        GroupType.WindowsPrinterGroupType,
        WindowsPrinterGroupProperties
    )

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
        NetworkCategoryProperty
    ]

    NetworkGroupType = GroupType(
        GroupType.NetworkGroupType,
        NetworkGroupProperties
    )

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
        VPNServerAddressProperty
    ]

    VPNConnectionGroupType = GroupType(
        GroupType.VPNConnectionGroupType,
        VPNConnectionProperties
    )

    FilePathProperty = GroupProperty(
        GroupProperty.FilePath,
        "File Path",
        "value of file path or name, supports wildcard"
    )

    FileGroupProperties = [
        FilePathProperty
    ]

    FileGroupType = GroupType(
        GroupType.FileGroupType,
        FileGroupProperties
    )

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
        PrintOutputFileNameProperty
    ]

    PrintJobGroupType = GroupType(
        GroupType.PrintJobType,
        PrintJobGroupProperties
    )
    

    supported_match_types = [
        "MatchAny",
        "MatchAll"
    ]

    def __init__(self,root,format,path):

        self.format = format
        self.path = path
        self._properties = []
        self.clauses = []
        self.root = root
        self.conditions = {}

        if format == "gpo" or format =="oma-uri":

            self.id = root.attrib["Id"]
            if "Type" in root.attrib.keys():
                self.type = root.attrib["Type"]
            else:
                self.type = "Device"

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
                self._properties.append(Property(descriptor.tag, descriptor.text))
                self.conditions[descriptor.tag] = descriptor.text

        elif format == "mac":
            if "id" in root.keys():
                self.id = root["id"]

            if "name" in root.keys():
                self.name = root["name"]

            if "$type" in root.keys():
                self.type = root["$type"]

            if "query" in root.keys():
                query = root["query"]

                if "$type" in query.keys():
                    self.match_type = query["$type"]

                if "clauses" in query.keys():
                    clauses = query["clauses"]
                    for clause in clauses:
                        self.clauses.append(Clause(clause, self.match_type))

                self.conditions = clauses

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
        return False
    
    def __hash__(self):
        hashList = []
        for property in self._properties:
            key = property.name
            value = property.value
            hashList.append(key+"="+value)

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


    def __init__(self,root, format, path, rule_index = 1):

                            
        self.root = root

        self.format = format
        self.path = path        
        self.rule_index = rule_index
        self.id = None
        self.name = None
        self.included_groups = []
        self.excluded_groups = []
        self.entries = []

        self.entry_type = None

        if format == "gpo" or format =="oma-uri":

            self.id = root.attrib["Id"]
            name_node = root.find(".//Name")
            if name_node is None:
                self.name = "?"
            else:
                self.name = name_node.text

            included_groups_node = root.find(".//IncludedIdList")
            if not included_groups_node is None:
                groups = included_groups_node.findall(".//GroupId")
                for group in groups:
                    self.included_groups.append(group.text)

            excluded_groups_node = root.find(".//ExcludedIdList")
            if not excluded_groups_node is None:
                groups = excluded_groups_node.findall(".//GroupId")
                for group in groups:
                    self.excluded_groups.append(group.text)

            for entry in root.findall(".//Entry"):
                self.entries.append(Entry(entry,self.format))     

        elif format == "mac":
            if "id" in root.keys():
                self.id = root["id"]

            if "name" in root.keys():
                self.name = root["name"]

            if "includeGroups" in root.keys():
                self.included_groups = root["includeGroups"]
            
            
            if "excludeGroups" in root.keys():
                self.excluded_groups = root["excludeGroups"]

            if "entries" in root.keys():
                entries = root["entries"]
                for entry in entries:
                    self.entries.append(Entry(entry,self.format))

        #set the entry_type for the rule
        # if there is more than 1 make it a generic device
        for entry in self.entries:
            if self.entry_type is None:
                self.entry_type = entry.entry_type
            elif self.entry_type is not entry.entry_type:
                if self.format == "mac":
                    self.entry_type = Entry.AppleGeneric
                else:
                    self.entry_type = Entry.WindowsDevice
                break
        

    def get_oma_uri(self):
        return "./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/"+urllib.parse.quote_plus(self.id)+"/RuleData"
    
    def toXML(self,indent = "\t"):

        out = indent + "<PolicyRule Id=\""+self.id+"\" >\n"
        out +=indent + "\t<!-- "+self.get_oma_uri()+" -->\n"
        out +=indent + "\t<Name>"+Util.xml_safe_text(self.name)+"</Name>\n"
        
        out +=indent + "\t<IncludedIdList>\n"
        for group in self.included_groups:
            out += indent +"\t\t<GroupId>"+group+"</GroupId>\n"
        out +=indent + "\t</IncludedIdList>\n"

        out += indent +"\t<ExcludedIdList>\n"
        for group in self.excluded_groups:
            out += indent +"\t\t<GroupId>"+group+"</GroupId>\n"
        out += indent +"\t</ExcludedIdList>\n"

        for entry in self.entries:

            out += entry.toXML(indent+"\t")


        out += indent +"</PolicyRule>"

        return out
    
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


    


    def __init__(self,name, label,access_masks):
        self.name = name
        self.access_masks = access_masks
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

    
    WindowsPrinter = WindowsEntryType("windows_printer","Windows Printer",
        [0x40]
    )
    WindowsDevice  = WindowsEntryType("windows_device","Windows Removable Device",
        [0x01,0x02,0x04,0x08,0x10,0x20]
    )
    WindowsGeneric  = WindowsEntryType("windows_generic","Windows Generic Device",
        [0x01,0x02,0x04,0x08,0x10,0x20,0x04]
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
                        self.entry_type = Entry.WindowsDevice
                    elif self.entry_type is not Entry.WindowsDevice:
                        has_mixed_entry_type = True
                            
                    if mask == 64:
                        if self.entry_type is None:
                            self.entry_type = Entry.WindowsPrinter
                        elif self.entry_type is not Entry.WindowsPrinter:
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

           
            sid = entry.find("./Sid")
            if sid is not None:
                self.sid = sid.text
            else:
                self.sid = "All Users"

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
                    print("Unknown type "+self.entry_type)
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
                            



    
    def get_group_ids(self):
        if self.parameters is not None:
            return self.parameters.get_group_ids()
        else:
            return []
    
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
                if mask not in unsupported_access_masks:
                    if mask not in WindowsEntryType.access_masks:
                        support.issues.append(mask+" is an unsupported access mask")
                    else:
                        support.issues.append(WindowsEntryType.access_masks[mask]+" ("+str(mask)+") is an unsupported access mask")
                
                

        if self.enforcement not in feature_data["supported_notifications"]:
            support.issues.append("Unsupported type of entry "+self.enforcement)
        else:
            unsupported_notifications = feature_data["supported_notifications"][self.enforcement]["unsupported_notifications"]
            notification_masks_for_type = WindowsEntryType.notification_masks[self.enforcement]
            for mask in notification_masks_for_type:
                if int(self.notifications) & mask:
                    if unsupported_notifications[mask]:
                        support.issues.append(notification_masks_for_type[mask]+" ("+str(mask)+") is an unsupported notification.")

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
        self.tag = condition.tag
        self.condition_type = condition.tag
        for group in condition.findall(".//GroupId"):
            self.groups.append(group.text)

    def get_group_ids(self):
        return self.groups
    
    def toXML(self,indent):
        out = indent + "<"+self.tag+" MatchType=\""+self.match_type+"\">\n"

        for group in self.groups:
            out += indent +"\t<GroupId>"+group+"</GroupId>\n"

        out += indent + "</"+self.tag+">\n"

        return out

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

    def get_unsupported_dictionary(supported_values):
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
            entry_data["unsupported_access_masks"] = Feature.get_unsupported_dictionary([])

        for type in entry_data["supported_notifications"]:
            notifications = entry_data["supported_notifications"][type]["notifications"]
            entry_data["supported_notifications"][type]["unsupported_notifications"] = Feature.get_unsupported_dictionary(notifications)



    def get_support_for(self,object):

        if object.id in self.support_data.keys():
            return self.support_data[object.id]
        
        support = Support()
        self.support_data[object.id] = support

        match object.__class__.__name__:
            case "Group":
                group_support = self.feature_data["group"]
                supported_group_types = group_support["supported_types"]
                if object.type not in supported_group_types:
                    support.issues.append(object.type+" groups not supported.")
                else:
                    supported_properties = supported_group_types[object.type]["properties"]
                    for property in object._properties:
                        propertyId = property.name
                        value = property.value
                        if propertyId not in supported_properties:
                            support.issues.append(propertyId+" not supported for "+object.type+" group.")
                        else: 
                            if "values" in supported_properties[propertyId].keys() and value not in supported_properties[propertyId]["values"]:
                                support.issues.append(value+" not supported for "+propertyId+" of "+object.type+" group.")

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
                "match_types": ["MatchAll","MatchAny"]
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
            "match_types": ["MatchAll","MatchAny"]
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
    
 
