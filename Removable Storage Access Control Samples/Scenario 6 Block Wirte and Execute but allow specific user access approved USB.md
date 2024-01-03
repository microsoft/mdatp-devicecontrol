# Device control policy sample: Scenario 6

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
            <td rowspan="1"><b>Block Write and Execute but allow specific user access approved USB</b></td>
            <td rowspan="1 valign="top">
                <ul><li>Any Removable Storage and CD-DVD and WPD Group_1<a href="#any-removable-storage-and-cd-dvd-and-wpd-group_1" title="MatchAny [{'PrimaryId': 'RemovableMediaDevices'}, {'PrimaryId': 'CdRomDevices'}, {'PrimaryId': 'WpdDevices'}]"> (details)</a></ul>
            </td>
            <td rowspan="1" valign="top">
                <ul><li>Approved USBs Group_1<a href="#approved-usbs-group_1" title="MatchAny [{'InstancePathId': 'USBSTOR\\DISK&VEN__USB&PROD__SANDISK_3.2GEN1&REV_1.00\\03003324080520232521&0'}]"> (details)</a></ul>
            </td>
            <td>Allow</td>
            <td>-</td>
            <td>:white_check_mark:</td>
            <td>:white_check_mark:</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>None (0)</td> 
            <td>xxxxxxxx</td>
            <td>
                <ul>
                </ul>
            </td>
        </tr><tr>
            <td rowspan="3"><b>Block removable storage and CdRom</b></td>
            <td rowspan="3 valign="top">
                <ul><li>Any Removable Storage and CD-DVD and WPD Group_1<a href="#any-removable-storage-and-cd-dvd-and-wpd-group_1" title="MatchAny [{'PrimaryId': 'RemovableMediaDevices'}, {'PrimaryId': 'CdRomDevices'}, {'PrimaryId': 'WpdDevices'}]"> (details)</a></ul>
            </td>
            <td rowspan="3" valign="top">
                <ul></ul>
            </td>
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
            <td>-</td>
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
            <td>Audit Denied</td>
            <td>:page_facing_up:</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>Show notification (1)</td>
            <td>All Users</td>
            <td>
                <ul>
                </ul>
            </td>
        </tr></table>

## Groups


### Approved USBs Group_1

This is a group of type *Device*. 
The match type for the group is *MatchAny*.

|  Property | Value |
|-----------|-------|
| InstancePathId | USBSTOR\DISK&VEN__USB&PROD__SANDISK_3.2GEN1&REV_1.00\03003324080520232521&0 |

<details>
<summary>View XML</summary>

```xml
<Group Id="{65fa649a-a111-4912-9294-fb6337a25038}" Type="Device">
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B65fa649a-a111-4912-9294-fb6337a25038%7D/GroupData -->
	<Name>Approved USBs Group_1</Name>
	<MatchType>MatchAny</MatchType>
	<DescriptorIdList>
		<InstancePathId>USBSTOR\DISK&amp;VEN__USB&amp;PROD__SANDISK_3.2GEN1&amp;REV_1.00\03003324080520232521&amp;0</InstancePathId>
	</DescriptorIdList>
</Group>
```
</details>

### Any Removable Storage and CD-DVD and WPD Group_1

This is a group of type *Device*. 
The match type for the group is *MatchAny*.

|  Property | Value |
|-----------|-------|
| PrimaryId | RemovableMediaDevices |
| PrimaryId | CdRomDevices |
| PrimaryId | WpdDevices |

<details>
<summary>View XML</summary>

```xml
<Group Id="{9b28fae8-72f7-4267-a1a5-685f747a7146}" Type="Device">
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B9b28fae8-72f7-4267-a1a5-685f747a7146%7D/GroupData -->
	<Name>Any Removable Storage and CD-DVD and WPD Group_1</Name>
	<MatchType>MatchAny</MatchType>
	<DescriptorIdList>
		<PrimaryId>RemovableMediaDevices</PrimaryId>
		<PrimaryId>CdRomDevices</PrimaryId>
		<PrimaryId>WpdDevices</PrimaryId>
	</DescriptorIdList>
</Group>
```
</details>


## Files
This policy is based on information in the following files:

- [Group Policy/Approved USBs Group.xml](Group%20Policy/Approved%20USBs%20Group.xml)
- [Group Policy/Any Removable Storage and CD-DVD and WPD Group.xml](Group%20Policy/Any%20Removable%20Storage%20and%20CD-DVD%20and%20WPD%20Group.xml)
- [Group Policy/Scenario 6 Block Wirte and Execute but allow specific user access approved USB.xml](Group%20Policy/Scenario%206%20Block%20Wirte%20and%20Execute%20but%20allow%20specific%20user%20access%20approved%20USB.xml)


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
<summary>Create a reusable setting for Approved USBs Group_1</summary> 

   1. Navigate to Home > Endpoint Security > Attack Surface Reduction
   2. Click on Reusable Settings
   3. Click (+) Add
   4. Enter the Approved USBs Group_1 for the name.  
   5. Optionally, enter a description
   6. Click on "Next"
   7. Set the match type toggle to MatchAny
   
      
   8. Add a Removable Storage object for InstancePathId
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Edit Instance"    
        4. Enter *InstancePathId* for Name
        5. Enter *USBSTOR\DISK&VEN__USB&PROD__SANDISK_3.2GEN1&REV_1.00\03003324080520232521&0* for InstancePathId
        6. Click "Save"
    
   
   8. Click "Next"
   9. Click "Add"
