# Device control policy sample: Allow unencrypted removable media devices with an exception full access

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
<Group Id="{7c4e7b65-3321-4d3c-8710-13d3ace0eb2f}" Type="Device">
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B7c4e7b65-3321-4d3c-8710-13d3ace0eb2f%7D/GroupData -->
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
- [rules/Allow unencrypted removable media devices with an exception full access.xml](rules/Allow%20unencrypted%20removable%20media%20devices%20with%20an%20exception%20full%20access.xml)


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
	<Group Id="{7c4e7b65-3321-4d3c-8710-13d3ace0eb2f}" Type="Device">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B7c4e7b65-3321-4d3c-8710-13d3ace0eb2f%7D/GroupData -->
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
	<PolicyRule Id="{42371a40-7589-4991-9deb-00c610683fe0}" >
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B42371a40-7589-4991-9deb-00c610683fe0%7D/RuleData -->
		<Name>Allow unencrypted removable media devices with an exception full access</Name>
		<IncludedIdList>
			<GroupId>{7c4e7b65-3321-4d3c-8710-13d3ace0eb2f}</GroupId>
		</IncludedIdList>
		<ExcludedIdList>
		</ExcludedIdList>
		<Entry Id="{df826fce-13b5-4443-bd63-9ac02c4a7181}">
			<Type>Allow</Type>
			<AccessMask>63</AccessMask>
			<Options>0</Options>
		</Entry>
		<Entry Id="{e26630ec-dd5c-4356-abd7-20ba59ae5da8}">
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
<summary>Add a row for Allow unencrypted removable media devices with an exception full access</summary>  
   
   1. Click "Add"
   2. For Name, enter *Allow unencrypted removable media devices with an exception full access*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B42371a40-7589-4991-9deb-00c610683fe0%7D/RuleData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  */workspaces/mdatp-devicecontrol/deployable examples/bitlocker/windows/devicecontrol/rules/Allow unencrypted removable media devices with an exception full access.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for Full Access Exception</summary>  
   
   1. Click "Add"
   2. For Name, enter *Full Access Exception*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B7c4e7b65-3321-4d3c-8710-13d3ace0eb2f%7D/GroupData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  */workspaces/mdatp-devicecontrol/deployable examples/bitlocker/windows/devicecontrol/groups/Full Access Exception.xml*
         
   
   7. Click "Save"
</details>



