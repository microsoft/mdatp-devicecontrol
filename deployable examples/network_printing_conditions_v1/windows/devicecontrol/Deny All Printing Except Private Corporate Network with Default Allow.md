# Device control policy sample: Deny All Printing Except Private Corporate Network with Default Allow

Description: A policy              
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
            <td rowspan="2" valign="top"><b>Deny all printing except on network printers on private network</b></td>
            <td rowspan="2 valign="top">
                <ul><li>Group: Network Printers<a href="#network-printers" title="MatchAny {'PrinterConnectionId': 'Network'}"> (details)</a>  
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
                MatchAll:
                <ul><li> Windows Network: MatchExcludeAll 
                        <ul><li>Group: Private Network<a href="#private-network" title="MatchAll {'NameId': 'Network 3', 'NetworkCategoryId': 'Private'}"> (details)</a>  
</ul>
                </ul>
                </details></td>
        </tr><tr>
            <td>Audit Denied</td>
            <td>:page_facing_up:</td>
            <td>Send event (2)</td>
            <td> 
                <center>-</center></td>
        </tr></table>


## Groups


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
<Group Id="{83d4b74a-af7c-4399-812c-fb9037e2c2b7}" Type="Network">
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B83d4b74a-af7c-4399-812c-fb9037e2c2b7%7D/GroupData -->
	<Name>Private Network</Name>
	<MatchType>MatchAll</MatchType>
	<DescriptorIdList>
		<NameId>Network 3</NameId>
		<NetworkCategoryId>Private</NetworkCategoryId>
	</DescriptorIdList>
</Group>
```
</details>


## Settings






| Setting Name |  Setting Value | Description |Documentation |
|--------------|----------------|-------------|---------------|


## Files
This policy is based on information in the following files:

- [groups/Private Network.xml](groups/Private%20Network.xml)
- [rules/Deny all printing except on network printers on private network.xml](rules/Deny%20all%20printing%20except%20on%20network%20printers%20on%20private%20network.xml)
- [groups/Network Printers.xml](groups/Network%20Printers.xml)


# Deployment Instructions

Device control [policy rules](#policy-rules) and [groups](#groups) can be deployed through the following management tools:


## Windows
- [Intune UX](#intune-ux)
- [Intune Custom Settings](#intune-custom-settings)
- [Group Policy (GPO)](#group-policy-gpo)





## Intune UX

Intune UX is not supported for this policy because:
- Windows Network groups not supported.
- Parameters are not supported

Use [Intune custom settings](#intune-custom-settings) to deploy the policy instead.


## Group Policy (GPO)
<details>
<summary>Define device control policy groups</summary>

   1. Go to Computer Configuration > Administrative Templates > Windows Components > Microsoft Defender Antivirus > Device Control > Define device control policy groups.
   2. Save the XML below to a network share.
```xml
<Groups>
	<Group Id="{257e3e1e-790c-4e29-ae2c-45a5f3363201}" Type="Device">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B257e3e1e-790c-4e29-ae2c-45a5f3363201%7D/GroupData -->
		<Name>Network Printers</Name>
		<MatchType>MatchAny</MatchType>
		<DescriptorIdList>
			<PrinterConnectionId>Network</PrinterConnectionId>
		</DescriptorIdList>
	</Group>
	<Group Id="{83d4b74a-af7c-4399-812c-fb9037e2c2b7}" Type="Network">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B83d4b74a-af7c-4399-812c-fb9037e2c2b7%7D/GroupData -->
		<Name>Private Network</Name>
		<MatchType>MatchAll</MatchType>
		<DescriptorIdList>
			<NameId>Network 3</NameId>
			<NetworkCategoryId>Private</NetworkCategoryId>
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
		<Name>Deny all printing except on network printers on private network</Name>
		<IncludedIdList>
			<GroupId>{257e3e1e-790c-4e29-ae2c-45a5f3363201}</GroupId>
		</IncludedIdList>
		<ExcludedIdList>
		</ExcludedIdList>
		<Entry Id="{93cdb2fb-9fcd-428e-a2e1-b4b0fab19782}">
			<Type>Deny</Type>
			<AccessMask>64</AccessMask>
			<Options>0</Options>
			<Parameters MatchType="MatchAll">
				<Network MatchType="MatchExcludeAll">
					<GroupId>{83d4b74a-af7c-4399-812c-fb9037e2c2b7}</GroupId>
				</Network>
			</Parameters>
		</Entry>
		<Entry Id="{f1d1a11d-2b81-495c-b725-b37d473c5594}">
			<Type>AuditDenied</Type>
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
<summary>Add a row for Deny all printing except on network printers on private network</summary>  
   
   1. Click "Add"
   2. For Name, enter *Deny all printing except on network printers on private network*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7Bb4bf3ecb-cea9-450d-a3fa-fec9a73edc08%7D/RuleData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  */workspaces/mdatp-devicecontrol/deployable examples/network_printing_conditions_v1/windows/devicecontrol/rules/Deny all printing except on network printers on private network.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for Network Printers</summary>  
   
   1. Click "Add"
   2. For Name, enter *Network Printers*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B257e3e1e-790c-4e29-ae2c-45a5f3363201%7D/GroupData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  */workspaces/mdatp-devicecontrol/deployable examples/network_printing_conditions_v1/windows/devicecontrol/groups/Network Printers.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for Private Network</summary>  
   
   1. Click "Add"
   2. For Name, enter *Private Network*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B83d4b74a-af7c-4399-812c-fb9037e2c2b7%7D/GroupData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  */workspaces/mdatp-devicecontrol/deployable examples/network_printing_conditions_v1/windows/devicecontrol/groups/Private Network.xml*
         
   
   7. Click "Save"
</details>



