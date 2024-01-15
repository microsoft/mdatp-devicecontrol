# Device control policy sample: Demo_2_Policies

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
            <td rowspan="7"><b>Authorized removable storage policy</b></td>
            <td rowspan="7 valign="top">
                <ul><li>Approved USBs Group_0<a href="#approved-usbs-group_0" title="MatchAny {'InstancePathId': 'USBSTOR\\DISK&VEN__USB&PROD__SANDISK_3.2GEN1&REV_1.00\\03003324080520232521&*'}"> (details)</a></ul>
            </td>
            <td rowspan="7" valign="top">.
                <ul></ul>
            </td>
            <td>Deny</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>:x:</td>
            <td>-</td>
            <td>:x:</td>
            <td>None (0)</td> 
            <td>
                <details>
                <summary>View</summary>
                User condition: All Users<br>
                Parameters: MatchAll
                <ul>
                </ul>
                </details></td>
        </tr><tr>
            <td>Allow</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>:white_check_mark:</td>
            <td>-</td>
            <td>Create file evidence with file (8)</td>
            <td> 
                <details>
                <summary>View</summary>
                User Condition: xxxxx<br>
                Parameters: 
                <ul>
                </ul>
                </details></td>
        </tr><tr>
            <td>Allow</td>
            <td>-</td>
            <td>:white_check_mark:</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>None (0)</td>
            <td> 
                <details>
                <summary>View</summary>
                User Condition: xxxxx<br>
                Parameters: 
                <ul>
                </ul>
                </details></td>
        </tr><tr>
            <td>Allow</td>
            <td>:white_check_mark:</td>
            <td>-</td>
            <td>:white_check_mark:</td>
            <td>:white_check_mark:</td>
            <td>-</td>
            <td>:white_check_mark:</td>
            <td>None (0)</td>
            <td> 
                <center>-</center></td>
        </tr><tr>
            <td>Audit Allowed</td>
            <td>-</td>
            <td>:page_facing_up:</td>
            <td>:page_facing_up:</td>
            <td>-</td>
            <td>:page_facing_up:</td>
            <td>:page_facing_up:</td>
            <td>Send event (2)</td>
            <td> 
                <center>-</center></td>
        </tr><tr>
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
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>Show notification and Send event (3)</td>
            <td> 
                <center>-</center></td>
        </tr><tr>
            <td rowspan="5"><b>Authorized removable storage policy</b></td>
            <td rowspan="5 valign="top">
                <ul><li>Any Removable Storage and CD-DVD and WPD Group_0<a href="#any-removable-storage-and-cd-dvd-and-wpd-group_0" title="MatchAny {'PrimaryId': 'WpdDevices'}"> (details)</a></ul>
            </td>
            <td rowspan="5" valign="top">.
                <ul><li>Approved USBs Group_0<a href="#approved-usbs-group_0" title="MatchAny {'InstancePathId': 'USBSTOR\\DISK&VEN__USB&PROD__SANDISK_3.2GEN1&REV_1.00\\03003324080520232521&*'}"> (details)</a></ul>
            </td>
            <td>Deny</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>:x:</td>
            <td>-</td>
            <td>:x:</td>
            <td>None (0)</td> 
            <td>
                <details>
                <summary>View</summary>
                User condition: All Users<br>
                Parameters: MatchAll
                <ul>
                </ul>
                </details></td>
        </tr><tr>
            <td>Allow</td>
            <td>:white_check_mark:</td>
            <td>-</td>
            <td>:white_check_mark:</td>
            <td>:white_check_mark:</td>
            <td>-</td>
            <td>:white_check_mark:</td>
            <td>None (0)</td>
            <td> 
                <center>-</center></td>
        </tr><tr>
            <td>Audit Allowed</td>
            <td>-</td>
            <td>:page_facing_up:</td>
            <td>:page_facing_up:</td>
            <td>-</td>
            <td>:page_facing_up:</td>
            <td>:page_facing_up:</td>
            <td>Send event (2)</td>
            <td> 
                <center>-</center></td>
        </tr><tr>
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
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>Show notification and Send event (3)</td>
            <td> 
                <center>-</center></td>
        </tr></table>


