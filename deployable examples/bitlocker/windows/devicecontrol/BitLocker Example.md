# Device control policy sample: BitLocker Example

Description: A policy              
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
        </tr><tr>
            <td rowspan="2" valign="top"><b>Allow unencrypted removable media devices with an exception full access</b></td>
            <td rowspan="2 valign="top">
                <ul><li>Group: Full Access Exception<a href="#full-access-exception" title="MatchAny {'SerialNumberId': '6EA9150055800605'}"> (details)</a>  
</ul>
            </td>
            <td rowspan="2" valign="top">
                <ul></ul>
            </td>
            <td>Allow</td>
            <td>:white_check_mark:</td>
            <td>:white_check_mark:</td>
            <td>:white_check_mark:</td>
            <td>:white_check_mark:</td>
            <td>:white_check_mark:</td>
            <td>:white_check_mark:</td>
            <td>None (0)</td> 
            <td>
                <center>-</center></td>
        </tr><tr>
            <td>Audit Allowed</td>
            <td>-</td>
            <td>:page_facing_up:</td>
            <td>-</td>
            <td>-</td>
            <td>:page_facing_up:</td>
            <td>-</td>
            <td>Send event (2)</td>
            <td> 
                <center>-</center></td>
        </tr><tr>
            <td rowspan="2" valign="top"><b>Allow BitLocker encrypted removable media devices full access</b></td>
            <td rowspan="2 valign="top">
                <ul><li>Group: BitLocker Encrypted<a href="#bitlocker-encrypted" title="MatchAny {'DeviceEncryptionStateId': 'BitlockerEncrypted'}"> (details)</a>  
</ul>
            </td>
            <td rowspan="2" valign="top">
                <ul></ul>
            </td>
            <td>Allow</td>
            <td>:white_check_mark:</td>
            <td>:white_check_mark:</td>
            <td>:white_check_mark:</td>
            <td>:white_check_mark:</td>
            <td>:white_check_mark:</td>
            <td>:white_check_mark:</td>
            <td>None (0)</td> 
            <td>
                <center>-</center></td>
        </tr><tr>
            <td>Audit Allowed</td>
            <td>-</td>
            <td>:page_facing_up:</td>
            <td>-</td>
            <td>-</td>
            <td>:page_facing_up:</td>
            <td>-</td>
            <td>Send event (2)</td>
            <td> 
                <center>-</center></td>
        </tr></table>


## Groups


### Full Access Exception



This is a group of type *Device*. 
The match type for the group is *MatchAny*.


|  Property | Value |
|-----------|-------|
| SerialNumberId | 6EA9150055800605 |





<details>
<summary>View XML</summary>

```xml
<Group Id="{f1649cbf-717d-465f-9e6a-f75022b84f22}" Type="Device">
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Bf1649cbf-717d-465f-9e6a-f75022b84f22%7D/GroupData -->
	<Name>Full Access Exception</Name>
	<MatchType>MatchAny</MatchType>
	<DescriptorIdList>
		<SerialNumberId>6EA9150055800605</SerialNumberId>
	</DescriptorIdList>
</Group>
```
</details>

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
<Group Id="{34e4eaa3-6be5-4a94-8e38-7c8c86df94bf}" Type="Device">
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B34e4eaa3-6be5-4a94-8e38-7c8c86df94bf%7D/GroupData -->
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

### BitLocker Encrypted



This is a group of type *Device*. 
The match type for the group is *MatchAny*.


|  Property | Value |
|-----------|-------|
| DeviceEncryptionStateId | BitlockerEncrypted |





<details>
<summary>View XML</summary>

```xml
<Group Id="{c8525cba-62f3-477c-9d13-3c3a18ab1d1a}" Type="Device">
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Bc8525cba-62f3-477c-9d13-3c3a18ab1d1a%7D/GroupData -->
	<Name>BitLocker Encrypted</Name>
	<MatchType>MatchAny</MatchType>
	<DescriptorIdList>
		<DeviceEncryptionStateId>BitlockerEncrypted</DeviceEncryptionStateId>
	</DescriptorIdList>
</Group>
```
</details>


## Settings






| Setting Name |  Setting Value | Description |Documentation |
|--------------|----------------|-------------|---------------|


## Files
This policy is based on information in the following files:

