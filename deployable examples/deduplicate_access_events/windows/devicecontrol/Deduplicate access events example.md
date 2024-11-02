# Device control policy sample: Deduplicate access events example

**Description:** All devices access is audited              
**Device Type:** Windows Generic Device

A device control policy is a combination of [policy rules](#policy-rules), [groups](#groups) and [settings](#settings).  
This sample is based on the [sample files](#files).  
To configure the sample, follow the [deployment instructions](#deployment-instructions).  

## Policy Rules


<table>
    <tr>
        <th rowspan="2" valign="top">Name</th>
        <th colspan="2" valign="top"><center>Devices</center></th>
        <th rowspan="2" valign="top">Rule Type</th>
        <th colspan="7" valign="top"><center>Access</center></th><th rowspan="2" valign="top">Notification</th>
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
		<th>File Execute</th><th>Print</th>
        </tr><tr>
            <td rowspan="1" valign="top"><b>All Devices Audit and Notify Denies </b></td>
            <td rowspan="1 valign="top">
                <ul><li>Group: All Devices<a href="#all-devices" title="MatchAny {'PrimaryId': 'PrinterDevices'}"> (details)</a>  
</ul>
            </td>
            <td rowspan="1" valign="top">
                <ul></ul>
            </td>
            <td>Audit Denied</td>
            <td>:page_facing_up:</td>
            <td>:page_facing_up:</td>
            <td>:page_facing_up:</td>
            <td>:page_facing_up:</td>
            <td>:page_facing_up:</td>
            <td>:page_facing_up:</td>
            <td>:page_facing_up:</td>
            <td>Show notification and Send event (3)</td> 
            <td>
                <center>-</center></td>
        </tr><tr>
            <td rowspan="1" valign="top"><b>All Devices Audit Allows </b></td>
            <td rowspan="1 valign="top">
                <ul><li>Group: All Devices<a href="#all-devices" title="MatchAny {'PrimaryId': 'PrinterDevices'}"> (details)</a>  
</ul>
            </td>
            <td rowspan="1" valign="top">
                <ul></ul>
            </td>
            <td>Audit Allowed</td>
            <td>:page_facing_up:</td>
            <td>:page_facing_up:</td>
            <td>:page_facing_up:</td>
            <td>:page_facing_up:</td>
            <td>:page_facing_up:</td>
            <td>:page_facing_up:</td>
            <td>:page_facing_up:</td>
            <td>Send event (2)</td> 
            <td>
                <center>-</center></td>
        </tr></table>


## Groups


### All Devices



This is a group of type *Device*. 
The match type for the group is *MatchAny*.


|  Property | Value |
|-----------|-------|
| PrimaryId | RemovableMediaDevices |
| PrimaryId | CdRomDevices |
| PrimaryId | WpdDevices |
| PrimaryId | PrinterDevices |





<details>
<summary>View XML</summary>

```xml
<Group Id="{f16d624f-16fc-4ddc-a960-9f0d8dc82e1c}" Type="Device">
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Bf16d624f-16fc-4ddc-a960-9f0d8dc82e1c%7D/GroupData -->
	<Name>All Devices</Name>
	<MatchType>MatchAny</MatchType>
	<DescriptorIdList>
		<PrimaryId>RemovableMediaDevices</PrimaryId>
		<PrimaryId>CdRomDevices</PrimaryId>
		<PrimaryId>WpdDevices</PrimaryId>
		<PrimaryId>PrinterDevices</PrimaryId>
	</DescriptorIdList>
</Group>
```
</details>


## Settings






| Setting Name |  Setting Value | Description |Documentation |
|--------------|----------------|-------------|---------------|
DefaultEnforcement | Deny | Control Device Control default enforcement. This is the enforcement applied if there are no policy rules present or at the end of the policy rules evaluation none were matched. |[documentation](https://learn.microsoft.com/en-us/windows/client-management/mdm/defender-csp#configurationdefaultenforcement) |
DeduplicateAccessEvents | True | Deduplicates access events to only a single event when a device in first added. |[documentation](https://learn.microsoft.com/en-us/windows/client-management/mdm/defender-csp#configurationdevicecontrolenabled) |


## Files
This policy is based on information in the following files:

- [rules/All Devices Audit Allows .xml](rules/All%20Devices%20Audit%20Allows%20.xml)
- [rules/All Devices Audit and Notify Denies .xml](rules/All%20Devices%20Audit%20and%20Notify%20Denies%20.xml)
- [groups/All Devices.xml](groups/All%20Devices.xml)


# Deployment Instructions

Device control [policy rules](#policy-rules) and [groups](#groups) can be deployed through the following management tools:


## Windows
- [Intune UX](#intune-ux)
- [Intune Custom Settings](#intune-custom-settings)
- [Group Policy (GPO)](#group-policy-gpo)





## Intune UX

<details>
<summary>Create a reusable setting for All Devices</summary> 

   1. Navigate to Home > Endpoint Security > Attack Surface Reduction
   2. Click on Reusable Settings
   3. Click (+) Add
   4. Enter the *All Devices* for the name.  
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


   
   1. Create an entry for  *PrimaryId* = *PrinterDevices* 
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Configure setting"    
        4. Enter *PrimaryId( PrinterDevices )* for Name
        5. Enter *PrinterDevices* for PrimaryId
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

> [!IMPORTANT]
> This policy has more than 1 rule.  
> Policy ordering is not guaranteed by Intune.
> Make sure that policy is not dependent on order to achieve desired result.
> Consider using ```default deny```.   


<details>
<summary>Add a rule for All Devices Audit and Notify Denies  to the policy</summary>


   1. Click on "+ Set reusable settings" under Included Id

   1. Click on *All Devices*

   1. Click on "Select"


   1. Click on "+ Edit Entry"
   1. Enter *All Devices Audit and Notify Denies * for the name



   1. Select *Audit Denied* from "Type"
   1. Select *Show notification and Send event* from "Options"
   1. Select *Read, Write, Execute and Print* from "Access mask"


   1. Click "OK"
</details>

<details>
<summary>Add a rule for All Devices Audit Allows  to the policy</summary>

   1. Add another rule.  Click on "+ Add"


   1. Click on "+ Set reusable settings" under Included Id

   1. Click on *All Devices*

   1. Click on "Select"


   1. Click on "+ Edit Entry"
   1. Enter *All Devices Audit Allows * for the name



   1. Select *Audit Allowed* from "Type"
   1. Select *Send event* from "Options"
   1. Select *Read, Write, Execute and Print* from "Access mask"


   1. Click "OK"
</details>



## Group Policy (GPO)
<details>
<summary>Define device control policy groups</summary>

   1. Go to Computer Configuration > Administrative Templates > Windows Components > Microsoft Defender Antivirus > Device Control > Define device control policy groups.
   2. Save the XML below to a network share.
```xml
<Groups>
	<Group Id="{f16d624f-16fc-4ddc-a960-9f0d8dc82e1c}" Type="Device">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Bf16d624f-16fc-4ddc-a960-9f0d8dc82e1c%7D/GroupData -->
		<Name>All Devices</Name>
		<MatchType>MatchAny</MatchType>
		<DescriptorIdList>
			<PrimaryId>RemovableMediaDevices</PrimaryId>
			<PrimaryId>CdRomDevices</PrimaryId>
			<PrimaryId>WpdDevices</PrimaryId>
			<PrimaryId>PrinterDevices</PrimaryId>
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
	<PolicyRule Id="{4cb130b9-67e9-432a-92d4-de4fcb65dda7}" >
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B4cb130b9-67e9-432a-92d4-de4fcb65dda7%7D/RuleData -->
		<Name>All Devices Audit and Notify Denies </Name>
		<IncludedIdList>
			<GroupId>{f16d624f-16fc-4ddc-a960-9f0d8dc82e1c}</GroupId>
		</IncludedIdList>
		<ExcludedIdList>
		</ExcludedIdList>
		<Entry Id="{87512fe1-3811-4a6f-8dab-7484bb1284c4}">
			<Type>AuditDenied</Type>
			<AccessMask>127</AccessMask>
			<Options>3</Options>
		</Entry>
	</PolicyRule>
	<PolicyRule Id="{69f62ac4-5a31-478c-8cbb-376964777722}" >
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B69f62ac4-5a31-478c-8cbb-376964777722%7D/RuleData -->
		<Name>All Devices Audit Allows </Name>
		<IncludedIdList>
			<GroupId>{f16d624f-16fc-4ddc-a960-9f0d8dc82e1c}</GroupId>
		</IncludedIdList>
		<ExcludedIdList>
		</ExcludedIdList>
		<Entry Id="{14af8d13-13b7-46b0-bd43-4e5abe8fdeea}">
			<Type>AuditAllowed</Type>
			<AccessMask>127</AccessMask>
			<Options>2</Options>
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
<summary>Add a row for All Devices Audit Allows </summary>  
   
   1. Click "Add"
   2. For Name, enter *All Devices Audit Allows *
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B69f62ac4-5a31-478c-8cbb-376964777722%7D/RuleData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  */workspaces/mdatp-devicecontrol/deployable examples/deduplicate_access_events/windows/devicecontrol/rules/All Devices Audit Allows .xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for All Devices Audit and Notify Denies </summary>  
   
   1. Click "Add"
   2. For Name, enter *All Devices Audit and Notify Denies *
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B4cb130b9-67e9-432a-92d4-de4fcb65dda7%7D/RuleData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  */workspaces/mdatp-devicecontrol/deployable examples/deduplicate_access_events/windows/devicecontrol/rules/All Devices Audit and Notify Denies .xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for All Devices</summary>  
   
   1. Click "Add"
   2. For Name, enter *All Devices*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Bf16d624f-16fc-4ddc-a960-9f0d8dc82e1c%7D/GroupData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  */workspaces/mdatp-devicecontrol/deployable examples/deduplicate_access_events/windows/devicecontrol/groups/All Devices.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for DefaultEnforcement</summary>  
   
   1. Click "Add"
   2. For Name, enter *DefaultEnforcement*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DefaultEnforcement*
   5. For Data type, select *Integer*
   
   7. For Value, enter *2*
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for DeduplicateAccessEvents</summary>  
   
   1. Click "Add"
   2. For Name, enter *DeduplicateAccessEvents*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/DeduplicateAccessEvents*
   5. For Data type, select *Integer*
   
   7. For Value, enter *1*
   
   7. Click "Save"
</details>



