# Device control policy sample: audit_all_removable_media

Description: A sample policy              
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
            <td rowspan="2"><b>Audit RWX to all Removable Media Devices</b></td>
            <td rowspan="2 valign="top">
                <ul><li>All Removable Media Devices<a href="#all-removable-media-devices" title="all [{'$type': 'primaryId', 'value': 'removable_media_devices'}]"> (details)</a></ul>
            </td>
            <td rowspan="2" valign="top">.
                <ul></ul>
            </td>
            <td>allow</td>
            <td>:white_check_mark:</td>
            <td>:white_check_mark:</td>
            <td>:white_check_mark:</td>
            <td>None</td> 
        </tr><tr>
            <td>auditAllowed</td>
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
    "id": "94b5df10-bd2f-4b19-8a9f-539520b9d6ff",
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
| Setting Name |  Setting Value | Documentation |
|--------------|----------------|---------------|
SecuredDevicesConfiguration | {'appleDevice': {'disable': False}, 'removableMedia': {'disable': False}, 'portableDevice': {'disable': True}, 'bluetoothDevice': {'disable': True}} | [documentation](https://learn.microsoft.com/en-us/windows/client-management/mdm/defender-csp#configurationsecureddevicesconfiguration) |
DefaultEnforcement | Allow | [documentation](https://learn.microsoft.com/en-us/windows/client-management/mdm/defender-csp#configurationdefaultenforcement) |
UXNavigationTarget | http://www.microsoft.com | [documentation]() |


## Files
This policy is based on information in the following files:

- [macOS/policy/examples/all_removable_media_devices94b5df10-bd2f-4b19-8a9f-539520b9d6ff.xml](macOS/policy/examples/all_removable_media_devices94b5df10-bd2f-4b19-8a9f-539520b9d6ff.xml)
- [macOS/policy/examples/audit_all_removable_media.json](macOS/policy/examples/audit_all_removable_media.json)


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
            "id": "94b5df10-bd2f-4b19-8a9f-539520b9d6ff",
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
            "id": "2e18a6b9-eb30-440a-a6aa-1f930b443baf",
            "name": "Audit RWX to all Removable Media Devices",
            "includeGroups": [
                "94b5df10-bd2f-4b19-8a9f-539520b9d6ff"
            ],
            "entries": [
                {
                    "__comments": "Allow all Read, Write, and Execute operations.  Note: This entry is optional as global/defaultEnforcement is 'allow'.",
                    "$type": "removableMedia",
                    "id": "2566d326-d8e9-49be-9b8e-2fd0853e6641",
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
                    "__comments": "Send events for all allowed operations.  Note: This may result in a significant volume of events.  Adjust or remove this entry as desired.",
                    "$type": "removableMedia",
                    "id": "ea3ccfe9-ec04-4fa2-a6bb-06941c7b051a",
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
                "disable": false
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
            "id": "94b5df10-bd2f-4b19-8a9f-539520b9d6ff",
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
            "id": "2e18a6b9-eb30-440a-a6aa-1f930b443baf",
            "name": "Audit RWX to all Removable Media Devices",
            "includeGroups": [
                "94b5df10-bd2f-4b19-8a9f-539520b9d6ff"
            ],
            "entries": [
                {
                    "__comments": "Allow all Read, Write, and Execute operations.  Note: This entry is optional as global/defaultEnforcement is 'allow'.",
                    "$type": "removableMedia",
                    "id": "2566d326-d8e9-49be-9b8e-2fd0853e6641",
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
                    "__comments": "Send events for all allowed operations.  Note: This may result in a significant volume of events.  Adjust or remove this entry as desired.",
                    "$type": "removableMedia",
                    "id": "ea3ccfe9-ec04-4fa2-a6bb-06941c7b051a",
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
                "disable": false
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


