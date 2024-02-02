# Device control policy sample: Printer Example - Restrict Acccess by Network

Description: This policy allows printing only for network printers on the corporate network, and denies everything else.              
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
            <td rowspan="1" valign="top"><b>Allow printing only on network printers on corporate network</b></td>
            <td rowspan="1 valign="top">
                <ul><li>Group: Network Printers<a href="#network-printers" title="MatchAny {'PrinterConnectionId': 'Network'}"> (details)</a>  
</ul>
            </td>
            <td rowspan="1" valign="top">
                <ul></ul>
            </td>
            <td>Allow</td>
            <td>:white_check_mark:</td>
            <td>None (0)</td> 
            <td>
                <details>
                <summary>View</summary>
                MatchAll:
                <ul><li> Windows Network: MatchAll 
                        <ul><li>Group: Corporate Network<a href="#corporate-network" title="MatchAll {'NameId': 'corp.microsoft.com', 'NetworkCategoryId': 'DomainAuthenticated'}"> (details)</a>  
</ul>
                </ul>
                </details></td>
        </tr><tr>
            <td rowspan="2" valign="top"><b>Deny all other printing</b></td>
            <td rowspan="2 valign="top">
                <ul><li>Group: Any Printer<a href="#any-printer" title="MatchAny {'PrimaryId': 'PrinterDevices'}"> (details)</a>  
</ul>
            </td>
            <td rowspan="2" valign="top">
                <ul><li>Group: Network Printers<a href="#network-printers" title="MatchAny {'PrinterConnectionId': 'Network'}"> (details)</a>  
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

### Network Printers



This is a group of type *Device*. 
The match type for the group is *MatchAny*.


|  Property | Value |
|-----------|-------|
| PrinterConnectionId | Network |





<details>
<summary>View XML</summary>

```xml
<Group Id="{257e3e1e-790c-4e29-ae2c-45a5f3363201}" Type="Device">
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B257e3e1e-790c-4e29-ae2c-45a5f3363201%7D/GroupData -->
	<Name>Network Printers</Name>
	<MatchType>MatchAny</MatchType>
	<DescriptorIdList>
		<PrinterConnectionId>Network</PrinterConnectionId>
	</DescriptorIdList>
</Group>
```
</details>

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


