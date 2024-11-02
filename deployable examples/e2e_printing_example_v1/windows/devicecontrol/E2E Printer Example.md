# Device control policy sample: E2E Printer Example

**Description:** This is an end to end example of printer policies.  Printing to Network and Corporate printers are denied unless on the Private Network.  USB printing is only allowed on approved printers by VID PID.  Local priniting is never denied.  Other printers are always denied.              
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
            <td rowspan="2" valign="top"><b>USB Printing</b></td>
            <td rowspan="2 valign="top">
                <ul><li>Group: All USB Printers<a href="#all-usb-printers" title="MatchAny {'PrinterConnectionId': 'USB'}"> (details)</a>  
</ul>
            </td>
            <td rowspan="2" valign="top">
                <ul><li>Group: Authorized USB Printers<a href="#authorized-usb-printers" title="MatchAny {'VID_PID': '035E_0872'}"> (details)</a>  
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
        </tr><tr>
            <td rowspan="2" valign="top"><b>Corporate Printing</b></td>
            <td rowspan="2 valign="top">
                <ul><li>Group: All Corporate Printers<a href="#all-corporate-printers" title="MatchAny {'PrinterConnectionId': 'Corporate'}"> (details)</a>  
</ul>
            </td>
            <td rowspan="2" valign="top">
                <ul></ul>
            </td>
            <td>Deny</td>
            <td>:x:</td>
            <td>None (0)</td> 
            <td>
                <details>
                <summary>View</summary>
                MatchAny:
                <ul><li> Windows Network: MatchExcludeAll 
                        <ul><li>Group: Private Network<a href="#private-network" title="MatchAll {'NameId': 'Network 3', 'NetworkCategoryId': 'Private'}"> (details)</a>  
</ul>
                </ul>
                </details></td>
        </tr><tr>
            <td>Audit Denied</td>
            <td>:page_facing_up:</td>
            <td>Show notification and Send event (3)</td>
            <td> 
                <center>-</center></td>
        </tr><tr>
            <td rowspan="2" valign="top"><b>Other Printers</b></td>
            <td rowspan="2 valign="top">
                <ul></ul>
            </td>
            <td rowspan="2" valign="top">
                <ul><li>Group: All Network Printers<a href="#all-network-printers" title="MatchAny {'PrinterConnectionId': 'Network'}"> (details)</a>  
<li>Group: All File Printers<a href="#all-file-printers" title="MatchAny {'PrinterConnectionId': 'File'}"> (details)</a>  
<li>Group: All Corporate Printers<a href="#all-corporate-printers" title="MatchAny {'PrinterConnectionId': 'Corporate'}"> (details)</a>  
<li>Group: All USB Printers<a href="#all-usb-printers" title="MatchAny {'PrinterConnectionId': 'USB'}"> (details)</a>  
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
        </tr><tr>
            <td rowspan="2" valign="top"><b>Network Printing</b></td>
            <td rowspan="2 valign="top">
                <ul><li>Group: All Network Printers<a href="#all-network-printers" title="MatchAny {'PrinterConnectionId': 'Network'}"> (details)</a>  
</ul>
            </td>
            <td rowspan="2" valign="top">
                <ul></ul>
            </td>
            <td>Deny</td>
            <td>:x:</td>
            <td>None (0)</td> 
            <td>
                <details>
                <summary>View</summary>
                MatchAny:
                <ul><li> Windows Network: MatchExcludeAll 
                        <ul><li>Group: Private Network<a href="#private-network" title="MatchAll {'NameId': 'Network 3', 'NetworkCategoryId': 'Private'}"> (details)</a>  
</ul>
                </ul>
                </details></td>
        </tr><tr>
            <td>Audit Denied</td>
            <td>:page_facing_up:</td>
            <td>Show notification and Send event (3)</td>
            <td> 
                <center>-</center></td>
        </tr></table>


## Groups


### Authorized USB Printers



This is a group of type *Device*. 
The match type for the group is *MatchAny*.


