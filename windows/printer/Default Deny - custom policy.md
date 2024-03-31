# Device control policy sample: Default Deny - custom policy

Description: This is a policy.              
Device Type: Windows Printer

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
            <td rowspan="2" valign="top"><b>Default Deny</b></td>
            <td rowspan="2 valign="top">
                <ul><li>Group: Any Printer<a href="#any-printer" title="MatchAny {'PrimaryId': 'PrinterDevices'}"> (details)</a>  
</ul>
            </td>
            <td rowspan="2" valign="top">
                <ul><li>Group: PDF_XPS Printer<a href="#pdf_xps-printer" title="MatchAny {'PrinterConnectionId': 'File'}"> (details)</a>  
<li>Group: Authorized USB Printer<a href="#authorized-usb-printer" title="MatchAny {'VID_PID': '035E_0872'}"> (details)</a>  
</ul>
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


### Any Printer



This is a group of type *Device*. 
The match type for the group is *MatchAny*.


|  Property | Value |
|-----------|-------|
| PrimaryId | PrinterDevices |





<details>
<summary>View XML</summary>

```xml
<Group Id="{090b8e1d-5c7b-4f69-a4f2-fb76fa0535fc}" Type="Device">
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B090b8e1d-5c7b-4f69-a4f2-fb76fa0535fc%7D/GroupData -->
	<Name>Any Printer</Name>
	<MatchType>MatchAny</MatchType>
	<DescriptorIdList>
		<PrimaryId>PrinterDevices</PrimaryId>
	</DescriptorIdList>
</Group>
```
</details>

### PDF_XPS Printer



This is a group of type *Device*. 
The match type for the group is *MatchAny*.


|  Property | Value |
|-----------|-------|
| PrinterConnectionId | File |





<details>
<summary>View XML</summary>

```xml
<Group Id="{e5170dfb-19a9-4466-8109-d36c9c912b4e}" Type="Device">
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Be5170dfb-19a9-4466-8109-d36c9c912b4e%7D/GroupData -->
	<Name>PDF_XPS Printer</Name>
	<MatchType>MatchAny</MatchType>
	<DescriptorIdList>
		<PrinterConnectionId>File</PrinterConnectionId>
	</DescriptorIdList>
</Group>
```
</details>

### Authorized USB Printer



This is a group of type *Device*. 
The match type for the group is *MatchAny*.


|  Property | Value |
|-----------|-------|
| VID_PID | 03F0_ |
| VID_PID | 035E_0872 |





<details>
<summary>View XML</summary>

```xml
<Group Id="{05b56e90-e682-48ff-a6c0-5602c9638182}" Type="Device">
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B05b56e90-e682-48ff-a6c0-5602c9638182%7D/GroupData -->
	<Name>Authorized USB Printer</Name>
	<MatchType>MatchAny</MatchType>
	<DescriptorIdList>
		<VID_PID>03F0_</VID_PID>
		<VID_PID>035E_0872</VID_PID>
	</DescriptorIdList>
</Group>
```
</details>


## Settings






