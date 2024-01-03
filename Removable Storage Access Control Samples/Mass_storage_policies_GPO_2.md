# Device control policy sample: Mass_storage_policies_GPO_2

Description: A sample policy

A device control policy is a combination of [policy rules](#policy-rules) and [groups](#groups).  
This sample is based on the [sample files](#files).  
To configure the sample, follow the [deployment instructions](#deployment-instructions).  

## Policy Rules
<table>
    <tr>
        <th rowspan="2" valign="top">Name</th>
        <th rowspan="2" valign="top">Devices</th>
        <th rowspan="2" valign="top">Excluding</th>
        <th rowspan="2" valign="top">Rule Type</th>
        <th colspan="7" valign="top"><center>Access</center></th>
        <th rowspan="2" valign="top">Notification</th>
        <th rowspan="2" valign="top">User SID</th>
        <th rowspan="2" valign="top">Conditions</th>
    </tr>
    <tr>
		<th>Disk Read</th>
		<th>Disk Write</th>
		<th>Disk Execute</th>
		<th>File Read</th>
		<th>File Write</th>
		<th>File Execute</th>
		<th>Print</th>
	</tr><tr>
            <td rowspan="10"><b>Gestion des périphériques externes</b></td>
            <td rowspan="10 valign="top">
                <ul><li>Mass_storage_groups_GPO_2_1<a href="#mass_storage_groups_gpo_2_1" title="MatchAny [{'PrimaryId': 'RemovableMediaDevices'}, {'PrimaryId': 'CdRomDevices'}, {'PrimaryId': 'WpdDevices'}, {'FriendlyNameId': 'SDHC*'}, {'FriendlyNameId': 'SDXC*'}, {'DeviceId': 'USBSTOR\\CDROM&VEN_KINGSTON&PROD_DTLOCKER+G3'}, {'VID_PID': '0951_169D'}, {'VID_PID': '2009_16AF'}, {'VID_PID': '1908_0226'}]"> (details)</a></ul>
            </td>
            <td rowspan="10" valign="top">
                <ul><li>Mass_storage_groups_GPO_2_2<a href="#mass_storage_groups_gpo_2_2" title="MatchAny [{'VID_PID': '07B4_0232'}, {'VID_PID': '07B4_0279'}, {'VID_PID': '07B4_0244'}, {'VID_PID': '07B4_0264'}, {'VID_PID': '07B4_0236'}, {'VID_PID': '07B4_0245'}, {'VID_PID': '0911_1F40'}, {'VID_PID': '0911_251C'}, {'VID_PID': '1D54_1072'}, {'VID_PID': '1D54_1070'}, {'VID_PID': '1D54_1080'}, {'VID_PID': '054C_0B6F'}]"> (details)</a><li>Mass_storage_groups_GPO_2_3<a href="#mass_storage_groups_gpo_2_3" title="MatchAny [{'VID_PID': '046D_0837'}, {'VID_PID': '046D_085B'}, {'VID_PID': '046D_0825'}, {'VID_PID': '03F0_5705'}, {'VID_PID': '03F0_5D05'}, {'VID_PID': '040A_6030'}, {'VID_PID': '040A_601D'}, {'VID_PID': '1083_1646'}, {'VID_PID': '1083_1647'}, {'VID_PID': '04CA_7053'}, {'VID_PID': '04CA_7054'}, {'VID_PID': '04F2_B51C'}, {'VID_PID': '05C8_0383'}, {'VID_PID': '05C8_034B'}, {'VID_PID': '0461_4DFE'}]"> (details)</a><li>Mass_storage_groups_GPO_2_4<a href="#mass_storage_groups_gpo_2_4" title="MatchAny [{'VID_PID': '09CB_1007'}, {'VID_PID': '0F7E_900C'}]"> (details)</a></ul>
            </td>
            <td>Allow</td>
            <td>:white_check_mark:</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>None (0)</td> 
            <td>XXXXXX</td>
            <td>
                <ul>
                </ul>
            </td>
        </tr><tr>
            <td>Audit Allowed</td>
            <td>:page_facing_up:</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>Send event (2)</td>
            <td>XXXXXX</td>
            <td>
                <ul>
                </ul>
            </td>
        </tr><tr>
            <td>Allow</td>
            <td>:white_check_mark:</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>None (0)</td>
            <td>XXXXXX</td>
            <td>
                <ul>
                </ul>
            </td>
        </tr><tr>
            <td>Audit Allowed</td>
            <td>:page_facing_up:</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>Send event (2)</td>
            <td>XXXXXX</td>
            <td>
                <ul>
                </ul>
            </td>
        </tr><tr>
            <td>Allow</td>
            <td>:white_check_mark:</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>None (0)</td>
            <td>XXXXXX</td>
            <td>
                <ul>
                </ul>
            </td>
        </tr><tr>
            <td>Audit Allowed</td>
            <td>:page_facing_up:</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>Send event (2)</td>
            <td>XXXXXX</td>
            <td>
                <ul>
                </ul>
            </td>
        </tr><tr>
            <td>Allow</td>
            <td>:white_check_mark:</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>None (0)</td>
            <td>XXXXXX</td>
            <td>
                <ul>
                </ul>
            </td>
        </tr><tr>
            <td>Audit Allowed</td>
            <td>:page_facing_up:</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>Send event (2)</td>
            <td>XXXXXX</td>
            <td>
                <ul>
                </ul>
            </td>
        </tr><tr>
            <td>Deny</td>
            <td>:x:</td>
            <td>:x:</td>
            <td>:x:</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>None (0)</td>
            <td>All Users</td>
            <td>
                <ul>
                </ul>
            </td>
        </tr><tr>
            <td>Audit Denied</td>
            <td>:page_facing_up:</td>
            <td>:page_facing_up:</td>
            <td>:page_facing_up:</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>Show notification and Send event (3)</td>
            <td>All Users</td>
            <td>
                <ul>
                </ul>
            </td>
        </tr><tr>
            <td rowspan="8"><b>Gestion des dictaphones</b></td>
            <td rowspan="8 valign="top">
                <ul><li>Mass_storage_groups_GPO_2_2<a href="#mass_storage_groups_gpo_2_2" title="MatchAny [{'VID_PID': '07B4_0232'}, {'VID_PID': '07B4_0279'}, {'VID_PID': '07B4_0244'}, {'VID_PID': '07B4_0264'}, {'VID_PID': '07B4_0236'}, {'VID_PID': '07B4_0245'}, {'VID_PID': '0911_1F40'}, {'VID_PID': '0911_251C'}, {'VID_PID': '1D54_1072'}, {'VID_PID': '1D54_1070'}, {'VID_PID': '1D54_1080'}, {'VID_PID': '054C_0B6F'}]"> (details)</a></ul>
            </td>
            <td rowspan="8" valign="top">
                <ul></ul>
            </td>
            <td>Allow</td>
            <td>:white_check_mark:</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>None (0)</td> 
            <td>XXXXXX</td>
            <td>
                <ul>
                </ul>
            </td>
        </tr><tr>
            <td>Audit Allowed</td>
            <td>:page_facing_up:</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>Send event (2)</td>
            <td>XXXXXX</td>
            <td>
                <ul>
                </ul>
            </td>
        </tr><tr>
            <td>Allow</td>
            <td>:white_check_mark:</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>None (0)</td>
            <td>XXXXXX</td>
            <td>
                <ul>
                </ul>
            </td>
        </tr><tr>
            <td>Audit Allowed</td>
            <td>:page_facing_up:</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>Send event (2)</td>
            <td>XXXXXX</td>
            <td>
                <ul>
                </ul>
            </td>
        </tr><tr>
            <td>Allow</td>
            <td>:white_check_mark:</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>None (0)</td>
            <td>XXXXXX</td>
            <td>
                <ul>
                </ul>
            </td>
        </tr><tr>
            <td>Audit Allowed</td>
            <td>:page_facing_up:</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>Send event (2)</td>
            <td>XXXXXX</td>
            <td>
                <ul>
                </ul>
            </td>
        </tr><tr>
            <td>Deny</td>
            <td>:x:</td>
            <td>:x:</td>
            <td>:x:</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>None (0)</td>
            <td>All Users</td>
            <td>
                <ul>
                </ul>
            </td>
        </tr><tr>
            <td>Audit Denied</td>
            <td>:page_facing_up:</td>
            <td>:page_facing_up:</td>
            <td>:page_facing_up:</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>Show notification and Send event (3)</td>
            <td>All Users</td>
            <td>
                <ul>
                </ul>
            </td>
        </tr><tr>
            <td rowspan="8"><b>Gestion des appareils immobiliers</b></td>
            <td rowspan="8 valign="top">
                <ul><li>Mass_storage_groups_GPO_2_4<a href="#mass_storage_groups_gpo_2_4" title="MatchAny [{'VID_PID': '09CB_1007'}, {'VID_PID': '0F7E_900C'}]"> (details)</a></ul>
            </td>
            <td rowspan="8" valign="top">
                <ul></ul>
            </td>
            <td>Allow</td>
            <td>:white_check_mark:</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>None (0)</td> 
            <td>XXXXXX</td>
            <td>
                <ul>
                </ul>
            </td>
        </tr><tr>
            <td>Audit Allowed</td>
            <td>:page_facing_up:</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>Send event (2)</td>
            <td>XXXXXX</td>
            <td>
                <ul>
                </ul>
            </td>
        </tr><tr>
            <td>Allow</td>
            <td>:white_check_mark:</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>None (0)</td>
            <td>XXXXXX</td>
            <td>
                <ul>
                </ul>
            </td>
        </tr><tr>
            <td>Audit Allowed</td>
            <td>:page_facing_up:</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>Send event (2)</td>
            <td>XXXXXX</td>
            <td>
                <ul>
                </ul>
            </td>
        </tr><tr>
            <td>Allow</td>
            <td>:white_check_mark:</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>None (0)</td>
            <td>XXXXXX</td>
            <td>
                <ul>
                </ul>
            </td>
        </tr><tr>
            <td>Audit Allowed</td>
            <td>:page_facing_up:</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>Send event (2)</td>
            <td>XXXXXX</td>
            <td>
                <ul>
                </ul>
            </td>
        </tr><tr>
            <td>Deny</td>
            <td>:x:</td>
            <td>:x:</td>
            <td>:x:</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>None (0)</td>
            <td>All Users</td>
            <td>
                <ul>
                </ul>
            </td>
        </tr><tr>
            <td>Audit Denied</td>
            <td>:page_facing_up:</td>
            <td>:page_facing_up:</td>
            <td>:page_facing_up:</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>Show notification and Send event (3)</td>
            <td>All Users</td>
            <td>
                <ul>
                </ul>
            </td>
        </tr></table>

## Groups


### Mass_storage_groups_GPO_2_4

This is a group of type *Device*. 
The match type for the group is *MatchAny*.

|  Property | Value |
|-----------|-------|
| VID_PID | 09CB_1007 |
| VID_PID | 0F7E_900C |

<details>
<summary>View XML</summary>

```xml
<Group Id="{d2887bd4-a916-4011-a385-83c6b15df529}" Type="Device">
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Bd2887bd4-a916-4011-a385-83c6b15df529%7D/GroupData -->
	<Name>Mass_storage_groups_GPO_2_4</Name>
	<MatchType>MatchAny</MatchType>
	<DescriptorIdList>
		<VID_PID>09CB_1007</VID_PID>
		<VID_PID>0F7E_900C</VID_PID>
	</DescriptorIdList>
</Group>
```
</details>

### Mass_storage_groups_GPO_2_1

This is a group of type *Device*. 
The match type for the group is *MatchAny*.

|  Property | Value |
|-----------|-------|
| PrimaryId | RemovableMediaDevices |
| PrimaryId | CdRomDevices |
| PrimaryId | WpdDevices |
| FriendlyNameId | SDHC* |
| FriendlyNameId | SDXC* |
| DeviceId | USBSTOR\CDROM&VEN_KINGSTON&PROD_DTLOCKER+G3 |
| VID_PID | 0951_169D |
| VID_PID | 2009_16AF |
| VID_PID | 1908_0226 |

<details>
<summary>View XML</summary>

```xml
<Group Id="{fb4ad01e-f41a-46c6-9ac1-268efa0ea083}" Type="Device">
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Bfb4ad01e-f41a-46c6-9ac1-268efa0ea083%7D/GroupData -->
	<Name>Mass_storage_groups_GPO_2_1</Name>
	<MatchType>MatchAny</MatchType>
	<DescriptorIdList>
		<PrimaryId>RemovableMediaDevices</PrimaryId>
		<PrimaryId>CdRomDevices</PrimaryId>
		<PrimaryId>WpdDevices</PrimaryId>
		<FriendlyNameId>SDHC*</FriendlyNameId>
		<FriendlyNameId>SDXC*</FriendlyNameId>
		<DeviceId>USBSTOR\CDROM&amp;VEN_KINGSTON&amp;PROD_DTLOCKER+G3</DeviceId>
		<VID_PID>0951_169D</VID_PID>
		<VID_PID>2009_16AF</VID_PID>
		<VID_PID>1908_0226</VID_PID>
	</DescriptorIdList>
</Group>
```
</details>

### Mass_storage_groups_GPO_2_2

This is a group of type *Device*. 
The match type for the group is *MatchAny*.

|  Property | Value |
|-----------|-------|
| VID_PID | 07B4_0232 |
| VID_PID | 07B4_0279 |
| VID_PID | 07B4_0244 |
| VID_PID | 07B4_0264 |
| VID_PID | 07B4_0236 |
| VID_PID | 07B4_0245 |
| VID_PID | 0911_1F40 |
| VID_PID | 0911_251C |
| VID_PID | 1D54_1072 |
| VID_PID | 1D54_1070 |
| VID_PID | 1D54_1080 |
| VID_PID | 054C_0B6F |

<details>
<summary>View XML</summary>

```xml
<Group Id="{7f191817-c305-451d-812a-1c4b03ebcec8}" Type="Device">
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B7f191817-c305-451d-812a-1c4b03ebcec8%7D/GroupData -->
	<Name>Mass_storage_groups_GPO_2_2</Name>
	<MatchType>MatchAny</MatchType>
	<DescriptorIdList>
		<VID_PID>07B4_0232</VID_PID>
		<VID_PID>07B4_0279</VID_PID>
		<VID_PID>07B4_0244</VID_PID>
		<VID_PID>07B4_0264</VID_PID>
		<VID_PID>07B4_0236</VID_PID>
		<VID_PID>07B4_0245</VID_PID>
		<VID_PID>0911_1F40</VID_PID>
		<VID_PID>0911_251C</VID_PID>
		<VID_PID>1D54_1072</VID_PID>
		<VID_PID>1D54_1070</VID_PID>
		<VID_PID>1D54_1080</VID_PID>
		<VID_PID>054C_0B6F</VID_PID>
	</DescriptorIdList>
</Group>
```
</details>

### Mass_storage_groups_GPO_2_3

This is a group of type *Device*. 
The match type for the group is *MatchAny*.

|  Property | Value |
|-----------|-------|
| VID_PID | 046D_0837 |
| VID_PID | 046D_085B |
| VID_PID | 046D_0825 |
| VID_PID | 03F0_5705 |
| VID_PID | 03F0_5D05 |
| VID_PID | 040A_6030 |
| VID_PID | 040A_601D |
| VID_PID | 1083_1646 |
| VID_PID | 1083_1647 |
| VID_PID | 04CA_7053 |
| VID_PID | 04CA_7054 |
| VID_PID | 04F2_B51C |
| VID_PID | 05C8_0383 |
| VID_PID | 05C8_034B |
| VID_PID | 0461_4DFE |

<details>
<summary>View XML</summary>

```xml
<Group Id="{1653593b-5b92-47e6-975a-c43ffa9cd28d}" Type="Device">
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B1653593b-5b92-47e6-975a-c43ffa9cd28d%7D/GroupData -->
	<Name>Mass_storage_groups_GPO_2_3</Name>
	<MatchType>MatchAny</MatchType>
	<DescriptorIdList>
		<VID_PID>046D_0837</VID_PID>
		<VID_PID>046D_085B</VID_PID>
		<VID_PID>046D_0825</VID_PID>
		<VID_PID>03F0_5705</VID_PID>
		<VID_PID>03F0_5D05</VID_PID>
		<VID_PID>040A_6030</VID_PID>
		<VID_PID>040A_601D</VID_PID>
		<VID_PID>1083_1646</VID_PID>
		<VID_PID>1083_1647</VID_PID>
		<VID_PID>04CA_7053</VID_PID>
		<VID_PID>04CA_7054</VID_PID>
		<VID_PID>04F2_B51C</VID_PID>
		<VID_PID>05C8_0383</VID_PID>
		<VID_PID>05C8_034B</VID_PID>
		<VID_PID>0461_4DFE</VID_PID>
	</DescriptorIdList>
</Group>
```
</details>


## Files
This policy is based on information in the following files:

- [Group Policy/Mass_storage_policies_GPO_2.xml](Group%20Policy/Mass_storage_policies_GPO_2.xml)
- [Group Policy/Mass_storage_groups_GPO_2.xml](Group%20Policy/Mass_storage_groups_GPO_2.xml)


# Deployment Instructions

Device control [policy rules](#policy-rules) and [groups](#groups) can be deployed through the following management tools:

## Windows
- [Intune UX](#intune-ux)
- [Intune Custom Settings](#intune-custom-settings)
- [Group Policy (GPO)](#group-policy-gpo)

## Mac
- [Mac Policy](#mac-policy)

## Intune UX

<details>
<summary>Create a reusable setting for Mass_storage_groups_GPO_2_4</summary> 

   1. Navigate to Home > Endpoint Security > Attack Surface Reduction
   2. Click on Reusable Settings
   3. Click (+) Add
   4. Enter the Mass_storage_groups_GPO_2_4 for the name.  
   5. Optionally, enter a description
   6. Click on "Next"
   7. Set the match type toggle to MatchAny
   
      
   8. Add a Removable Storage object for VID_PID
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Edit Instance"    
        4. Enter *VID_PID* for Name
        5. Enter *09CB_1007* for VID_PID
        6. Click "Save"
    
   
      
   8. Add a Removable Storage object for VID_PID
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Edit Instance"    
        4. Enter *VID_PID* for Name
        5. Enter *0F7E_900C* for VID_PID
        6. Click "Save"
    
   
   8. Click "Next"
   9. Click "Add"
</details>
<details>
<summary>Create a reusable setting for Mass_storage_groups_GPO_2_1</summary> 

   1. Navigate to Home > Endpoint Security > Attack Surface Reduction
   2. Click on Reusable Settings
   3. Click (+) Add
   4. Enter the Mass_storage_groups_GPO_2_1 for the name.  
   5. Optionally, enter a description
   6. Click on "Next"
   7. Set the match type toggle to MatchAny
   
      
   8. Add a Removable Storage object for PrimaryId
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Edit Instance"    
        4. Enter *PrimaryId* for Name
        5. Enter *RemovableMediaDevices* for PrimaryId
        6. Click "Save"
    
   
      
   8. Add a Removable Storage object for PrimaryId
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Edit Instance"    
        4. Enter *PrimaryId* for Name
        5. Enter *CdRomDevices* for PrimaryId
        6. Click "Save"
    
   
      
   8. Add a Removable Storage object for PrimaryId
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Edit Instance"    
        4. Enter *PrimaryId* for Name
        5. Enter *WpdDevices* for PrimaryId
        6. Click "Save"
    
   
      
   8. Add a Removable Storage object for FriendlyNameId
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Edit Instance"    
        4. Enter *FriendlyNameId* for Name
        5. Enter *SDHC** for FriendlyNameId
        6. Click "Save"
    
   
      
   8. Add a Removable Storage object for FriendlyNameId
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Edit Instance"    
        4. Enter *FriendlyNameId* for Name
        5. Enter *SDXC** for FriendlyNameId
        6. Click "Save"
    
   
      
   8. Add a Removable Storage object for DeviceId
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Edit Instance"    
        4. Enter *DeviceId* for Name
        5. Enter *USBSTOR\CDROM&VEN_KINGSTON&PROD_DTLOCKER+G3* for DeviceId
        6. Click "Save"
    
   
      
   8. Add a Removable Storage object for VID_PID
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Edit Instance"    
        4. Enter *VID_PID* for Name
        5. Enter *0951_169D* for VID_PID
        6. Click "Save"
    
   
      
   8. Add a Removable Storage object for VID_PID
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Edit Instance"    
        4. Enter *VID_PID* for Name
        5. Enter *2009_16AF* for VID_PID
        6. Click "Save"
    
   
      
   8. Add a Removable Storage object for VID_PID
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Edit Instance"    
        4. Enter *VID_PID* for Name
        5. Enter *1908_0226* for VID_PID
        6. Click "Save"
    
   
   8. Click "Next"
   9. Click "Add"
</details>
<details>
<summary>Create a reusable setting for Mass_storage_groups_GPO_2_2</summary> 

   1. Navigate to Home > Endpoint Security > Attack Surface Reduction
   2. Click on Reusable Settings
   3. Click (+) Add
   4. Enter the Mass_storage_groups_GPO_2_2 for the name.  
   5. Optionally, enter a description
   6. Click on "Next"
   7. Set the match type toggle to MatchAny
   
      
   8. Add a Removable Storage object for VID_PID
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Edit Instance"    
        4. Enter *VID_PID* for Name
        5. Enter *07B4_0232* for VID_PID
        6. Click "Save"
    
   
      
   8. Add a Removable Storage object for VID_PID
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Edit Instance"    
        4. Enter *VID_PID* for Name
        5. Enter *07B4_0279* for VID_PID
        6. Click "Save"
    
   
      
   8. Add a Removable Storage object for VID_PID
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Edit Instance"    
        4. Enter *VID_PID* for Name
        5. Enter *07B4_0244* for VID_PID
        6. Click "Save"
    
   
      
   8. Add a Removable Storage object for VID_PID
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Edit Instance"    
        4. Enter *VID_PID* for Name
        5. Enter *07B4_0264* for VID_PID
        6. Click "Save"
    
   
      
   8. Add a Removable Storage object for VID_PID
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Edit Instance"    
        4. Enter *VID_PID* for Name
        5. Enter *07B4_0236* for VID_PID
        6. Click "Save"
    
   
      
   8. Add a Removable Storage object for VID_PID
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Edit Instance"    
        4. Enter *VID_PID* for Name
        5. Enter *07B4_0245* for VID_PID
        6. Click "Save"
    
   
      
   8. Add a Removable Storage object for VID_PID
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Edit Instance"    
        4. Enter *VID_PID* for Name
        5. Enter *0911_1F40* for VID_PID
        6. Click "Save"
    
   
      
   8. Add a Removable Storage object for VID_PID
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Edit Instance"    
        4. Enter *VID_PID* for Name
        5. Enter *0911_251C* for VID_PID
        6. Click "Save"
    
   
      
   8. Add a Removable Storage object for VID_PID
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Edit Instance"    
        4. Enter *VID_PID* for Name
        5. Enter *1D54_1072* for VID_PID
        6. Click "Save"
    
   
      
   8. Add a Removable Storage object for VID_PID
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Edit Instance"    
        4. Enter *VID_PID* for Name
        5. Enter *1D54_1070* for VID_PID
        6. Click "Save"
    
   
      
   8. Add a Removable Storage object for VID_PID
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Edit Instance"    
        4. Enter *VID_PID* for Name
        5. Enter *1D54_1080* for VID_PID
        6. Click "Save"
    
   
      
   8. Add a Removable Storage object for VID_PID
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Edit Instance"    
        4. Enter *VID_PID* for Name
        5. Enter *054C_0B6F* for VID_PID
        6. Click "Save"
    
   
   8. Click "Next"
   9. Click "Add"
</details>
<details>
<summary>Create a reusable setting for Mass_storage_groups_GPO_2_3</summary> 

   1. Navigate to Home > Endpoint Security > Attack Surface Reduction
   2. Click on Reusable Settings
   3. Click (+) Add
   4. Enter the Mass_storage_groups_GPO_2_3 for the name.  
   5. Optionally, enter a description
   6. Click on "Next"
   7. Set the match type toggle to MatchAny
   
      
   8. Add a Removable Storage object for VID_PID
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Edit Instance"    
        4. Enter *VID_PID* for Name
        5. Enter *046D_0837* for VID_PID
        6. Click "Save"
    
   
      
   8. Add a Removable Storage object for VID_PID
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Edit Instance"    
        4. Enter *VID_PID* for Name
        5. Enter *046D_085B* for VID_PID
        6. Click "Save"
    
   
      
   8. Add a Removable Storage object for VID_PID
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Edit Instance"    
        4. Enter *VID_PID* for Name
        5. Enter *046D_0825* for VID_PID
        6. Click "Save"
    
   
      
   8. Add a Removable Storage object for VID_PID
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Edit Instance"    
        4. Enter *VID_PID* for Name
        5. Enter *03F0_5705* for VID_PID
        6. Click "Save"
    
   
      
   8. Add a Removable Storage object for VID_PID
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Edit Instance"    
        4. Enter *VID_PID* for Name
        5. Enter *03F0_5D05* for VID_PID
        6. Click "Save"
    
   
      
   8. Add a Removable Storage object for VID_PID
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Edit Instance"    
        4. Enter *VID_PID* for Name
        5. Enter *040A_6030* for VID_PID
        6. Click "Save"
    
   
      
   8. Add a Removable Storage object for VID_PID
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Edit Instance"    
        4. Enter *VID_PID* for Name
        5. Enter *040A_601D* for VID_PID
        6. Click "Save"
    
   
      
   8. Add a Removable Storage object for VID_PID
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Edit Instance"    
        4. Enter *VID_PID* for Name
        5. Enter *1083_1646* for VID_PID
        6. Click "Save"
    
   
      
   8. Add a Removable Storage object for VID_PID
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Edit Instance"    
        4. Enter *VID_PID* for Name
        5. Enter *1083_1647* for VID_PID
        6. Click "Save"
    
   
      
   8. Add a Removable Storage object for VID_PID
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Edit Instance"    
        4. Enter *VID_PID* for Name
        5. Enter *04CA_7053* for VID_PID
        6. Click "Save"
    
   
      
   8. Add a Removable Storage object for VID_PID
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Edit Instance"    
        4. Enter *VID_PID* for Name
        5. Enter *04CA_7054* for VID_PID
        6. Click "Save"
    
   
      
   8. Add a Removable Storage object for VID_PID
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Edit Instance"    
        4. Enter *VID_PID* for Name
        5. Enter *04F2_B51C* for VID_PID
        6. Click "Save"
    
   
      
   8. Add a Removable Storage object for VID_PID
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Edit Instance"    
        4. Enter *VID_PID* for Name
        5. Enter *05C8_0383* for VID_PID
        6. Click "Save"
    
   
      
   8. Add a Removable Storage object for VID_PID
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Edit Instance"    
        4. Enter *VID_PID* for Name
        5. Enter *05C8_034B* for VID_PID
        6. Click "Save"
    
   
      
   8. Add a Removable Storage object for VID_PID
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Edit Instance"    
        4. Enter *VID_PID* for Name
        5. Enter *0461_4DFE* for VID_PID
        6. Click "Save"
    
   
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

> [!IMPORTANT]
> This policy has more than 1 rule.  
> Policy ordering is not guaranteed by Intune.
> Make sure that policy is not dependent on order to achieve desired result.
> Consider using ```default deny```.   


<details>
<summary>Add a rule for Gestion des périphériques externes to the policy</summary>


   1. Click on "+ Set reusable settings" under Included Id

   1. Click on *Mass_storage_groups_GPO_2_1*

   1. Click on "Select"


   1. Click on "+ Set reusable settings" under Excluded Id

   1. Click on *Mass_storage_groups_GPO_2_2*

   1. Click on *Mass_storage_groups_GPO_2_3*

   1. Click on *Mass_storage_groups_GPO_2_4*

   1. Click on "Select"

   1. Click on "+ Edit Entry"
   1. Enter *Gestion des périphériques externes* for the name



   1. Select *Allow* from "Type"
   1. Select *None* from "Options"
   1. Select *Read* from "Access mask"

   1. Enter *XXXXXX* for "Sid"




   1. Add another entry.  Click on "+ Add"

   1. Select *Audit Allowed* from "Type"
   1. Select *Send event* from "Options"
   1. Select *Read* from "Access mask"

   1. Enter *XXXXXX* for "Sid"




   1. Add another entry.  Click on "+ Add"

   1. Select *Allow* from "Type"
   1. Select *None* from "Options"
   1. Select *Read* from "Access mask"

   1. Enter *XXXXXX* for "Sid"




   1. Add another entry.  Click on "+ Add"

   1. Select *Audit Allowed* from "Type"
   1. Select *Send event* from "Options"
   1. Select *Read* from "Access mask"

   1. Enter *XXXXXX* for "Sid"




   1. Add another entry.  Click on "+ Add"

   1. Select *Allow* from "Type"
   1. Select *None* from "Options"
   1. Select *Read* from "Access mask"

   1. Enter *XXXXXX* for "Sid"




   1. Add another entry.  Click on "+ Add"

   1. Select *Audit Allowed* from "Type"
   1. Select *Send event* from "Options"
   1. Select *Read* from "Access mask"

   1. Enter *XXXXXX* for "Sid"




   1. Add another entry.  Click on "+ Add"

   1. Select *Allow* from "Type"
   1. Select *None* from "Options"
   1. Select *Read* from "Access mask"

   1. Enter *XXXXXX* for "Sid"




   1. Add another entry.  Click on "+ Add"

   1. Select *Audit Allowed* from "Type"
   1. Select *Send event* from "Options"
   1. Select *Read* from "Access mask"

   1. Enter *XXXXXX* for "Sid"




   1. Add another entry.  Click on "+ Add"

   1. Select *Deny* from "Type"
   1. Select *None* from "Options"
   1. Select *Read, Write and Execute* from "Access mask"




   1. Add another entry.  Click on "+ Add"

   1. Select *Audit Denied* from "Type"
   1. Select *Show notification and Send event* from "Options"
   1. Select *Read, Write and Execute* from "Access mask"


   1. Click "OK"
</details>

<details>
<summary>Add a rule for Gestion des dictaphones to the policy</summary>

   1. Add another rule.  Click on "+ Add"


   1. Click on "+ Set reusable settings" under Included Id

   1. Click on *Mass_storage_groups_GPO_2_2*

   1. Click on "Select"


   1. Click on "+ Edit Entry"
   1. Enter *Gestion des dictaphones* for the name



   1. Select *Allow* from "Type"
   1. Select *None* from "Options"
   1. Select *Read* from "Access mask"

   1. Enter *XXXXXX* for "Sid"




   1. Add another entry.  Click on "+ Add"

   1. Select *Audit Allowed* from "Type"
   1. Select *Send event* from "Options"
   1. Select *Read* from "Access mask"

   1. Enter *XXXXXX* for "Sid"




   1. Add another entry.  Click on "+ Add"

   1. Select *Allow* from "Type"
   1. Select *None* from "Options"
   1. Select *Read* from "Access mask"

   1. Enter *XXXXXX* for "Sid"




   1. Add another entry.  Click on "+ Add"

   1. Select *Audit Allowed* from "Type"
   1. Select *Send event* from "Options"
   1. Select *Read* from "Access mask"

   1. Enter *XXXXXX* for "Sid"




   1. Add another entry.  Click on "+ Add"

   1. Select *Allow* from "Type"
   1. Select *None* from "Options"
   1. Select *Read* from "Access mask"

   1. Enter *XXXXXX* for "Sid"




   1. Add another entry.  Click on "+ Add"

   1. Select *Audit Allowed* from "Type"
   1. Select *Send event* from "Options"
   1. Select *Read* from "Access mask"

   1. Enter *XXXXXX* for "Sid"




   1. Add another entry.  Click on "+ Add"

   1. Select *Deny* from "Type"
   1. Select *None* from "Options"
   1. Select *Read, Write and Execute* from "Access mask"




   1. Add another entry.  Click on "+ Add"

   1. Select *Audit Denied* from "Type"
   1. Select *Show notification and Send event* from "Options"
   1. Select *Read, Write and Execute* from "Access mask"


   1. Click "OK"
</details>

<details>
<summary>Add a rule for Gestion des appareils immobiliers to the policy</summary>

   1. Add another rule.  Click on "+ Add"


   1. Click on "+ Set reusable settings" under Included Id

   1. Click on *Mass_storage_groups_GPO_2_4*

   1. Click on "Select"


   1. Click on "+ Edit Entry"
   1. Enter *Gestion des appareils immobiliers* for the name



   1. Select *Allow* from "Type"
   1. Select *None* from "Options"
   1. Select *Read* from "Access mask"

   1. Enter *XXXXXX* for "Sid"




   1. Add another entry.  Click on "+ Add"

   1. Select *Audit Allowed* from "Type"
   1. Select *Send event* from "Options"
   1. Select *Read* from "Access mask"

   1. Enter *XXXXXX* for "Sid"




   1. Add another entry.  Click on "+ Add"

   1. Select *Allow* from "Type"
   1. Select *None* from "Options"
   1. Select *Read* from "Access mask"

   1. Enter *XXXXXX* for "Sid"




   1. Add another entry.  Click on "+ Add"

   1. Select *Audit Allowed* from "Type"
   1. Select *Send event* from "Options"
   1. Select *Read* from "Access mask"

   1. Enter *XXXXXX* for "Sid"




   1. Add another entry.  Click on "+ Add"

   1. Select *Allow* from "Type"
   1. Select *None* from "Options"
   1. Select *Read* from "Access mask"

   1. Enter *XXXXXX* for "Sid"




   1. Add another entry.  Click on "+ Add"

   1. Select *Audit Allowed* from "Type"
   1. Select *Send event* from "Options"
   1. Select *Read* from "Access mask"

   1. Enter *XXXXXX* for "Sid"




   1. Add another entry.  Click on "+ Add"

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
	<Group Id="{d2887bd4-a916-4011-a385-83c6b15df529}" Type="Device">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Bd2887bd4-a916-4011-a385-83c6b15df529%7D/GroupData -->
		<Name>Mass_storage_groups_GPO_2_4</Name>
		<MatchType>MatchAny</MatchType>
		<DescriptorIdList>
			<VID_PID>09CB_1007</VID_PID>
			<VID_PID>0F7E_900C</VID_PID>
		</DescriptorIdList>
	</Group>
	<Group Id="{fb4ad01e-f41a-46c6-9ac1-268efa0ea083}" Type="Device">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Bfb4ad01e-f41a-46c6-9ac1-268efa0ea083%7D/GroupData -->
		<Name>Mass_storage_groups_GPO_2_1</Name>
		<MatchType>MatchAny</MatchType>
		<DescriptorIdList>
			<PrimaryId>RemovableMediaDevices</PrimaryId>
			<PrimaryId>CdRomDevices</PrimaryId>
			<PrimaryId>WpdDevices</PrimaryId>
			<FriendlyNameId>SDHC*</FriendlyNameId>
			<FriendlyNameId>SDXC*</FriendlyNameId>
			<DeviceId>USBSTOR\CDROM&amp;VEN_KINGSTON&amp;PROD_DTLOCKER+G3</DeviceId>
			<VID_PID>0951_169D</VID_PID>
			<VID_PID>2009_16AF</VID_PID>
			<VID_PID>1908_0226</VID_PID>
		</DescriptorIdList>
	</Group>
	<Group Id="{7f191817-c305-451d-812a-1c4b03ebcec8}" Type="Device">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B7f191817-c305-451d-812a-1c4b03ebcec8%7D/GroupData -->
		<Name>Mass_storage_groups_GPO_2_2</Name>
		<MatchType>MatchAny</MatchType>
		<DescriptorIdList>
			<VID_PID>07B4_0232</VID_PID>
			<VID_PID>07B4_0279</VID_PID>
			<VID_PID>07B4_0244</VID_PID>
			<VID_PID>07B4_0264</VID_PID>
			<VID_PID>07B4_0236</VID_PID>
			<VID_PID>07B4_0245</VID_PID>
			<VID_PID>0911_1F40</VID_PID>
			<VID_PID>0911_251C</VID_PID>
			<VID_PID>1D54_1072</VID_PID>
			<VID_PID>1D54_1070</VID_PID>
			<VID_PID>1D54_1080</VID_PID>
			<VID_PID>054C_0B6F</VID_PID>
		</DescriptorIdList>
	</Group>
	<Group Id="{1653593b-5b92-47e6-975a-c43ffa9cd28d}" Type="Device">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B1653593b-5b92-47e6-975a-c43ffa9cd28d%7D/GroupData -->
		<Name>Mass_storage_groups_GPO_2_3</Name>
		<MatchType>MatchAny</MatchType>
		<DescriptorIdList>
			<VID_PID>046D_0837</VID_PID>
			<VID_PID>046D_085B</VID_PID>
			<VID_PID>046D_0825</VID_PID>
			<VID_PID>03F0_5705</VID_PID>
			<VID_PID>03F0_5D05</VID_PID>
			<VID_PID>040A_6030</VID_PID>
			<VID_PID>040A_601D</VID_PID>
			<VID_PID>1083_1646</VID_PID>
			<VID_PID>1083_1647</VID_PID>
			<VID_PID>04CA_7053</VID_PID>
			<VID_PID>04CA_7054</VID_PID>
			<VID_PID>04F2_B51C</VID_PID>
			<VID_PID>05C8_0383</VID_PID>
			<VID_PID>05C8_034B</VID_PID>
			<VID_PID>0461_4DFE</VID_PID>
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
	<PolicyRule Id="{466faba8-dddf-4ae5-9871-dabbb600d4f3}" >
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B466faba8-dddf-4ae5-9871-dabbb600d4f3%7D/RuleData -->
		<Name>Gestion des périphériques externes</Name>
		<IncludedIdList>
			<GroupId>{fb4ad01e-f41a-46c6-9ac1-268efa0ea083}</GroupId>
		</IncludedIdList>
		<ExcludedIdList>
			<GroupId>{7f191817-c305-451d-812a-1c4b03ebcec8}</GroupId>
			<GroupId>{1653593b-5b92-47e6-975a-c43ffa9cd28d}</GroupId>
			<GroupId>{d2887bd4-a916-4011-a385-83c6b15df529}</GroupId>
		</ExcludedIdList>
		<Entry Id="{f577a950-ce74-4153-90fd-c79d3bf0eb3d}">
			<Type>Allow</Type>
			<AccessMask>1</AccessMask>
			<Options>0</Options>
			<Sid>XXXXXX</Sid>
		</Entry>
		<Entry Id="{428e439f-d8ee-4314-9a8a-92685c4d961c}">
			<Type>AuditAllowed</Type>
			<AccessMask>1</AccessMask>
			<Options>2</Options>
			<Sid>XXXXXX</Sid>
		</Entry>
		<Entry Id="{a3886e5f-093f-4e9c-812f-d7334d5ee052}">
			<Type>Allow</Type>
			<AccessMask>1</AccessMask>
			<Options>0</Options>
			<Sid>XXXXXX</Sid>
		</Entry>
		<Entry Id="{4565ab13-0d58-4a7c-8399-5b65f470ecae}">
			<Type>AuditAllowed</Type>
			<AccessMask>1</AccessMask>
			<Options>2</Options>
			<Sid>XXXXXX</Sid>
		</Entry>
		<Entry Id="{f7cd79af-e330-4fea-9345-467d9bb51131}">
			<Type>Allow</Type>
			<AccessMask>1</AccessMask>
			<Options>0</Options>
			<Sid>XXXXXX</Sid>
		</Entry>
		<Entry Id="{e8e9077f-5111-4a7d-ade6-723c08fd7797}">
			<Type>AuditAllowed</Type>
			<AccessMask>1</AccessMask>
			<Options>2</Options>
			<Sid>XXXXXX</Sid>
		</Entry>
		<Entry Id="{a3421c37-ac07-4085-9bbd-ec9b4ebbd60e}">
			<Type>Allow</Type>
			<AccessMask>1</AccessMask>
			<Options>0</Options>
			<Sid>XXXXXX</Sid>
		</Entry>
		<Entry Id="{e2f263f2-c597-406d-a5f7-9d91909a32c6}">
			<Type>AuditAllowed</Type>
			<AccessMask>1</AccessMask>
			<Options>2</Options>
			<Sid>XXXXXX</Sid>
		</Entry>
		<Entry Id="{170070b1-b68d-4175-9cd4-753a76197496}">
			<Type>Deny</Type>
			<AccessMask>7</AccessMask>
			<Options>0</Options>
		</Entry>
		<Entry Id="{ca86bec9-ba43-4849-a632-e59e5e5c207b}">
			<Type>AuditDenied</Type>
			<AccessMask>7</AccessMask>
			<Options>3</Options>
		</Entry>
	</PolicyRule>
	<PolicyRule Id="{540efb7f-1836-4956-8888-5d41d981d6ba}" >
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B540efb7f-1836-4956-8888-5d41d981d6ba%7D/RuleData -->
		<Name>Gestion des dictaphones</Name>
		<IncludedIdList>
			<GroupId>{7f191817-c305-451d-812a-1c4b03ebcec8}</GroupId>
		</IncludedIdList>
		<ExcludedIdList>
		</ExcludedIdList>
		<Entry Id="{bdd26ee1-4d28-487a-9931-6322ae9e3f91}">
			<Type>Allow</Type>
			<AccessMask>1</AccessMask>
			<Options>0</Options>
			<Sid>XXXXXX</Sid>
		</Entry>
		<Entry Id="{92237bd0-84bf-4d1a-81c0-2507d6274532}">
			<Type>AuditAllowed</Type>
			<AccessMask>1</AccessMask>
			<Options>2</Options>
			<Sid>XXXXXX</Sid>
		</Entry>
		<Entry Id="{cd7fb4ed-fe8d-4122-949e-3c8306152978}">
			<Type>Allow</Type>
			<AccessMask>1</AccessMask>
			<Options>0</Options>
			<Sid>XXXXXX</Sid>
		</Entry>
		<Entry Id="{84a53752-fbdc-4e39-b15c-8787130bc6d6}">
			<Type>AuditAllowed</Type>
			<AccessMask>1</AccessMask>
			<Options>2</Options>
			<Sid>XXXXXX</Sid>
		</Entry>
		<Entry Id="{873026a4-0c93-4061-b784-b1f7bb43b891}">
			<Type>Allow</Type>
			<AccessMask>1</AccessMask>
			<Options>0</Options>
			<Sid>XXXXXX</Sid>
		</Entry>
		<Entry Id="{77073a70-eacd-4008-b031-9bdce7cb65be}">
			<Type>AuditAllowed</Type>
			<AccessMask>1</AccessMask>
			<Options>2</Options>
			<Sid>XXXXXX</Sid>
		</Entry>
		<Entry Id="{d3255814-cacb-4a78-8cf7-5195db00b049}">
			<Type>Deny</Type>
			<AccessMask>7</AccessMask>
			<Options>0</Options>
		</Entry>
		<Entry Id="{5bdd9755-6e5a-4692-ba71-d597b709d2dd}">
			<Type>AuditDenied</Type>
			<AccessMask>7</AccessMask>
			<Options>3</Options>
		</Entry>
	</PolicyRule>
	<PolicyRule Id="{505e2563-1de8-40aa-b8f9-472a37b2f6ee}" >
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B505e2563-1de8-40aa-b8f9-472a37b2f6ee%7D/RuleData -->
		<Name>Gestion des appareils immobiliers</Name>
		<IncludedIdList>
			<GroupId>{d2887bd4-a916-4011-a385-83c6b15df529}</GroupId>
		</IncludedIdList>
		<ExcludedIdList>
		</ExcludedIdList>
		<Entry Id="{9ca73bfa-4ee9-4b2d-acfd-5a2106a83d05}">
			<Type>Allow</Type>
			<AccessMask>1</AccessMask>
			<Options>0</Options>
			<Sid>XXXXXX</Sid>
		</Entry>
		<Entry Id="{927520b9-d12e-4d68-b7e0-d3c0e639a341}">
			<Type>AuditAllowed</Type>
			<AccessMask>1</AccessMask>
			<Options>2</Options>
			<Sid>XXXXXX</Sid>
		</Entry>
		<Entry Id="{125f91ef-0253-4846-8532-cc83fe9c3187}">
			<Type>Allow</Type>
			<AccessMask>1</AccessMask>
			<Options>0</Options>
			<Sid>XXXXXX</Sid>
		</Entry>
		<Entry Id="{6597a4ba-f8e7-4cf2-a184-4e17cc7c3a62}">
			<Type>AuditAllowed</Type>
			<AccessMask>1</AccessMask>
			<Options>2</Options>
			<Sid>XXXXXX</Sid>
		</Entry>
		<Entry Id="{79fca045-f064-4d07-8b25-213687f3ee75}">
			<Type>Allow</Type>
			<AccessMask>1</AccessMask>
			<Options>0</Options>
			<Sid>XXXXXX</Sid>
		</Entry>
		<Entry Id="{8db057be-a510-4efe-b8b4-d64e9c5848c3}">
			<Type>AuditAllowed</Type>
			<AccessMask>1</AccessMask>
			<Options>2</Options>
			<Sid>XXXXXX</Sid>
		</Entry>
		<Entry Id="{92d71792-5349-4c64-8a72-b9f35fbd4cab}">
			<Type>Deny</Type>
			<AccessMask>7</AccessMask>
			<Options>0</Options>
		</Entry>
		<Entry Id="{d110deed-4386-4e50-816c-4584e2902de2}">
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
<summary>Add a row for Gestion des périphériques externes</summary>  
   
   1. Click "Add"
   2. For Name, enter *Gestion des périphériques externes*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B466faba8-dddf-4ae5-9871-dabbb600d4f3%7D/RuleData*
   5. For Data type, select *String (XML File)*
   
        
   6. Save this XML to a file. 
   ```xml
   <PolicyRule Id="{466faba8-dddf-4ae5-9871-dabbb600d4f3}" >
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B466faba8-dddf-4ae5-9871-dabbb600d4f3%7D/RuleData -->
	<Name>Gestion des périphériques externes</Name>
	<IncludedIdList>
		<GroupId>{fb4ad01e-f41a-46c6-9ac1-268efa0ea083}</GroupId>
	</IncludedIdList>
	<ExcludedIdList>
		<GroupId>{7f191817-c305-451d-812a-1c4b03ebcec8}</GroupId>
		<GroupId>{1653593b-5b92-47e6-975a-c43ffa9cd28d}</GroupId>
		<GroupId>{d2887bd4-a916-4011-a385-83c6b15df529}</GroupId>
	</ExcludedIdList>
	<Entry Id="{f577a950-ce74-4153-90fd-c79d3bf0eb3d}">
		<Type>Allow</Type>
		<AccessMask>1</AccessMask>
		<Options>0</Options>
		<Sid>XXXXXX</Sid>
	</Entry>
	<Entry Id="{428e439f-d8ee-4314-9a8a-92685c4d961c}">
		<Type>AuditAllowed</Type>
		<AccessMask>1</AccessMask>
		<Options>2</Options>
		<Sid>XXXXXX</Sid>
	</Entry>
	<Entry Id="{a3886e5f-093f-4e9c-812f-d7334d5ee052}">
		<Type>Allow</Type>
		<AccessMask>1</AccessMask>
		<Options>0</Options>
		<Sid>XXXXXX</Sid>
	</Entry>
	<Entry Id="{4565ab13-0d58-4a7c-8399-5b65f470ecae}">
		<Type>AuditAllowed</Type>
		<AccessMask>1</AccessMask>
		<Options>2</Options>
		<Sid>XXXXXX</Sid>
	</Entry>
	<Entry Id="{f7cd79af-e330-4fea-9345-467d9bb51131}">
		<Type>Allow</Type>
		<AccessMask>1</AccessMask>
		<Options>0</Options>
		<Sid>XXXXXX</Sid>
	</Entry>
	<Entry Id="{e8e9077f-5111-4a7d-ade6-723c08fd7797}">
		<Type>AuditAllowed</Type>
		<AccessMask>1</AccessMask>
		<Options>2</Options>
		<Sid>XXXXXX</Sid>
	</Entry>
	<Entry Id="{a3421c37-ac07-4085-9bbd-ec9b4ebbd60e}">
		<Type>Allow</Type>
		<AccessMask>1</AccessMask>
		<Options>0</Options>
		<Sid>XXXXXX</Sid>
	</Entry>
	<Entry Id="{e2f263f2-c597-406d-a5f7-9d91909a32c6}">
		<Type>AuditAllowed</Type>
		<AccessMask>1</AccessMask>
		<Options>2</Options>
		<Sid>XXXXXX</Sid>
	</Entry>
	<Entry Id="{170070b1-b68d-4175-9cd4-753a76197496}">
		<Type>Deny</Type>
		<AccessMask>7</AccessMask>
		<Options>0</Options>
	</Entry>
	<Entry Id="{ca86bec9-ba43-4849-a632-e59e5e5c207b}">
		<Type>AuditDenied</Type>
		<AccessMask>7</AccessMask>
		<Options>3</Options>
	</Entry>
</PolicyRule>
   ```
   
   7. For Custom XML, select the file.
         
   
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for Gestion des dictaphones</summary>  
   
   1. Click "Add"
   2. For Name, enter *Gestion des dictaphones*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B540efb7f-1836-4956-8888-5d41d981d6ba%7D/RuleData*
   5. For Data type, select *String (XML File)*
   
        
   6. Save this XML to a file. 
   ```xml
   <PolicyRule Id="{540efb7f-1836-4956-8888-5d41d981d6ba}" >
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B540efb7f-1836-4956-8888-5d41d981d6ba%7D/RuleData -->
	<Name>Gestion des dictaphones</Name>
	<IncludedIdList>
		<GroupId>{7f191817-c305-451d-812a-1c4b03ebcec8}</GroupId>
	</IncludedIdList>
	<ExcludedIdList>
	</ExcludedIdList>
	<Entry Id="{bdd26ee1-4d28-487a-9931-6322ae9e3f91}">
		<Type>Allow</Type>
		<AccessMask>1</AccessMask>
		<Options>0</Options>
		<Sid>XXXXXX</Sid>
	</Entry>
	<Entry Id="{92237bd0-84bf-4d1a-81c0-2507d6274532}">
		<Type>AuditAllowed</Type>
		<AccessMask>1</AccessMask>
		<Options>2</Options>
		<Sid>XXXXXX</Sid>
	</Entry>
	<Entry Id="{cd7fb4ed-fe8d-4122-949e-3c8306152978}">
		<Type>Allow</Type>
		<AccessMask>1</AccessMask>
		<Options>0</Options>
		<Sid>XXXXXX</Sid>
	</Entry>
	<Entry Id="{84a53752-fbdc-4e39-b15c-8787130bc6d6}">
		<Type>AuditAllowed</Type>
		<AccessMask>1</AccessMask>
		<Options>2</Options>
		<Sid>XXXXXX</Sid>
	</Entry>
	<Entry Id="{873026a4-0c93-4061-b784-b1f7bb43b891}">
		<Type>Allow</Type>
		<AccessMask>1</AccessMask>
		<Options>0</Options>
		<Sid>XXXXXX</Sid>
	</Entry>
	<Entry Id="{77073a70-eacd-4008-b031-9bdce7cb65be}">
		<Type>AuditAllowed</Type>
		<AccessMask>1</AccessMask>
		<Options>2</Options>
		<Sid>XXXXXX</Sid>
	</Entry>
	<Entry Id="{d3255814-cacb-4a78-8cf7-5195db00b049}">
		<Type>Deny</Type>
		<AccessMask>7</AccessMask>
		<Options>0</Options>
	</Entry>
	<Entry Id="{5bdd9755-6e5a-4692-ba71-d597b709d2dd}">
		<Type>AuditDenied</Type>
		<AccessMask>7</AccessMask>
		<Options>3</Options>
	</Entry>
</PolicyRule>
   ```
   
   7. For Custom XML, select the file.
         
   
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for Gestion des appareils immobiliers</summary>  
   
   1. Click "Add"
   2. For Name, enter *Gestion des appareils immobiliers*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B505e2563-1de8-40aa-b8f9-472a37b2f6ee%7D/RuleData*
   5. For Data type, select *String (XML File)*
   
        
   6. Save this XML to a file. 
   ```xml
   <PolicyRule Id="{505e2563-1de8-40aa-b8f9-472a37b2f6ee}" >
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B505e2563-1de8-40aa-b8f9-472a37b2f6ee%7D/RuleData -->
	<Name>Gestion des appareils immobiliers</Name>
	<IncludedIdList>
		<GroupId>{d2887bd4-a916-4011-a385-83c6b15df529}</GroupId>
	</IncludedIdList>
	<ExcludedIdList>
	</ExcludedIdList>
	<Entry Id="{9ca73bfa-4ee9-4b2d-acfd-5a2106a83d05}">
		<Type>Allow</Type>
		<AccessMask>1</AccessMask>
		<Options>0</Options>
		<Sid>XXXXXX</Sid>
	</Entry>
	<Entry Id="{927520b9-d12e-4d68-b7e0-d3c0e639a341}">
		<Type>AuditAllowed</Type>
		<AccessMask>1</AccessMask>
		<Options>2</Options>
		<Sid>XXXXXX</Sid>
	</Entry>
	<Entry Id="{125f91ef-0253-4846-8532-cc83fe9c3187}">
		<Type>Allow</Type>
		<AccessMask>1</AccessMask>
		<Options>0</Options>
		<Sid>XXXXXX</Sid>
	</Entry>
	<Entry Id="{6597a4ba-f8e7-4cf2-a184-4e17cc7c3a62}">
		<Type>AuditAllowed</Type>
		<AccessMask>1</AccessMask>
		<Options>2</Options>
		<Sid>XXXXXX</Sid>
	</Entry>
	<Entry Id="{79fca045-f064-4d07-8b25-213687f3ee75}">
		<Type>Allow</Type>
		<AccessMask>1</AccessMask>
		<Options>0</Options>
		<Sid>XXXXXX</Sid>
	</Entry>
	<Entry Id="{8db057be-a510-4efe-b8b4-d64e9c5848c3}">
		<Type>AuditAllowed</Type>
		<AccessMask>1</AccessMask>
		<Options>2</Options>
		<Sid>XXXXXX</Sid>
	</Entry>
	<Entry Id="{92d71792-5349-4c64-8a72-b9f35fbd4cab}">
		<Type>Deny</Type>
		<AccessMask>7</AccessMask>
		<Options>0</Options>
	</Entry>
	<Entry Id="{d110deed-4386-4e50-816c-4584e2902de2}">
		<Type>AuditDenied</Type>
		<AccessMask>7</AccessMask>
		<Options>3</Options>
	</Entry>
</PolicyRule>
   ```
   
   7. For Custom XML, select the file.
         
   
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for Mass_storage_groups_GPO_2_1</summary>  
   
   1. Click "Add"
   2. For Name, enter *Mass_storage_groups_GPO_2_1*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Bfb4ad01e-f41a-46c6-9ac1-268efa0ea083%7D/GroupData*
   5. For Data type, select *String (XML File)*
   
        
   6. Save this XML to a file. 
   ```xml
   <Group Id="{fb4ad01e-f41a-46c6-9ac1-268efa0ea083}" Type="Device">
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Bfb4ad01e-f41a-46c6-9ac1-268efa0ea083%7D/GroupData -->
	<Name>Mass_storage_groups_GPO_2_1</Name>
	<MatchType>MatchAny</MatchType>
	<DescriptorIdList>
		<PrimaryId>RemovableMediaDevices</PrimaryId>
		<PrimaryId>CdRomDevices</PrimaryId>
		<PrimaryId>WpdDevices</PrimaryId>
		<FriendlyNameId>SDHC*</FriendlyNameId>
		<FriendlyNameId>SDXC*</FriendlyNameId>
		<DeviceId>USBSTOR\CDROM&amp;VEN_KINGSTON&amp;PROD_DTLOCKER+G3</DeviceId>
		<VID_PID>0951_169D</VID_PID>
		<VID_PID>2009_16AF</VID_PID>
		<VID_PID>1908_0226</VID_PID>
	</DescriptorIdList>
</Group>
   ```
   
   7. For Custom XML, select the file.
         
   
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for Mass_storage_groups_GPO_2_2</summary>  
   
   1. Click "Add"
   2. For Name, enter *Mass_storage_groups_GPO_2_2*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B7f191817-c305-451d-812a-1c4b03ebcec8%7D/GroupData*
   5. For Data type, select *String (XML File)*
   
        
   6. Save this XML to a file. 
   ```xml
   <Group Id="{7f191817-c305-451d-812a-1c4b03ebcec8}" Type="Device">
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B7f191817-c305-451d-812a-1c4b03ebcec8%7D/GroupData -->
	<Name>Mass_storage_groups_GPO_2_2</Name>
	<MatchType>MatchAny</MatchType>
	<DescriptorIdList>
		<VID_PID>07B4_0232</VID_PID>
		<VID_PID>07B4_0279</VID_PID>
		<VID_PID>07B4_0244</VID_PID>
		<VID_PID>07B4_0264</VID_PID>
		<VID_PID>07B4_0236</VID_PID>
		<VID_PID>07B4_0245</VID_PID>
		<VID_PID>0911_1F40</VID_PID>
		<VID_PID>0911_251C</VID_PID>
		<VID_PID>1D54_1072</VID_PID>
		<VID_PID>1D54_1070</VID_PID>
		<VID_PID>1D54_1080</VID_PID>
		<VID_PID>054C_0B6F</VID_PID>
	</DescriptorIdList>
</Group>
   ```
   
   7. For Custom XML, select the file.
         
   
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for Mass_storage_groups_GPO_2_3</summary>  
   
   1. Click "Add"
   2. For Name, enter *Mass_storage_groups_GPO_2_3*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B1653593b-5b92-47e6-975a-c43ffa9cd28d%7D/GroupData*
   5. For Data type, select *String (XML File)*
   
        
   6. Save this XML to a file. 
   ```xml
   <Group Id="{1653593b-5b92-47e6-975a-c43ffa9cd28d}" Type="Device">
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B1653593b-5b92-47e6-975a-c43ffa9cd28d%7D/GroupData -->
	<Name>Mass_storage_groups_GPO_2_3</Name>
	<MatchType>MatchAny</MatchType>
	<DescriptorIdList>
		<VID_PID>046D_0837</VID_PID>
		<VID_PID>046D_085B</VID_PID>
		<VID_PID>046D_0825</VID_PID>
		<VID_PID>03F0_5705</VID_PID>
		<VID_PID>03F0_5D05</VID_PID>
		<VID_PID>040A_6030</VID_PID>
		<VID_PID>040A_601D</VID_PID>
		<VID_PID>1083_1646</VID_PID>
		<VID_PID>1083_1647</VID_PID>
		<VID_PID>04CA_7053</VID_PID>
		<VID_PID>04CA_7054</VID_PID>
		<VID_PID>04F2_B51C</VID_PID>
		<VID_PID>05C8_0383</VID_PID>
		<VID_PID>05C8_034B</VID_PID>
		<VID_PID>0461_4DFE</VID_PID>
	</DescriptorIdList>
</Group>
   ```
   
   7. For Custom XML, select the file.
         
   
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for Mass_storage_groups_GPO_2_4</summary>  
   
   1. Click "Add"
   2. For Name, enter *Mass_storage_groups_GPO_2_4*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Bd2887bd4-a916-4011-a385-83c6b15df529%7D/GroupData*
   5. For Data type, select *String (XML File)*
   
        
   6. Save this XML to a file. 
   ```xml
   <Group Id="{d2887bd4-a916-4011-a385-83c6b15df529}" Type="Device">
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Bd2887bd4-a916-4011-a385-83c6b15df529%7D/GroupData -->
	<Name>Mass_storage_groups_GPO_2_4</Name>
	<MatchType>MatchAny</MatchType>
	<DescriptorIdList>
		<VID_PID>09CB_1007</VID_PID>
		<VID_PID>0F7E_900C</VID_PID>
	</DescriptorIdList>
</Group>
   ```
   
   7. For Custom XML, select the file.
         
   
   
   7. Click "Save"
</details>


## Mac Policy

This policy is not supported on Mac because Primary ID [CdRomDevices] is not supported on macOS.

Learn more
- [Mac device control examples](../Removable%20Storage%20Access%20Control%20Samples/macOS/policy/examples/README.md)

