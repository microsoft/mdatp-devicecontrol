# Device control policy sample: Different devices with different permissions

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
            <td rowspan="2" valign="top"><b>Deny all expect allowed USBs</b></td>
            <td rowspan="2 valign="top">
                <ul><li>Group: All Other Devices<a href="#all-other-devices" title="MatchAny {'PrimaryId': 'WpdDevices'}"> (details)</a>  
</ul>
            </td>
            <td rowspan="2" valign="top">
                <ul><li>Group: Allowed RO USBs<a href="#allowed-ro-usbs" title="MatchAny {'VID_PID': '090C_1000'}"> (details)</a>  
<li>Group: Allowed Full Access USBs<a href="#allowed-full-access-usbs" title="MatchAny {'SerialNumberId': '6EA9150055800605'}"> (details)</a>  
</ul>
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
            <td>Show notification (1)</td>
            <td> 
                <center>-</center></td>
        </tr><tr>
            <td rowspan="2" valign="top"><b>Grant RO access to allowed RO access USBs</b></td>
            <td rowspan="2 valign="top">
                <ul><li>Group: Allowed RO USBs<a href="#allowed-ro-usbs" title="MatchAny {'VID_PID': '090C_1000'}"> (details)</a>  
</ul>
            </td>
            <td rowspan="2" valign="top">
                <ul></ul>
            </td>
            <td>Deny</td>
            <td>-</td>
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
            <td>-</td>
            <td>:page_facing_up:</td>
            <td>:page_facing_up:</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>Show notification (1)</td>
            <td> 
                <center>-</center></td>
        </tr></table>


## Groups


### Allowed Full Access USBs



This is a group of type *Device*. 
The match type for the group is *MatchAny*.


|  Property | Value |
|-----------|-------|
| SerialNumberId | 6EA9150055800605 |





<details>
<summary>View XML</summary>

```xml
<Group Id="{f9393e5b-199c-4051-94a3-bcf4016658e4}" Type="Device">
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Bf9393e5b-199c-4051-94a3-bcf4016658e4%7D/GroupData -->
	<Name>Allowed Full Access USBs</Name>
	<MatchType>MatchAny</MatchType>
	<DescriptorIdList>
		<SerialNumberId>6EA9150055800605</SerialNumberId>
	</DescriptorIdList>
</Group>
```
</details>

### Allowed RO USBs



This is a group of type *Device*. 
The match type for the group is *MatchAny*.


|  Property | Value |
|-----------|-------|
| VID_PID | 090C_1000 |





<details>
<summary>View XML</summary>

```xml
<Group Id="{7ca89e2d-4f3d-497a-8e06-2b21877f3641}" Type="Device">
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B7ca89e2d-4f3d-497a-8e06-2b21877f3641%7D/GroupData -->
	<Name>Allowed RO USBs</Name>
	<MatchType>MatchAny</MatchType>
	<DescriptorIdList>
		<VID_PID>090C_1000</VID_PID>
	</DescriptorIdList>
</Group>
```
</details>

### All Other Devices



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
<Group Id="{805c79c2-8731-43a7-8128-fa58d830127f}" Type="Device">
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B805c79c2-8731-43a7-8128-fa58d830127f%7D/GroupData -->
	<Name>All Other Devices</Name>
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






| Setting Name |  Setting Value | Description |Documentation |
|--------------|----------------|-------------|---------------|


## Files
This policy is based on information in the following files:

- [groups/All Other Devices.xml](groups/All%20Other%20Devices.xml)
- [groups/Allowed RO USBs.xml](groups/Allowed%20RO%20USBs.xml)
- [groups/Allowed Full Access USBs.xml](groups/Allowed%20Full%20Access%20USBs.xml)
- [rules/Deny all expect allowed USBs.xml](rules/Deny%20all%20expect%20allowed%20USBs.xml)
- [rules/Grant RO access to allowed RO access USBs.xml](rules/Grant%20RO%20access%20to%20allowed%20RO%20access%20USBs.xml)


# Deployment Instructions