## Groups


### Approved USBs Group_0



This is a group of type *Device*. 
The match type for the group is *MatchAny*.


|  Property | Value |
|-----------|-------|
| InstancePathId | USBSTOR\DISK&VEN__USB&PROD__SANDISK_3.2GEN1&REV_1.00\03003324080520232521&* |





<details>
<summary>View XML</summary>

```xml
<Group Id="{65fa649a-a111-4912-9294-fb6337a25038}" Type="Device">
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B65fa649a-a111-4912-9294-fb6337a25038%7D/GroupData -->
	<Name>Approved USBs Group_0</Name>
	<MatchType>MatchAny</MatchType>
	<DescriptorIdList>
		<InstancePathId>USBSTOR\DISK&amp;VEN__USB&amp;PROD__SANDISK_3.2GEN1&amp;REV_1.00\03003324080520232521&amp;*</InstancePathId>
	</DescriptorIdList>
</Group>
```
</details>

### Block Read and Write access to specific file _Groups_2



This is a group of type *File*. 
The match type for the group is *MatchAny*.


|  Property | Value |
|-----------|-------|
| PathId | *.exe |
| PathId | *.dll |





<details>
<summary>View XML</summary>

```xml
<Group Id="{e5f619a7-5c58-4927-90cd-75da2348a30f}" Type="File">
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Be5f619a7-5c58-4927-90cd-75da2348a30f%7D/GroupData -->
	<Name>Block Read and Write access to specific file _Groups_2</Name>
	<MatchType>MatchAny</MatchType>
	<DescriptorIdList>
		<PathId>*.exe</PathId>
		<PathId>*.dll</PathId>
	</DescriptorIdList>
</Group>
```
</details>

### Any Removable Storage and CD-DVD and WPD Group_0



This is a group of type *Device*. 
The match type for the group is *MatchAny*.


|  Property | Value |
|-----------|-------|
| PrimaryId | RemovableMediaDevices |
| PrimaryId | CdRomDevices |
| PrimaryId | WpdDevices |





<details>
<summary>View XML</summary>

