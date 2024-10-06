# Device control policy sample: Deny USB printers by port name

**Description:** An example of using PrinterPortNameId to define groups of printers by port name              
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
            <td rowspan="2" valign="top"><b>Deny USB Printing</b></td>
            <td rowspan="2 valign="top">
                <ul><li>Group: USB Printers<a href="#usb-printers" title="MatchAny {'PrinterPortNameId': 'USB*'}"> (details)</a>  
</ul>
            </td>
            <td rowspan="2" valign="top">
                <ul></ul>
            </td>
            <td>Deny</td>
            <td>:x:</td>
            <td>None (0)</td> 
            <td>
                <center>-</center></td>
        </tr><tr>
            <td>Audit Denied</td>
            <td>:page_facing_up:</td>
            <td>Show notification and Send event (3)</td>
            <td> 
                <center>-</center></td>
        </tr></table>


## Groups


### USB Printers



This is a group of type *Device*. 
The match type for the group is *MatchAny*.


|  Property | Value |
|-----------|-------|
| PrinterPortNameId | USB* |





<details>
<summary>View XML</summary>

```xml
<Group Id="{1a598b22-c309-4b33-8016-bc1372186caa}" Type="Device">
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B1a598b22-c309-4b33-8016-bc1372186caa%7D/GroupData -->
	<Name>USB Printers</Name>
	<MatchType>MatchAny</MatchType>
	<DescriptorIdList>
		<PrinterPortNameId>USB*</PrinterPortNameId>
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

- [groups/USB Printers.xml](groups/USB%20Printers.xml)
- [rules/Deny USB Printing.xml](rules/Deny%20USB%20Printing.xml)


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
	<Group Id="{1a598b22-c309-4b33-8016-bc1372186caa}" Type="Device">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B1a598b22-c309-4b33-8016-bc1372186caa%7D/GroupData -->
		<Name>USB Printers</Name>
		<MatchType>MatchAny</MatchType>
		<DescriptorIdList>
			<PrinterPortNameId>USB*</PrinterPortNameId>
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
	<PolicyRule Id="{f428ee00-232f-42e7-badd-fc6173d292da}" >
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7Bf428ee00-232f-42e7-badd-fc6173d292da%7D/RuleData -->
		<Name>Deny USB Printing</Name>
		<IncludedIdList>
			<GroupId>{1a598b22-c309-4b33-8016-bc1372186caa}</GroupId>
		</IncludedIdList>
		<ExcludedIdList>
		</ExcludedIdList>
		<Entry Id="{42a1c5d8-b033-4d0a-ba06-77a1d00745fe}">
			<Type>Deny</Type>
			<AccessMask>64</AccessMask>
			<Options>0</Options>
		</Entry>
		<Entry Id="{070ad1af-18ab-44a6-9bf4-4bfb716095e9}">
			<Type>AuditDenied</Type>
			<AccessMask>64</AccessMask>
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
<summary>Add a row for Deny USB Printing</summary>  
   
   1. Click "Add"
   2. For Name, enter *Deny USB Printing*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7Bf428ee00-232f-42e7-badd-fc6173d292da%7D/RuleData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  */workspaces/mdatp-devicecontrol/deployable examples/deny_usb_print_by_port_name/windows/devicecontrol/rules/Deny USB Printing.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for USB Printers</summary>  
   
   1. Click "Add"
   2. For Name, enter *USB Printers*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B1a598b22-c309-4b33-8016-bc1372186caa%7D/GroupData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  */workspaces/mdatp-devicecontrol/deployable examples/deny_usb_print_by_port_name/windows/devicecontrol/groups/USB Printers.xml*
         
   
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