Device control [policy rules](#policy-rules) and [groups](#groups) can be deployed through the following management tools:


## Windows
- [Intune UX](#intune-ux)
- [Intune Custom Settings](#intune-custom-settings)
- [Group Policy (GPO)](#group-policy-gpo)





## Intune UX

<details>
<summary>Create a reusable setting for Allowed Full Access USBs</summary> 

   1. Navigate to Home > Endpoint Security > Attack Surface Reduction
   2. Click on Reusable Settings
   3. Click (+) Add
   4. Enter the *Allowed Full Access USBs* for the name.  
   5. Optionally, enter a description
   6. Click on "Next"
   
   1. Create an entry for  *SerialNumberId* = *6EA9150055800605* 
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Configure setting"    
        4. Enter *SerialNumberId( 6EA9150055800605 )* for Name
        5. Enter *6EA9150055800605* for SerialNumberId
        6. Click "Save"


   
   7. Set the match type drop down to MatchAny
   8. Click "Next"
   9. Click "Add"
</details>
<details>
<summary>Create a reusable setting for Allowed RO USBs</summary> 

   1. Navigate to Home > Endpoint Security > Attack Surface Reduction
   2. Click on Reusable Settings
   3. Click (+) Add
   4. Enter the *Allowed RO USBs* for the name.  
   5. Optionally, enter a description
   6. Click on "Next"
   
   1. Create an entry for  *VID_PID* = *090C_1000* 
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Configure setting"    
        4. Enter *VID_PID( 090C_1000 )* for Name
        5. Enter *090C_1000* for VID_PID
        6. Click "Save"


   
   7. Set the match type drop down to MatchAny
   8. Click "Next"
   9. Click "Add"
</details>
<details>
<summary>Create a reusable setting for All Other Devices</summary> 

   1. Navigate to Home > Endpoint Security > Attack Surface Reduction
   2. Click on Reusable Settings
   3. Click (+) Add
   4. Enter the *All Other Devices* for the name.  
   5. Optionally, enter a description
   6. Click on "Next"
   
   1. Create an entry for  *PrimaryId* = *RemovableMediaDevices* 
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Configure setting"    
        4. Enter *PrimaryId( RemovableMediaDevices )* for Name
        5. Enter *RemovableMediaDevices* for PrimaryId
        6. Click "Save"


   
   1. Create an entry for  *PrimaryId* = *CdRomDevices* 
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Configure setting"    
        4. Enter *PrimaryId( CdRomDevices )* for Name
        5. Enter *CdRomDevices* for PrimaryId
        6. Click "Save"


   
   1. Create an entry for  *PrimaryId* = *WpdDevices* 
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Configure setting"    
        4. Enter *PrimaryId( WpdDevices )* for Name
        5. Enter *WpdDevices* for PrimaryId
        6. Click "Save"


   
   7. Set the match type drop down to MatchAny
   8. Click "Next"
   9. Click "Add"
</details>
<details>
<summary>Create a Device Control Rules configuration profile</summary>  

   1. Navigate to Home > Endpoint Security > Attack Surface Reduction
   2. Click on "Create Policy"
   3. Under Platform, select "Windows 10 and later"
   4. Under Profile, select "Device Control Rules"
   5. Click "Create"
   6. Under Name, enter **
   7. Optionally, enter a description
   8. Click "Next"
</details>

> [!IMPORTANT]
> This policy has more than 1 rule.  
> Policy ordering is not guaranteed by Intune.
> Make sure that policy is not dependent on order to achieve desired result.
> Consider using ```default deny```.   


<details>
<summary>Add a rule for Deny all expect allowed USBs to the policy</summary>


   1. Click on "+ Set reusable settings" under Included Id

   1. Click on *All Other Devices*

   1. Click on "Select"


   1. Click on "+ Set reusable settings" under Excluded Id

   1. Click on *Allowed RO USBs*

   1. Click on *Allowed Full Access USBs*

   1. Click on "Select"

   1. Click on "+ Edit Entry"
   1. Enter *Deny all expect allowed USBs* for the name



   1. Select *Deny* from "Type"
   1. Select *None* from "Options"
   1. Select *Read, Write and Execute* from "Access mask"




   1. Add another entry.  Click on "+ Add"

   1. Select *Audit Denied* from "Type"
   1. Select *Show notification* from "Options"
   1. Select *Read, Write and Execute* from "Access mask"


   1. Click "OK"
</details>

<details>
<summary>Add a rule for Grant RO access to allowed RO access USBs to the policy</summary>

   1. Add another rule.  Click on "+ Add"


   1. Click on "+ Set reusable settings" under Included Id

   1. Click on *Allowed RO USBs*

   1. Click on "Select"


   1. Click on "+ Edit Entry"
   1. Enter *Grant RO access to allowed RO access USBs* for the name



   1. Select *Deny* from "Type"
   1. Select *None* from "Options"
   1. Select *Write and Execute* from "Access mask"




   1. Add another entry.  Click on "+ Add"

   1. Select *Audit Denied* from "Type"
   1. Select *Show notification* from "Options"
   1. Select *Write and Execute* from "Access mask"


   1. Click "OK"
</details>



## Group Policy (GPO)
<details>
<summary>Define device control policy groups</summary>

   1. Go to Computer Configuration > Administrative Templates > Windows Components > Microsoft Defender Antivirus > Device Control > Define device control policy groups.
   2. Save the XML below to a network share.
```xml
<Groups>
	<Group Id="{f9393e5b-199c-4051-94a3-bcf4016658e4}" Type="Device">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Bf9393e5b-199c-4051-94a3-bcf4016658e4%7D/GroupData -->
		<Name>Allowed Full Access USBs</Name>
		<MatchType>MatchAny</MatchType>
		<DescriptorIdList>
			<SerialNumberId>6EA9150055800605</SerialNumberId>
		</DescriptorIdList>
	</Group>
	<Group Id="{7ca89e2d-4f3d-497a-8e06-2b21877f3641}" Type="Device">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B7ca89e2d-4f3d-497a-8e06-2b21877f3641%7D/GroupData -->
		<Name>Allowed RO USBs</Name>
		<MatchType>MatchAny</MatchType>
		<DescriptorIdList>
			<VID_PID>090C_1000</VID_PID>
		</DescriptorIdList>
	</Group>
	<Group Id="{805c79c2-8731-43a7-8128-fa58d830127f}" Type="Device">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B805c79c2-8731-43a7-8128-fa58d830127f%7D/GroupData -->
		<Name>All Other Devices</Name>
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
	<PolicyRule Id="{9bf94b1d-3f0d-4133-adaf-38a0fbadccb2}" >
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B9bf94b1d-3f0d-4133-adaf-38a0fbadccb2%7D/RuleData -->
		<Name>Deny all expect allowed USBs</Name>
		<IncludedIdList>
			<GroupId>{805c79c2-8731-43a7-8128-fa58d830127f}</GroupId>
		</IncludedIdList>
		<ExcludedIdList>
			<GroupId>{7ca89e2d-4f3d-497a-8e06-2b21877f3641}</GroupId>
			<GroupId>{f9393e5b-199c-4051-94a3-bcf4016658e4}</GroupId>
		</ExcludedIdList>
		<Entry Id="{e8a0e636-6d46-4051-8193-2632cbb6865a}">
			<Type>Deny</Type>
			<AccessMask>7</AccessMask>
			<Options>0</Options>
		</Entry>
		<Entry Id="{5498a7cf-16bb-4374-808f-5270e11bc65c}">
			<Type>AuditDenied</Type>
			<AccessMask>7</AccessMask>
			<Options>1</Options>
		</Entry>
	</PolicyRule>
	<PolicyRule Id="{0fe59e26-908d-45eb-9896-ea420ca8942f}" >
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B0fe59e26-908d-45eb-9896-ea420ca8942f%7D/RuleData -->
		<Name>Grant RO access to allowed RO access USBs</Name>
		<IncludedIdList>
			<GroupId>{7ca89e2d-4f3d-497a-8e06-2b21877f3641}</GroupId>
		</IncludedIdList>
		<ExcludedIdList>
		</ExcludedIdList>
		<Entry Id="{f236a7c3-dc8d-442c-afb0-49876a93f79c}">
			<Type>Deny</Type>
			<AccessMask>6</AccessMask>
			<Options>0</Options>
		</Entry>
		<Entry Id="{c8bbf42a-3173-4487-b2aa-8dca677a2ac0}">
			<Type>AuditDenied</Type>
			<AccessMask>6</AccessMask>
			<Options>1</Options>
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
<summary>Add a row for Deny all expect allowed USBs</summary>  
   
   1. Click "Add"
   2. For Name, enter *Deny all expect allowed USBs*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B9bf94b1d-3f0d-4133-adaf-38a0fbadccb2%7D/RuleData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  */workspaces/mdatp-devicecontrol/deployable examples/windows_planning_deployment_3_v2/windows/devicecontrol/rules/Deny all expect allowed USBs.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for Grant RO access to allowed RO access USBs</summary>  
   
   1. Click "Add"
   2. For Name, enter *Grant RO access to allowed RO access USBs*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B0fe59e26-908d-45eb-9896-ea420ca8942f%7D/RuleData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  */workspaces/mdatp-devicecontrol/deployable examples/windows_planning_deployment_3_v2/windows/devicecontrol/rules/Grant RO access to allowed RO access USBs.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for All Other Devices</summary>  
   
   1. Click "Add"
   2. For Name, enter *All Other Devices*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B805c79c2-8731-43a7-8128-fa58d830127f%7D/GroupData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  */workspaces/mdatp-devicecontrol/deployable examples/windows_planning_deployment_3_v2/windows/devicecontrol/groups/All Other Devices.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for Allowed RO USBs</summary>  
   
   1. Click "Add"
   2. For Name, enter *Allowed RO USBs*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B7ca89e2d-4f3d-497a-8e06-2b21877f3641%7D/GroupData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  */workspaces/mdatp-devicecontrol/deployable examples/windows_planning_deployment_3_v2/windows/devicecontrol/groups/Allowed RO USBs.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for Allowed Full Access USBs</summary>  
   
   1. Click "Add"
   2. For Name, enter *Allowed Full Access USBs*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7Bf9393e5b-199c-4051-94a3-bcf4016658e4%7D/GroupData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  */workspaces/mdatp-devicecontrol/deployable examples/windows_planning_deployment_3_v2/windows/devicecontrol/groups/Allowed Full Access USBs.xml*
         
   
   7. Click "Save"
</details>



