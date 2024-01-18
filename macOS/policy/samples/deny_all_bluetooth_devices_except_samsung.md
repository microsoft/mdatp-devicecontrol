# Device control policy sample: deny_all_bluetooth_devices_except_samsung

Description: A sample policy              
Device Type: Apple Bluetooth Device

A device control policy is a combination of [policy rules](#policy-rules), [groups](#groups) and [settings](#settings).  
This sample is based on the [sample files](#files).  
To configure the sample, follow the [deployment instructions](#deployment-instructions).  

## Policy Rules

<table>
    <tr>
        <th rowspan="2" valign="top">Name</th>
        <th colspan="2" valign="top">Devices</th>
        <th rowspan="2" valign="top">Rule Type</th>
        <th colspan="2" valign="top"><center>Access</center></th>
        <th rowspan="2" valign="top">Notification</th>
    </tr>
    <tr>
        <th>Included</th>
        <th>Excluded</th><th>Download files</th><th>Send files</th></tr><tr>
            <td rowspan="1"><b>Audit S21</b></td>
            <td rowspan="1 valign="top">
                <ul><li>Samsung Galaxy S21<a href="#samsung-galaxy-s21" title="and [{'$type': 'primaryId', 'value': 'bluetooth_devices'}, {'$type': 'vendorId', 'value': '0075'}, {'$type': 'productId', 'value': '0100'}]"> (details)</a></ul>
            </td>
            <td rowspan="1" valign="top">.
                <ul></ul>
            </td>
            <td>Audit Allowed</td>
            <td>:page_facing_up:</td>
            <td>:page_facing_up:</td>
            <td>Send event</td> 
        </tr><tr>
            <td rowspan="2"><b>Deny all Bluetooth Devices</b></td>
            <td rowspan="2 valign="top">
                <ul><li>All Bluetooth Devices<a href="#all-bluetooth-devices" title="or [{'$type': 'primaryId', 'value': 'bluetooth_devices'}]"> (details)</a></ul>
            </td>
            <td rowspan="2" valign="top">.
                <ul><li>Samsung Galaxy S21<a href="#samsung-galaxy-s21" title="and [{'$type': 'primaryId', 'value': 'bluetooth_devices'}, {'$type': 'vendorId', 'value': '0075'}, {'$type': 'productId', 'value': '0100'}]"> (details)</a></ul>
            </td>
            <td>Deny</td>
            <td>:x:</td>
            <td>:x:</td>
            <td>None</td> 
        </tr><tr>
            <td>Audit Denied</td>
            <td>:page_facing_up:</td>
            <td>:page_facing_up:</td>
            <td>Send event and Show notification</td>
        </tr></table>


## Groups


### Samsung Galaxy S21



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

<td>bluetooth_devices</td>

</tr>

<tr>

<td>and</td>

<td>vendorId</td>

<td>0075</td>

</tr>

<tr>

<td>and</td>

<td>productId</td>

<td>0100</td>

</tr>

</table>


#### Available properties for Samsung Galaxy S21


<details>
<summary>View JSON</summary>

```json
{
    "$type": "device",
    "id": "1A783D32-C6A3-4F5F-9D47-271B12130DFD",
    "name": "Samsung Galaxy S21",
    "query": {
        "$type": "and",
        "clauses": [
            {
                "$type": "primaryId",
                "value": "bluetooth_devices"
            },
            {
                "$type": "vendorId",
                "value": "0075"
            },
            {
                "$type": "productId",
                "value": "0100"
            }
        ]
    }
}
```
</details>

### All Bluetooth Devices



This is a group of type *device*. 
The match type for the group is *or*.


<table>
<tr>
<th>Operator</th>
<th>Property</th>
<th>Value</th>
</tr>

<tr>

<td></td>

<td>primaryId</td>

<td>bluetooth_devices</td>

</tr>

</table>


#### Available properties for All Bluetooth Devices


<details>
<summary>View JSON</summary>

```json
{
    "$type": "device",
    "id": "3f082cd3-f701-4c21-9a6a-ed115c28e417",
    "name": "All Bluetooth Devices",
    "query": {
        "$type": "or",
        "clauses": [
            {
                "$type": "primaryId",
                "value": "bluetooth_devices"
            }
        ]
    }
}
```
</details>


## Settings
| Setting Name |  Setting Value | Documentation |
|--------------|----------------|---------------|
SecuredDevicesConfiguration | {'appleDevice': {'disable': False}, 'removableMedia': {'disable': True}, 'portableDevice': {'disable': True}, 'bluetoothDevice': {'disable': False}} | [documentation](https://learn.microsoft.com/en-us/windows/client-management/mdm/defender-csp#configurationsecureddevicesconfiguration) |
DefaultEnforcement | Allow | [documentation](https://learn.microsoft.com/en-us/windows/client-management/mdm/defender-csp#configurationdefaultenforcement) |
UXNavigationTarget | http://www.microsoft.com | [documentation]() |


## Files
This policy is based on information in the following files:

- [macOS/policy/samples/deny_all_bluetooth_devices_except_samsung.json](/macOS/policy/samples/deny_all_bluetooth_devices_except_samsung.json)


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
            "id": "1A783D32-C6A3-4F5F-9D47-271B12130DFD",
            "name": "Samsung Galaxy S21",
            "query": {
                "$type": "and",
                "clauses": [
                    {
                        "$type": "primaryId",
                        "value": "bluetooth_devices"
                    },
                    {
                        "$type": "vendorId",
                        "value": "0075"
                    },
                    {
                        "$type": "productId",
                        "value": "0100"
                    }
                ]
            }
        },
        {
            "$type": "device",
            "id": "3f082cd3-f701-4c21-9a6a-ed115c28e417",
            "name": "All Bluetooth Devices",
            "query": {
                "$type": "or",
                "clauses": [
                    {
                        "$type": "primaryId",
                        "value": "bluetooth_devices"
                    }
                ]
            }
        }
    ],
    "rules": [
        {
            "id": "3C094B7B-DB94-4F17-86B8-3AA1D6547C58",
            "name": "Audit S21",
            "includeGroups": [
                "1A783D32-C6A3-4F5F-9D47-271B12130DFD"
            ],
            "entries": [
                {
                    "$type": "bluetoothDevice",
                    "id": "477C626F-510E-4881-B475-592CF6E501AF",
                    "enforcement": {
                        "$type": "auditAllow",
                        "options": [
                            "send_event"
                        ]
                    },
                    "access": [
                        "download_files_from_device",
                        "send_files_to_device"
                    ]
                }
            ]
        },
        {
            "id": "772cef80-229f-48b4-bd17-a6913009248d",
            "name": "Deny all Bluetooth Devices",
            "includeGroups": [
                "3f082cd3-f701-4c21-9a6a-ed115c28e417"
            ],
            "excludeGroups": [
                "1A783D32-C6A3-4F5F-9D47-271B12130DFD"
            ],
            "entries": [
                {
                    "$type": "bluetoothDevice",
                    "id": "803B32D7-639A-4A05-BFFB-E8998AA3304B",
                    "enforcement": {
                        "$type": "deny"
                    },
                    "access": [
                        "download_files_from_device",
                        "send_files_to_device"
                    ]
                },
                {
                    "$type": "bluetoothDevice",
                    "id": "5AC7FBBF-5D96-4440-A5C2-87AB9055B45F",
                    "enforcement": {
                        "$type": "auditDeny",
                        "options": [
                            "send_event",
                            "show_notification"
                        ]
                    },
                    "access": [
                        "download_files_from_device",
                        "send_files_to_device"
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
            "id": "1A783D32-C6A3-4F5F-9D47-271B12130DFD",
            "name": "Samsung Galaxy S21",
            "query": {
                "$type": "and",
                "clauses": [
                    {
                        "$type": "primaryId",
                        "value": "bluetooth_devices"
                    },
                    {
                        "$type": "vendorId",
                        "value": "0075"
                    },
                    {
                        "$type": "productId",
                        "value": "0100"
                    }
                ]
            }
        },
        {
            "$type": "device",
            "id": "3f082cd3-f701-4c21-9a6a-ed115c28e417",
            "name": "All Bluetooth Devices",
            "query": {
                "$type": "or",
                "clauses": [
                    {
                        "$type": "primaryId",
                        "value": "bluetooth_devices"
                    }
                ]
            }
        }
    ],
    "rules": [
        {
            "id": "3C094B7B-DB94-4F17-86B8-3AA1D6547C58",
            "name": "Audit S21",
            "includeGroups": [
                "1A783D32-C6A3-4F5F-9D47-271B12130DFD"
            ],
            "entries": [
                {
                    "$type": "bluetoothDevice",
                    "id": "477C626F-510E-4881-B475-592CF6E501AF",
                    "enforcement": {
                        "$type": "auditAllow",
                        "options": [
                            "send_event"
                        ]
                    },
                    "access": [
                        "download_files_from_device",
                        "send_files_to_device"
                    ]
                }
            ]
        },
        {
            "id": "772cef80-229f-48b4-bd17-a6913009248d",
            "name": "Deny all Bluetooth Devices",
            "includeGroups": [
                "3f082cd3-f701-4c21-9a6a-ed115c28e417"
            ],
            "excludeGroups": [
                "1A783D32-C6A3-4F5F-9D47-271B12130DFD"
            ],
            "entries": [
                {
                    "$type": "bluetoothDevice",
                    "id": "803B32D7-639A-4A05-BFFB-E8998AA3304B",
                    "enforcement": {
                        "$type": "deny"
                    },
                    "access": [
                        "download_files_from_device",
                        "send_files_to_device"
                    ]
                },
                {
                    "$type": "bluetoothDevice",
                    "id": "5AC7FBBF-5D96-4440-A5C2-87AB9055B45F",
                    "enforcement": {
                        "$type": "auditDeny",
                        "options": [
                            "send_event",
                            "show_notification"
                        ]
                    },
                    "access": [
                        "download_files_from_device",
                        "send_files_to_device"
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


