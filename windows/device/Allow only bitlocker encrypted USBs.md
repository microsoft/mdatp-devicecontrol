# Device control policy sample: Allow only bitlocker encrypted USBs

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
            <td rowspan="2" valign="top"><b>Allow Only Bitlocker Encrypted USBs</b></td>
            <td rowspan="2 valign="top">
                <ul><li>Group: bitlocker encrypted USBs_0<a href="#bitlocker-encrypted-usbs_0" title="MatchAll {'PrimaryId': 'RemovableMediaDevices', 'DeviceEncryptionStateId': 'BitlockerEncrypted'}"> (details)</a>  
</ul>
            </td>
            <td rowspan="2" valign="top">
                <ul><li>Group: bitlocker unencrypted USBs_0<a href="#bitlocker-unencrypted-usbs_0" title="MatchAll {'PrimaryId': 'RemovableMediaDevices', 'DeviceEncryptionStateId': 'Plain'}"> (details)</a>  
</ul>
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


### bitlocker encrypted USBs_0



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
	<Name>bitlocker encrypted USBs_0</Name>
	<MatchType>MatchAll</MatchType>
	<DescriptorIdList>
		<PrimaryId>RemovableMediaDevices</PrimaryId>
		<DeviceEncryptionStateId>BitlockerEncrypted</DeviceEncryptionStateId>
	</DescriptorIdList>
</Group>
```
</details>

### bitlocker unencrypted USBs_0



This is a group of type *Device*. 
The match type for the group is *MatchAll*.


|  Property | Value |
|-----------|-------|
| PrimaryId | RemovableMediaDevices |
| DeviceEncryptionStateId | Plain |





<details>
<summary>View XML</summary>

```xml
<Group Id="{3ed80052-0861-4a8e-bab0-3e185820ee2e}" Type="Device">
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B3ed80052-0861-4a8e-bab0-3e185820ee2e%7D/GroupData -->
	<Name>bitlocker unencrypted USBs_0</Name>
	<MatchType>MatchAll</MatchType>
	<DescriptorIdList>
		<PrimaryId>RemovableMediaDevices</PrimaryId>
		<DeviceEncryptionStateId>Plain</DeviceEncryptionStateId>
	</DescriptorIdList>
</Group>
```
</details>


## Settings
| Setting Name |  Setting Value | Documentation |
|--------------|----------------|---------------|
DeviceControlEnabled | True | [documentation](https://learn.microsoft.com/en-us/windows/client-management/mdm/defender-csp#configurationdevicecontrolenabled) |
DefaultEnforcement | Deny | [documentation](https://learn.microsoft.com/en-us/windows/client-management/mdm/defender-csp#configurationdefaultenforcement) |
SecuredDevicesConfiguration | RemovableMediaDevices | [documentation](https://learn.microsoft.com/en-us/windows/client-management/mdm/defender-csp#configurationsecureddevicesconfiguration) |


## Files
This policy is based on information in the following files:

- [windows/device/Intune OMA-URI/bitlocker encrypted USBs.xml](/windows/device/Intune%20OMA-URI/bitlocker%20encrypted%20USBs.xml)
- [windows/device/Intune OMA-URI/bitlocker unencrypted USBs.xml](/windows/device/Intune%20OMA-URI/bitlocker%20unencrypted%20USBs.xml)
- [windows/device/Intune OMA-URI/Allow only bitlocker encrypted USBs.xml](/windows/device/Intune%20OMA-URI/Allow%20only%20bitlocker%20encrypted%20USBs.xml)


# Deployment Instructions

Device control [policy rules](#policy-rules) and [groups](#groups) can be deployed through the following management tools:


## Windows
- [Intune UX](#intune-ux)
- [Intune Custom Settings](#intune-custom-settings)
- [Group Policy (GPO)](#group-policy-gpo)





## Intune UX

Intune UX is not supported for this policy because:
- File Read (8) is an unsupported access mask
- File Execute (32) is an unsupported access mask
- File Write (16) is an unsupported access mask

Use [Intune custom settings](#intune-custom-settings) to deploy the policy instead.


## Group Policy (GPO)
<details>
<summary>Define device control policy groups</summary>

   1. Go to Computer Configuration > Administrative Templates > Windows Components > Microsoft Defender Antivirus > Device Control > Define device control policy groups.
   2. Save the XML below to a network share.
```xml
<Groups>
	<Group Id="{33e06f08-8787-4219-9dca-5872854f9d79}" Type="Device">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B33e06f08-8787-4219-9dca-5872854f9d79%7D/GroupData -->
		<Name>bitlocker encrypted USBs_0</Name>
		<MatchType>MatchAll</MatchType>
		<DescriptorIdList>
			<PrimaryId>RemovableMediaDevices</PrimaryId>
			<DeviceEncryptionStateId>BitlockerEncrypted</DeviceEncryptionStateId>
		</DescriptorIdList>
	</Group>
	<Group Id="{3ed80052-0861-4a8e-bab0-3e185820ee2e}" Type="Device">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B3ed80052-0861-4a8e-bab0-3e185820ee2e%7D/GroupData -->
		<Name>bitlocker unencrypted USBs_0</Name>
		<MatchType>MatchAll</MatchType>
		<DescriptorIdList>
			<PrimaryId>RemovableMediaDevices</PrimaryId>
			<DeviceEncryptionStateId>Plain</DeviceEncryptionStateId>
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
	<PolicyRule Id="{2da643ac-fdfe-4764-802b-adeed59c32b9}" >
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B2da643ac-fdfe-4764-802b-adeed59c32b9%7D/RuleData -->
		<Name>Allow Only Bitlocker Encrypted USBs</Name>
		<IncludedIdList>
			<GroupId>{33e06f08-8787-4219-9dca-5872854f9d79}</GroupId>
		</IncludedIdList>
		<ExcludedIdList>
			<GroupId>{3ed80052-0861-4a8e-bab0-3e185820ee2e}</GroupId>
		</ExcludedIdList>
		<Entry Id="{66fd76ff-4233-4534-bded-f7ba13fd3011}">
			<Type>Allow</Type>
			<AccessMask>63</AccessMask>
			<Options>0</Options>
		</Entry>
		<Entry Id="{4f9737f9-7fc7-44fe-8b55-3f3cb3240f3c}">
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
<summary>Add a row for Allow Only Bitlocker Encrypted USBs</summary>  
   
   1. Click "Add"
   2. For Name, enter *Allow Only Bitlocker Encrypted USBs*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B2da643ac-fdfe-4764-802b-adeed59c32b9%7D/RuleData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  *windows\device\Intune OMA-URI\Allow only bitlocker encrypted USBs.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for bitlocker encrypted USBs_0</summary>  
   
   1. Click "Add"
   2. For Name, enter *bitlocker encrypted USBs_0*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B33e06f08-8787-4219-9dca-5872854f9d79%7D/GroupData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  *windows\device\Intune OMA-URI\bitlocker encrypted USBs.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for bitlocker unencrypted USBs_0</summary>  
   
   1. Click "Add"
   2. For Name, enter *bitlocker unencrypted USBs_0*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B3ed80052-0861-4a8e-bab0-3e185820ee2e%7D/GroupData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  *windows\device\Intune OMA-URI\bitlocker unencrypted USBs.xml*
         
   
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
   
   7. For Value, enter *2*
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for SecuredDevicesConfiguration</summary>  
   
   1. Click "Add"
   2. For Name, enter *SecuredDevicesConfiguration*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/SecuredDevicesConfiguration*
   5. For Data type, select *String*
   
   7. For Value, enter *RemovableMediaDevices*
   
   7. Click "Save"
</details>



