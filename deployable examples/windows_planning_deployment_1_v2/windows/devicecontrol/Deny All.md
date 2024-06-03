# Device control policy sample: Deny All

Description: A policy              
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
            <td rowspan="2" valign="top"><b>Default Deny</b></td>
            <td rowspan="2 valign="top">
                <ul><li>Group: All Other Devices<a href="#all-other-devices" title="MatchAny {'PrimaryId': 'WpdDevices'}"> (details)</a>  
</ul>
            </td>
            <td rowspan="2" valign="top">
                <ul></ul>
            </td>
            <td>Deny</td>
            <td>:x:</td>
            <td>:x:</td>
            <td>:x:</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>None (0)</td> 
            <td>
                <center>-</center></td>
        </tr><tr>
            <td>Audit Denied</td>
            <td>:page_facing_up:</td>
            <td>:page_facing_up:</td>
            <td>:page_facing_up:</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>Show notification (1)</td>
            <td> 
                <center>-</center></td>
        </tr></table>


## Groups


### All Other Devices



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
<Group Id="{f1a50d64-1f14-470d-96a8-ed24b7ccef7b}" Type="Device">
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Bf1a50d64-1f14-470d-96a8-ed24b7ccef7b%7D/GroupData -->
	<Name>All Other Devices</Name>
	<MatchType>MatchAny</MatchType>
	<DescriptorIdList>
		<PrimaryId>RemovableMediaDevices</PrimaryId>
		<PrimaryId>CdRomDevices</PrimaryId>
		<PrimaryId>WpdDevices</PrimaryId>
	</DescriptorIdList>
</Group>
```
</details>


## Settings






| Setting Name |  Setting Value | Description |Documentation |
|--------------|----------------|-------------|---------------|


## Files
This policy is based on information in the following files:

- [groups/All Other Devices.xml](groups/All%20Other%20Devices.xml)
- [rules/Default Deny.xml](rules/Default%20Deny.xml)


# Deployment Instructions

Device control [policy rules](#policy-rules) and [groups](#groups) can be deployed through the following management tools:


## Windows
- [Intune UX](#intune-ux)
- [Intune Custom Settings](#intune-custom-settings)
- [Group Policy (GPO)](#group-policy-gpo)





## Intune UX

<details>
<summary>Create a reusable setting for All Other Devices</summary> 

   1. Navigate to Home > Endpoint Security > Attack Surface Reduction
   2. Click on Reusable Settings
   3. Click (+) Add
   4. Enter the *All Other Devices* for the name.  
   5. Optionally, enter a description
   6. Click on "Next"
   
   1. Create an entry for  *PrimaryId* = *RemovableMediaDevices* 
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Configure setting"    
        4. Enter *PrimaryId( RemovableMediaDevices )* for Name
        5. Enter *RemovableMediaDevices* for PrimaryId
        6. Click "Save"


   
   1. Create an entry for  *PrimaryId* = *CdRomDevices* 
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Configure setting"    
        4. Enter *PrimaryId( CdRomDevices )* for Name
        5. Enter *CdRomDevices* for PrimaryId
        6. Click "Save"


   
   1. Create an entry for  *PrimaryId* = *WpdDevices* 
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Configure setting"    
        4. Enter *PrimaryId( WpdDevices )* for Name
        5. Enter *WpdDevices* for PrimaryId
        6. Click "Save"


   
   7. Set the match type drop down to MatchAny
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
<summary>Add a rule for Default Deny to the policy</summary>


   1. Click on "+ Set reusable settings" under Included Id

   1. Click on *All Other Devices*

   1. Click on "Select"


   1. Click on "+ Edit Entry"
   1. Enter *Default Deny* for the name



   1. Select *Deny* from "Type"
   1. Select *None* from "Options"
   1. Select *Read, Write and Execute* from "Access mask"




   1. Add another entry.  Click on "+ Add"

   1. Select *Audit Denied* from "Type"
   1. Select *Show notification* from "Options"
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
	<Group Id="{f1a50d64-1f14-470d-96a8-ed24b7ccef7b}" Type="Device">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Bf1a50d64-1f14-470d-96a8-ed24b7ccef7b%7D/GroupData -->
		<Name>All Other Devices</Name>
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
	<PolicyRule Id="{6058f08e-8682-44a4-b914-79406f63c993}" >
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B6058f08e-8682-44a4-b914-79406f63c993%7D/RuleData -->
		<Name>Default Deny</Name>
		<IncludedIdList>
			<GroupId>{f1a50d64-1f14-470d-96a8-ed24b7ccef7b}</GroupId>
		</IncludedIdList>
		<ExcludedIdList>
		</ExcludedIdList>
		<Entry Id="{b6521de0-09a6-4d16-a2d0-2e785fb0616f}">
			<Type>Deny</Type>
			<AccessMask>7</AccessMask>
			<Options>0</Options>
		</Entry>
		<Entry Id="{f97a6941-9a61-4a64-aae1-4ea100348007}">
			<Type>AuditDenied</Type>
			<AccessMask>7</AccessMask>
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
<summary>Add a row for Default Deny</summary>  
   
   1. Click "Add"
   2. For Name, enter *Default Deny*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B6058f08e-8682-44a4-b914-79406f63c993%7D/RuleData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  */workspaces/mdatp-devicecontrol/deployable examples/windows_planning_deployment_1_v2/windows/devicecontrol/rules/Default Deny.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for All Other Devices</summary>  
   
   1. Click "Add"
   2. For Name, enter *All Other Devices*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Bf1a50d64-1f14-470d-96a8-ed24b7ccef7b%7D/GroupData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  */workspaces/mdatp-devicecontrol/deployable examples/windows_planning_deployment_1_v2/windows/devicecontrol/groups/All Other Devices.xml*
         
   
   7. Click "Save"
</details>



