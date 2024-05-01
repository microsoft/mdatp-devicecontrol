# Device control policy sample: deny_mobile_devices

Description: This is a policy.              
Device Type: Apple Generic Device

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
            <td rowspan="2"><b>Block All Apple Devices</b></td>
            <td rowspan="2 valign="top">
                <ul><li>All Apple Devices<a href="#all-apple-devices" title="and [{'$type': 'primaryId', 'value': 'apple_devices'}]"> (details)</a></ul>
            </td>
            <td rowspan="2" valign="top">.
                <ul></ul>
            </td>
            <td>Deny</td>
            <td>:x:</td>
            <td>:x:</td>
            <td>:x:</td>
            <td>:x:</td>
            <td>:x:</td>
            <td>None</td> 
        </tr><tr>
            <td>Audit Denied</td>
            <td>:page_facing_up:</td>
            <td>:page_facing_up:</td>
            <td>:page_facing_up:</td>
            <td>:page_facing_up:</td>
            <td>:page_facing_up:</td>
            <td>Send event and Show notification</td>
        </tr><tr>
            <td rowspan="2"><b>Block All Portable Devices</b></td>
            <td rowspan="2 valign="top">
                <ul><li>All Portable Devices<a href="#all-portable-devices" title="and [{'$type': 'primaryId', 'value': 'portable_devices'}]"> (details)</a></ul>
            </td>
            <td rowspan="2" valign="top">.
                <ul></ul>
            </td>
            <td>Deny</td>
            <td>:x:</td>
            <td>:x:</td>
            <td>:x:</td>
            <td>:x:</td>
            <td>None</td> 
        </tr><tr>
            <td>Audit Denied</td>
            <td>:page_facing_up:</td>
            <td>:page_facing_up:</td>
            <td>:page_facing_up:</td>
            <td>:page_facing_up:</td>
            <td>Send event and Show notification</td>
        </tr></table>


## Groups


### All Apple Devices



This is a group of type *device*. 
The match type for the group is *and*.


<table>
<tr>
<th>Operator</th>
<th>Property</th>
<th>Value</th>
</tr>

<tr>

<td></td>

<td>primaryId</td>

<td>apple_devices</td>

</tr>

</table>


#### Available properties for All Apple Devices


<details>
<summary>View JSON</summary>

```json
{
    "$type": "device",
    "id": "3D2A9EF0-E587-4B90-A60F-C9BD6F9D2BB4",
    "name": "All Apple Devices",
    "query": {
        "$type": "and",
        "clauses": [
            {
                "$type": "primaryId",
                "value": "apple_devices"
            }
        ]
    }
}
```
</details>

### All Portable Devices



This is a group of type *device*. 
The match type for the group is *and*.


<table>
<tr>
<th>Operator</th>
<th>Property</th>
<th>Value</th>
</tr>

<tr>

<td></td>

<td>primaryId</td>

<td>portable_devices</td>

</tr>

</table>


#### Available properties for All Portable Devices


<details>
<summary>View JSON</summary>

```json
{
    "$type": "device",
    "id": "0B2198B2-8E29-4AAB-AFC8-8B2CF827CDE9",
    "name": "All Portable Devices",
    "query": {
        "$type": "and",
        "clauses": [
            {
                "$type": "primaryId",
                "value": "portable_devices"
            }
        ]
    }
}
```
</details>


## Settings