</details>
<details>
<summary>Create a reusable setting for Any Removable Storage and CD-DVD and WPD Group_1</summary> 

   1. Navigate to Home > Endpoint Security > Attack Surface Reduction
   2. Click on Reusable Settings
   3. Click (+) Add
   4. Enter the Any Removable Storage and CD-DVD and WPD Group_1 for the name.  
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
<summary>Add a rule for Block Write and Execute but allow specific user access approved USB to the policy</summary>


   1. Click on "+ Set reusable settings" under Included Id

   1. Click on *Any Removable Storage and CD-DVD and WPD Group_1*

   1. Click on "Select"


   1. Click on "+ Set reusable settings" under Excluded Id

   1. Click on *Approved USBs Group_1*

   1. Click on "Select"

   1. Click on "+ Edit Entry"
   1. Enter *Block Write and Execute but allow specific user access approved USB* for the name



   1. Select *Allow* from "Type"
   1. Select *None* from "Options"
   1. Select *Write and Execute* from "Access mask"

   1. Enter *xxxxxxxx* for "Sid"


   1. Click "OK"
</details>

<details>
<summary>Add a rule for Block removable storage and CdRom to the policy</summary>

   1. Add another rule.  Click on "+ Add"


   1. Click on "+ Set reusable settings" under Included Id

   1. Click on *Any Removable Storage and CD-DVD and WPD Group_1*

   1. Click on "Select"


   1. Click on "+ Edit Entry"
   1. Enter *Block removable storage and CdRom* for the name



   1. Select *Deny* from "Type"
   1. Select *None* from "Options"
   1. Select *Read, Write and Execute* from "Access mask"




   1. Add another entry.  Click on "+ Add"

   1. Select *Audit Denied* from "Type"
   1. Select *Show notification and Send event* from "Options"
   1. Select *Write and Execute* from "Access mask"




   1. Add another entry.  Click on "+ Add"

   1. Select *Audit Denied* from "Type"
   1. Select *Show notification* from "Options"
   1. Select *Read* from "Access mask"


   1. Click "OK"
</details>



## Group Policy (GPO)
<details>
<summary>Define device control policy groups</summary>

   1. Go to Computer Configuration > Administrative Templates > Windows Components > Microsoft Defender Antivirus > Device Control > Define device control policy groups.
   2. Save the XML below to a network share.
