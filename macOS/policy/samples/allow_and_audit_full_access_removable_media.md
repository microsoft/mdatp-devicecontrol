# Device control policy sample: allow_and_audit_full_access_removable_media

Description: Allow and audit full access for any removable media              
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
            <td rowspan="2"><b>Allow and audit full access to removable media devices</b></td>
            <td rowspan="2 valign="top">
                <ul><li>All Removable Media Devices<a href="#all-removable-media-devices" title="all [{'$type': 'primaryId', 'value': 'removable_media_devices'}]"> (details)</a></ul>
            </td>
            <td rowspan="2" valign="top">.
                <ul></ul>
            </td>
            <td>Allow</td>
            <td>:white_check_mark:</td>
            <td>:white_check_mark:</td>
            <td>:white_check_mark:</td>
            <td>None</td> 
        </tr><tr>
            <td>Audit Allowed</td>
            <td>:page_facing_up:</td>
            <td>:page_facing_up:</td>
            <td>:page_facing_up:</td>
            <td>Send event</td>
        </tr></table>


## Groups


### All Removable Media Devices



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

<td>primaryId</td>

<td>removable_media_devices</td>

</tr>

</table>


#### Available properties for All Removable Media Devices


<details>
<summary>View JSON</summary>

```json
{
    "$type": "device",
    "id": "531278a2-a318-48d7-8e6a-0f0fd7589b07",
    "name": "All Removable Media Devices",
    "query": {
        "$type": "all",
        "clauses": [
            {
                "$type": "primaryId",
                "value": "removable_media_devices"
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
DefaultEnforcement | Deny | Control Device Control default enforcement. This is the enforcement applied if there are no policy rules present or at the end of the policy rules evaluation none were matched. |[documentation](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/mac-device-control-overview?view=o365-worldwide#settings) |
UXNavigationTarget | http://www.microsoft.com | Notification hyperlink |[documentation](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/mac-device-control-overview?view=o365-worldwide#settings) |


## Files
This policy is based on information in the following files:

- [audit_deny_all_removable_media.json](audit_deny_all_removable_media.json)
- [allow_and_audit_full_access_removable_media.json](allow_and_audit_full_access_removable_media.json)


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
            "id": "531278a2-a318-48d7-8e6a-0f0fd7589b07",
            "name": "All Removable Media Devices",
            "query": {
                "$type": "all",
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
            "id": "aa0f349b-fe01-4520-80a3-1004df3dc530",
            "name": "Allow and audit full access to removable media devices",
            "includeGroups": [
                "531278a2-a318-48d7-8e6a-0f0fd7589b07"
            ],
            "entries": [
                {
                    "$type": "removableMedia",
                    "id": "27f4a011-b8a0-42bd-a53f-ca3e75234869",
                    "enforcement": {
                        "$type": "allow"
                    },
                    "access": [
                        "read",
                        "write",
                        "execute"
                    ]
                },
                {
                    "$type": "removableMedia",
                    "id": "21fd9576-8deb-4824-98cc-8c29564a74b1",
                    "enforcement": {
                        "$type": "auditAllow",
                        "options": [
                            "send_event"
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
            "defaultEnforcement": "deny"
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
            "id": "531278a2-a318-48d7-8e6a-0f0fd7589b07",
            "name": "All Removable Media Devices",
            "query": {
                "$type": "all",
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
            "id": "aa0f349b-fe01-4520-80a3-1004df3dc530",
            "name": "Allow and audit full access to removable media devices",
            "includeGroups": [
                "531278a2-a318-48d7-8e6a-0f0fd7589b07"
            ],
            "entries": [
                {
                    "$type": "removableMedia",
                    "id": "27f4a011-b8a0-42bd-a53f-ca3e75234869",
                    "enforcement": {
                        "$type": "allow"
                    },
                    "access": [
                        "read",
                        "write",
                        "execute"
                    ]
                },
                {
                    "$type": "removableMedia",
                    "id": "21fd9576-8deb-4824-98cc-8c29564a74b1",
                    "enforcement": {
                        "$type": "auditAllow",
                        "options": [
                            "send_event"
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
            "defaultEnforcement": "deny"
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