|  Property | Value |
|-----------|-------|
| VID_PID | 03F0_ |
| VID_PID | 035E_0872 |





<details>
<summary>View XML</summary>

```xml
<Group Id="{005999fd-2973-44a6-b0c7-2ce4be43c451}" Type="Device">
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B005999fd-2973-44a6-b0c7-2ce4be43c451%7D/GroupData -->
	<Name>Authorized USB Printers</Name>
	<MatchType>MatchAny</MatchType>
	<DescriptorIdList>
		<VID_PID>03F0_</VID_PID>
		<VID_PID>035E_0872</VID_PID>
	</DescriptorIdList>
</Group>
```
</details>

### All USB Printers



This is a group of type *Device*. 
The match type for the group is *MatchAny*.


|  Property | Value |
|-----------|-------|
| PrinterConnectionId | USB |





<details>
<summary>View XML</summary>

```xml
<Group Id="{42e9ee1b-adc5-46fb-a51b-8ca3a7928f0d}" Type="Device">
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B42e9ee1b-adc5-46fb-a51b-8ca3a7928f0d%7D/GroupData -->
	<Name>All USB Printers</Name>
	<MatchType>MatchAny</MatchType>
	<DescriptorIdList>
		<PrinterConnectionId>USB</PrinterConnectionId>
	</DescriptorIdList>
</Group>
```
</details>

### Private Network



This is a group of type *Network*. 
The match type for the group is *MatchAll*.


|  Property | Value |
|-----------|-------|
| NameId | Network 3 |
| NetworkCategoryId | Private |





<details>
<summary>View XML</summary>

```xml
<Group Id="{45a8d131-ed6a-4cdb-a1d5-2dbf329dd2d4}" Type="Network">
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B45a8d131-ed6a-4cdb-a1d5-2dbf329dd2d4%7D/GroupData -->
	<Name>Private Network</Name>
	<MatchType>MatchAll</MatchType>
	<DescriptorIdList>
		<NameId>Network 3</NameId>
		<NetworkCategoryId>Private</NetworkCategoryId>
	</DescriptorIdList>
</Group>
```
</details>

### All Corporate Printers



This is a group of type *Device*. 
The match type for the group is *MatchAny*.


|  Property | Value |
|-----------|-------|
| PrinterConnectionId | Corporate |





<details>
<summary>View XML</summary>

```xml
<Group Id="{3bb1fc07-98c1-4d9f-8be4-04717ccd6357}" Type="Device">
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B3bb1fc07-98c1-4d9f-8be4-04717ccd6357%7D/GroupData -->
	<Name>All Corporate Printers</Name>
	<MatchType>MatchAny</MatchType>
	<DescriptorIdList>
		<PrinterConnectionId>Corporate</PrinterConnectionId>
	</DescriptorIdList>
</Group>
```
</details>

### All Network Printers



This is a group of type *Device*. 
The match type for the group is *MatchAny*.


|  Property | Value |
|-----------|-------|
| PrinterConnectionId | Network |





<details>
<summary>View XML</summary>

```xml
<Group Id="{7de3417e-4b6f-4601-8e13-c41bffa6c04c}" Type="Device">
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B7de3417e-4b6f-4601-8e13-c41bffa6c04c%7D/GroupData -->
	<Name>All Network Printers</Name>
	<MatchType>MatchAny</MatchType>
	<DescriptorIdList>
		<PrinterConnectionId>Network</PrinterConnectionId>
	</DescriptorIdList>
</Group>
```
</details>

### All File Printers



This is a group of type *Device*. 
The match type for the group is *MatchAny*.


|  Property | Value |
|-----------|-------|
| PrinterConnectionId | File |





<details>
<summary>View XML</summary>

```xml
<Group Id="{edf98528-02e2-434c-b121-191f18a80a95}" Type="Device">
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Bedf98528-02e2-434c-b121-191f18a80a95%7D/GroupData -->
	<Name>All File Printers</Name>
	<MatchType>MatchAny</MatchType>
	<DescriptorIdList>
		<PrinterConnectionId>File</PrinterConnectionId>
	</DescriptorIdList>
</Group>
```
</details>


