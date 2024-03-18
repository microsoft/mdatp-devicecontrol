# Device control policy sample: Demo_2_Policies

Description: This is a policy {'oma_uri': {'./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B6f3f8bbb-607f-4ed5-96af-51e3428db8f7%7D/RuleData': <devicecontrol.IntuneCustomRow object at 0x000002AE247A1AF0>, './Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B3984f1f4-7f66-4848-96de-491e2d038b07%7D/RuleData': <devicecontrol.IntuneCustomRow object at 0x000002AE23F32F60>, './Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B65fa649a-a111-4912-9294-fb6337a25038%7D/GroupData': <devicecontrol.IntuneCustomRow object at 0x000002AE247A22D0>, './Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Be5f619a7-5c58-4927-90cd-75da2348a30f%7D/GroupData': <devicecontrol.IntuneCustomRow object at 0x000002AE247A0D10>, './Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B9b28fae8-72f7-4267-a1a5-685f747a7146%7D/GroupData': <devicecontrol.IntuneCustomRow object at 0x000002AE247A31D0>, './Vendor/MSFT/Defender/Configuration/DefaultEnforcement': <devicecontrol.IntuneCustomRow object at 0x000002AE247A2990>, './Vendor/MSFT/Defender/Configuration/DeviceControlEnabled': <devicecontrol.IntuneCustomRow object at 0x000002AE247A3B60>}, 'web_paths': ['windows/device/Group Policy/Any Removable Storage and CD-DVD and WPD Group.xml', 'windows/device/Group Policy/Demo_2_Policies.xml', 'windows/device/Group Policy/Block Read and Write access to specific file _Groups.xml', 'windows/device/Intune OMA-URI/Approved USBs Group.xml'], 'rules': {'{6f3f8bbb-607f-4ed5-96af-51e3428db8f7}': <devicecontrol.PolicyRule object at 0x000002AE24614C20>, '{3984f1f4-7f66-4848-96de-491e2d038b07}': <devicecontrol.PolicyRule object at 0x000002AE2425F710>}, 'groups': {'{65fa649a-a111-4912-9294-fb6337a25038}': <devicecontrol.Group object at 0x000002AE246CEED0>, '{e5f619a7-5c58-4927-90cd-75da2348a30f}': <devicecontrol.Group object at 0x000002AE245D7A40>, '{9b28fae8-72f7-4267-a1a5-685f747a7146}': <devicecontrol.Group object at 0x000002AE24593EF0>}, 'intune_ux_support': <devicecontrol.Support object at 0x000002AE247A2960>, 'groupsXML': '<Groups>\n\t<Group Id="{65fa649a-a111-4912-9294-fb6337a25038}" Type="Device">\n\t\t<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B65fa649a-a111-4912-9294-fb6337a25038%7D/GroupData -->\n\t\t<Name>Approved USBs Group_0</Name>\n\t\t<MatchType>MatchAny</MatchType>\n\t\t<DescriptorIdList>\n\t\t\t<InstancePathId>USBSTOR\\DISK&amp;VEN__USB&amp;PROD__SANDISK_3.2GEN1&amp;REV_1.00\\03003324080520232521&amp;*</InstancePathId>\n\t\t</DescriptorIdList>\n\t</Group>\n\t<Group Id="{e5f619a7-5c58-4927-90cd-75da2348a30f}" Type="File">\n\t\t<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Be5f619a7-5c58-4927-90cd-75da2348a30f%7D/GroupData -->\n\t\t<Name>Block Read and Write access to specific file _Groups_2</Name>\n\t\t<MatchType>MatchAny</MatchType>\n\t\t<DescriptorIdList>\n\t\t\t<PathId>*.exe</PathId>\n\t\t\t<PathId>*.dll</PathId>\n\t\t</DescriptorIdList>\n\t</Group>\n\t<Group Id="{9b28fae8-72f7-4267-a1a5-685f747a7146}" Type="Device">\n\t\t<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B9b28fae8-72f7-4267-a1a5-685f747a7146%7D/GroupData -->\n\t\t<Name>Any Removable Storage and CD-DVD and WPD Group_1</Name>\n\t\t<MatchType>MatchAny</MatchType>\n\t\t<DescriptorIdList>\n\t\t\t<PrimaryId>RemovableMediaDevices</PrimaryId>\n\t\t\t<PrimaryId>CdRomDevices</PrimaryId>\n\t\t\t<PrimaryId>WpdDevices</PrimaryId>\n\t\t</DescriptorIdList>\n\t</Group>\n</Groups>', 'rulesXML': '<PolicyRules>\n\t<PolicyRule Id="{6f3f8bbb-607f-4ed5-96af-51e3428db8f7}" >\n\t\t<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B6f3f8bbb-607f-4ed5-96af-51e3428db8f7%7D/RuleData -->\n\t\t<Name>Authorized removable storage policy</Name>\n\t\t<IncludedIdList>\n\t\t\t<GroupId>{65fa649a-a111-4912-9294-fb6337a25038}</GroupId>\n\t\t</IncludedIdList>\n\t\t<ExcludedIdList>\n\t\t</ExcludedIdList>\n\t\t<Entry Id="{9f421985-127d-4819-ae64-84b4d526e6d5}">\n\t\t\t<Type>Deny</Type>\n\t\t\t<AccessMask>40</AccessMask>\n\t\t\t<Options>0</Options>\n\t\t\t<Parameters MatchType="MatchAll">\n\t\t\t\t<File MatchType="MatchAny">\n\t\t\t\t\t<GroupId>{e5f619a7-5c58-4927-90cd-75da2348a30f}</GroupId>\n\t\t\t\t</File>\n\t\t\t</Parameters>\n\t\t</Entry>\n\t\t<Entry Id="{49eb971a-8ef5-4db0-a790-27163447d5c3}">\n\t\t\t<Type>Allow</Type>\n\t\t\t<AccessMask>16</AccessMask>\n\t\t\t<Options>8</Options>\n\t\t\t<Sid>xxxxx</Sid>\n\t\t</Entry>\n\t\t<Entry Id="{cf378fd0-ef21-4a17-b101-20ad0909e91a}">\n\t\t\t<Type>Allow</Type>\n\t\t\t<AccessMask>2</AccessMask>\n\t\t\t<Options>0</Options>\n\t\t\t<Sid>xxxxx</Sid>\n\t\t</Entry>\n\t\t<Entry Id="{94325d58-0a7b-4ef6-868f-765a0673777e}">\n\t\t\t<Type>Allow</Type>\n\t\t\t<AccessMask>45</AccessMask>\n\t\t\t<Options>0</Options>\n\t\t</Entry>\n\t\t<Entry Id="{11ba2408-3ad9-4a8e-9d57-c069eff74d00}">\n\t\t\t<Type>AuditAllowed</Type>\n\t\t\t<AccessMask>54</AccessMask>\n\t\t\t<Options>2</Options>\n\t\t</Entry>\n\t\t<Entry Id="{0ee3bb3f-7fe7-48fa-972d-6eefd85d66e9}">\n\t\t\t<Type>Deny</Type>\n\t\t\t<AccessMask>63</AccessMask>\n\t\t\t<Options>0</Options>\n\t\t</Entry>\n\t\t<Entry Id="{bf1b0973-7ea6-4a31-a7c3-5022baa9ea1a}">\n\t\t\t<Type>AuditDenied</Type>\n\t\t\t<AccessMask>7</AccessMask>\n\t\t\t<Options>3</Options>\n\t\t</Entry>\n\t</PolicyRule>\n\t<PolicyRule Id="{3984f1f4-7f66-4848-96de-491e2d038b07}" >\n\t\t<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B3984f1f4-7f66-4848-96de-491e2d038b07%7D/RuleData -->\n\t\t<Name>Authorized removable storage policy</Name>\n\t\t<IncludedIdList>\n\t\t\t<GroupId>{9b28fae8-72f7-4267-a1a5-685f747a7146}</GroupId>\n\t\t</IncludedIdList>\n\t\t<ExcludedIdList>\n\t\t\t<GroupId>{65fa649a-a111-4912-9294-fb6337a25038}</GroupId>\n\t\t</ExcludedIdList>\n\t\t<Entry Id="{3d15f184-1f3b-4a32-b5b6-47b560b0c44b}">\n\t\t\t<Type>Deny</Type>\n\t\t\t<AccessMask>40</AccessMask>\n\t\t\t<Options>0</Options>\n\t\t\t<Parameters MatchType="MatchAll">\n\t\t\t\t<File MatchType="MatchAny">\n\t\t\t\t\t<GroupId>{e5f619a7-5c58-4927-90cd-75da2348a30f}</GroupId>\n\t\t\t\t</File>\n\t\t\t</Parameters>\n\t\t</Entry>\n\t\t<Entry Id="{61e73502-ce08-4dab-80a3-d5847d21b651}">\n\t\t\t<Type>Allow</Type>\n\t\t\t<AccessMask>45</AccessMask>\n\t\t\t<Options>0</Options>\n\t\t</Entry>\n\t\t<Entry Id="{69ae539b-66f7-4b3a-aaec-53982d2b5254}">\n\t\t\t<Type>AuditAllowed</Type>\n\t\t\t<AccessMask>54</AccessMask>\n\t\t\t<Options>2</Options>\n\t\t</Entry>\n\t\t<Entry Id="{ac0c096f-f612-4c5d-a191-d39ea0093eea}">\n\t\t\t<Type>Deny</Type>\n\t\t\t<AccessMask>63</AccessMask>\n\t\t\t<Options>0</Options>\n\t\t</Entry>\n\t\t<Entry Id="{2c03a431-ac9a-4cdb-b260-7dac59550a37}">\n\t\t\t<Type>AuditDenied</Type>\n\t\t\t<AccessMask>7</AccessMask>\n\t\t\t<Options>3</Options>\n\t\t</Entry>\n\t</PolicyRule>\n</PolicyRules>', 'mac_policy': None, 'mac_error': 'Unsupported Descriptor ID InstancePathId', 'windows_support': <devicecontrol.Support object at 0x000002AE247A33E0>, 'entry_type': <devicecontrol.WindowsEntryType object at 0x000002AE24590E60>, 'description': <__main__.Description object at 0x000002AE23F870E0>}              
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
            <td rowspan="7" valign="top"><b>Authorized removable storage policy</b></td>
            <td rowspan="7 valign="top">
                <ul><li>Group: Approved USBs Group_0<a href="#approved-usbs-group_0" title="MatchAny {'InstancePathId': 'USBSTOR\\DISK&VEN__USB&PROD__SANDISK_3.2GEN1&REV_1.00\\03003324080520232521&*'}"> (details)</a>  
