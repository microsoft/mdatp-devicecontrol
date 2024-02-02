# Device control policy sample: Printer Policies

Description: An example showing how device control can restrict access to printers based on device properties, network, and VPN connection.              
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
            <td>None (0)</td> 
            <td>
                <center>-</center></td>
        </tr><tr>
            <td>Audit Allowed</td>
            <td>:page_facing_up:</td>
            <td>Send event (2)</td>
            <td> 
                <center>-</center></td>
        </tr><tr>
            <td rowspan="2" valign="top"><b>Allow approved USB Printer</b></td>
            <td rowspan="2 valign="top">
                <ul><li>Group: Authorized USB Printer<a href="#authorized-usb-printer" title="MatchAny {'VID_PID': '035E_0872'}"> (details)</a>  
</ul>
            </td>
            <td rowspan="2" valign="top">
                <ul></ul>
            </td>
            <td>Allow</td>
            <td>:white_check_mark:</td>
            <td>None (0)</td> 
            <td>
                <details>
                <summary>View</summary>
                MatchAny:
                <ul><li> Windows Network: MatchAny 
                        <ul><li>Group: Corporate Network<a href="#corporate-network" title="MatchAll {'NameId': 'corp.microsoft.com', 'NetworkCategoryId': 'DomainAuthenticated'}"> (details)</a>  
</ul><li> Windows VPN Connection: MatchAny 
                        <ul><li>Group: Corporate VPN<a href="#corporate-vpn" title="MatchAll {'NameId': 'MSFTVPN', 'VPNServerAddressId': 'msftvpn.*.microsoft.com', 'VPNDnsSuffixId': 'corp.microsoft.com', 'VPNConnectionStatusId': 'Connected'}"> (details)</a>  
</ul>
                </ul>
                </details></td>
        </tr><tr>
            <td>Audit Allowed</td>
            <td>:page_facing_up:</td>
            <td>Send event (2)</td>
            <td> 
                <center>-</center></td>
        </tr><tr>
            <td rowspan="1" valign="top"><b>Default Deny</b></td>
            <td rowspan="1 valign="top">
                <ul></ul>
            </td>
            <td rowspan="1" valign="top">
                <ul></ul>
            </td>
            <td>Audit Denied</td>
            <td>:page_facing_up:</td>
            <td>Show notification and Send event (3)</td> 
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

### Corporate Network



This is a group of type *Network*. 
The match type for the group is *MatchAll*.


|  Property | Value |
|-----------|-------|
| NameId | corp.microsoft.com |
| NetworkCategoryId | DomainAuthenticated |





<details>
<summary>View XML</summary>

```xml
<Group Id="{83d4b74a-af7c-4399-812c-fb9037e2c2b7}" Type="Network">
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B83d4b74a-af7c-4399-812c-fb9037e2c2b7%7D/GroupData -->
	<Name>Corporate Network</Name>
	<MatchType>MatchAll</MatchType>
	<DescriptorIdList>
		<NameId>corp.microsoft.com</NameId>
		<NetworkCategoryId>DomainAuthenticated</NetworkCategoryId>
	</DescriptorIdList>
</Group>
```
</details>

### Corporate VPN



This is a group of type *VPNConnection*. 
The match type for the group is *MatchAll*.


|  Property | Value |
|-----------|-------|
| NameId | MSFTVPN |
| VPNServerAddressId | msftvpn.*.microsoft.com |
| VPNDnsSuffixId | corp.microsoft.com |
| VPNConnectionStatusId | Connected |





<details>
<summary>View XML</summary>

