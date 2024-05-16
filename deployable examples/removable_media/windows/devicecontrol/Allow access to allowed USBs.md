# Device control policy sample: Allow access to allowed USBs

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
            <td rowspan="2" valign="top"><b>Allow access to allowed USBs</b></td>
            <td rowspan="2 valign="top">
                <ul><li>Group: Allowed USBs<a href="#allowed-usbs" title="MatchAny {'SerialNumberId': '6EA9150055800605'}"> (details)</a>  
</ul>
            </td>
            <td rowspan="2" valign="top">
                <ul></ul>
            </td>
            <td>Allow</td>
            <td>:white_check_mark:</td>
            <td>:white_check_mark:</td>
            <td>:white_check_mark:</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>None (0)</td> 
            <td>
                <center>-</center></td>
        </tr><tr>
            <td>Audit Allowed</td>
            <td>-</td>
            <td>:page_facing_up:</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>Send event (2)</td>
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
<Group Id="{af19f2da-4cd4-4c27-8c31-00aad629f7a6}" Type="Device">
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Baf19f2da-4cd4-4c27-8c31-00aad629f7a6%7D/GroupData -->
	<Name>Allowed USBs</Name>
	<MatchType>MatchAny</MatchType>
	<DescriptorIdList>
		<SerialNumberId>6EA9150055800605</SerialNumberId>
	</DescriptorIdList>
</Group>
```
</details>


## Settings






| Setting Name |  Setting Value | Description |Documentation |
|--------------|----------------|-------------|---------------|


## Files
This policy is based on information in the following files:

- [groups/Allowed USBs.xml](groups/Allowed%20USBs.xml)
- [rules/Allow access to allowed USBs.xml](rules/Allow%20access%20to%20allowed%20USBs.xml)


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
   4. Enter the Allowed USBs for the name.  
   5. Optionally, enter a description
   6. Click on "Next"
   7. Set the match type toggle to MatchAny
   
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
<summary>Add a rule for Allow access to allowed USBs to the policy</summary>


   1. Click on "+ Set reusable settings" under Included Id

   1. Click on *Allowed USBs*

   1. Click on "Select"


   1. Click on "+ Edit Entry"
   1. Enter *Allow access to allowed USBs* for the name



   1. Select *Allow* from "Type"
   1. Select *None* from "Options"
   1. Select *Read, Write and Execute* from "Access mask"




   1. Add another entry.  Click on "+ Add"

   1. Select *Audit Allowed* from "Type"
   1. Select *Send event* from "Options"
   1. Select *Write* from "Access mask"


   1. Click "OK"
</details>



## Group Policy (GPO)
<details>
<summary>Define device control policy groups</summary>

   1. Go to Computer Configuration > Administrative Templates > Windows Components > Microsoft Defender Antivirus > Device Control > Define device control policy groups.
   2. Save the XML below to a network share.
```xml
<Groups>
	<Group Id="{af19f2da-4cd4-4c27-8c31-00aad629f7a6}" Type="Device">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Baf19f2da-4cd4-4c27-8c31-00aad629f7a6%7D/GroupData -->
		<Name>Allowed USBs</Name>
		<MatchType>MatchAny</MatchType>
		<DescriptorIdList>
			<SerialNumberId>6EA9150055800605</SerialNumberId>
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
	<PolicyRule Id="{64cc3e83-8c37-411c-8b83-740bd2854734}" >
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B64cc3e83-8c37-411c-8b83-740bd2854734%7D/RuleData -->
		<Name>Allow access to allowed USBs</Name>
		<IncludedIdList>
			<GroupId>{af19f2da-4cd4-4c27-8c31-00aad629f7a6}</GroupId>
		</IncludedIdList>
		<ExcludedIdList>
		</ExcludedIdList>
		<Entry Id="{98e1cfb7-d97c-4928-8f53-4443ddb78be1}">
			<Type>Allow</Type>
			<AccessMask>7</AccessMask>
			<Options>0</Options>
		</Entry>
		<Entry Id="{a84312e2-cf97-47a5-b2bd-cead4558f9cf}">
			<Type>AuditAllowed</Type>
			<AccessMask>2</AccessMask>
			<Options>2</Options>
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
<summary>Add a row for Allow access to allowed USBs</summary>  
   
   1. Click "Add"
   2. For Name, enter *Allow access to allowed USBs*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B64cc3e83-8c37-411c-8b83-740bd2854734%7D/RuleData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  */workspaces/mdatp-devicecontrol/deployable examples/removable_media/windows/devicecontrol/rules/Allow access to allowed USBs.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for Allowed USBs</summary>  
   
   1. Click "Add"
   2. For Name, enter *Allowed USBs*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Baf19f2da-4cd4-4c27-8c31-00aad629f7a6%7D/GroupData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  */workspaces/mdatp-devicecontrol/deployable examples/removable_media/windows/devicecontrol/groups/Allowed USBs.xml*
         
   
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
            "id": "af19f2da-4cd4-4c27-8c31-00aad629f7a6",
            "query": {
                "$type": "or",
                "clauses": [
                    {
                        "$type": "serialNumber",
                        "value": "6EA9150055800605"
                    }
                ]
            }
        }
    ],
    "rules": [
        {
            "id": "64cc3e83-8c37-411c-8b83-740bd2854734",
            "name": "Allow access to allowed USBs",
            "includeGroups": [
                "af19f2da-4cd4-4c27-8c31-00aad629f7a6"
            ],
            "excludeGroups": [],
            "entries": [
                {
                    "$type": "generic",
                    "id": "98e1cfb7-d97c-4928-8f53-4443ddb78be1",
                    "enforcement": {
                        "$type": "allow"
                    },
                    "access": [
                        "generic_read",
                        "generic_write",
                        "generic_execute"
                    ]
                },
                {
                    "$type": "generic",
                    "id": "a84312e2-cf97-47a5-b2bd-cead4558f9cf",
                    "enforcement": {
                        "$type": "auditAllow",
                        "options": [
                            "send_event"
                        ]
                    },
                    "access": [
                        "generic_write"
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
            "id": "af19f2da-4cd4-4c27-8c31-00aad629f7a6",
            "query": {
                "$type": "or",
                "clauses": [
                    {
                        "$type": "serialNumber",
                        "value": "6EA9150055800605"
                    }
                ]
            }
        }
    ],
    "rules": [
        {
            "id": "64cc3e83-8c37-411c-8b83-740bd2854734",
            "name": "Allow access to allowed USBs",
            "includeGroups": [
                "af19f2da-4cd4-4c27-8c31-00aad629f7a6"
            ],
            "excludeGroups": [],
            "entries": [
                {
                    "$type": "generic",
                    "id": "98e1cfb7-d97c-4928-8f53-4443ddb78be1",
                    "enforcement": {
                        "$type": "allow"
                    },
                    "access": [
                        "generic_read",
                        "generic_write",
                        "generic_execute"
                    ]
                },
                {
                    "$type": "generic",
                    "id": "a84312e2-cf97-47a5-b2bd-cead4558f9cf",
                    "enforcement": {
                        "$type": "auditAllow",
                        "options": [
                            "send_event"
                        ]
                    },
                    "access": [
                        "generic_write"
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