</ul>
            </td>
            <td rowspan="7" valign="top">
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
                MatchAll:
                <ul><li> Windows File: MatchAny 
                        <ul><li>Group: Block Read and Write access to specific file _Groups_2<a href="#block-read-and-write-access-to-specific-file-_groups_2" title="MatchAny {'PathId': '*.dll'}"> (details)</a>  
</ul>
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
                User: xxxxx<br></td>
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
                User: xxxxx<br></td>
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
            <td rowspan="5" valign="top"><b>Authorized removable storage policy</b></td>
            <td rowspan="5 valign="top">
                <ul><li>Group: Any Removable Storage and CD-DVD and WPD Group_1<a href="#any-removable-storage-and-cd-dvd-and-wpd-group_1" title="MatchAny {'PrimaryId': 'WpdDevices'}"> (details)</a>  
</ul>
            </td>
            <td rowspan="5" valign="top">
                <ul><li>Group: Approved USBs Group_0<a href="#approved-usbs-group_0" title="MatchAny {'InstancePathId': 'USBSTOR\\DISK&VEN__USB&PROD__SANDISK_3.2GEN1&REV_1.00\\03003324080520232521&*'}"> (details)</a>  
</ul>
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
                MatchAll:
                <ul><li> Windows File: MatchAny 
                        <ul><li>Group: Block Read and Write access to specific file _Groups_2<a href="#block-read-and-write-access-to-specific-file-_groups_2" title="MatchAny {'PathId': '*.dll'}"> (details)</a>  