```xml
<Group Id="{9b28fae8-72f7-4267-a1a5-685f747a7146}" Type="Device">
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B9b28fae8-72f7-4267-a1a5-685f747a7146%7D/GroupData -->
	<Name>Any Removable Storage and CD-DVD and WPD Group_0</Name>
	<MatchType>MatchAny</MatchType>
	<DescriptorIdList>
		<PrimaryId>RemovableMediaDevices</PrimaryId>
		<PrimaryId>CdRomDevices</PrimaryId>
		<PrimaryId>WpdDevices</PrimaryId>
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

- [Group Policy/Block Read and Write access to specific file _Groups.xml](Group%20Policy/Block%20Read%20and%20Write%20access%20to%20specific%20file%20_Groups.xml)
- [Intune OMA-URI/Any Removable Storage and CD-DVD and WPD Group.xml](Intune%20OMA-URI/Any%20Removable%20Storage%20and%20CD-DVD%20and%20WPD%20Group.xml)
- [Intune OMA-URI/Approved USBs Group.xml](Intune%20OMA-URI/Approved%20USBs%20Group.xml)
- [Group Policy/Demo_2_Policies.xml](Group%20Policy/Demo_2_Policies.xml)


# Deployment Instructions

Device control [policy rules](#policy-rules) and [groups](#groups) can be deployed through the following management tools:


## Windows
- [Intune UX](#intune-ux)
- [Intune Custom Settings](#intune-custom-settings)
- [Group Policy (GPO)](#group-policy-gpo)





## Intune UX

Intune UX is not supported for this policy because:
- Device groups not supported.
- Send event (2) is an unsupported notification.
- Create File Evidence (8) is an unsupported notification.
- Show notification (1) is an unsupported notification.
- Parameters are not supported
- File groups not supported.

Use [Intune custom settings](#intune-custom-settings) to deploy the policy instead.


## Group Policy (GPO)
<details>
<summary>Define device control policy groups</summary>

   1. Go to Computer Configuration > Administrative Templates > Windows Components > Microsoft Defender Antivirus > Device Control > Define device control policy groups.
   2. Save the XML below to a network share.
```xml
<Groups>
	<Group Id="{65fa649a-a111-4912-9294-fb6337a25038}" Type="Device">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B65fa649a-a111-4912-9294-fb6337a25038%7D/GroupData -->
		<Name>Approved USBs Group_0</Name>
		<MatchType>MatchAny</MatchType>
		<DescriptorIdList>
			<InstancePathId>USBSTOR\DISK&amp;VEN__USB&amp;PROD__SANDISK_3.2GEN1&amp;REV_1.00\03003324080520232521&amp;*</InstancePathId>
		</DescriptorIdList>
	</Group>
	<Group Id="{e5f619a7-5c58-4927-90cd-75da2348a30f}" Type="File">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Be5f619a7-5c58-4927-90cd-75da2348a30f%7D/GroupData -->
		<Name>Block Read and Write access to specific file _Groups_2</Name>
		<MatchType>MatchAny</MatchType>
		<DescriptorIdList>
			<PathId>*.exe</PathId>
			<PathId>*.dll</PathId>
		</DescriptorIdList>
	</Group>
	<Group Id="{9b28fae8-72f7-4267-a1a5-685f747a7146}" Type="Device">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B9b28fae8-72f7-4267-a1a5-685f747a7146%7D/GroupData -->
		<Name>Any Removable Storage and CD-DVD and WPD Group_0</Name>
		<MatchType>MatchAny</MatchType>
		<DescriptorIdList>
			<PrimaryId>RemovableMediaDevices</PrimaryId>
			<PrimaryId>CdRomDevices</PrimaryId>
			<PrimaryId>WpdDevices</PrimaryId>
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
	<PolicyRule Id="{6f3f8bbb-607f-4ed5-96af-51e3428db8f7}" >
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B6f3f8bbb-607f-4ed5-96af-51e3428db8f7%7D/RuleData -->
		<Name>Authorized removable storage policy</Name>
		<IncludedIdList>
			<GroupId>{65fa649a-a111-4912-9294-fb6337a25038}</GroupId>
		</IncludedIdList>
		<ExcludedIdList>
		</ExcludedIdList>
		<Entry Id="{9f421985-127d-4819-ae64-84b4d526e6d5}">
			<Type>Deny</Type>
			<AccessMask>40</AccessMask>
			<Options>0</Options>
			<Parameters MatchType="MatchAll">
				<File MatchType="MatchAny">
					<GroupId>{e5f619a7-5c58-4927-90cd-75da2348a30f}</GroupId>
				</File>
			</Parameters>
		</Entry>
		<Entry Id="{49eb971a-8ef5-4db0-a790-27163447d5c3}">
			<Type>Allow</Type>
			<AccessMask>16</AccessMask>
			<Options>8</Options>
			<Sid>xxxxx</Sid>
		</Entry>
		<Entry Id="{cf378fd0-ef21-4a17-b101-20ad0909e91a}">
			<Type>Allow</Type>
			<AccessMask>2</AccessMask>
			<Options>0</Options>
			<Sid>xxxxx</Sid>
		</Entry>
		<Entry Id="{94325d58-0a7b-4ef6-868f-765a0673777e}">
			<Type>Allow</Type>
			<AccessMask>45</AccessMask>
			<Options>0</Options>
		</Entry>
		<Entry Id="{11ba2408-3ad9-4a8e-9d57-c069eff74d00}">
			<Type>AuditAllowed</Type>
			<AccessMask>54</AccessMask>
			<Options>2</Options>
		</Entry>
		<Entry Id="{0ee3bb3f-7fe7-48fa-972d-6eefd85d66e9}">
			<Type>Deny</Type>
			<AccessMask>63</AccessMask>
			<Options>0</Options>
		</Entry>
		<Entry Id="{bf1b0973-7ea6-4a31-a7c3-5022baa9ea1a}">
			<Type>AuditDenied</Type>
			<AccessMask>7</AccessMask>
			<Options>3</Options>
		</Entry>
	</PolicyRule>
	<PolicyRule Id="{3984f1f4-7f66-4848-96de-491e2d038b07}" >
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B3984f1f4-7f66-4848-96de-491e2d038b07%7D/RuleData -->
		<Name>Authorized removable storage policy</Name>
		<IncludedIdList>
			<GroupId>{9b28fae8-72f7-4267-a1a5-685f747a7146}</GroupId>
		</IncludedIdList>
		<ExcludedIdList>
			<GroupId>{65fa649a-a111-4912-9294-fb6337a25038}</GroupId>
		</ExcludedIdList>
		<Entry Id="{3d15f184-1f3b-4a32-b5b6-47b560b0c44b}">
			<Type>Deny</Type>
			<AccessMask>40</AccessMask>
			<Options>0</Options>
			<Parameters MatchType="MatchAll">
				<File MatchType="MatchAny">
					<GroupId>{e5f619a7-5c58-4927-90cd-75da2348a30f}</GroupId>
				</File>
			</Parameters>
		</Entry>
		<Entry Id="{61e73502-ce08-4dab-80a3-d5847d21b651}">
			<Type>Allow</Type>
			<AccessMask>45</AccessMask>
			<Options>0</Options>
		</Entry>
		<Entry Id="{69ae539b-66f7-4b3a-aaec-53982d2b5254}">
			<Type>AuditAllowed</Type>
			<AccessMask>54</AccessMask>
			<Options>2</Options>
		</Entry>
		<Entry Id="{ac0c096f-f612-4c5d-a191-d39ea0093eea}">
			<Type>Deny</Type>
			<AccessMask>63</AccessMask>
			<Options>0</Options>
		</Entry>
		<Entry Id="{2c03a431-ac9a-4cdb-b260-7dac59550a37}">
			<Type>AuditDenied</Type>
			<AccessMask>7</AccessMask>
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
<summary>Add a row for Authorized removable storage policy</summary>  
   
   1. Click "Add"
   2. For Name, enter *Authorized removable storage policy*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B6f3f8bbb-607f-4ed5-96af-51e3428db8f7%7D/RuleData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  *.\Group Policy\authorized_removable_storage_policy{6f3f8bbb-607f-4ed5-96af-51e3428db8f7}.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for Authorized removable storage policy</summary>  
   
   1. Click "Add"
   2. For Name, enter *Authorized removable storage policy*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B3984f1f4-7f66-4848-96de-491e2d038b07%7D/RuleData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  *.\Group Policy\authorized_removable_storage_policy{3984f1f4-7f66-4848-96de-491e2d038b07}.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for Approved USBs Group_0</summary>  
   
   1. Click "Add"
   2. For Name, enter *Approved USBs Group_0*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B65fa649a-a111-4912-9294-fb6337a25038%7D/GroupData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  *.\Intune OMA-URI\Approved USBs Group.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for Unauthorized File Group_0</summary>  
   
   1. Click "Add"
   2. For Name, enter *Unauthorized File Group_0*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Be5f619a7-5c58-4927-90cd-75da2348a30f%7D/GroupData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  *.\Intune OMA-URI\Unauthorized File Group.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for Any Removable Storage and CD-DVD and WPD Group_0</summary>  
   
   1. Click "Add"
   2. For Name, enter *Any Removable Storage and CD-DVD and WPD Group_0*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B9b28fae8-72f7-4267-a1a5-685f747a7146%7D/GroupData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  *.\Intune OMA-URI\Any Removable Storage and CD-DVD and WPD Group.xml*
         
   
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



