# Device control policy sample: Require BitLocker Encryption to Write with Exceptions

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
                <ul><li>Group: Any Removable Media<a href="#any-removable-media" title="MatchAny {'PrimaryId': 'RemovableMediaDevices'}"> (details)</a>  
</ul>
            </td>
            <td rowspan="3" valign="top">
                <ul><li>Group: bitlocker encrypted USBs<a href="#bitlocker-encrypted-usbs" title="MatchAll {'PrimaryId': 'RemovableMediaDevices', 'DeviceEncryptionStateId': 'BitlockerEncrypted'}"> (details)</a>  
<li>Group: allowed bitlocker unencrypted USBs<a href="#allowed-bitlocker-unencrypted-usbs" title="MatchAll {'PrimaryId': 'RemovableMediaDevices', 'DeviceEncryptionStateId': 'Plain', 'SerialNumberId': 'FBH1111183400787'}"> (details)</a>  
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
                <ul><li>Group: allowed bitlocker unencrypted USBs<a href="#allowed-bitlocker-unencrypted-usbs" title="MatchAll {'PrimaryId': 'RemovableMediaDevices', 'DeviceEncryptionStateId': 'Plain', 'SerialNumberId': 'FBH1111183400787'}"> (details)</a>  
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
                <ul><li>Group: bitlocker encrypted USBs<a href="#bitlocker-encrypted-usbs" title="MatchAll {'PrimaryId': 'RemovableMediaDevices', 'DeviceEncryptionStateId': 'BitlockerEncrypted'}"> (details)</a>  
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


### allowed bitlocker unencrypted USBs



This is a group of type *Device*. 
The match type for the group is *MatchAll*.


|  Property | Value |
|-----------|-------|
| PrimaryId | RemovableMediaDevices |
| DeviceEncryptionStateId | Plain |
| SerialNumberId | FBH1111183400787 |





<details>
<summary>View XML</summary>

```xml
<Group Id="{36e10524-d902-4097-8491-95aa24bd0221}" Type="Device">
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B36e10524-d902-4097-8491-95aa24bd0221%7D/GroupData -->
	<Name>allowed bitlocker unencrypted USBs</Name>
	<MatchType>MatchAll</MatchType>
	<DescriptorIdList>
		<PrimaryId>RemovableMediaDevices</PrimaryId>
		<DeviceEncryptionStateId>Plain</DeviceEncryptionStateId>
		<SerialNumberId>FBH1111183400787</SerialNumberId>
	</DescriptorIdList>
</Group>
```
</details>

### Any Removable Media



This is a group of type *Device*. 
The match type for the group is *MatchAny*.


|  Property | Value |
|-----------|-------|
| PrimaryId | RemovableMediaDevices |





<details>
<summary>View XML</summary>

```xml
<Group Id="{bdfbd64c-8586-4eb8-ae11-2f839e019532}" Type="Device">
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Bbdfbd64c-8586-4eb8-ae11-2f839e019532%7D/GroupData -->
	<Name>Any Removable Media</Name>
	<MatchType>MatchAny</MatchType>
	<DescriptorIdList>
		<PrimaryId>RemovableMediaDevices</PrimaryId>
	</DescriptorIdList>
</Group>
```
</details>

### bitlocker encrypted USBs



This is a group of type *Device*. 
The match type for the group is *MatchAll*.


|  Property | Value |
|-----------|-------|
| PrimaryId | RemovableMediaDevices |
| DeviceEncryptionStateId | BitlockerEncrypted |





<details>
<summary>View XML</summary>