```xml
<Group Id="{d633d17d-d1d1-4c73-aa27-c545c343b6d7}" Type="VPNConnection">
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Bd633d17d-d1d1-4c73-aa27-c545c343b6d7%7D/GroupData -->
	<Name>Corporate VPN</Name>
	<MatchType>MatchAll</MatchType>
	<DescriptorIdList>
		<NameId>MSFTVPN</NameId>
		<VPNServerAddressId>msftvpn.*.microsoft.com</VPNServerAddressId>
		<VPNDnsSuffixId>corp.microsoft.com</VPNDnsSuffixId>
		<VPNConnectionStatusId>Connected</VPNConnectionStatusId>
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

- [windows/printer/Intune OMA-URI/Authorized USB Printer.xml](/windows/printer/Intune%20OMA-URI/Authorized%20USB%20Printer.xml)
- [windows/printer/Intune OMA-URI/Corporate VPN.xml](/windows/printer/Intune%20OMA-URI/Corporate%20VPN.xml)
- [windows/printer/Group Policy/Printer_Policies.xml](/windows/printer/Group%20Policy/Printer_Policies.xml)
- [windows/printer/Group Policy/Printer_Groups.xml](/windows/printer/Group%20Policy/Printer_Groups.xml)


# Deployment Instructions

Device control [policy rules](#policy-rules) and [groups](#groups) can be deployed through the following management tools:


## Windows
- [Intune UX](#intune-ux)
- [Intune Custom Settings](#intune-custom-settings)
- [Group Policy (GPO)](#group-policy-gpo)





## Intune UX

Intune UX is not supported for this policy because:
- Windows VPN Connection groups not supported.
- Parameters are not supported
- Windows Network groups not supported.

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
	<Group Id="{05b56e90-e682-48ff-a6c0-5602c9638182}" Type="Device">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B05b56e90-e682-48ff-a6c0-5602c9638182%7D/GroupData -->
		<Name>Authorized USB Printer</Name>
		<MatchType>MatchAny</MatchType>
		<DescriptorIdList>
			<VID_PID>03F0_</VID_PID>
			<VID_PID>035E_0872</VID_PID>
		</DescriptorIdList>
	</Group>
	<Group Id="{83d4b74a-af7c-4399-812c-fb9037e2c2b7}" Type="Network">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B83d4b74a-af7c-4399-812c-fb9037e2c2b7%7D/GroupData -->
		<Name>Corporate Network</Name>
		<MatchType>MatchAll</MatchType>
		<DescriptorIdList>
			<NameId>corp.microsoft.com</NameId>
			<NetworkCategoryId>DomainAuthenticated</NetworkCategoryId>
		</DescriptorIdList>
	</Group>
	<Group Id="{d633d17d-d1d1-4c73-aa27-c545c343b6d7}" Type="VPNConnection">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Bd633d17d-d1d1-4c73-aa27-c545c343b6d7%7D/GroupData -->
		<Name>Corporate VPN</Name>
		<MatchType>MatchAll</MatchType>
		<DescriptorIdList>
			<NameId>MSFTVPN</NameId>
			<VPNServerAddressId>msftvpn.*.microsoft.com</VPNServerAddressId>
			<VPNDnsSuffixId>corp.microsoft.com</VPNDnsSuffixId>
			<VPNConnectionStatusId>Connected</VPNConnectionStatusId>
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
	<PolicyRule Id="{f5877f47-78ab-4f33-94e4-c44f18ec6dca}" >
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7Bf5877f47-78ab-4f33-94e4-c44f18ec6dca%7D/RuleData -->
		<Name>Allow PDF and XPS Printing</Name>
		<IncludedIdList>
			<GroupId>{e5170dfb-19a9-4466-8109-d36c9c912b4e}</GroupId>
		</IncludedIdList>
		<ExcludedIdList>
		</ExcludedIdList>
		<Entry Id="{12bd5f8e-94e8-4205-a990-635c24e43c59}">
			<Type>Allow</Type>
			<AccessMask>64</AccessMask>
			<Options>0</Options>
		</Entry>
		<Entry Id="{0fef09f8-7a68-4827-841b-d48afef6ba4c}">
			<Type>AuditAllowed</Type>
			<AccessMask>64</AccessMask>
			<Options>2</Options>
		</Entry>
	</PolicyRule>
	<PolicyRule Id="{f7e75634-7eec-4e67-bec5-5e7750cb9e02}" >
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7Bf7e75634-7eec-4e67-bec5-5e7750cb9e02%7D/RuleData -->
		<Name>Allow approved USB Printer</Name>
		<IncludedIdList>
			<GroupId>{05b56e90-e682-48ff-a6c0-5602c9638182}</GroupId>
		</IncludedIdList>
		<ExcludedIdList>
		</ExcludedIdList>
		<Entry Id="{27c79875-25d2-4765-aec2-cb2d1000613f}">
			<Type>Allow</Type>
			<AccessMask>64</AccessMask>
			<Options>0</Options>
			<Parameters MatchType="MatchAny">
				<Network MatchType="MatchAny">
					<GroupId>{83d4b74a-af7c-4399-812c-fb9037e2c2b7}</GroupId>
				</Network>
				<VPNConnection MatchType="MatchAny">
					<GroupId>{d633d17d-d1d1-4c73-aa27-c545c343b6d7}</GroupId>
				</VPNConnection>
			</Parameters>
		</Entry>
		<Entry Id="{b280c2bf-ca5d-46a1-afc9-7e34d8098ca7}">
			<Type>AuditAllowed</Type>
			<AccessMask>64</AccessMask>
			<Options>2</Options>
		</Entry>
	</PolicyRule>
	<PolicyRule Id="{e6ccf2cb-20d6-4478-bf2d-66f247ced6f3}" >
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7Be6ccf2cb-20d6-4478-bf2d-66f247ced6f3%7D/RuleData -->
		<Name>Default Deny</Name>
		<IncludedIdList>
		</IncludedIdList>
		<ExcludedIdList>
		</ExcludedIdList>
		<Entry Id="{6b9cf286-ec70-4463-bfaf-29f32bb5f0dc}">
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
<summary>Add a row for Allow PDF and XPS Printing</summary>  
   
   1. Click "Add"
   2. For Name, enter *Allow PDF and XPS Printing*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7Bf5877f47-78ab-4f33-94e4-c44f18ec6dca%7D/RuleData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  *windows\printer\Intune OMA-URI\allow_pdf_and_xps_printing{f5877f47-78ab-4f33-94e4-c44f18ec6dca}.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for Allow approved USB Printer</summary>  
   
   1. Click "Add"
   2. For Name, enter *Allow approved USB Printer*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7Bf7e75634-7eec-4e67-bec5-5e7750cb9e02%7D/RuleData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  *windows\printer\Intune OMA-URI\allow_approved_usb_printer{f7e75634-7eec-4e67-bec5-5e7750cb9e02}.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for Default Deny</summary>  
   
   1. Click "Add"
   2. For Name, enter *Default Deny*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7Be6ccf2cb-20d6-4478-bf2d-66f247ced6f3%7D/RuleData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  *windows\printer\Intune OMA-URI\default_deny{e6ccf2cb-20d6-4478-bf2d-66f247ced6f3}.xml*
         
   
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
<summary>Add a row for Authorized USB Printer</summary>  
   
   1. Click "Add"
   2. For Name, enter *Authorized USB Printer*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B05b56e90-e682-48ff-a6c0-5602c9638182%7D/GroupData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  *windows\printer\Intune OMA-URI\Authorized USB Printer.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for Corporate Network</summary>  
   
   1. Click "Add"
   2. For Name, enter *Corporate Network*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B83d4b74a-af7c-4399-812c-fb9037e2c2b7%7D/GroupData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  *windows\printer\Intune OMA-URI\Corporate Network.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for Corporate VPN</summary>  
   
   1. Click "Add"
   2. For Name, enter *Corporate VPN*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Bd633d17d-d1d1-4c73-aa27-c545c343b6d7%7D/GroupData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  *windows\printer\Intune OMA-URI\Corporate VPN.xml*
         
   
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



