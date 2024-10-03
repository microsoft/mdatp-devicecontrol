# Device control policy sample: Deduplicate access events example

**Description:** Basic policy demonstrating the deduplicate access events setting              
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
            <td rowspan="1" valign="top"><b>Audit Allowed Example</b></td>
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
<Group Id="{e00dae45-b54a-4223-bbb2-62e1613f2062}" Type="Device">
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Be00dae45-b54a-4223-bbb2-62e1613f2062%7D/GroupData -->
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
DefaultEnforcement | Allow | Control Device Control default enforcement. This is the enforcement applied if there are no policy rules present or at the end of the policy rules evaluation none were matched. |[documentation](https://learn.microsoft.com/en-us/windows/client-management/mdm/defender-csp#configurationdefaultenforcement) |
DeduplicateAccessEvents | True | Deduplicates access events to only a single event when a device in first added. |[documentation](https://learn.microsoft.com/en-us/windows/client-management/mdm/defender-csp#configurationdevicecontrolenabled) |


## Files
This policy is based on information in the following files:

- [groups/All Devices.xml](groups/All%20Devices.xml)
- [rules/Audit Allowed Example.xml](rules/Audit%20Allowed%20Example.xml)


# Deployment Instructions

Device control [policy rules](#policy-rules) and [groups](#groups) can be deployed through the following management tools:


## Windows
- [Intune UX](#intune-ux)
- [Intune Custom Settings](#intune-custom-settings)
- [Group Policy (GPO)](#group-policy-gpo)





## Intune UX

Intune UX is not supported for this policy because:
- File Write (16) is an unsupported access mask
- File Read (8) is an unsupported access mask
- File Execute (32) is an unsupported access mask

Use [Intune custom settings](#intune-custom-settings) to deploy the policy instead.


## Group Policy (GPO)
<details>
<summary>Define device control policy groups</summary>

   1. Go to Computer Configuration > Administrative Templates > Windows Components > Microsoft Defender Antivirus > Device Control > Define device control policy groups.
   2. Save the XML below to a network share.
```xml
<Groups>
	<Group Id="{e00dae45-b54a-4223-bbb2-62e1613f2062}" Type="Device">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Be00dae45-b54a-4223-bbb2-62e1613f2062%7D/GroupData -->
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
	<PolicyRule Id="{214d63fb-23d8-426c-924e-e1e7ff94c45c}" >
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B214d63fb-23d8-426c-924e-e1e7ff94c45c%7D/RuleData -->
		<Name>Audit Allowed Example</Name>
		<IncludedIdList>
			<GroupId>{e00dae45-b54a-4223-bbb2-62e1613f2062}</GroupId>
		</IncludedIdList>
		<ExcludedIdList>
		</ExcludedIdList>
		<Entry Id="{ef52ad96-f013-4524-bef4-c93e2d0836c3}">
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
<summary>Add a row for Audit Allowed Example</summary>  
   
   1. Click "Add"
   2. For Name, enter *Audit Allowed Example*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B214d63fb-23d8-426c-924e-e1e7ff94c45c%7D/RuleData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  */workspaces/mdatp-devicecontrol/deployable examples/deduplicate_access_events/windows/devicecontrol/rules/Audit Allowed Example.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for All Devices</summary>  
   
   1. Click "Add"
   2. For Name, enter *All Devices*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Be00dae45-b54a-4223-bbb2-62e1613f2062%7D/GroupData*
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
   
   7. For Value, enter *1*
   
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



