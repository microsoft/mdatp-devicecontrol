# Device control policy sample: Allow PDF_XPS Printer - File Evidence

Description: A sample policy              
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
            <td rowspan="2" valign="top"><b>Allow PDF and XPS Printing</b></td>
            <td rowspan="2 valign="top">
                <ul><li>Group: PDF_XPS Printer<a href="#pdf_xps-printer" title="MatchAny {'PrinterConnectionId': 'File'}"> (details)</a>  
</ul>
            </td>
            <td rowspan="2" valign="top">
                <ul></ul>
            </td>
            <td>Allow</td>
            <td>:white_check_mark:</td>
            <td>Create file evidence with file (8)</td> 
            <td>
                <center>-</center></td>
        </tr><tr>
            <td>Audit Allowed</td>
            <td>:page_facing_up:</td>
            <td>Send event (2)</td>
            <td> 
                <center>-</center></td>
        </tr></table>


## Groups


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


## Settings
| Setting Name |  Setting Value | Documentation |
|--------------|----------------|---------------|
DefaultEnforcement | Deny | [documentation](https://learn.microsoft.com/en-us/windows/client-management/mdm/defender-csp#configurationdefaultenforcement) |
DeviceControlEnabled | True | [documentation](https://learn.microsoft.com/en-us/windows/client-management/mdm/defender-csp#configurationdevicecontrolenabled) |


## Files
This policy is based on information in the following files:

- [windows/printer/Intune OMA-URI/Allow PDF_XPS Printer - File Evidence.xml](/windows/printer/Intune%20OMA-URI/Allow%20PDF_XPS%20Printer%20-%20File%20Evidence.xml)
- [windows/printer/Group Policy/Printer_Groups.xml](/windows/printer/Group%20Policy/Printer_Groups.xml)


# Deployment Instructions

Device control [policy rules](#policy-rules) and [groups](#groups) can be deployed through the following management tools:


## Windows
- [Intune UX](#intune-ux)
- [Intune Custom Settings](#intune-custom-settings)
- [Group Policy (GPO)](#group-policy-gpo)





## Intune UX

Intune UX is not supported for this policy because:
- Create file evidence with file is an unsupported notification.

Use [Intune custom settings](#intune-custom-settings) to deploy the policy instead.


## Group Policy (GPO)
<details>
<summary>Define device control policy groups</summary>

   1. Go to Computer Configuration > Administrative Templates > Windows Components > Microsoft Defender Antivirus > Device Control > Define device control policy groups.
   2. Save the XML below to a network share.
```xml
<Groups>
	<Group Id="{e5170dfb-19a9-4466-8109-d36c9c912b4e}" Type="Device">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Be5170dfb-19a9-4466-8109-d36c9c912b4e%7D/GroupData -->
		<Name>PDF_XPS Printer</Name>
		<MatchType>MatchAny</MatchType>
		<DescriptorIdList>
			<PrinterConnectionId>File</PrinterConnectionId>
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
	<PolicyRule Id="{07fb98fd-f25b-4aec-bb99-69d4abd4ec4d}" >
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B07fb98fd-f25b-4aec-bb99-69d4abd4ec4d%7D/RuleData -->
		<Name>Allow PDF and XPS Printing</Name>
		<IncludedIdList>
			<GroupId>{e5170dfb-19a9-4466-8109-d36c9c912b4e}</GroupId>
		</IncludedIdList>
		<ExcludedIdList>
		</ExcludedIdList>
		<Entry Id="{e8cc55ec-17a8-4900-8df5-1af801342e9d}">
			<Type>Allow</Type>
			<AccessMask>64</AccessMask>
			<Options>8</Options>
		</Entry>
		<Entry Id="{2b410b9c-c940-42ec-be1c-1fcb8cc32bc4}">
			<Type>AuditAllowed</Type>
			<AccessMask>64</AccessMask>
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
<summary>Add a row for Allow PDF and XPS Printing</summary>  
   
   1. Click "Add"
   2. For Name, enter *Allow PDF and XPS Printing*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B07fb98fd-f25b-4aec-bb99-69d4abd4ec4d%7D/RuleData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  *windows\printer\Intune OMA-URI\Allow PDF_XPS Printer - File Evidence.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for PDF_XPS Printer</summary>  
   
   1. Click "Add"
   2. For Name, enter *PDF_XPS Printer*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Be5170dfb-19a9-4466-8109-d36c9c912b4e%7D/GroupData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  *windows\printer\Intune OMA-URI\PDF_XPS Printer.xml*
         
   
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