| Setting Name |  Setting Value | Description |Documentation |
|--------------|----------------|-------------|---------------|
DefaultEnforcement | Deny | Control Device Control default enforcement. This is the enforcement applied if there are no policy rules present or at the end of the policy rules evaluation none were matched. |[documentation](https://learn.microsoft.com/en-us/windows/client-management/mdm/defender-csp#configurationdefaultenforcement) |
DeviceControlEnabled | True | Enables/disables device control |[documentation](https://learn.microsoft.com/en-us/windows/client-management/mdm/defender-csp#configurationdevicecontrolenabled) |


## Files
This policy is based on information in the following files:

- [Group Policy/Printer_Groups.xml](Group%20Policy/Printer_Groups.xml)
- [Intune OMA-URI/Default Deny - custom policy.xml](Intune%20OMA-URI/Default%20Deny%20-%20custom%20policy.xml)
- [Intune OMA-URI/Any printer group.xml](Intune%20OMA-URI/Any%20printer%20group.xml)
- [Intune OMA-URI/PDF_XPS Printer.xml](Intune%20OMA-URI/PDF_XPS%20Printer.xml)


# Deployment Instructions

Device control [policy rules](#policy-rules) and [groups](#groups) can be deployed through the following management tools:


## Windows
- [Intune UX](#intune-ux)
- [Intune Custom Settings](#intune-custom-settings)
- [Group Policy (GPO)](#group-policy-gpo)





## Intune UX

<details>
<summary>Create a reusable setting for Any Printer</summary> 

   1. Navigate to Home > Endpoint Security > Attack Surface Reduction
   2. Click on Reusable Settings
   3. Click (+) Add
   4. Enter the Any Printer for the name.  
   5. Optionally, enter a description
   6. Click on "Next"
   7. Set the match type toggle to MatchAny
   
   8. Click "Next"
   9. Click "Add"
</details>
<details>
<summary>Create a reusable setting for PDF_XPS Printer</summary> 

   1. Navigate to Home > Endpoint Security > Attack Surface Reduction
   2. Click on Reusable Settings
   3. Click (+) Add
   4. Enter the PDF_XPS Printer for the name.  
   5. Optionally, enter a description
   6. Click on "Next"
   7. Set the match type toggle to MatchAny
   
   8. Click "Next"
   9. Click "Add"
</details>
<details>
<summary>Create a reusable setting for Authorized USB Printer</summary> 

   1. Navigate to Home > Endpoint Security > Attack Surface Reduction
   2. Click on Reusable Settings
   3. Click (+) Add
   4. Enter the Authorized USB Printer for the name.  
   5. Optionally, enter a description
   6. Click on "Next"
   7. Set the match type toggle to MatchAny
   
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

   1. Click on *Any Printer*

   1. Click on "Select"


   1. Click on "+ Set reusable settings" under Excluded Id

   1. Click on *PDF_XPS Printer*

   1. Click on *Authorized USB Printer*

   1. Click on "Select"

   1. Click on "+ Edit Entry"
   1. Enter *Default Deny* for the name



   1. Select *Deny* from "Type"
   1. Select *None* from "Options"
   1. Select *Print* from "Access mask"




   1. Add another entry.  Click on "+ Add"

   1. Select *Audit Denied* from "Type"
   1. Select *Show notification and Send event* from "Options"
   1. Select *Print* from "Access mask"


   1. Click "OK"
</details>



## Group Policy (GPO)
<details>
<summary>Define device control policy groups</summary>

   1. Go to Computer Configuration > Administrative Templates > Windows Components > Microsoft Defender Antivirus > Device Control > Define device control policy groups.
   2. Save the XML below to a network share.
```xml
<Groups>
	<Group Id="{090b8e1d-5c7b-4f69-a4f2-fb76fa0535fc}" Type="Device">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B090b8e1d-5c7b-4f69-a4f2-fb76fa0535fc%7D/GroupData -->
		<Name>Any Printer</Name>
		<MatchType>MatchAny</MatchType>
		<DescriptorIdList>
			<PrimaryId>PrinterDevices</PrimaryId>
		</DescriptorIdList>
	</Group>
	<Group Id="{e5170dfb-19a9-4466-8109-d36c9c912b4e}" Type="Device">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Be5170dfb-19a9-4466-8109-d36c9c912b4e%7D/GroupData -->
		<Name>PDF_XPS Printer</Name>
		<MatchType>MatchAny</MatchType>
		<DescriptorIdList>
			<PrinterConnectionId>File</PrinterConnectionId>
		</DescriptorIdList>
	</Group>
	<Group Id="{05b56e90-e682-48ff-a6c0-5602c9638182}" Type="Device">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B05b56e90-e682-48ff-a6c0-5602c9638182%7D/GroupData -->
		<Name>Authorized USB Printer</Name>
		<MatchType>MatchAny</MatchType>
		<DescriptorIdList>
			<VID_PID>03F0_</VID_PID>
			<VID_PID>035E_0872</VID_PID>
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
	<PolicyRule Id="{e6ccf2cb-20d6-4478-bf2d-66f247ced6f3}" >
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7Be6ccf2cb-20d6-4478-bf2d-66f247ced6f3%7D/RuleData -->
		<Name>Default Deny</Name>
		<IncludedIdList>
			<GroupId>{090b8e1d-5c7b-4f69-a4f2-fb76fa0535fc}</GroupId>
		</IncludedIdList>
		<ExcludedIdList>
			<GroupId>{e5170dfb-19a9-4466-8109-d36c9c912b4e}</GroupId>
			<GroupId>{05b56e90-e682-48ff-a6c0-5602c9638182}</GroupId>
		</ExcludedIdList>
		<Entry Id="{6b9cf286-ec70-4463-bfaf-29f32bb5f0dc}">
			<Type>Deny</Type>
			<AccessMask>64</AccessMask>
			<Options>0</Options>
		</Entry>
		<Entry Id="{48fe1c20-83ef-4163-aa99-882f49f3ec1d}">
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
<summary>Add a row for Default Deny</summary>  
   
   1. Click "Add"
   2. For Name, enter *Default Deny*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7Be6ccf2cb-20d6-4478-bf2d-66f247ced6f3%7D/RuleData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  *windows/printer/Intune OMA-URI/Default Deny - custom policy.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for Any Printer</summary>  
   
   1. Click "Add"
   2. For Name, enter *Any Printer*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B090b8e1d-5c7b-4f69-a4f2-fb76fa0535fc%7D/GroupData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  *windows/printer/Intune OMA-URI/Any printer group.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for PDF_XPS Printer</summary>  
   
   1. Click "Add"
   2. For Name, enter *PDF_XPS Printer*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Be5170dfb-19a9-4466-8109-d36c9c912b4e%7D/GroupData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  *windows/printer/Intune OMA-URI/PDF_XPS Printer.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for Authorized USB Printer</summary>  
   
   1. Click "Add"
   2. For Name, enter *Authorized USB Printer*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B05b56e90-e682-48ff-a6c0-5602c9638182%7D/GroupData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  *windows/printer/Intune OMA-URI/Authorized USB Printer.xml*
         
   
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
<summary>Add a row for DeviceControlEnabled</summary>  
   
   1. Click "Add"
   2. For Name, enter *DeviceControlEnabled*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControlEnabled*
   5. For Data type, select *Integer*
   
   7. For Value, enter *1*
   
   7. Click "Save"
</details>