```xml
<Group Id="{33e06f08-8787-4219-9dca-5872854f9d79}" Type="Device">
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B33e06f08-8787-4219-9dca-5872854f9d79%7D/GroupData -->
	<Name>bitlocker encrypted USBs</Name>
	<MatchType>MatchAll</MatchType>
	<DescriptorIdList>
		<PrimaryId>RemovableMediaDevices</PrimaryId>
		<DeviceEncryptionStateId>BitlockerEncrypted</DeviceEncryptionStateId>
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

- [Group Policy/example_1_groups.xml](Group%20Policy/example_1_groups.xml)
- [Intune OMA-URI/bitlocker_encrypted_usbs{33e06f08-8787-4219-9dca-5872854f9d79}.xml](Intune%20OMA-URI/bitlocker_encrypted_usbs%7B33e06f08-8787-4219-9dca-5872854f9d79%7D.xml)
- [Intune OMA-URI/any_removable_media{bdfbd64c-8586-4eb8-ae11-2f839e019532}.xml](Intune%20OMA-URI/any_removable_media%7Bbdfbd64c-8586-4eb8-ae11-2f839e019532%7D.xml)
- [Group Policy/example_1_rules.xml](Group%20Policy/example_1_rules.xml)


# Deployment Instructions

Device control [policy rules](#policy-rules) and [groups](#groups) can be deployed through the following management tools:


## Windows
- [Intune UX](#intune-ux)
- [Intune Custom Settings](#intune-custom-settings)
- [Group Policy (GPO)](#group-policy-gpo)





## Intune UX

Intune UX is not supported for this policy because:
- File Execute (32) is an unsupported access mask
- File Read (8) is an unsupported access mask
- File Write (16) is an unsupported access mask

Use [Intune custom settings](#intune-custom-settings) to deploy the policy instead.


## Group Policy (GPO)
<details>
<summary>Define device control policy groups</summary>

   1. Go to Computer Configuration > Administrative Templates > Windows Components > Microsoft Defender Antivirus > Device Control > Define device control policy groups.
   2. Save the XML below to a network share.
```xml
<Groups>
	<Group Id="{36e10524-d902-4097-8491-95aa24bd0221}" Type="Device">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B36e10524-d902-4097-8491-95aa24bd0221%7D/GroupData -->
		<Name>allowed bitlocker unencrypted USBs</Name>
		<MatchType>MatchAll</MatchType>
		<DescriptorIdList>
			<PrimaryId>RemovableMediaDevices</PrimaryId>
			<DeviceEncryptionStateId>Plain</DeviceEncryptionStateId>
			<SerialNumberId>FBH1111183400787</SerialNumberId>
		</DescriptorIdList>
	</Group>
	<Group Id="{bdfbd64c-8586-4eb8-ae11-2f839e019532}" Type="Device">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Bbdfbd64c-8586-4eb8-ae11-2f839e019532%7D/GroupData -->
		<Name>Any Removable Media</Name>
		<MatchType>MatchAny</MatchType>
		<DescriptorIdList>
			<PrimaryId>RemovableMediaDevices</PrimaryId>
		</DescriptorIdList>
	</Group>
	<Group Id="{33e06f08-8787-4219-9dca-5872854f9d79}" Type="Device">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B33e06f08-8787-4219-9dca-5872854f9d79%7D/GroupData -->
		<Name>bitlocker encrypted USBs</Name>
		<MatchType>MatchAll</MatchType>
		<DescriptorIdList>
			<PrimaryId>RemovableMediaDevices</PrimaryId>
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
	<PolicyRule Id="{783b7807-4516-41cb-b5ad-b460f91629fe}" >
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B783b7807-4516-41cb-b5ad-b460f91629fe%7D/RuleData -->
		<Name>Allow unencrypted removable media devices read access only</Name>
		<IncludedIdList>
			<GroupId>{bdfbd64c-8586-4eb8-ae11-2f839e019532}</GroupId>
		</IncludedIdList>
		<ExcludedIdList>
			<GroupId>{33e06f08-8787-4219-9dca-5872854f9d79}</GroupId>
			<GroupId>{36e10524-d902-4097-8491-95aa24bd0221}</GroupId>
		</ExcludedIdList>
		<Entry Id="{b55414c8-b850-47a8-b3fa-4cd28ec45df0}">
			<Type>Allow</Type>
			<AccessMask>9</AccessMask>
			<Options>0</Options>
		</Entry>
		<Entry Id="{7b4c10fa-ecdf-4889-b8c1-569ec36f9673}">
			<Type>Deny</Type>
			<AccessMask>54</AccessMask>
			<Options>0</Options>
		</Entry>
		<Entry Id="{089fa13c-8e93-4b64-a53f-8ed8f882e63d}">
			<Type>AuditDenied</Type>
			<AccessMask>54</AccessMask>
			<Options>3</Options>
		</Entry>
	</PolicyRule>
	<PolicyRule Id="{f98c7d59-4165-4817-a01b-4685ed089912}" >
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7Bf98c7d59-4165-4817-a01b-4685ed089912%7D/RuleData -->
		<Name>Allow unencrypted removable media devices with an exception full access</Name>
		<IncludedIdList>
			<GroupId>{36e10524-d902-4097-8491-95aa24bd0221}</GroupId>
		</IncludedIdList>
		<ExcludedIdList>
		</ExcludedIdList>
		<Entry Id="{467726b6-a548-4f09-80d0-e8a0efc90bce}">
			<Type>Allow</Type>
			<AccessMask>63</AccessMask>
			<Options>0</Options>
		</Entry>
		<Entry Id="{b8f94674-7bab-46e1-968e-4deee14323bb}">
			<Type>AuditAllowed</Type>
			<AccessMask>18</AccessMask>
			<Options>2</Options>
		</Entry>
	</PolicyRule>
	<PolicyRule Id="{7583e1fa-8e54-4858-8b9b-73f62e6e7fae}" >
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B7583e1fa-8e54-4858-8b9b-73f62e6e7fae%7D/RuleData -->
		<Name>Allow BitLocker encrypted removable media devices full access</Name>
		<IncludedIdList>
			<GroupId>{33e06f08-8787-4219-9dca-5872854f9d79}</GroupId>
		</IncludedIdList>
		<ExcludedIdList>
		</ExcludedIdList>
		<Entry Id="{5cc20581-f103-469f-9f04-9b8044de1c5d}">
			<Type>Allow</Type>
			<AccessMask>63</AccessMask>
			<Options>0</Options>
		</Entry>
		<Entry Id="{72deb164-87e4-4f95-a49f-2ed9f2265f54}">
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
<summary>Add a row for Allow unencrypted removable media devices read access only</summary>  
   
   1. Click "Add"
   2. For Name, enter *Allow unencrypted removable media devices read access only*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B783b7807-4516-41cb-b5ad-b460f91629fe%7D/RuleData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  *Intune OMA-URI/allow_unencrypted_removable_media_devices_read_access_only{783b7807-4516-41cb-b5ad-b460f91629fe}.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for Allow unencrypted removable media devices with an exception full access</summary>  
   
   1. Click "Add"
   2. For Name, enter *Allow unencrypted removable media devices with an exception full access*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7Bf98c7d59-4165-4817-a01b-4685ed089912%7D/RuleData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  *Intune OMA-URI/allow_unencrypted_removable_media_devices_with_an_exception_full_access{f98c7d59-4165-4817-a01b-4685ed089912}.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for Allow BitLocker encrypted removable media devices full access</summary>  
   
   1. Click "Add"
   2. For Name, enter *Allow BitLocker encrypted removable media devices full access*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B7583e1fa-8e54-4858-8b9b-73f62e6e7fae%7D/RuleData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  *Intune OMA-URI/allow_bitlocker_encrypted_removable_media_devices_full_access{7583e1fa-8e54-4858-8b9b-73f62e6e7fae}.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for Any Removable Media</summary>  
   
   1. Click "Add"
   2. For Name, enter *Any Removable Media*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Bbdfbd64c-8586-4eb8-ae11-2f839e019532%7D/GroupData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  *Intune OMA-URI/any_removable_media{bdfbd64c-8586-4eb8-ae11-2f839e019532}.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for bitlocker encrypted USBs</summary>  
   
   1. Click "Add"
   2. For Name, enter *bitlocker encrypted USBs*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B33e06f08-8787-4219-9dca-5872854f9d79%7D/GroupData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  *Intune OMA-URI/bitlocker_encrypted_usbs{33e06f08-8787-4219-9dca-5872854f9d79}.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for allowed bitlocker unencrypted USBs</summary>  
   
   1. Click "Add"
   2. For Name, enter *allowed bitlocker unencrypted USBs*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B36e10524-d902-4097-8491-95aa24bd0221%7D/GroupData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  *Intune OMA-URI/allowed_bitlocker_unencrypted_usbs{36e10524-d902-4097-8491-95aa24bd0221}.xml*
         
   
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



