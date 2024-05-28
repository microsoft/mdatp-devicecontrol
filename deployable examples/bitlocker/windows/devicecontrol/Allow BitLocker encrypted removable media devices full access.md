# Device control policy sample: Allow BitLocker encrypted removable media devices full access

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


### BitLocker Encrypted



This is a group of type *Device*. 
The match type for the group is *MatchAny*.


|  Property | Value |
|-----------|-------|
| DeviceEncryptionStateId | BitlockerEncrypted |





<details>
<summary>View XML</summary>

```xml
<Group Id="{88de708f-9802-4845-ac01-bdfe58371d79}" Type="Device">
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B88de708f-9802-4845-ac01-bdfe58371d79%7D/GroupData -->
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

- [groups/BitLocker Encrypted.xml](groups/BitLocker%20Encrypted.xml)
- [rules/Allow BitLocker encrypted removable media devices full access.xml](rules/Allow%20BitLocker%20encrypted%20removable%20media%20devices%20full%20access.xml)


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
	<Group Id="{88de708f-9802-4845-ac01-bdfe58371d79}" Type="Device">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B88de708f-9802-4845-ac01-bdfe58371d79%7D/GroupData -->
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
	<PolicyRule Id="{6a5a1462-80c6-4a84-a5b4-1627c34b10ab}" >
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B6a5a1462-80c6-4a84-a5b4-1627c34b10ab%7D/RuleData -->
		<Name>Allow BitLocker encrypted removable media devices full access</Name>
		<IncludedIdList>
			<GroupId>{88de708f-9802-4845-ac01-bdfe58371d79}</GroupId>
		</IncludedIdList>
		<ExcludedIdList>
		</ExcludedIdList>
		<Entry Id="{b5e1f3ad-ccf1-4fb6-8fa7-b25366241e3b}">
			<Type>Allow</Type>
			<AccessMask>63</AccessMask>
			<Options>0</Options>
		</Entry>
		<Entry Id="{ee9cef93-ed55-48a3-8431-f5362ca6876e}">
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
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B6a5a1462-80c6-4a84-a5b4-1627c34b10ab%7D/RuleData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  */workspaces/mdatp-devicecontrol/deployable examples/bitlocker/windows/devicecontrol/rules/Allow BitLocker encrypted removable media devices full access.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for BitLocker Encrypted</summary>  
   
   1. Click "Add"
   2. For Name, enter *BitLocker Encrypted*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B88de708f-9802-4845-ac01-bdfe58371d79%7D/GroupData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  */workspaces/mdatp-devicecontrol/deployable examples/bitlocker/windows/devicecontrol/groups/BitLocker Encrypted.xml*
         
   
   7. Click "Save"
</details>



