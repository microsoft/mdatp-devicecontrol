# Device control policy sample: Scenario 5

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
            <td rowspan="4"><b>Block Wirte and Execute but allow specific user and approved USB</b></td>
            <td rowspan="4 valign="top">
                <ul><li>Any Removable Storage and CD-DVD and WPD Group_1<a href="#any-removable-storage-and-cd-dvd-and-wpd-group_1" title="MatchAny [{'PrimaryId': 'RemovableMediaDevices'}, {'PrimaryId': 'CdRomDevices'}, {'PrimaryId': 'WpdDevices'}]"> (details)</a></ul>
            </td>
            <td rowspan="4" valign="top">
                <ul><li>Approved USBs Group_0<a href="#approved-usbs-group_0" title="MatchAny [{'InstancePathId': 'USBSTOR\\DISK&VEN__USB&PROD__SANDISK_3.2GEN1&REV_1.00\\03003324080520232521&*'}]"> (details)</a></ul>
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
            <td>Audit Allowed</td>
            <td>-</td>
            <td>:page_facing_up:</td>
            <td>:page_facing_up:</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>Send event (2)</td>
            <td>xxxxxxxx</td>
            <td>
                <ul>
                </ul>
            </td>
        </tr><tr>
            <td>Deny</td>
            <td>-</td>
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
        </tr></table>

## Groups


### Approved USBs Group_0

This is a group of type *Device*. 
The match type for the group is *MatchAny*.

|  Property | Value |
|-----------|-------|
| InstancePathId | USBSTOR\DISK&VEN__USB&PROD__SANDISK_3.2GEN1&REV_1.00\03003324080520232521&* |

<details>
<summary>View XML</summary>

```xml
<Group Id="{65fa649a-a111-4912-9294-fb6337a25038}" Type="Device">
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B65fa649a-a111-4912-9294-fb6337a25038%7D/GroupData -->
	<Name>Approved USBs Group_0</Name>
	<MatchType>MatchAny</MatchType>
	<DescriptorIdList>
		<InstancePathId>USBSTOR\DISK&amp;VEN__USB&amp;PROD__SANDISK_3.2GEN1&amp;REV_1.00\03003324080520232521&amp;*</InstancePathId>
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

- [Group Policy/Any Removable Storage and CD-DVD and WPD Group.xml](Group%20Policy/Any%20Removable%20Storage%20and%20CD-DVD%20and%20WPD%20Group.xml)
- [Intune OMA-URI/Approved USBs Group.xml](Intune%20OMA-URI/Approved%20USBs%20Group.xml)
- [Intune OMA-URI/Scenario 5 Block Wirte and Execute but allow specific user access and approved USB.xml](Intune%20OMA-URI/Scenario%205%20Block%20Wirte%20and%20Execute%20but%20allow%20specific%20user%20access%20and%20approved%20USB.xml)


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
<summary>Create a reusable setting for Approved USBs Group_0</summary> 

   1. Navigate to Home > Endpoint Security > Attack Surface Reduction
   2. Click on Reusable Settings
   3. Click (+) Add
   4. Enter the Approved USBs Group_0 for the name.  
   5. Optionally, enter a description
   6. Click on "Next"
   7. Set the match type toggle to MatchAny
   
      
   8. Add a Removable Storage object for InstancePathId
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Edit Instance"    
        4. Enter *InstancePathId* for Name
        5. Enter *USBSTOR\DISK&VEN__USB&PROD__SANDISK_3.2GEN1&REV_1.00\03003324080520232521&** for InstancePathId
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


<details>
<summary>Add a rule for Block Wirte and Execute but allow specific user and approved USB to the policy</summary>


   1. Click on "+ Set reusable settings" under Included Id

   1. Click on *Any Removable Storage and CD-DVD and WPD Group_1*

   1. Click on "Select"


   1. Click on "+ Set reusable settings" under Excluded Id

   1. Click on *Approved USBs Group_0*

   1. Click on "Select"

   1. Click on "+ Edit Entry"
   1. Enter *Block Wirte and Execute but allow specific user and approved USB* for the name



   1. Select *Allow* from "Type"
   1. Select *None* from "Options"
   1. Select *Write and Execute* from "Access mask"

   1. Enter *xxxxxxxx* for "Sid"




   1. Add another entry.  Click on "+ Add"

   1. Select *Audit Allowed* from "Type"
   1. Select *Send event* from "Options"
   1. Select *Write and Execute* from "Access mask"

   1. Enter *xxxxxxxx* for "Sid"




   1. Add another entry.  Click on "+ Add"

   1. Select *Deny* from "Type"
   1. Select *None* from "Options"
   1. Select *Write and Execute* from "Access mask"




   1. Add another entry.  Click on "+ Add"

   1. Select *Audit Denied* from "Type"
   1. Select *Show notification and Send event* from "Options"
   1. Select *Write and Execute* from "Access mask"


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
		<Name>Approved USBs Group_0</Name>
		<MatchType>MatchAny</MatchType>
		<DescriptorIdList>
			<InstancePathId>USBSTOR\DISK&amp;VEN__USB&amp;PROD__SANDISK_3.2GEN1&amp;REV_1.00\03003324080520232521&amp;*</InstancePathId>
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
		<Name>Block Wirte and Execute but allow specific user and approved USB</Name>
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
		<Entry Id="{f9f6d219-1332-4c64-b6cb-2e14c65cd243}">
			<Type>AuditAllowed</Type>
			<AccessMask>6</AccessMask>
			<Options>2</Options>
			<Sid>xxxxxxxx</Sid>
		</Entry>
		<Entry Id="{07234f5c-304f-4073-a332-2434cd269816}">
			<Type>Deny</Type>
			<AccessMask>6</AccessMask>
			<Options>0</Options>
		</Entry>
		<Entry Id="{b2827dd5-db81-48d8-8cde-fb2c84a8367f}">
			<Type>AuditDenied</Type>
			<AccessMask>6</AccessMask>
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
<summary>Add a row for Block Wirte and Execute but allow specific user and approved USB</summary>  
   
   1. Click "Add"
   2. For Name, enter *Block Wirte and Execute but allow specific user and approved USB*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B83c390b6-b01e-4d83-8834-c8015a2316f2%7D/RuleData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  *.\Intune OMA-URI\Scenario 5 Block Wirte and Execute but allow specific user access and approved USB.xml*
         
   
   
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

