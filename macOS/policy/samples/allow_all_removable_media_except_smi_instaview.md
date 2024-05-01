# Device control policy sample: allow_all_removable_media_except_smi_instaview

Description: Allow all removable media expect a device by VID PID              
Device Type: Apple Removable Media

A device control policy is a combination of [policy rules](#policy-rules), [groups](#groups) and [settings](#settings).  
This sample is based on the [sample files](#files).  
To configure the sample, follow the [deployment instructions](#deployment-instructions).  

## Policy Rules

<table>
    <tr>
        <th rowspan="2" valign="top">Name</th>
        <th colspan="2" valign="top">Devices</th>
        <th rowspan="2" valign="top">Rule Type</th>
        <th colspan="3" valign="top"><center>Access</center></th>
        <th rowspan="2" valign="top">Notification</th>
    </tr>
    <tr>
        <th>Included</th>
        <th>Excluded</th><th>Read</th><th>Write</th><th>Execute</th></tr><tr>
            <td rowspan="2"><b>Allow RWX to all Removable Media Devices except SMI INSTAVIEW</b></td>
            <td rowspan="2 valign="top">
                <ul><li>SMI Instaview<a href="#smi-instaview" title="all [{'$type': 'vendorId', 'value': '2316'}, {'$type': 'productId', 'value': '8192'}]"> (details)</a></ul>
            </td>
            <td rowspan="2" valign="top">.
                <ul></ul>
            </td>
            <td>Deny</td>
            <td>:x:</td>
            <td>:x:</td>
            <td>:x:</td>
            <td>None</td> 
        </tr><tr>
            <td>Audit Denied</td>
            <td>:page_facing_up:</td>
            <td>:page_facing_up:</td>
            <td>:page_facing_up:</td>
            <td>Send event and Show notification</td>
        </tr></table>


## Groups


### SMI Instaview



This is a group of type *device*. 
The match type for the group is *all*.


<table>
<tr>
<th>Operator</th>
<th>Property</th>
<th>Value</th>
</tr>

<tr>

<td></td>

<td>vendorId</td>

<td>2316</td>

</tr>

<tr>

<td>all</td>

<td>productId</td>

<td>8192</td>

</tr>

</table>


#### Available properties for SMI Instaview


<details>
<summary>View JSON</summary>

```json
{
    "$type": "device",
    "id": "c5c2fd68-0e09-44eb-880a-bfa662933f17",
    "name": "SMI Instaview",
    "query": {
        "$type": "all",
        "clauses": [
            {
                "$type": "vendorId",
                "value": "2316"
            },
            {
                "$type": "productId",
                "value": "8192"
            }
        ]
    }
}
```
</details>


## Settings






| Setting Name |  Setting Value | Description |Documentation |
|--------------|----------------|-------------|---------------|
SecuredDevicesConfiguration | {'appleDevice': {'disable': True}, 'removableMedia': {'disable': False}, 'portableDevice': {'disable': True}, 'bluetoothDevice': {'disable': True}} | Defines which device's primary ids should be secured by Defender Device Control. If this configuration isn't set the default value will be applied, meaning all supported devices will be secured. |[documentation](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/mac-device-control-overview?view=o365-worldwide#settings) |
DefaultEnforcement | Allow | Control Device Control default enforcement. This is the enforcement applied if there are no policy rules present or at the end of the policy rules evaluation none were matched. |[documentation](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/mac-device-control-overview?view=o365-worldwide#settings) |
UXNavigationTarget | http://www.microsoft.com | Notification hyperlink |[documentation](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/mac-device-control-overview?view=o365-worldwide#settings) |


## Files
This policy is based on information in the following files:

- [allow_all_removable_media_except_smi_instaview.json](allow_all_removable_media_except_smi_instaview.json)


# Deployment Instructions

Device control [policy rules](#policy-rules) and [groups](#groups) can be deployed through the following management tools:




## Mac
- [Mac Deployment with Intune](#mac-deployment-with-intune)
- [Mac Deployment with JAMF](#mac-deployment-with-jamf)
- [Manual Mac Deployment](#manual-mac-deployment)





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
            "id": "c5c2fd68-0e09-44eb-880a-bfa662933f17",
            "name": "SMI Instaview",
            "query": {
                "$type": "all",
                "clauses": [
                    {
                        "$type": "vendorId",
                        "value": "2316"
                    },
                    {
                        "$type": "productId",
                        "value": "8192"
                    }
                ]
            }
        }
    ],
    "rules": [
        {
            "id": "dd3a68d3-c3b7-4b61-a6c9-ab11c4193356",
            "name": "Allow RWX to all Removable Media Devices except SMI INSTAVIEW",
            "includeGroups": [
                "c5c2fd68-0e09-44eb-880a-bfa662933f17"
            ],
            "entries": [
                {
                    "$type": "removableMedia",
                    "id": "6c937114-8860-4127-a678-1b38ae196409",
                    "enforcement": {
                        "$type": "deny"
                    },
                    "access": [
                        "read",
                        "write",
                        "execute"
                    ]
                },
                {
                    "$type": "removableMedia",
                    "id": "f5aac001-8a24-4565-a436-7a8331c035d2",
                    "enforcement": {
                        "$type": "auditDeny",
                        "options": [
                            "send_event",
                            "show_notification"
                        ]
                    },
                    "access": [
                        "read",
                        "write",
                        "execute"
                    ]
                }
            ]
        }
    ],
    "settings": {
        "features": {
            "appleDevice": {
                "disable": true
            },
            "removableMedia": {
                "disable": false
            },
            "portableDevice": {
                "disable": true
            },
            "bluetoothDevice": {
                "disable": true
            }
        },
        "global": {
            "defaultEnforcement": "allow"
        },
        "ux": {
            "navigationTarget": "http://www.microsoft.com"
        }
    }
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
            "id": "c5c2fd68-0e09-44eb-880a-bfa662933f17",
            "name": "SMI Instaview",
            "query": {
                "$type": "all",
                "clauses": [
                    {
                        "$type": "vendorId",
                        "value": "2316"
                    },
                    {
                        "$type": "productId",
                        "value": "8192"
                    }
                ]
            }
        }
    ],
    "rules": [
        {
            "id": "dd3a68d3-c3b7-4b61-a6c9-ab11c4193356",
            "name": "Allow RWX to all Removable Media Devices except SMI INSTAVIEW",
            "includeGroups": [
                "c5c2fd68-0e09-44eb-880a-bfa662933f17"
            ],
            "entries": [
                {
                    "$type": "removableMedia",
                    "id": "6c937114-8860-4127-a678-1b38ae196409",
                    "enforcement": {
                        "$type": "deny"
                    },
                    "access": [
                        "read",
                        "write",
                        "execute"
                    ]
                },
                {
                    "$type": "removableMedia",
                    "id": "f5aac001-8a24-4565-a436-7a8331c035d2",
                    "enforcement": {
                        "$type": "auditDeny",
                        "options": [
                            "send_event",
                            "show_notification"
                        ]
                    },
                    "access": [
                        "read",
                        "write",
                        "execute"
                    ]
                }
            ]
        }
    ],
    "settings": {
        "features": {
            "appleDevice": {
                "disable": true
            },
            "removableMedia": {
                "disable": false
            },
            "portableDevice": {
                "disable": true
            },
            "bluetoothDevice": {
                "disable": true
            }
        },
        "global": {
            "defaultEnforcement": "allow"
        },
        "ux": {
            "navigationTarget": "http://www.microsoft.com"
        }
    }
}
```
</details>


2. Use ```mdatp config device-control policy set --path <full-path-to-policy.json>``` to apply the policy.



### Mac Deployment with JAMF

Instructions on how to deploy the policy with JAMF can be found [here](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/mac-device-control-jamf?view=o365-worldwide#deploy-policy-by-using-jamf)

Learn more
- [Mac device control examples](../Removable%20Storage%20Access%20Control%20Samples/macOS/policy/examples/README.md)


