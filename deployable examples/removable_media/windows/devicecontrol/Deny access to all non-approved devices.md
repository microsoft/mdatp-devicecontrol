# Device control policy sample: Deny access to all non-approved devices

Description: This is a policy.              
Device Type: Windows Removable Device

A device control policy is a combination of [policy rules](#policy-rules), [groups](#groups) and [settings](#settings).  
This sample is based on the [sample files](#files).  
To configure the sample, follow the [deployment instructions](#deployment-instructions).  

## Policy Rules


<table>
    <tr>
        <th rowspan="2" valign="top">Name</th>
        <th colspan="2" valign="top"><center>Devices</center></th>
        <th rowspan="2" valign="top">Rule Type</th>
        <th colspan="6" valign="top"><center>Access</center></th>
        <th rowspan="2" valign="top">Notification</th>
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
		<th>File Execute</th></tr><tr>
            <td rowspan="2" valign="top"><b>Deny access to all non-approved devices</b></td>
            <td rowspan="2 valign="top">
                <ul><li>Group: All Removable Media Devices<a href="#all-removable-media-devices" title="MatchAny {'PrimaryId': 'RemovableMediaDevices'}"> (details)</a>  
</ul>
            </td>
            <td rowspan="2" valign="top">
                <ul><li>Group: Allowed USBs<a href="#allowed-usbs" title="MatchAny {'SerialNumberId': '6EA9150055800605'}"> (details)</a>  
</ul>
            </td>
            <td>Deny</td>
            <td>:x:</td>
            <td>:x:</td>
            <td>:x:</td>
            <td>:x:</td>
            <td>:x:</td>
            <td>:x:</td>
            <td>None (0)</td> 
            <td>
                <center>-</center></td>
        </tr><tr>
            <td>Audit Denied</td>
            <td>:page_facing_up:</td>
            <td>:page_facing_up:</td>
            <td>:page_facing_up:</td>
            <td>:page_facing_up:</td>
            <td>:page_facing_up:</td>
            <td>:page_facing_up:</td>
            <td>Show notification and Send event (3)</td>
            <td> 
                <center>-</center></td>
        </tr></table>


## Groups


### Allowed USBs



This is a group of type *Device*. 
The match type for the group is *MatchAny*.


|  Property | Value |
|-----------|-------|
| SerialNumberId | 6EA9150055800605 |





<details>
<summary>View XML</summary>

```xml
<Group Id="{00b72954-e837-4523-8186-ad7cb4075584}" Type="Device">
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B00b72954-e837-4523-8186-ad7cb4075584%7D/GroupData -->
	<Name>Allowed USBs</Name>
	<MatchType>MatchAny</MatchType>
	<DescriptorIdList>
		<SerialNumberId>6EA9150055800605</SerialNumberId>
	</DescriptorIdList>
</Group>
```
</details>

### All Removable Media Devices



This is a group of type *Device*. 
The match type for the group is *MatchAny*.


|  Property | Value |
|-----------|-------|
| PrimaryId | RemovableMediaDevices |





<details>
<summary>View XML</summary>

```xml
<Group Id="{e2461b64-bc0b-4d85-8cb8-424cabe97f55}" Type="Device">
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Be2461b64-bc0b-4d85-8cb8-424cabe97f55%7D/GroupData -->
	<Name>All Removable Media Devices</Name>
	<MatchType>MatchAny</MatchType>
	<DescriptorIdList>
		<PrimaryId>RemovableMediaDevices</PrimaryId>
	</DescriptorIdList>
</Group>
```
</details>


## Settings






| Setting Name |  Setting Value | Description |Documentation |
|--------------|----------------|-------------|---------------|


## Files
This policy is based on information in the following files:

- [groups/All Removable Media Devices.xml](groups/All%20Removable%20Media%20Devices.xml)
- [groups/Allowed USBs.xml](groups/Allowed%20USBs.xml)
- [rules/Deny access to all non-approved devices.xml](rules/Deny%20access%20to%20all%20non-approved%20devices.xml)


# Deployment Instructions

Device control [policy rules](#policy-rules) and [groups](#groups) can be deployed through the following management tools:


## Windows
- [Intune UX](#intune-ux)
- [Intune Custom Settings](#intune-custom-settings)
- [Group Policy (GPO)](#group-policy-gpo)





## Intune UX

Intune UX is not supported for this policy because:
- File Write (16) is an unsupported access mask
- File Execute (32) is an unsupported access mask
- File Read (8) is an unsupported access mask

Use [Intune custom settings](#intune-custom-settings) to deploy the policy instead.


## Group Policy (GPO)
<details>
<summary>Define device control policy groups</summary>

   1. Go to Computer Configuration > Administrative Templates > Windows Components > Microsoft Defender Antivirus > Device Control > Define device control policy groups.
   2. Save the XML below to a network share.
```xml
<Groups>
	<Group Id="{00b72954-e837-4523-8186-ad7cb4075584}" Type="Device">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B00b72954-e837-4523-8186-ad7cb4075584%7D/GroupData -->
		<Name>Allowed USBs</Name>
		<MatchType>MatchAny</MatchType>
		<DescriptorIdList>
			<SerialNumberId>6EA9150055800605</SerialNumberId>
		</DescriptorIdList>
	</Group>
	<Group Id="{e2461b64-bc0b-4d85-8cb8-424cabe97f55}" Type="Device">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Be2461b64-bc0b-4d85-8cb8-424cabe97f55%7D/GroupData -->
		<Name>All Removable Media Devices</Name>
		<MatchType>MatchAny</MatchType>
		<DescriptorIdList>
			<PrimaryId>RemovableMediaDevices</PrimaryId>
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
	<PolicyRule Id="{7458f924-0925-4a0f-8c2c-fb50b0c3350c}" >
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B7458f924-0925-4a0f-8c2c-fb50b0c3350c%7D/RuleData -->
		<Name>Deny access to all non-approved devices</Name>
		<IncludedIdList>
			<GroupId>{e2461b64-bc0b-4d85-8cb8-424cabe97f55}</GroupId>
		</IncludedIdList>
		<ExcludedIdList>
			<GroupId>{00b72954-e837-4523-8186-ad7cb4075584}</GroupId>
		</ExcludedIdList>
		<Entry Id="{79c97158-1d4f-420e-afd5-cfe435c1e6f4}">
			<Type>Deny</Type>
			<AccessMask>63</AccessMask>
			<Options>0</Options>
		</Entry>
		<Entry Id="{3a29b377-c54c-4986-8a7c-a159651bbf17}">
			<Type>AuditDenied</Type>
			<AccessMask>63</AccessMask>
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
<summary>Add a row for Deny access to all non-approved devices</summary>  
   
   1. Click "Add"
   2. For Name, enter *Deny access to all non-approved devices*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B7458f924-0925-4a0f-8c2c-fb50b0c3350c%7D/RuleData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  */workspaces/mdatp-devicecontrol/deployable examples/removable_media/windows/devicecontrol/rules/Deny access to all non-approved devices.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for All Removable Media Devices</summary>  
   
   1. Click "Add"
   2. For Name, enter *All Removable Media Devices*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Be2461b64-bc0b-4d85-8cb8-424cabe97f55%7D/GroupData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  */workspaces/mdatp-devicecontrol/deployable examples/removable_media/windows/devicecontrol/groups/All Removable Media Devices.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for Allowed USBs</summary>  
   
   1. Click "Add"
   2. For Name, enter *Allowed USBs*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B00b72954-e837-4523-8186-ad7cb4075584%7D/GroupData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  */workspaces/mdatp-devicecontrol/deployable examples/removable_media/windows/devicecontrol/groups/Allowed USBs.xml*
         
   
   7. Click "Save"
</details>



