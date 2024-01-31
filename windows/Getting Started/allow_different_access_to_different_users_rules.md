# Device control policy sample: Step 4 - Allow different access to different devices for different users

Description: A sample policy              
Device Type: Windows Removable Device

A device control policy is a combination of [policy rules](#policy-rules), [groups](#groups) and [settings](#settings).  
This sample is based on the [sample files](#files).  
To configure the sample, follow the [deployment instructions](#deployment-instructions).  

## Policy Rules


<table>
    <tr>
        <th rowspan="2" valign="top">Name</th>
        <th colspan="2" valign="top">Devices</th>
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
            <td rowspan="2"><b>Step 4 - Deny all other USBs</b></td>
            <td rowspan="2 valign="top">
                <ul><li>All removable media devices<a href="#all-removable-media-devices" title="MatchAny {'PrimaryId': 'RemovableMediaDevices'}"> (details)</a></ul>
            </td>
            <td rowspan="2" valign="top">.
                <ul><li>Authorized USBs<a href="#authorized-usbs" title="MatchAny {'InstancePathId': 'USB\\VID_154B&PID_0028\\6EA9150055800605'}"> (details)</a><li>Readonly USBs<a href="#readonly-usbs" title="MatchAny {'VID_PID': '090C_1000'}"> (details)</a></ul>
            </td>
            <td>Deny</td>
            <td>:x:</td>
            <td>:x:</td>
            <td>:x:</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>None (0)</td> 
            <td>
                <center>-</center></td>
        </tr><tr>
            <td>Audit Denied</td>
            <td>:page_facing_up:</td>
            <td>:page_facing_up:</td>
            <td>:page_facing_up:</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>Show notification and Send event (3)</td>
            <td> 
                <center>-</center></td>
        </tr><tr>
            <td rowspan="1"><b>Step 4 - Allow Access to Writeable USBs for some users</b></td>
            <td rowspan="1 valign="top">
                <ul><li>Authorized USBs<a href="#authorized-usbs" title="MatchAny {'InstancePathId': 'USB\\VID_154B&PID_0028\\6EA9150055800605'}"> (details)</a></ul>
            </td>
            <td rowspan="1" valign="top">.
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
                <details>
                <summary>View</summary>
                User condition: S-1-1-0<br>
                Parameters: 
                <ul>
                </ul>
                </details></td>
        </tr><tr>
            <td rowspan="1"><b>Step 4 - Allow Read Only Access to Read Only USBs for some users</b></td>
            <td rowspan="1 valign="top">
                <ul><li>Readonly USBs<a href="#readonly-usbs" title="MatchAny {'VID_PID': '090C_1000'}"> (details)</a></ul>
            </td>
            <td rowspan="1" valign="top">.
                <ul></ul>
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
                <details>
                <summary>View</summary>
                User condition: S-1-1-0<br>
                Parameters: 
                <ul>
                </ul>
                </details></td>
        </tr></table>


## Groups


### Readonly USBs



This is a group of type *Device*. 
The match type for the group is *MatchAny*.


|  Property | Value |
|-----------|-------|
| VID_PID | 090C_1000 |





<details>
<summary>View XML</summary>

```xml
<Group Id="{23c24566-98a5-4218-8802-59614513b97e}" Type="Device">
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B23c24566-98a5-4218-8802-59614513b97e%7D/GroupData -->
	<Name>Readonly USBs</Name>
	<MatchType>MatchAny</MatchType>
	<DescriptorIdList>
		<VID_PID>090C_1000</VID_PID>
	</DescriptorIdList>
</Group>
```
</details>

### All removable media devices



This is a group of type *Device*. 
The match type for the group is *MatchAny*.


|  Property | Value |
|-----------|-------|
| PrimaryId | RemovableMediaDevices |





<details>
<summary>View XML</summary>

```xml
<Group Id="{d8819053-24f4-444a-a0fb-9ce5a9e97862}" Type="Device">
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Bd8819053-24f4-444a-a0fb-9ce5a9e97862%7D/GroupData -->
	<Name>All removable media devices</Name>
	<MatchType>MatchAny</MatchType>
	<DescriptorIdList>
		<PrimaryId>RemovableMediaDevices</PrimaryId>
	</DescriptorIdList>
</Group>
```
</details>

### Authorized USBs



This is a group of type *Device*. 
The match type for the group is *MatchAny*.


|  Property | Value |
|-----------|-------|
| InstancePathId | USB\VID_154B&PID_0028\6EA9150055800605 |





<details>
<summary>View XML</summary>

```xml
<Group Id="{368a2c82-17be-4137-bffa-370bbdff9672}" Type="Device">
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B368a2c82-17be-4137-bffa-370bbdff9672%7D/GroupData -->
	<Name>Authorized USBs</Name>
	<MatchType>MatchAny</MatchType>
	<DescriptorIdList>
		<InstancePathId>USB\VID_154B&amp;PID_0028\6EA9150055800605</InstancePathId>
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

- [windows/Getting Started/Intune OMA-URI/all_removable_media_devices{d8819053-24f4-444a-a0fb-9ce5a9e97862}.xml](/windows/Getting%20Started/Intune%20OMA-URI/all_removable_media_devices%7Bd8819053-24f4-444a-a0fb-9ce5a9e97862%7D.xml)
- [windows/Getting Started/Step 2/allow_authorized_usbs_groups.xml](/windows/Getting%20Started/Step%202/allow_authorized_usbs_groups.xml)
- [windows/Getting Started/Step 3/allow_different_access_to_different_groups.xml](/windows/Getting%20Started/Step%203/allow_different_access_to_different_groups.xml)
- [windows/Getting Started/Step 4/allow_different_access_to_different_users_rules.xml](/windows/Getting%20Started/Step%204/allow_different_access_to_different_users_rules.xml)


# Deployment Instructions

Device control [policy rules](#policy-rules) and [groups](#groups) can be deployed through the following management tools:


## Windows
- [Intune UX](#intune-ux)
- [Intune Custom Settings](#intune-custom-settings)
- [Group Policy (GPO)](#group-policy-gpo)





## Intune UX

Intune UX is not supported for this policy because:
- File Write (16) is an unsupported access mask
- File Read (8) is an unsupported access mask
- File Execute (32) is an unsupported access mask

Use [Intune custom settings](#intune-custom-settings) to deploy the policy instead.


## Group Policy (GPO)
<details>
<summary>Define device control policy groups</summary>

   1. Go to Computer Configuration > Administrative Templates > Windows Components > Microsoft Defender Antivirus > Device Control > Define device control policy groups.
   2. Save the XML below to a network share.
```xml
<Groups>
	<Group Id="{23c24566-98a5-4218-8802-59614513b97e}" Type="Device">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B23c24566-98a5-4218-8802-59614513b97e%7D/GroupData -->
		<Name>Readonly USBs</Name>
		<MatchType>MatchAny</MatchType>
		<DescriptorIdList>
			<VID_PID>090C_1000</VID_PID>
		</DescriptorIdList>
	</Group>
	<Group Id="{d8819053-24f4-444a-a0fb-9ce5a9e97862}" Type="Device">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Bd8819053-24f4-444a-a0fb-9ce5a9e97862%7D/GroupData -->
		<Name>All removable media devices</Name>
		<MatchType>MatchAny</MatchType>
		<DescriptorIdList>
			<PrimaryId>RemovableMediaDevices</PrimaryId>
		</DescriptorIdList>
	</Group>
	<Group Id="{368a2c82-17be-4137-bffa-370bbdff9672}" Type="Device">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B368a2c82-17be-4137-bffa-370bbdff9672%7D/GroupData -->
		<Name>Authorized USBs</Name>
		<MatchType>MatchAny</MatchType>
		<DescriptorIdList>
			<InstancePathId>USB\VID_154B&amp;PID_0028\6EA9150055800605</InstancePathId>
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
	<PolicyRule Id="{7beca8fe-313a-46f2-a090-399eb3d74318}" >
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B7beca8fe-313a-46f2-a090-399eb3d74318%7D/RuleData -->
		<Name>Step 4 - Deny all other USBs</Name>
		<IncludedIdList>
			<GroupId>{d8819053-24f4-444a-a0fb-9ce5a9e97862}</GroupId>
		</IncludedIdList>
		<ExcludedIdList>
			<GroupId>{368a2c82-17be-4137-bffa-370bbdff9672}</GroupId>
			<GroupId>{23c24566-98a5-4218-8802-59614513b97e}</GroupId>
		</ExcludedIdList>
		<Entry Id="{c82cb32c-4c56-4c76-8897-b2cc99558299}">
			<Type>Deny</Type>
			<AccessMask>7</AccessMask>
			<Options>0</Options>
		</Entry>
		<Entry Id="{70582e83-ea91-4b14-8f6c-f3921dab9d7a}">
			<Type>AuditDenied</Type>
			<AccessMask>7</AccessMask>
			<Options>3</Options>
		</Entry>
	</PolicyRule>
	<PolicyRule Id="{a054bbcf-3454-4b95-9058-f7ed00deeee9}" >
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7Ba054bbcf-3454-4b95-9058-f7ed00deeee9%7D/RuleData -->
		<Name>Step 4 - Allow Access to Writeable USBs for some users</Name>
		<IncludedIdList>
			<GroupId>{368a2c82-17be-4137-bffa-370bbdff9672}</GroupId>
		</IncludedIdList>
		<ExcludedIdList>
		</ExcludedIdList>
		<Entry Id="{e78857e3-9e36-473b-a07c-fe1a1f356ec9}">
			<Type>Allow</Type>
			<AccessMask>63</AccessMask>
			<Options>0</Options>
			<Sid>S-1-1-0</Sid>
		</Entry>
	</PolicyRule>
	<PolicyRule Id="{b2b9cfc0-799d-457c-babc-da617d9a8b83}" >
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7Bb2b9cfc0-799d-457c-babc-da617d9a8b83%7D/RuleData -->
		<Name>Step 4 - Allow Read Only Access to Read Only USBs for some users</Name>
		<IncludedIdList>
			<GroupId>{23c24566-98a5-4218-8802-59614513b97e}</GroupId>
		</IncludedIdList>
		<ExcludedIdList>
		</ExcludedIdList>
		<Entry Id="{e78857e3-9e36-473b-a07c-fe1a1f356ec9}">
			<Type>Allow</Type>
			<AccessMask>9</AccessMask>
			<Options>0</Options>
			<Sid>S-1-1-0</Sid>
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
<summary>Add a row for Step 4 - Deny all other USBs</summary>  
   
   1. Click "Add"
   2. For Name, enter *Step 4 - Deny all other USBs*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B7beca8fe-313a-46f2-a090-399eb3d74318%7D/RuleData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  *windows\Getting Started\Step 4\allow_different_access_to_different_users_rules.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for Step 4 - Allow Access to Writeable USBs for some users</summary>  
   
   1. Click "Add"
   2. For Name, enter *Step 4 - Allow Access to Writeable USBs for some users*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7Ba054bbcf-3454-4b95-9058-f7ed00deeee9%7D/RuleData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  *windows\Getting Started\Step 4\allow_different_access_to_different_users_rules.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for Step 4 - Allow Read Only Access to Read Only USBs for some users</summary>  
   
   1. Click "Add"
   2. For Name, enter *Step 4 - Allow Read Only Access to Read Only USBs for some users*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7Bb2b9cfc0-799d-457c-babc-da617d9a8b83%7D/RuleData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  *windows\Getting Started\Step 4\allow_different_access_to_different_users_rules.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for All removable media devices</summary>  
   
   1. Click "Add"
   2. For Name, enter *All removable media devices*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Bd8819053-24f4-444a-a0fb-9ce5a9e97862%7D/GroupData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  *windows\Getting Started\Intune OMA-URI\all_removable_media_devices{d8819053-24f4-444a-a0fb-9ce5a9e97862}.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for Authorized USBs</summary>  
   
   1. Click "Add"
   2. For Name, enter *Authorized USBs*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B368a2c82-17be-4137-bffa-370bbdff9672%7D/GroupData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  *windows\Getting Started\Intune OMA-URI\authorized_usbs{368a2c82-17be-4137-bffa-370bbdff9672}.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for Readonly USBs</summary>  
   
   1. Click "Add"
   2. For Name, enter *Readonly USBs*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B23c24566-98a5-4218-8802-59614513b97e%7D/GroupData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  *windows\Getting Started\Intune OMA-URI\readonly_usbs{23c24566-98a5-4218-8802-59614513b97e}.xml*
         
   
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