## Settings
| Setting Name |  Setting Value | Documentation |
|--------------|----------------|---------------|
DeviceControlEnabled | True | [documentation](https://learn.microsoft.com/en-us/windows/client-management/mdm/defender-csp#configurationdevicecontrolenabled) |
DefaultEnforcement | Allow | [documentation](https://learn.microsoft.com/en-us/windows/client-management/mdm/defender-csp#configurationdefaultenforcement) |
SecuredDevicesConfiguration | PrinterDevices | [documentation](https://learn.microsoft.com/en-us/windows/client-management/mdm/defender-csp#configurationsecureddevicesconfiguration) |


## Files
This policy is based on information in the following files:

- [windows/printer/Intune OMA-URI/network_printers{257e3e1e-790c-4e29-ae2c-45a5f3363201}.xml](/windows/printer/Intune%20OMA-URI/network_printers%7B257e3e1e-790c-4e29-ae2c-45a5f3363201%7D.xml)
- [windows/printer/Group Policy/Allow Printing to Corporate Network Printers Only.xml](/windows/printer/Group%20Policy/Allow%20Printing%20to%20Corporate%20Network%20Printers%20Only.xml)
- [windows/printer/Group Policy/Printer_Groups.xml](/windows/printer/Group%20Policy/Printer_Groups.xml)


# Deployment Instructions

Device control [policy rules](#policy-rules) and [groups](#groups) can be deployed through the following management tools:


## Windows
- [Intune UX](#intune-ux)
- [Intune Custom Settings](#intune-custom-settings)
- [Group Policy (GPO)](#group-policy-gpo)





## Intune UX

Intune UX is not supported for this policy because:
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
	<Group Id="{83d4b74a-af7c-4399-812c-fb9037e2c2b7}" Type="Network">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B83d4b74a-af7c-4399-812c-fb9037e2c2b7%7D/GroupData -->
		<Name>Corporate Network</Name>
		<MatchType>MatchAll</MatchType>
		<DescriptorIdList>
			<NameId>corp.microsoft.com</NameId>
			<NetworkCategoryId>DomainAuthenticated</NetworkCategoryId>
		</DescriptorIdList>
	</Group>
	<Group Id="{257e3e1e-790c-4e29-ae2c-45a5f3363201}" Type="Device">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B257e3e1e-790c-4e29-ae2c-45a5f3363201%7D/GroupData -->
		<Name>Network Printers</Name>
		<MatchType>MatchAny</MatchType>
		<DescriptorIdList>
			<PrinterConnectionId>Network</PrinterConnectionId>
		</DescriptorIdList>
	</Group>
	<Group Id="{090b8e1d-5c7b-4f69-a4f2-fb76fa0535fc}" Type="Device">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B090b8e1d-5c7b-4f69-a4f2-fb76fa0535fc%7D/GroupData -->
		<Name>Any Printer</Name>
		<MatchType>MatchAny</MatchType>
		<DescriptorIdList>
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
	<PolicyRule Id="{b4bf3ecb-cea9-450d-a3fa-fec9a73edc08}" >
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7Bb4bf3ecb-cea9-450d-a3fa-fec9a73edc08%7D/RuleData -->
		<Name>Allow printing only on network printers on corporate network</Name>
		<IncludedIdList>
			<GroupId>{257e3e1e-790c-4e29-ae2c-45a5f3363201}</GroupId>
		</IncludedIdList>
		<ExcludedIdList>
		</ExcludedIdList>
		<Entry Id="{93cdb2fb-9fcd-428e-a2e1-b4b0fab19782}">
			<Type>Allow</Type>
			<AccessMask>64</AccessMask>
			<Options>0</Options>
			<Parameters MatchType="MatchAll">
				<Network MatchType="MatchAll">
					<GroupId>{83d4b74a-af7c-4399-812c-fb9037e2c2b7}</GroupId>
				</Network>
			</Parameters>
		</Entry>
	</PolicyRule>
	<PolicyRule Id="{47420f70-ef17-467e-a982-ab4c3abde16e}" >
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B47420f70-ef17-467e-a982-ab4c3abde16e%7D/RuleData -->
		<Name>Deny all other printing</Name>
		<IncludedIdList>
			<GroupId>{090b8e1d-5c7b-4f69-a4f2-fb76fa0535fc}</GroupId>
		</IncludedIdList>
		<ExcludedIdList>
			<GroupId>{257e3e1e-790c-4e29-ae2c-45a5f3363201}</GroupId>
		</ExcludedIdList>
		<Entry Id="{7de4d368-761e-46eb-a216-1c0114bc98b6}">
			<Type>Deny</Type>
			<AccessMask>64</AccessMask>
			<Options>0</Options>
		</Entry>
		<Entry Id="{31d84dd3-7f09-494b-ab1c-71e190bf268c}">
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
<summary>Add a row for Allow printing only on network printers on corporate network</summary>  
   
   1. Click "Add"
   2. For Name, enter *Allow printing only on network printers on corporate network*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7Bb4bf3ecb-cea9-450d-a3fa-fec9a73edc08%7D/RuleData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  *windows\printer\Intune OMA-URI\allow_printing_only_on_network_printers_on_corporate_network{b4bf3ecb-cea9-450d-a3fa-fec9a73edc08}.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for Deny all other printing</summary>  
   
   1. Click "Add"
   2. For Name, enter *Deny all other printing*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B47420f70-ef17-467e-a982-ab4c3abde16e%7D/RuleData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  *windows\printer\Intune OMA-URI\deny_all_other_printing{47420f70-ef17-467e-a982-ab4c3abde16e}.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for Network Printers</summary>  
   
   1. Click "Add"
   2. For Name, enter *Network Printers*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B257e3e1e-790c-4e29-ae2c-45a5f3363201%7D/GroupData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  *windows\printer\Intune OMA-URI\network_printers{257e3e1e-790c-4e29-ae2c-45a5f3363201}.xml*
         
   
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
<summary>Add a row for Any Printer</summary>  
   
   1. Click "Add"
   2. For Name, enter *Any Printer*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B090b8e1d-5c7b-4f69-a4f2-fb76fa0535fc%7D/GroupData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  *windows\printer\Intune OMA-URI\Any printer group.xml*
         
   
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
<summary>Add a row for SecuredDevicesConfiguration</summary>  
   
   1. Click "Add"
   2. For Name, enter *SecuredDevicesConfiguration*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/SecuredDevicesConfiguration*
   5. For Data type, select *String*
   
   7. For Value, enter *PrinterDevices*
   
   7. Click "Save"
</details>



