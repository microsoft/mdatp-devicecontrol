# Device control policy sample: Allow USB printers by port name example

**Description:** Allows printers in the Authorized Printers group to print.  The Authorized Printers groupmatches based on PrinterPortNameId              
**Device Type:** Windows Printer

A device control policy is a combination of [policy rules](#policy-rules), [groups](#groups) and [settings](#settings).  
This sample is based on the [sample files](#files).  
To configure the sample, follow the [deployment instructions](#deployment-instructions).  

## Policy Rules


<table>
    <tr>
        <th rowspan="2" valign="top">Name</th>
        <th colspan="2" valign="top"><center>Devices</center></th>
        <th rowspan="2" valign="top">Rule Type</th>
        <th colspan="1" valign="top"><center>Access</center></th>
        <th rowspan="2" valign="top">Notification</th>
        <th rowspan="2" valign="top">Conditions</th>
    </tr>
    <tr>
        <th>Included</th>
        <th>Excluded</th>
        <th>Print</th>
        </tr><tr>
            <td rowspan="1" valign="top"><b>Allow Print for Authorized Printers</b></td>
            <td rowspan="1 valign="top">
                <ul><li>Group: Authorized Printers<a href="#authorized-printers" title="MatchAny {'PrinterPortNameId': 'WSD*'}"> (details)</a>  
</ul>
            </td>
            <td rowspan="1" valign="top">
                <ul></ul>
            </td>
            <td>Allow</td>
            <td>:white_check_mark:</td>
            <td>None (0)</td> 
            <td>
                <center>-</center></td>
        </tr></table>


## Groups


### Authorized Printers



This is a group of type *Device*. 
The match type for the group is *MatchAny*.


|  Property | Value |
|-----------|-------|
| PrinterPortNameId | WSD* |





<details>
<summary>View XML</summary>

```xml
<Group Id="{3f782150-39c2-47c0-8061-486759099de8}" Type="Device">
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B3f782150-39c2-47c0-8061-486759099de8%7D/GroupData -->
	<Name>Authorized Printers</Name>
	<MatchType>MatchAny</MatchType>
	<DescriptorIdList>
		<PrinterPortNameId>WSD*</PrinterPortNameId>
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

- [rules/Allow Print for Authorized Printers.xml](rules/Allow%20Print%20for%20Authorized%20Printers.xml)
- [groups/Authorized Printers.xml](groups/Authorized%20Printers.xml)


# Deployment Instructions

Device control [policy rules](#policy-rules) and [groups](#groups) can be deployed through the following management tools:


## Windows
- [Intune UX](#intune-ux)
- [Intune Custom Settings](#intune-custom-settings)
- [Group Policy (GPO)](#group-policy-gpo)





## Intune UX

Intune UX is not supported for this policy because:
- PrinterPortNameId not supported

Use [Intune custom settings](#intune-custom-settings) to deploy the policy instead.


## Group Policy (GPO)
<details>
<summary>Define device control policy groups</summary>

   1. Go to Computer Configuration > Administrative Templates > Windows Components > Microsoft Defender Antivirus > Device Control > Define device control policy groups.
   2. Save the XML below to a network share.
```xml
<Groups>
	<Group Id="{3f782150-39c2-47c0-8061-486759099de8}" Type="Device">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B3f782150-39c2-47c0-8061-486759099de8%7D/GroupData -->
		<Name>Authorized Printers</Name>
		<MatchType>MatchAny</MatchType>
		<DescriptorIdList>
			<PrinterPortNameId>WSD*</PrinterPortNameId>
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
	<PolicyRule Id="{f91786e9-a531-4663-82d0-d97dbc4ee602}" >
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7Bf91786e9-a531-4663-82d0-d97dbc4ee602%7D/RuleData -->
		<Name>Allow Print for Authorized Printers</Name>
		<IncludedIdList>
			<GroupId>{3f782150-39c2-47c0-8061-486759099de8}</GroupId>
		</IncludedIdList>
		<ExcludedIdList>
		</ExcludedIdList>
		<Entry Id="{aceec5d3-3c95-4bfc-b481-5091cc104460}">
			<Type>Allow</Type>
			<AccessMask>64</AccessMask>
			<Options>0</Options>
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
<summary>Add a row for Allow Print for Authorized Printers</summary>  
   
   1. Click "Add"
   2. For Name, enter *Allow Print for Authorized Printers*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7Bf91786e9-a531-4663-82d0-d97dbc4ee602%7D/RuleData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  */workspaces/mdatp-devicecontrol/deployable examples/allow_usb_print_by_port_name/windows/devicecontrol/rules/Allow Print for Authorized Printers.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for Authorized Printers</summary>  
   
   1. Click "Add"
   2. For Name, enter *Authorized Printers*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B3f782150-39c2-47c0-8061-486759099de8%7D/GroupData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  */workspaces/mdatp-devicecontrol/deployable examples/allow_usb_print_by_port_name/windows/devicecontrol/groups/Authorized Printers.xml*
         
   
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



