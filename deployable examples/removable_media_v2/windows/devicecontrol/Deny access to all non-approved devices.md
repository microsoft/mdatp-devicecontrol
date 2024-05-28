# Device control policy sample: Deny access to all non-approved devices

Description: This is a policy.              
Device Type: Windows Removable Device

A device control policy is a combination of [policy rules](#policy-rules), [groups](#groups) and [settings](#settings).  
This sample is based on the [sample files](#files).  
To configure the sample, follow the [deployment instructions](#deployment-instructions).  

## Policy Rules


<table>
    <tr>
        <th rowspan="2" valign="top">Name</th>
        <th colspan="2" valign="top"><center>Devices</center></th>
        <th rowspan="2" valign="top">Rule Type</th>
        <th colspan="6" valign="top"><center>Access</center></th>
        <th rowspan="2" valign="top">Notification</th>
        <th rowspan="2" valign="top">Conditions</th>
    </tr>
    <tr>
        <th>Included</th>
        <th>Excluded</th>
        <th>Disk Read</th>
		<th>Disk Write</th>
		<th>Disk Execute</th>
		<th>File Read</th>
		<th>File Write</th>
		<th>File Execute</th></tr><tr>
            <td rowspan="2" valign="top"><b>Deny access to all non-approved devices</b></td>
            <td rowspan="2 valign="top">
                <ul><li>Group: All Removable Media Devices<a href="#all-removable-media-devices" title="MatchAny {'PrimaryId': 'RemovableMediaDevices'}"> (details)</a>  
</ul>
            </td>
            <td rowspan="2" valign="top">
                <ul><li>Group: Allowed USBs<a href="#allowed-usbs" title="MatchAny {'SerialNumberId': '6EA9150055800605'}"> (details)</a>  
</ul>
            </td>
            <td>Deny</td>
            <td>:x:</td>
            <td>:x:</td>
            <td>:x:</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>None (0)</td> 
            <td>
                <center>-</center></td>
        </tr><tr>
            <td>Audit Denied</td>
            <td>:page_facing_up:</td>
            <td>:page_facing_up:</td>
            <td>:page_facing_up:</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>Show notification and Send event (3)</td>
            <td> 
                <center>-</center></td>
        </tr></table>


## Groups


### Allowed USBs



This is a group of type *Device*. 
The match type for the group is *MatchAny*.


|  Property | Value |
|-----------|-------|
| SerialNumberId | 6EA9150055800605 |





<details>
<summary>View XML</summary>

```xml
<Group Id="{5e233630-f613-483a-92d9-290d44b84ca2}" Type="Device">
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B5e233630-f613-483a-92d9-290d44b84ca2%7D/GroupData -->
	<Name>Allowed USBs</Name>
	<MatchType>MatchAny</MatchType>
	<DescriptorIdList>
		<SerialNumberId>6EA9150055800605</SerialNumberId>
	</DescriptorIdList>
</Group>
```
</details>

### All Removable Media Devices



This is a group of type *Device*. 
The match type for the group is *MatchAny*.


|  Property | Value |
|-----------|-------|
| PrimaryId | RemovableMediaDevices |





<details>
<summary>View XML</summary>

```xml
<Group Id="{b7e99129-3e3c-44aa-b71e-f95e3f65336f}" Type="Device">
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Bb7e99129-3e3c-44aa-b71e-f95e3f65336f%7D/GroupData -->
	<Name>All Removable Media Devices</Name>
	<MatchType>MatchAny</MatchType>
	<DescriptorIdList>
		<PrimaryId>RemovableMediaDevices</PrimaryId>
	</DescriptorIdList>
</Group>
```
</details>


## Settings






| Setting Name |  Setting Value | Description |Documentation |
|--------------|----------------|-------------|---------------|


## Files
This policy is based on information in the following files:

- [rules/Deny access to all non-approved devices.xml](rules/Deny%20access%20to%20all%20non-approved%20devices.xml)
- [groups/All Removable Media Devices.xml](groups/All%20Removable%20Media%20Devices.xml)
- [groups/Allowed USBs.xml](groups/Allowed%20USBs.xml)


# Deployment Instructions

Device control [policy rules](#policy-rules) and [groups](#groups) can be deployed through the following management tools:


## Windows
- [Intune UX](#intune-ux)
- [Intune Custom Settings](#intune-custom-settings)
- [Group Policy (GPO)](#group-policy-gpo)



## Mac
- [Mac Deployment with Intune](#mac-deployment-with-intune)
- [Mac Deployment with JAMF](#mac-deployment-with-jamf)
- [Manual Mac Deployment](#manual-mac-deployment)



## Intune UX

<details>
<summary>Create a reusable setting for Allowed USBs</summary> 

   1. Navigate to Home > Endpoint Security > Attack Surface Reduction
   2. Click on Reusable Settings
   3. Click (+) Add
   4. Enter the *Allowed USBs* for the name.  
   5. Optionally, enter a description
   6. Click on "Next"
   
   1. Create an entry for  *SerialNumberId* = *6EA9150055800605* 
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Configure setting"    
        4. Enter *SerialNumberId( 6EA9150055800605 )* for Name
        5. Enter *6EA9150055800605* for SerialNumberId
        6. Click "Save"


   
   7. Set the match type drop down to MatchAny
   8. Click "Next"
   9. Click "Add"
</details>
<details>
<summary>Create a reusable setting for All Removable Media Devices</summary> 

   1. Navigate to Home > Endpoint Security > Attack Surface Reduction
   2. Click on Reusable Settings
   3. Click (+) Add
   4. Enter the *All Removable Media Devices* for the name.  
   5. Optionally, enter a description
   6. Click on "Next"
   
   1. Create an entry for  *PrimaryId* = *RemovableMediaDevices* 
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Configure setting"    
        4. Enter *PrimaryId( RemovableMediaDevices )* for Name
        5. Enter *RemovableMediaDevices* for PrimaryId
        6. Click "Save"


   
   7. Set the match type drop down to MatchAny
   8. Click "Next"
   9. Click "Add"
</details>
<details>
<summary>Create a Device Control Rules configuration profile</summary>  

   1. Navigate to Home > Endpoint Security > Attack Surface Reduction
   2. Click on "Create Policy"
   3. Under Platform, select "Windows 10 and later"
   4. Under Profile, select "Device Control Rules"
   5. Click "Create"
   6. Under Name, enter **
   7. Optionally, enter a description
   8. Click "Next"
</details>


<details>
<summary>Add a rule for Deny access to all non-approved devices to the policy</summary>


   1. Click on "+ Set reusable settings" under Included Id

   1. Click on *All Removable Media Devices*

   1. Click on "Select"


   1. Click on "+ Set reusable settings" under Excluded Id

   1. Click on *Allowed USBs*

   1. Click on "Select"

   1. Click on "+ Edit Entry"
   1. Enter *Deny access to all non-approved devices* for the name



   1. Select *Deny* from "Type"
   1. Select *None* from "Options"
   1. Select *Read, Write and Execute* from "Access mask"




   1. Add another entry.  Click on "+ Add"

   1. Select *Audit Denied* from "Type"
   1. Select *Show notification and Send event* from "Options"
   1. Select *Read, Write and Execute* from "Access mask"


   1. Click "OK"
</details>



## Group Policy (GPO)
<details>
<summary>Define device control policy groups</summary>

   1. Go to Computer Configuration > Administrative Templates > Windows Components > Microsoft Defender Antivirus > Device Control > Define device control policy groups.
   2. Save the XML below to a network share.
```xml
<Groups>
	<Group Id="{5e233630-f613-483a-92d9-290d44b84ca2}" Type="Device">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B5e233630-f613-483a-92d9-290d44b84ca2%7D/GroupData -->
		<Name>Allowed USBs</Name>
		<MatchType>MatchAny</MatchType>
		<DescriptorIdList>
			<SerialNumberId>6EA9150055800605</SerialNumberId>
		</DescriptorIdList>
	</Group>
	<Group Id="{b7e99129-3e3c-44aa-b71e-f95e3f65336f}" Type="Device">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Bb7e99129-3e3c-44aa-b71e-f95e3f65336f%7D/GroupData -->
		<Name>All Removable Media Devices</Name>
		<MatchType>MatchAny</MatchType>
		<DescriptorIdList>
			<PrimaryId>RemovableMediaDevices</PrimaryId>
		</DescriptorIdList>
	</Group>
</Groups>
```
   3. In the Define device control policy groups window, select *Enabled* and specify the network share file path containing the XML groups data.
</details>

<details>
<summary>Define device control policy rules</summary>
 
  1. Go to Computer Configuration > Administrative Templates > Windows Components > Microsoft Defender Antivirus > Device Control > Define device control policy rules.
  2. Save the XML below to a network share.
```xml
<PolicyRules>
	<PolicyRule Id="{0632485f-12e0-491a-b9f4-1d8ca7d555a3}" >
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B0632485f-12e0-491a-b9f4-1d8ca7d555a3%7D/RuleData -->
		<Name>Deny access to all non-approved devices</Name>
		<IncludedIdList>
			<GroupId>{b7e99129-3e3c-44aa-b71e-f95e3f65336f}</GroupId>
		</IncludedIdList>
		<ExcludedIdList>
			<GroupId>{5e233630-f613-483a-92d9-290d44b84ca2}</GroupId>
		</ExcludedIdList>
		<Entry Id="{69f48608-0272-465b-81cc-ed63d56f84fa}">
			<Type>Deny</Type>
			<AccessMask>7</AccessMask>
			<Options>0</Options>
		</Entry>
		<Entry Id="{5612f935-3175-48bb-ab49-cc2c811ad3b9}">
			<Type>AuditDenied</Type>
			<AccessMask>7</AccessMask>
			<Options>3</Options>
		</Entry>
	</PolicyRule>
</PolicyRules>
```
  3. In the Define device control policy rules window, select *Enabled*, and enter the network share file path containing the XML rules data.
</details>

## Intune Custom Settings

<details>
<summary>Create custom intune configuration</summary>

   1. Navigate to Devices > Configuration profiles
   2. Click Create (New Policy)
   3. Select Platform "Windows 10 and Later"
   4. Select Profile "Templates"
   5. Select Template Name "Custom"
   6. Click "Create"
   7. Under Name, enter **
   8. Optionally, enter a description
   9. Click "Next" 
</details>
<details>
<summary>Add a row for Deny access to all non-approved devices</summary>  
   
   1. Click "Add"
   2. For Name, enter *Deny access to all non-approved devices*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B0632485f-12e0-491a-b9f4-1d8ca7d555a3%7D/RuleData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  */workspaces/mdatp-devicecontrol/deployable examples/removable_media_v2/windows/devicecontrol/rules/Deny access to all non-approved devices.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for All Removable Media Devices</summary>  
   
   1. Click "Add"
   2. For Name, enter *All Removable Media Devices*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Bb7e99129-3e3c-44aa-b71e-f95e3f65336f%7D/GroupData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  */workspaces/mdatp-devicecontrol/deployable examples/removable_media_v2/windows/devicecontrol/groups/All Removable Media Devices.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for Allowed USBs</summary>  
   
   1. Click "Add"
   2. For Name, enter *Allowed USBs*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B5e233630-f613-483a-92d9-290d44b84ca2%7D/GroupData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  */workspaces/mdatp-devicecontrol/deployable examples/removable_media_v2/windows/devicecontrol/groups/Allowed USBs.xml*
         
   
   7. Click "Save"
</details>




## Mac Policy
### Mac Deployment with Intune

1. Create the .mobileconfig file

<details>
    <summary>Copy the contents below into a file, and save it.</summary>       

```xml
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1">
    <dict>
        <key>PayloadUUID</key>
        <string>C4E6A782-0C8D-44AB-A025-EB893987A295</string>
        <key>PayloadType</key>
        <string>Configuration</string>
        <key>PayloadOrganization</key>
        <string>Microsoft</string>
        <key>PayloadIdentifier</key>
        <string>com.microsoft.wdav</string>
        <key>PayloadDisplayName</key>
        <string>Microsoft Defender settings</string>
        <key>PayloadDescription</key>
        <string>Microsoft Defender configuration settings</string>
        <key>PayloadVersion</key>
        <integer>1</integer>
        <key>PayloadEnabled</key>
        <true/>
        <key>PayloadRemovalDisallowed</key>
        <true/>
        <key>PayloadScope</key>
        <string>System</string>
        <key>PayloadContent</key>
        <array>
            <dict>
                <key>PayloadUUID</key>
                <string>99DBC2BC-3B3A-46A2-A413-C8F9BB9A7295</string>
                <key>PayloadType</key>
                <string>com.microsoft.wdav</string>
                <key>PayloadOrganization</key>
                <string>Microsoft</string>
                <key>PayloadIdentifier</key>
                <string>com.microsoft.wdav</string>
                <key>PayloadDisplayName</key>
                <string>Microsoft Defender configuration settings</string>
                <key>PayloadDescription</key>
                <string/>
                <key>PayloadVersion</key>
                <integer>1</integer>
                <key>PayloadEnabled</key>
                <true/>
                <key>dlp</key>
                <dict>
                  <key>features</key>
                    <array>
                        <dict>
                            <key>name</key>
                            <string>DC_in_dlp</string>
                            <key>state</key>
                            <string>enabled</string>
                        </dict>
                    </array>
                </dict>
                <key>deviceControl</key>
                <dict>
                    <key>policy</key>
                    <string>
{
    "groups": [
        {
            "$type": "device",
            "id": "5e233630-f613-483a-92d9-290d44b84ca2",
            "query": {
                "$type": "or",
                "clauses": [
                    {
                        "$type": "serialNumber",
                        "value": "6EA9150055800605"
                    }
                ]
            }
        },
        {
            "$type": "device",
            "id": "b7e99129-3e3c-44aa-b71e-f95e3f65336f",
            "query": {
                "$type": "or",
                "clauses": [
                    {
                        "$type": "primaryId",
                        "value": "removable_media_devices"
                    }
                ]
            }
        }
    ],
    "rules": [
        {
            "id": "0632485f-12e0-491a-b9f4-1d8ca7d555a3",
            "name": "Deny access to all non-approved devices",
            "includeGroups": [
                "b7e99129-3e3c-44aa-b71e-f95e3f65336f"
            ],
            "excludeGroups": [
                "5e233630-f613-483a-92d9-290d44b84ca2"
            ],
            "entries": [
                {
                    "$type": "generic",
                    "id": "69f48608-0272-465b-81cc-ed63d56f84fa",
                    "enforcement": {
                        "$type": "deny"
                    },
                    "access": [
                        "generic_read",
                        "generic_write",
                        "generic_execute"
                    ]
                },
                {
                    "$type": "generic",
                    "id": "5612f935-3175-48bb-ab49-cc2c811ad3b9",
                    "enforcement": {
                        "$type": "auditDeny",
                        "options": [
                            "show_notification",
                            "send_event"
                        ]
                    },
                    "access": [
                        "generic_read",
                        "generic_write",
                        "generic_execute"
                    ]
                }
            ]
        }
    ],
    "settings": {}
}
                    </string>
                </dict>
            </dict>
        </array>
    </dict>
</plist>
```
</details>



2. Deploy the .mobileconfig file using Intune

    1.   Navigate to https://endpoint.microsoft.com/ > **Devices** > **macOS** > ** Configuration profiles
    2.   Click on create + New Policy
    3.   Select Profile type Templates
    4.   Select Custom profile
    5.   Enter the name of the policy, optionally a description, and then click Next
    6.   Select the device deployment channel
    7.   Choose the .mobileconfig that you created
    8.   Click "Next"
    9.   Scope, assign and deploy the policy.



### Manual Mac Deployment


1. Create the .json file

<details>
     <summary>Save the .json to a file</summary>

```json
{
    "groups": [
        {
            "$type": "device",
            "id": "5e233630-f613-483a-92d9-290d44b84ca2",
            "query": {
                "$type": "or",
                "clauses": [
                    {
                        "$type": "serialNumber",
                        "value": "6EA9150055800605"
                    }
                ]
            }
        },
        {
            "$type": "device",
            "id": "b7e99129-3e3c-44aa-b71e-f95e3f65336f",
            "query": {
                "$type": "or",
                "clauses": [
                    {
                        "$type": "primaryId",
                        "value": "removable_media_devices"
                    }
                ]
            }
        }
    ],
    "rules": [
        {
            "id": "0632485f-12e0-491a-b9f4-1d8ca7d555a3",
            "name": "Deny access to all non-approved devices",
            "includeGroups": [
                "b7e99129-3e3c-44aa-b71e-f95e3f65336f"
            ],
            "excludeGroups": [
                "5e233630-f613-483a-92d9-290d44b84ca2"
            ],
            "entries": [
                {
                    "$type": "generic",
                    "id": "69f48608-0272-465b-81cc-ed63d56f84fa",
                    "enforcement": {
                        "$type": "deny"
                    },
                    "access": [
                        "generic_read",
                        "generic_write",
                        "generic_execute"
                    ]
                },
                {
                    "$type": "generic",
                    "id": "5612f935-3175-48bb-ab49-cc2c811ad3b9",
                    "enforcement": {
                        "$type": "auditDeny",
                        "options": [
                            "show_notification",
                            "send_event"
                        ]
                    },
                    "access": [
                        "generic_read",
                        "generic_write",
                        "generic_execute"
                    ]
                }
            ]
        }
    ],
    "settings": {}
}
```
</details>


2. Use ```mdatp config device-control policy set --path <full-path-to-policy.json>``` to apply the policy.



### Mac Deployment with JAMF

Instructions on how to deploy the policy with JAMF can be found [here](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/mac-device-control-jamf?view=o365-worldwide#deploy-policy-by-using-jamf)

Learn more
- [Mac device control examples](../Removable%20Storage%20Access%20Control%20Samples/macOS/policy/examples/README.md)