- [groups/All Devices.xml](groups/All%20Devices.xml)
- [rules/Allow unencrypted removable media devices with an exception full access.xml](rules/Allow%20unencrypted%20removable%20media%20devices%20with%20an%20exception%20full%20access.xml)
- [rules/Allow unencrypted removable media devices read access only.xml](rules/Allow%20unencrypted%20removable%20media%20devices%20read%20access%20only.xml)
- [groups/Full Access Exception.xml](groups/Full%20Access%20Exception.xml)
- [rules/Allow BitLocker encrypted removable media devices full access.xml](rules/Allow%20BitLocker%20encrypted%20removable%20media%20devices%20full%20access.xml)
- [groups/BitLocker Encrypted.xml](groups/BitLocker%20Encrypted.xml)


# Deployment Instructions

Device control [policy rules](#policy-rules) and [groups](#groups) can be deployed through the following management tools:


## Windows
- [Intune UX](#intune-ux)
- [Intune Custom Settings](#intune-custom-settings)
- [Group Policy (GPO)](#group-policy-gpo)





## Intune UX

Intune UX is not supported for this policy because:
- File Execute (32) is an unsupported access mask
- DeviceEncryptionStateId not supported
- File Write (16) is an unsupported access mask
- File Read (8) is an unsupported access mask

Use [Intune custom settings](#intune-custom-settings) to deploy the policy instead.


## Group Policy (GPO)
<details>
<summary>Define device control policy groups</summary>

   1. Go to Computer Configuration > Administrative Templates > Windows Components > Microsoft Defender Antivirus > Device Control > Define device control policy groups.
   2. Save the XML below to a network share.
```xml
<Groups>
	<Group Id="{f1649cbf-717d-465f-9e6a-f75022b84f22}" Type="Device">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Bf1649cbf-717d-465f-9e6a-f75022b84f22%7D/GroupData -->
		<Name>Full Access Exception</Name>
		<MatchType>MatchAny</MatchType>
		<DescriptorIdList>
			<SerialNumberId>6EA9150055800605</SerialNumberId>
		</DescriptorIdList>
	</Group>
	<Group Id="{34e4eaa3-6be5-4a94-8e38-7c8c86df94bf}" Type="Device">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B34e4eaa3-6be5-4a94-8e38-7c8c86df94bf%7D/GroupData -->
		<Name>All Devices</Name>
		<MatchType>MatchAny</MatchType>
		<DescriptorIdList>
			<PrimaryId>RemovableMediaDevices</PrimaryId>
			<PrimaryId>CdRomDevices</PrimaryId>
			<PrimaryId>WpdDevices</PrimaryId>
			<PrimaryId>PrinterDevices</PrimaryId>
		</DescriptorIdList>
	</Group>
	<Group Id="{c8525cba-62f3-477c-9d13-3c3a18ab1d1a}" Type="Device">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Bc8525cba-62f3-477c-9d13-3c3a18ab1d1a%7D/GroupData -->
		<Name>BitLocker Encrypted</Name>
		<MatchType>MatchAny</MatchType>
		<DescriptorIdList>
			<DeviceEncryptionStateId>BitlockerEncrypted</DeviceEncryptionStateId>
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
	<PolicyRule Id="{c30e715b-fb8e-4c81-b4c2-bed294421002}" >
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7Bc30e715b-fb8e-4c81-b4c2-bed294421002%7D/RuleData -->
		<Name>Allow unencrypted removable media devices read access only</Name>
		<IncludedIdList>
			<GroupId>{34e4eaa3-6be5-4a94-8e38-7c8c86df94bf}</GroupId>
		</IncludedIdList>
		<ExcludedIdList>
			<GroupId>{f1649cbf-717d-465f-9e6a-f75022b84f22}</GroupId>
		</ExcludedIdList>
		<Entry Id="{271a0529-43ee-459a-921e-b66cd804996b}">
			<Type>Allow</Type>
			<AccessMask>9</AccessMask>
			<Options>0</Options>
		</Entry>
		<Entry Id="{cf1f4b37-adc4-4b32-a4b1-4d801a979e12}">
			<Type>Deny</Type>
			<AccessMask>54</AccessMask>
			<Options>0</Options>
		</Entry>
		<Entry Id="{af76762d-3734-43eb-a196-1f1b637a7472}">
			<Type>AuditDenied</Type>
			<AccessMask>54</AccessMask>
			<Options>3</Options>
		</Entry>
	</PolicyRule>
	<PolicyRule Id="{ca89fd62-c273-49fb-8298-9af6fc6eddf9}" >
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7Bca89fd62-c273-49fb-8298-9af6fc6eddf9%7D/RuleData -->
		<Name>Allow unencrypted removable media devices with an exception full access</Name>
		<IncludedIdList>
			<GroupId>{f1649cbf-717d-465f-9e6a-f75022b84f22}</GroupId>
		</IncludedIdList>
		<ExcludedIdList>
		</ExcludedIdList>
		<Entry Id="{ff991397-8757-469f-b478-9b07c8854a91}">
			<Type>Allow</Type>
			<AccessMask>63</AccessMask>
			<Options>0</Options>
		</Entry>
		<Entry Id="{adee8cf8-a06f-4022-b707-388f4d9dacb4}">
			<Type>AuditAllowed</Type>
			<AccessMask>18</AccessMask>
			<Options>2</Options>
		</Entry>
	</PolicyRule>
	<PolicyRule Id="{1b9c099d-17df-45b3-a5c3-305e381b4d6f}" >
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B1b9c099d-17df-45b3-a5c3-305e381b4d6f%7D/RuleData -->
		<Name>Allow BitLocker encrypted removable media devices full access</Name>
		<IncludedIdList>
			<GroupId>{c8525cba-62f3-477c-9d13-3c3a18ab1d1a}</GroupId>
		</IncludedIdList>
		<ExcludedIdList>
		</ExcludedIdList>
		<Entry Id="{7a6eb836-aa54-4e85-bacb-50e7f8097d10}">
			<Type>Allow</Type>
			<AccessMask>63</AccessMask>
			<Options>0</Options>
		</Entry>
		<Entry Id="{e3ad138e-1619-49a9-b009-62fb0b31e9e7}">
			<Type>AuditAllowed</Type>
			<AccessMask>18</AccessMask>
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
<summary>Add a row for Allow BitLocker encrypted removable media devices full access</summary>  
   
   1. Click "Add"
   2. For Name, enter *Allow BitLocker encrypted removable media devices full access*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B1b9c099d-17df-45b3-a5c3-305e381b4d6f%7D/RuleData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  */workspaces/mdatp-devicecontrol/deployable examples/bitlocker/windows/devicecontrol/rules/Allow BitLocker encrypted removable media devices full access.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for Allow unencrypted removable media devices with an exception full access</summary>  
   
   1. Click "Add"
   2. For Name, enter *Allow unencrypted removable media devices with an exception full access*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7Bca89fd62-c273-49fb-8298-9af6fc6eddf9%7D/RuleData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  */workspaces/mdatp-devicecontrol/deployable examples/bitlocker/windows/devicecontrol/rules/Allow unencrypted removable media devices with an exception full access.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for Allow unencrypted removable media devices read access only</summary>  
   
   1. Click "Add"
   2. For Name, enter *Allow unencrypted removable media devices read access only*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7Bc30e715b-fb8e-4c81-b4c2-bed294421002%7D/RuleData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  */workspaces/mdatp-devicecontrol/deployable examples/bitlocker/windows/devicecontrol/rules/Allow unencrypted removable media devices read access only.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for All Devices</summary>  
   
   1. Click "Add"
   2. For Name, enter *All Devices*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B34e4eaa3-6be5-4a94-8e38-7c8c86df94bf%7D/GroupData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  */workspaces/mdatp-devicecontrol/deployable examples/bitlocker/windows/devicecontrol/groups/All Devices.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for Full Access Exception</summary>  
   
   1. Click "Add"
   2. For Name, enter *Full Access Exception*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Bf1649cbf-717d-465f-9e6a-f75022b84f22%7D/GroupData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  */workspaces/mdatp-devicecontrol/deployable examples/bitlocker/windows/devicecontrol/groups/Full Access Exception.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for BitLocker Encrypted</summary>  
   
   1. Click "Add"
   2. For Name, enter *BitLocker Encrypted*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Bc8525cba-62f3-477c-9d13-3c3a18ab1d1a%7D/GroupData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  */workspaces/mdatp-devicecontrol/deployable examples/bitlocker/windows/devicecontrol/groups/BitLocker Encrypted.xml*
         
   
   7. Click "Save"
</details>



