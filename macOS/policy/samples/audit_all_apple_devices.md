# Device control policy sample: audit_all_apple_devices

Description: A sample policy              
Device Type: Apple Device

A device control policy is a combination of [policy rules](#policy-rules), [groups](#groups) and [settings](#settings).  
This sample is based on the [sample files](#files).  
To configure the sample, follow the [deployment instructions](#deployment-instructions).  

## Policy Rules

<table>
    <tr>
        <th rowspan="2" valign="top">Name</th>
        <th colspan="2" valign="top">Devices</th>
        <th rowspan="2" valign="top">Rule Type</th>
        <th colspan="5" valign="top"><center>Access</center></th>
        <th rowspan="2" valign="top">Notification</th>
    </tr>
    <tr>
        <th>Included</th>
        <th>Excluded</th><th>Backup device</th><th>Update device</th><th>Download photos</th><th>Download files</th><th>Synch device</th></tr><tr>
            <td rowspan="1"><b>Audit all Apple Devices</b></td>
            <td rowspan="1 valign="top">
                <ul><li>All Apple Devices<a href="#all-apple-devices" title="all [{'$type': 'primaryId', 'value': 'apple_devices'}]"> (details)</a></ul>
            </td>
            <td rowspan="1" valign="top">.
                <ul></ul>
            </td>
            <td>Audit Allowed</td>
            <td>:page_facing_up:</td>
            <td>:page_facing_up:</td>
            <td>:page_facing_up:</td>
            <td>:page_facing_up:</td>
            <td>:page_facing_up:</td>
            <td>Send event</td> 
        </tr></table>


## Groups


### All Apple Devices



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

<td>apple_devices</td>

</tr>

</table>


#### Available properties for All Apple Devices


<details>
<summary>View JSON</summary>

```json
{
    "$type": "device",
    "id": "3f082cd3-f701-4c21-9a6a-ed115c28e217",
    "name": "All Apple Devices",
    "query": {
        "$type": "all",
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


## Settings
| Setting Name |  Setting Value | Documentation |
|--------------|----------------|---------------|
SecuredDevicesConfiguration | {'appleDevice': {'disable': False}, 'removableMedia': {'disable': True}, 'portableDevice': {'disable': True}, 'bluetoothDevice': {'disable': True}} | [documentation](https://learn.microsoft.com/en-us/windows/client-management/mdm/defender-csp#configurationsecureddevicesconfiguration) |
DefaultEnforcement | Allow | [documentation](https://learn.microsoft.com/en-us/windows/client-management/mdm/defender-csp#configurationdefaultenforcement) |
UXNavigationTarget | http://www.microsoft.com | [documentation]() |


## Files
This policy is based on information in the following files:

- [macOS/policy/samples/audit_all_apple_devices.json](/macOS/policy/samples/audit_all_apple_devices.json)


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
            "id": "3f082cd3-f701-4c21-9a6a-ed115c28e217",
            "name": "All Apple Devices",
            "query": {
                "$type": "all",
                "clauses": [
                    {
                        "$type": "primaryId",
                        "value": "apple_devices"
                    }
                ]
            }
        }
    ],
    "rules": [
        {
            "id": "772cef80-229f-48b4-bd17-a6913009298e",
            "name": "Audit all Apple Devices",
            "includeGroups": [
                "3f082cd3-f701-4c21-9a6a-ed115c28e217"
            ],
            "entries": [
                {
                    "$type": "appleDevice",
                    "id": "2E75C9DE-5C96-40C1-8333-A52A9409DEB1",
                    "enforcement": {
                        "$type": "auditAllow",
                        "options": [
                            "send_event"
                        ]
                    },
                    "access": [
                        "download_files_from_device",
                        "sync_content_to_device",
                        "backup_device",
                        "update_device",
                        "download_photos_from_device"
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
                "disable": true
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
            "id": "3f082cd3-f701-4c21-9a6a-ed115c28e217",
            "name": "All Apple Devices",
            "query": {
                "$type": "all",
                "clauses": [
                    {
                        "$type": "primaryId",
                        "value": "apple_devices"
                    }
                ]
            }
        }
    ],
    "rules": [
        {
            "id": "772cef80-229f-48b4-bd17-a6913009298e",
            "name": "Audit all Apple Devices",
            "includeGroups": [
                "3f082cd3-f701-4c21-9a6a-ed115c28e217"
            ],
            "entries": [
                {
                    "$type": "appleDevice",
                    "id": "2E75C9DE-5C96-40C1-8333-A52A9409DEB1",
                    "enforcement": {
                        "$type": "auditAllow",
                        "options": [
                            "send_event"
                        ]
                    },
                    "access": [
                        "download_files_from_device",
                        "sync_content_to_device",
                        "backup_device",
                        "update_device",
                        "download_photos_from_device"
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
                "disable": true
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