```xml
<Groups>
	<Group Id="{65fa649a-a111-4912-9294-fb6337a25038}" Type="Device">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B65fa649a-a111-4912-9294-fb6337a25038%7D/GroupData -->
		<Name>Approved USBs Group_1</Name>
		<MatchType>MatchAny</MatchType>
		<DescriptorIdList>
			<InstancePathId>USBSTOR\DISK&amp;VEN__USB&amp;PROD__SANDISK_3.2GEN1&amp;REV_1.00\03003324080520232521&amp;0</InstancePathId>
		</DescriptorIdList>
	</Group>
	<Group Id="{9b28fae8-72f7-4267-a1a5-685f747a7146}" Type="Device">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B9b28fae8-72f7-4267-a1a5-685f747a7146%7D/GroupData -->
		<Name>Any Removable Storage and CD-DVD and WPD Group_1</Name>
		<MatchType>MatchAny</MatchType>
		<DescriptorIdList>
			<PrimaryId>RemovableMediaDevices</PrimaryId>
			<PrimaryId>CdRomDevices</PrimaryId>
			<PrimaryId>WpdDevices</PrimaryId>
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
	<PolicyRule Id="{83c390b6-b01e-4d83-8834-c8015a2316f2}" >
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B83c390b6-b01e-4d83-8834-c8015a2316f2%7D/RuleData -->
		<Name>Block Write and Execute but allow specific user access approved USB</Name>
		<IncludedIdList>
			<GroupId>{9b28fae8-72f7-4267-a1a5-685f747a7146}</GroupId>
		</IncludedIdList>
		<ExcludedIdList>
			<GroupId>{65fa649a-a111-4912-9294-fb6337a25038}</GroupId>
		</ExcludedIdList>
		<Entry Id="{5d660ff3-a19f-47ae-8779-ca6a989d9780}">
			<Type>Allow</Type>
			<AccessMask>6</AccessMask>
			<Options>0</Options>
			<Sid>xxxxxxxx</Sid>
		</Entry>
	</PolicyRule>
	<PolicyRule Id="{d2193a7f-ceec-4729-a72a-fe949639db55}" >
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7Bd2193a7f-ceec-4729-a72a-fe949639db55%7D/RuleData -->
		<Name>Block removable storage and CdRom</Name>
		<IncludedIdList>
			<GroupId>{9b28fae8-72f7-4267-a1a5-685f747a7146}</GroupId>
		</IncludedIdList>
		<ExcludedIdList>
		</ExcludedIdList>
		<Entry Id="{c1adfc3e-0347-4096-88c3-6e0777b2a15b}">
			<Type>Deny</Type>
			<AccessMask>7</AccessMask>
			<Options>0</Options>
		</Entry>
		<Entry Id="{fee5f127-951b-4ece-9196-fa1c9ff21678}">
			<Type>AuditDenied</Type>
			<AccessMask>6</AccessMask>
			<Options>3</Options>
		</Entry>
		<Entry Id="{ad04437c-e279-41a3-8a1a-b76b7e35bce5}">
			<Type>AuditDenied</Type>
			<AccessMask>1</AccessMask>
			<Options>1</Options>
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
<summary>Add a row for Block Write and Execute but allow specific user access approved USB</summary>  
   
   1. Click "Add"
   2. For Name, enter *Block Write and Execute but allow specific user access approved USB*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B83c390b6-b01e-4d83-8834-c8015a2316f2%7D/RuleData*
   5. For Data type, select *String (XML File)*
   
        
   6. Save this XML to a file. 
   ```xml
   <PolicyRule Id="{83c390b6-b01e-4d83-8834-c8015a2316f2}" >
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B83c390b6-b01e-4d83-8834-c8015a2316f2%7D/RuleData -->
	<Name>Block Write and Execute but allow specific user access approved USB</Name>
	<IncludedIdList>
		<GroupId>{9b28fae8-72f7-4267-a1a5-685f747a7146}</GroupId>
	</IncludedIdList>
	<ExcludedIdList>
		<GroupId>{65fa649a-a111-4912-9294-fb6337a25038}</GroupId>
	</ExcludedIdList>
	<Entry Id="{5d660ff3-a19f-47ae-8779-ca6a989d9780}">
		<Type>Allow</Type>
		<AccessMask>6</AccessMask>
		<Options>0</Options>
		<Sid>xxxxxxxx</Sid>
	</Entry>
</PolicyRule>
   ```
   
   7. For Custom XML, select the file.
         
   
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for Block removable storage and CdRom</summary>  
   
   1. Click "Add"
   2. For Name, enter *Block removable storage and CdRom*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7Bd2193a7f-ceec-4729-a72a-fe949639db55%7D/RuleData*
   5. For Data type, select *String (XML File)*
   
        
   6. Save this XML to a file. 
   ```xml
   <PolicyRule Id="{d2193a7f-ceec-4729-a72a-fe949639db55}" >
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7Bd2193a7f-ceec-4729-a72a-fe949639db55%7D/RuleData -->
	<Name>Block removable storage and CdRom</Name>
	<IncludedIdList>
		<GroupId>{9b28fae8-72f7-4267-a1a5-685f747a7146}</GroupId>
	</IncludedIdList>
	<ExcludedIdList>
	</ExcludedIdList>
	<Entry Id="{c1adfc3e-0347-4096-88c3-6e0777b2a15b}">
		<Type>Deny</Type>
		<AccessMask>7</AccessMask>
		<Options>0</Options>
	</Entry>
	<Entry Id="{fee5f127-951b-4ece-9196-fa1c9ff21678}">
		<Type>AuditDenied</Type>
		<AccessMask>6</AccessMask>
		<Options>3</Options>
	</Entry>
	<Entry Id="{ad04437c-e279-41a3-8a1a-b76b7e35bce5}">
		<Type>AuditDenied</Type>
		<AccessMask>1</AccessMask>
		<Options>1</Options>
	</Entry>
</PolicyRule>
   ```
   
   7. For Custom XML, select the file.
         
   
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for Any Removable Storage and CD-DVD and WPD Group_0</summary>  
   
   1. Click "Add"
   2. For Name, enter *Any Removable Storage and CD-DVD and WPD Group_0*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B9b28fae8-72f7-4267-a1a5-685f747a7146%7D/GroupData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  *.\Intune OMA-URI\Any Removable Storage and CD-DVD and WPD Group.xml*
         
   
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for Approved USBs Group_0</summary>  
   
   1. Click "Add"
   2. For Name, enter *Approved USBs Group_0*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B65fa649a-a111-4912-9294-fb6337a25038%7D/GroupData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  *.\Intune OMA-URI\Approved USBs Group.xml*
         
   
   
   7. Click "Save"
</details>


## Mac Policy

This policy is not supported on Mac because Unsupported Descriptor ID InstancePathId

Learn more
- [Mac device control examples](../Removable%20Storage%20Access%20Control%20Samples/macOS/policy/examples/README.md)