| Setting Name |  Setting Value | Description |Documentation |
|--------------|----------------|-------------|---------------|
SecuredDevicesConfiguration | {'appleDevice': {'disable': False}, 'removableMedia': {'disable': False}, 'portableDevice': {'disable': False}, 'bluetoothDevice': {'disable': False}} | Defines which device's primary ids should be secured by Defender Device Control. If this configuration isn't set the default value will be applied, meaning all supported devices will be secured. |[documentation](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/mac-device-control-overview?view=o365-worldwide#settings) |
DefaultEnforcement | Allow | Control Device Control default enforcement. This is the enforcement applied if there are no policy rules present or at the end of the policy rules evaluation none were matched. |[documentation](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/mac-device-control-overview?view=o365-worldwide#settings) |
UXNavigationTarget | http://www.microsoft.com | Notification hyperlink |[documentation](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/mac-device-control-overview?view=o365-worldwide#settings) |


## Files
This policy is based on information in the following files:

- [deny_mobile_devices.json](deny_mobile_devices.json)


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
            "id": "3D2A9EF0-E587-4B90-A60F-C9BD6F9D2BB4",
            "name": "All Apple Devices",
            "query": {
                "$type": "and",
                "clauses": [
                    {
                        "$type": "primaryId",
                        "value": "apple_devices"
                    }
                ]
            }
        },
        {
            "$type": "device",
            "id": "0B2198B2-8E29-4AAB-AFC8-8B2CF827CDE9",
            "name": "All Portable Devices",
            "query": {
                "$type": "and",
                "clauses": [
                    {
                        "$type": "primaryId",
                        "value": "portable_devices"
                    }
                ]
            }
        }
    ],
    "rules": [
        {
            "id": "D861EEB3-9201-45F4-AC63-F823D4957D59",
            "name": "Block All Apple Devices",
            "includeGroups": [
                "3D2A9EF0-E587-4B90-A60F-C9BD6F9D2BB4"
            ],
            "entries": [
                {
                    "$type": "appleDevice",
                    "id": "03420B37-4F71-4AF3-AAE8-82D16817A194",
                    "enforcement": {
                        "$type": "deny"
                    },
                    "__comments": "Customize Access Below",
                    "access": [
                        "download_files_from_device",
                        "sync_content_to_device",
                        "backup_device",
                        "update_device",
                        "download_photos_from_device"
                    ]
                },
                {
                    "$type": "appleDevice",
                    "id": "8C66DF38-A4A2-4C98-B69C-BF5D13F32044",
                    "enforcement": {
                        "$type": "auditDeny",
                        "options": [
                            "send_event",
                            "show_notification"
                        ]
                    },
                    "__comments": "Customize Access Below",
                    "access": [
                        "download_files_from_device",
                        "sync_content_to_device",
                        "backup_device",
                        "update_device",
                        "download_photos_from_device"
                    ]
                }
            ]
        },
        {
            "id": "350C4528-DE48-4E73-9298-0C9823CA1064",
            "name": "Block All Portable Devices",
            "includeGroups": [
                "0B2198B2-8E29-4AAB-AFC8-8B2CF827CDE9"
            ],
            "entries": [
                {
                    "$type": "portableDevice",
                    "id": "E0DB2A03-CAF8-48C6-9FC0-EB6A834166CA",
                    "enforcement": {
                        "$type": "deny"
                    },
                    "__comments": "Customize Access Below",
                    "access": [
                        "download_files_from_device",
                        "send_files_to_device",
                        "download_photos_from_device",
                        "debug"
                    ]
                },
                {
                    "$type": "portableDevice",
                    "id": "E8112895-D818-4CBE-B4CA-EE9FFE351A4C",
                    "enforcement": {
                        "$type": "auditDeny",
                        "options": [
                            "send_event",
                            "show_notification"
                        ]
                    },
                    "__comments": "Customize Access Below",
                    "access": [
                        "download_files_from_device",
                        "send_files_to_device",
                        "download_photos_from_device",
                        "debug"
                    ]
                }
            ]
        }
    ],
    "settings": {
        "features": {
            "appleDevice": {
                "disable": false
            },
            "removableMedia": {
                "disable": false
            },
            "portableDevice": {
                "disable": false
            },
            "bluetoothDevice": {
                "disable": false
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
            "id": "3D2A9EF0-E587-4B90-A60F-C9BD6F9D2BB4",
            "name": "All Apple Devices",
            "query": {
                "$type": "and",
                "clauses": [
                    {
                        "$type": "primaryId",
                        "value": "apple_devices"
                    }
                ]
            }
        },
        {
            "$type": "device",
            "id": "0B2198B2-8E29-4AAB-AFC8-8B2CF827CDE9",
            "name": "All Portable Devices",
            "query": {
                "$type": "and",
                "clauses": [
                    {
                        "$type": "primaryId",
                        "value": "portable_devices"
                    }
                ]
            }
        }
    ],
    "rules": [
        {
            "id": "D861EEB3-9201-45F4-AC63-F823D4957D59",
            "name": "Block All Apple Devices",
            "includeGroups": [
                "3D2A9EF0-E587-4B90-A60F-C9BD6F9D2BB4"
            ],
            "entries": [
                {
                    "$type": "appleDevice",
                    "id": "03420B37-4F71-4AF3-AAE8-82D16817A194",
                    "enforcement": {
                        "$type": "deny"
                    },
                    "__comments": "Customize Access Below",
                    "access": [
                        "download_files_from_device",
                        "sync_content_to_device",
                        "backup_device",
                        "update_device",
                        "download_photos_from_device"
                    ]
                },
                {
                    "$type": "appleDevice",
                    "id": "8C66DF38-A4A2-4C98-B69C-BF5D13F32044",
                    "enforcement": {
                        "$type": "auditDeny",
                        "options": [
                            "send_event",
                            "show_notification"
                        ]
                    },
                    "__comments": "Customize Access Below",
                    "access": [
                        "download_files_from_device",
                        "sync_content_to_device",
                        "backup_device",
                        "update_device",
                        "download_photos_from_device"
                    ]
                }
            ]
        },
        {
            "id": "350C4528-DE48-4E73-9298-0C9823CA1064",
            "name": "Block All Portable Devices",
            "includeGroups": [
                "0B2198B2-8E29-4AAB-AFC8-8B2CF827CDE9"
            ],
            "entries": [
                {
                    "$type": "portableDevice",
                    "id": "E0DB2A03-CAF8-48C6-9FC0-EB6A834166CA",
                    "enforcement": {
                        "$type": "deny"
                    },
                    "__comments": "Customize Access Below",
                    "access": [
                        "download_files_from_device",
                        "send_files_to_device",
                        "download_photos_from_device",
                        "debug"
                    ]
                },
                {
                    "$type": "portableDevice",
                    "id": "E8112895-D818-4CBE-B4CA-EE9FFE351A4C",
                    "enforcement": {
                        "$type": "auditDeny",
                        "options": [
                            "send_event",
                            "show_notification"
                        ]
                    },
                    "__comments": "Customize Access Below",
                    "access": [
                        "download_files_from_device",
                        "send_files_to_device",
                        "download_photos_from_device",
                        "debug"
                    ]
                }
            ]
        }
    ],
    "settings": {
        "features": {
            "appleDevice": {
                "disable": false
            },
            "removableMedia": {
                "disable": false
            },
            "portableDevice": {
                "disable": false
            },
            "bluetoothDevice": {
                "disable": false
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


