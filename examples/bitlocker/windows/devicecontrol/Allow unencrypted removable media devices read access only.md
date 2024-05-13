# Device control policy sample: Allow unencrypted removable media devices read access only

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
            <td rowspan="3" valign="top"><b>Allow unencrypted removable media devices read access only</b></td>
            <td rowspan="3 valign="top">
                <ul><li>Group: All Devices<a href="#all-devices" title="MatchAny {'PrimaryId': 'PrinterDevices'}"> (details)</a>  
</ul>
            </td>
            <td rowspan="3" valign="top">
                <ul><li>Group: Full Access Exception<a href="#full-access-exception" title="MatchAny {'SerialNumberId': '6EA9150055800605'}"> (details)</a>  
</ul>
            </td>
            <td>Allow</td>
            <td>:white_check_mark:</td>
            <td>-</td>
            <td>-</td>
            <td>:white_check_mark:</td>
            <td>-</td>
            <td>-</td>
            <td>None (0)</td> 
            <td>
                <center>-</center></td>
        </tr><tr>
            <td>Deny</td>
            <td>-</td>
            <td>:x:</td>
            <td>:x:</td>
            <td>-</td>
            <td>:x:</td>
            <td>:x:</td>
            <td>None (0)</td>
            <td> 
                <center>-</center></td>
        </tr><tr>
            <td>Audit Denied</td>
            <td>-</td>
            <td>:page_facing_up:</td>
            <td>:page_facing_up:</td>
            <td>-</td>
            <td>:page_facing_up:</td>
            <td>:page_facing_up:</td>
            <td>Show notification and Send event (3)</td>
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
<Group Id="{d817ae9e-ce99-468d-a145-2527c7b166cd}" Type="Device">
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Bd817ae9e-ce99-468d-a145-2527c7b166cd%7D/GroupData -->
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

### Full Access Exception



This is a group of type *Device*. 
The match type for the group is *MatchAny*.


|  Property | Value |
|-----------|-------|
| SerialNumberId | 6EA9150055800605 |





<details>
<summary>View XML</summary>

```xml
<Group Id="{ecc0323b-9c95-4d2a-9a68-2abb3a07b4bc}" Type="Device">
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Becc0323b-9c95-4d2a-9a68-2abb3a07b4bc%7D/GroupData -->
	<Name>Full Access Exception</Name>
	<MatchType>MatchAny</MatchType>
	<DescriptorIdList>
		<SerialNumberId>6EA9150055800605</SerialNumberId>
	</DescriptorIdList>
</Group>
```
</details>


## Settings






| Setting Name |  Setting Value | Description |Documentation |
|--------------|----------------|-------------|---------------|


## Files
This policy is based on information in the following files:

- [groups/Full Access Exception.xml](groups/Full%20Access%20Exception.xml)
- [rules/Allow unencrypted removable media devices read access only.xml](rules/Allow%20unencrypted%20removable%20media%20devices%20read%20access%20only.xml)
- [groups/All Devices.xml](groups/All%20Devices.xml)


# Deployment Instructions

Device control [policy rules](#policy-rules) and [groups](#groups) can be deployed through the following management tools:


## Windows
- [Intune UX](#intune-ux)
- [Intune Custom Settings](#intune-custom-settings)
- [Group Policy (GPO)](#group-policy-gpo)





## Intune UX

Intune UX is not supported for this policy because:
- File Read (8) is an unsupported access mask
- File Write (16) is an unsupported access mask
- File Execute (32) is an unsupported access mask

Use [Intune custom settings](#intune-custom-settings) to deploy the policy instead.


## Group Policy (GPO)
<details>
<summary>Define device control policy groups</summary>

   1. Go to Computer Configuration > Administrative Templates > Windows Components > Microsoft Defender Antivirus > Device Control > Define device control policy groups.
   2. Save the XML below to a network share.
```xml
<Groups>
	<Group Id="{d817ae9e-ce99-468d-a145-2527c7b166cd}" Type="Device">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Bd817ae9e-ce99-468d-a145-2527c7b166cd%7D/GroupData -->
		<Name>All Devices</Name>
		<MatchType>MatchAny</MatchType>
		<DescriptorIdList>
			<PrimaryId>RemovableMediaDevices</PrimaryId>
			<PrimaryId>CdRomDevices</PrimaryId>
			<PrimaryId>WpdDevices</PrimaryId>
			<PrimaryId>PrinterDevices</PrimaryId>
		</DescriptorIdList>
	</Group>
	<Group Id="{ecc0323b-9c95-4d2a-9a68-2abb3a07b4bc}" Type="Device">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Becc0323b-9c95-4d2a-9a68-2abb3a07b4bc%7D/GroupData -->
		<Name>Full Access Exception</Name>
		<MatchType>MatchAny</MatchType>
		<DescriptorIdList>
			<SerialNumberId>6EA9150055800605</SerialNumberId>
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
	<PolicyRule Id="{b5ed42d8-4ac3-4dc8-8771-cef0891e15ab}" >
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7Bb5ed42d8-4ac3-4dc8-8771-cef0891e15ab%7D/RuleData -->
		<Name>Allow unencrypted removable media devices read access only</Name>
		<IncludedIdList>
			<GroupId>{d817ae9e-ce99-468d-a145-2527c7b166cd}</GroupId>
		</IncludedIdList>
		<ExcludedIdList>
			<GroupId>{ecc0323b-9c95-4d2a-9a68-2abb3a07b4bc}</GroupId>
		</ExcludedIdList>
		<Entry Id="{f1d41e5d-f3ed-4fda-8454-60343ef45004}">
			<Type>Allow</Type>
			<AccessMask>9</AccessMask>
			<Options>0</Options>
		</Entry>
		<Entry Id="{12138964-0efb-424f-994c-3f3c17b168ab}">
			<Type>Deny</Type>
			<AccessMask>54</AccessMask>
			<Options>0</Options>
		</Entry>
		<Entry Id="{d346f712-fc3d-4184-ba9c-b40512054887}">
			<Type>AuditDenied</Type>
			<AccessMask>54</AccessMask>
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
<summary>Add a row for Allow unencrypted removable media devices read access only</summary>  
   
   1. Click "Add"
   2. For Name, enter *Allow unencrypted removable media devices read access only*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7Bb5ed42d8-4ac3-4dc8-8771-cef0891e15ab%7D/RuleData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  */workspaces/mdatp-devicecontrol/examples/bitlocker/windows/devicecontrol/rules/Allow unencrypted removable media devices read access only.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for All Devices</summary>  
   
   1. Click "Add"
   2. For Name, enter *All Devices*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Bd817ae9e-ce99-468d-a145-2527c7b166cd%7D/GroupData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  */workspaces/mdatp-devicecontrol/examples/bitlocker/windows/devicecontrol/groups/All Devices.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for Full Access Exception</summary>  
   
   1. Click "Add"
   2. For Name, enter *Full Access Exception*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Becc0323b-9c95-4d2a-9a68-2abb3a07b4bc%7D/GroupData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  */workspaces/mdatp-devicecontrol/examples/bitlocker/windows/devicecontrol/groups/Full Access Exception.xml*
         
   
   7. Click "Save"
</details>