</ul>
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

### Any Removable Storage and CD-DVD and WPD Group_1



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
	<Name>Any Removable Storage and CD-DVD and WPD Group_1</Name>
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

- [windows/device/Group Policy/Any Removable Storage and CD-DVD and WPD Group.xml](/windows/device/Group%20Policy/Any%20Removable%20Storage%20and%20CD-DVD%20and%20WPD%20Group.xml)
- [windows/device/Group Policy/Demo_2_Policies.xml](/windows/device/Group%20Policy/Demo_2_Policies.xml)
- [windows/device/Group Policy/Block Read and Write access to specific file _Groups.xml](/windows/device/Group%20Policy/Block%20Read%20and%20Write%20access%20to%20specific%20file%20_Groups.xml)
- [windows/device/Intune OMA-URI/Approved USBs Group.xml](/windows/device/Intune%20OMA-URI/Approved%20USBs%20Group.xml)


# Deployment Instructions

Device control [policy rules](#policy-rules) and [groups](#groups) can be deployed through the following management tools:


## Windows
- [Intune UX](#intune-ux)
- [Intune Custom Settings](#intune-custom-settings)
- [Group Policy (GPO)](#group-policy-gpo)





## Intune UX

Intune UX is not supported for this policy because:
- Windows File groups not supported.
- File Execute (32) is an unsupported access mask
- File Read (8) is an unsupported access mask
- Create file evidence with file is an unsupported notification.
- Parameters are not supported
- File Write (16) is an unsupported access mask

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
		<Name>Any Removable Storage and CD-DVD and WPD Group_1</Name>
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
   
        
   6. For Custom XML, select  *windows\device\Intune OMA-URI\authorized_removable_storage_policy{6f3f8bbb-607f-4ed5-96af-51e3428db8f7}.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for Authorized removable storage policy</summary>  
   
   1. Click "Add"
   2. For Name, enter *Authorized removable storage policy*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B3984f1f4-7f66-4848-96de-491e2d038b07%7D/RuleData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  *windows\device\Intune OMA-URI\authorized_removable_storage_policy{3984f1f4-7f66-4848-96de-491e2d038b07}.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for Approved USBs Group_0</summary>  
   
   1. Click "Add"
   2. For Name, enter *Approved USBs Group_0*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B65fa649a-a111-4912-9294-fb6337a25038%7D/GroupData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  *windows\device\Intune OMA-URI\Approved USBs Group.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for Unauthorized File Group_0</summary>  
   
   1. Click "Add"
   2. For Name, enter *Unauthorized File Group_0*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Be5f619a7-5c58-4927-90cd-75da2348a30f%7D/GroupData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  *windows\device\Intune OMA-URI\Unauthorized File Group.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for Any Removable Storage and CD-DVD and WPD Group_0</summary>  
   
   1. Click "Add"
   2. For Name, enter *Any Removable Storage and CD-DVD and WPD Group_0*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B9b28fae8-72f7-4267-a1a5-685f747a7146%7D/GroupData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  *windows\device\Intune OMA-URI\Any Removable Storage and CD-DVD and WPD Group.xml*
         
   
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