## Settings






| Setting Name |  Setting Value | Description |Documentation |
|--------------|----------------|-------------|---------------|
DefaultEnforcement | Allow | Control Device Control default enforcement. This is the enforcement applied if there are no policy rules present or at the end of the policy rules evaluation none were matched. |[documentation](https://learn.microsoft.com/en-us/windows/client-management/mdm/defender-csp#configurationdefaultenforcement) |


## Files
This policy is based on information in the following files:

- [groups/All File Printers.xml](groups/All%20File%20Printers.xml)
- [rules/Network Printing.xml](rules/Network%20Printing.xml)
- [groups/All USB Printers.xml](groups/All%20USB%20Printers.xml)
- [groups/All Network Printers.xml](groups/All%20Network%20Printers.xml)
- [rules/Other Printers.xml](rules/Other%20Printers.xml)
- [groups/Authorized USB Printers.xml](groups/Authorized%20USB%20Printers.xml)
- [rules/USB Printing.xml](rules/USB%20Printing.xml)
- [groups/All Corporate Printers.xml](groups/All%20Corporate%20Printers.xml)
- [groups/Private Network.xml](groups/Private%20Network.xml)
- [rules/Corporate Printing.xml](rules/Corporate%20Printing.xml)


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
	<Group Id="{005999fd-2973-44a6-b0c7-2ce4be43c451}" Type="Device">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B005999fd-2973-44a6-b0c7-2ce4be43c451%7D/GroupData -->
		<Name>Authorized USB Printers</Name>
		<MatchType>MatchAny</MatchType>
		<DescriptorIdList>
			<VID_PID>03F0_</VID_PID>
			<VID_PID>035E_0872</VID_PID>
		</DescriptorIdList>
	</Group>
	<Group Id="{42e9ee1b-adc5-46fb-a51b-8ca3a7928f0d}" Type="Device">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B42e9ee1b-adc5-46fb-a51b-8ca3a7928f0d%7D/GroupData -->
		<Name>All USB Printers</Name>
		<MatchType>MatchAny</MatchType>
		<DescriptorIdList>
			<PrinterConnectionId>USB</PrinterConnectionId>
		</DescriptorIdList>
	</Group>
	<Group Id="{45a8d131-ed6a-4cdb-a1d5-2dbf329dd2d4}" Type="Network">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B45a8d131-ed6a-4cdb-a1d5-2dbf329dd2d4%7D/GroupData -->
		<Name>Private Network</Name>
		<MatchType>MatchAll</MatchType>
		<DescriptorIdList>
			<NameId>Network 3</NameId>
			<NetworkCategoryId>Private</NetworkCategoryId>
		</DescriptorIdList>
	</Group>
	<Group Id="{3bb1fc07-98c1-4d9f-8be4-04717ccd6357}" Type="Device">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B3bb1fc07-98c1-4d9f-8be4-04717ccd6357%7D/GroupData -->
		<Name>All Corporate Printers</Name>
		<MatchType>MatchAny</MatchType>
		<DescriptorIdList>
			<PrinterConnectionId>Corporate</PrinterConnectionId>
		</DescriptorIdList>
	</Group>
	<Group Id="{7de3417e-4b6f-4601-8e13-c41bffa6c04c}" Type="Device">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B7de3417e-4b6f-4601-8e13-c41bffa6c04c%7D/GroupData -->
		<Name>All Network Printers</Name>
		<MatchType>MatchAny</MatchType>
		<DescriptorIdList>
			<PrinterConnectionId>Network</PrinterConnectionId>
		</DescriptorIdList>
	</Group>
	<Group Id="{edf98528-02e2-434c-b121-191f18a80a95}" Type="Device">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Bedf98528-02e2-434c-b121-191f18a80a95%7D/GroupData -->
		<Name>All File Printers</Name>
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
	<PolicyRule Id="{9c09ea0f-c2de-4cf9-9b30-92588aad0fd8}" >
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B9c09ea0f-c2de-4cf9-9b30-92588aad0fd8%7D/RuleData -->
		<Name>USB Printing</Name>
		<IncludedIdList>
			<GroupId>{42e9ee1b-adc5-46fb-a51b-8ca3a7928f0d}</GroupId>
		</IncludedIdList>
		<ExcludedIdList>
			<GroupId>{005999fd-2973-44a6-b0c7-2ce4be43c451}</GroupId>
		</ExcludedIdList>
		<Entry Id="{f752b1ab-44d5-41a7-9d31-9b647942a575}">
			<Type>Deny</Type>
			<AccessMask>64</AccessMask>
			<Options>0</Options>
		</Entry>
		<Entry Id="{8a6ca048-a441-44cf-9a3c-aa495d47546b}">
			<Type>AuditDenied</Type>
			<AccessMask>64</AccessMask>
			<Options>3</Options>
		</Entry>
	</PolicyRule>
	<PolicyRule Id="{da7170af-134b-40f7-ab45-269720509566}" >
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7Bda7170af-134b-40f7-ab45-269720509566%7D/RuleData -->
		<Name>Corporate Printing</Name>
		<IncludedIdList>
			<GroupId>{3bb1fc07-98c1-4d9f-8be4-04717ccd6357}</GroupId>
		</IncludedIdList>
		<ExcludedIdList>
		</ExcludedIdList>
		<Entry Id="{9e696ad1-b9a2-42be-8850-972da1e53514}">
			<Type>Deny</Type>
			<AccessMask>64</AccessMask>
			<Options>0</Options>
			<Parameters MatchType="MatchAny">
				<Network MatchType="MatchExcludeAll">
					<GroupId>{45a8d131-ed6a-4cdb-a1d5-2dbf329dd2d4}</GroupId>
				</Network>
			</Parameters>
		</Entry>
		<Entry Id="{e84db75a-ee6f-4228-ad39-fc3de783284d}">
			<Type>AuditDenied</Type>
			<AccessMask>64</AccessMask>
			<Options>3</Options>
		</Entry>
	</PolicyRule>
	<PolicyRule Id="{9b318360-2d2b-4fde-8e97-a9f6ff5576cd}" >
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B9b318360-2d2b-4fde-8e97-a9f6ff5576cd%7D/RuleData -->
		<Name>Other Printers</Name>
		<IncludedIdList>
		</IncludedIdList>
		<ExcludedIdList>
			<GroupId>{7de3417e-4b6f-4601-8e13-c41bffa6c04c}</GroupId>
			<GroupId>{edf98528-02e2-434c-b121-191f18a80a95}</GroupId>
			<GroupId>{3bb1fc07-98c1-4d9f-8be4-04717ccd6357}</GroupId>
			<GroupId>{42e9ee1b-adc5-46fb-a51b-8ca3a7928f0d}</GroupId>
		</ExcludedIdList>
		<Entry Id="{ec1a8f07-ac98-4551-b24f-c706203695e2}">
			<Type>Deny</Type>
			<AccessMask>64</AccessMask>
			<Options>0</Options>
		</Entry>
		<Entry Id="{9e567372-35f9-47a7-8f56-73956c0d76f6}">
			<Type>AuditDenied</Type>
			<AccessMask>64</AccessMask>
			<Options>3</Options>
		</Entry>
	</PolicyRule>
	<PolicyRule Id="{368df281-fc27-41d1-986b-cec12063638e}" >
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B368df281-fc27-41d1-986b-cec12063638e%7D/RuleData -->
		<Name>Network Printing</Name>
		<IncludedIdList>
			<GroupId>{7de3417e-4b6f-4601-8e13-c41bffa6c04c}</GroupId>
		</IncludedIdList>
		<ExcludedIdList>
		</ExcludedIdList>
		<Entry Id="{52a4ad72-429d-41e6-9dcf-410aecebdb6d}">
			<Type>Deny</Type>
			<AccessMask>64</AccessMask>
			<Options>0</Options>
			<Parameters MatchType="MatchAny">
				<Network MatchType="MatchExcludeAll">
					<GroupId>{45a8d131-ed6a-4cdb-a1d5-2dbf329dd2d4}</GroupId>
				</Network>
			</Parameters>
		</Entry>
		<Entry Id="{0479a46c-a8e2-4dd1-80ef-f77b96fb4734}">
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
<summary>Add a row for Network Printing</summary>  
   
   1. Click "Add"
   2. For Name, enter *Network Printing*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B368df281-fc27-41d1-986b-cec12063638e%7D/RuleData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  */workspaces/mdatp-devicecontrol/deployable examples/e2e_printing_example_v1/windows/devicecontrol/rules/Network Printing.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for Corporate Printing</summary>  
   
   1. Click "Add"
   2. For Name, enter *Corporate Printing*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7Bda7170af-134b-40f7-ab45-269720509566%7D/RuleData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  */workspaces/mdatp-devicecontrol/deployable examples/e2e_printing_example_v1/windows/devicecontrol/rules/Corporate Printing.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for USB Printing</summary>  
   
   1. Click "Add"
   2. For Name, enter *USB Printing*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B9c09ea0f-c2de-4cf9-9b30-92588aad0fd8%7D/RuleData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  */workspaces/mdatp-devicecontrol/deployable examples/e2e_printing_example_v1/windows/devicecontrol/rules/USB Printing.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for Other Printers</summary>  
   
   1. Click "Add"
   2. For Name, enter *Other Printers*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B9b318360-2d2b-4fde-8e97-a9f6ff5576cd%7D/RuleData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  */workspaces/mdatp-devicecontrol/deployable examples/e2e_printing_example_v1/windows/devicecontrol/rules/Other Printers.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for All USB Printers</summary>  
   
   1. Click "Add"
   2. For Name, enter *All USB Printers*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B42e9ee1b-adc5-46fb-a51b-8ca3a7928f0d%7D/GroupData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  */workspaces/mdatp-devicecontrol/deployable examples/e2e_printing_example_v1/windows/devicecontrol/groups/All USB Printers.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for Authorized USB Printers</summary>  
   
   1. Click "Add"
   2. For Name, enter *Authorized USB Printers*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B005999fd-2973-44a6-b0c7-2ce4be43c451%7D/GroupData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  */workspaces/mdatp-devicecontrol/deployable examples/e2e_printing_example_v1/windows/devicecontrol/groups/Authorized USB Printers.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for All Corporate Printers</summary>  
   
   1. Click "Add"
   2. For Name, enter *All Corporate Printers*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B3bb1fc07-98c1-4d9f-8be4-04717ccd6357%7D/GroupData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  */workspaces/mdatp-devicecontrol/deployable examples/e2e_printing_example_v1/windows/devicecontrol/groups/All Corporate Printers.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for Private Network</summary>  
   
   1. Click "Add"
   2. For Name, enter *Private Network*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B45a8d131-ed6a-4cdb-a1d5-2dbf329dd2d4%7D/GroupData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  */workspaces/mdatp-devicecontrol/deployable examples/e2e_printing_example_v1/windows/devicecontrol/groups/Private Network.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for All Network Printers</summary>  
   
   1. Click "Add"
   2. For Name, enter *All Network Printers*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B7de3417e-4b6f-4601-8e13-c41bffa6c04c%7D/GroupData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  */workspaces/mdatp-devicecontrol/deployable examples/e2e_printing_example_v1/windows/devicecontrol/groups/All Network Printers.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for All File Printers</summary>  
   
   1. Click "Add"
   2. For Name, enter *All File Printers*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Bedf98528-02e2-434c-b121-191f18a80a95%7D/GroupData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  */workspaces/mdatp-devicecontrol/deployable examples/e2e_printing_example_v1/windows/devicecontrol/groups/All File Printers.xml*
         
   
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



