# Device control policy sample: File Evidence

Description: This is a policy {'oma_uri': {'./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7Bb8615f3d-a41e-4c70-a70a-88e7b7aa7768%7D/RuleData': <devicecontrol.IntuneCustomRow object at 0x000002AE247A24B0>, './Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B9b28fae8-72f7-4267-a1a5-685f747a7146%7D/GroupData': <devicecontrol.IntuneCustomRow object at 0x000002AE24041B50>, './Vendor/MSFT/Defender/Configuration/DeviceControlEnabled': <devicecontrol.IntuneCustomRow object at 0x000002AE247A27E0>, './Vendor/MSFT/Defender/Configuration/DefaultEnforcement': <devicecontrol.IntuneCustomRow object at 0x000002AE247A2F90>, './Device/Vendor/MSFT/Defender/Configuration/DataDuplicationDirectory': <devicecontrol.IntuneCustomRow object at 0x000002AE247A2DE0>}, 'web_paths': ['windows/device/Group Policy/Any Removable Storage and CD-DVD and WPD Group.xml', 'windows/device/Group Policy/Audit File Information.xml'], 'rules': {'{b8615f3d-a41e-4c70-a70a-88e7b7aa7768}': <devicecontrol.PolicyRule object at 0x000002AE2275DEB0>}, 'groups': {'{9b28fae8-72f7-4267-a1a5-685f747a7146}': <devicecontrol.Group object at 0x000002AE24593EF0>}, 'intune_ux_support': <devicecontrol.Support object at 0x000002AE247A0E00>, 'groupsXML': '<Groups>\n\t<Group Id="{9b28fae8-72f7-4267-a1a5-685f747a7146}" Type="Device">\n\t\t<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B9b28fae8-72f7-4267-a1a5-685f747a7146%7D/GroupData -->\n\t\t<Name>Any Removable Storage and CD-DVD and WPD Group_1</Name>\n\t\t<MatchType>MatchAny</MatchType>\n\t\t<DescriptorIdList>\n\t\t\t<PrimaryId>RemovableMediaDevices</PrimaryId>\n\t\t\t<PrimaryId>CdRomDevices</PrimaryId>\n\t\t\t<PrimaryId>WpdDevices</PrimaryId>\n\t\t</DescriptorIdList>\n\t</Group>\n</Groups>', 'rulesXML': '<PolicyRules>\n\t<PolicyRule Id="{b8615f3d-a41e-4c70-a70a-88e7b7aa7768}" >\n\t\t<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7Bb8615f3d-a41e-4c70-a70a-88e7b7aa7768%7D/RuleData -->\n\t\t<Name>Audit File Information</Name>\n\t\t<IncludedIdList>\n\t\t\t<GroupId>{9b28fae8-72f7-4267-a1a5-685f747a7146}</GroupId>\n\t\t</IncludedIdList>\n\t\t<ExcludedIdList>\n\t\t</ExcludedIdList>\n\t\t<Entry Id="{ae40741a-cc96-42b7-9dab-f5ba59adef8a}">\n\t\t\t<Type>Allow</Type>\n\t\t\t<AccessMask>16</AccessMask>\n\t\t\t<Options>16</Options>\n\t\t</Entry>\n\t</PolicyRule>\n</PolicyRules>', 'mac_policy': None, 'mac_error': 'Primary ID [CdRomDevices] is not supported on macOS.', 'windows_support': <devicecontrol.Support object at 0x000002AE247A1DF0>, 'entry_type': <devicecontrol.WindowsEntryType object at 0x000002AE24590E60>, 'description': <__main__.Description object at 0x000002AE246E9C70>}              
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
            <td rowspan="1" valign="top"><b>Audit File Information</b></td>
            <td rowspan="1 valign="top">
                <ul><li>Group: Any Removable Storage and CD-DVD and WPD Group_1<a href="#any-removable-storage-and-cd-dvd-and-wpd-group_1" title="MatchAny {'PrimaryId': 'WpdDevices'}"> (details)</a>  
</ul>
            </td>
            <td rowspan="1" valign="top">
                <ul></ul>
            </td>
            <td>Allow</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>:white_check_mark:</td>
            <td>-</td>
            <td>Create file evidence without file (16)</td> 
            <td>
                <center>-</center></td>
        </tr></table>


## Groups


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
DeviceControlEnabled | True | [documentation](https://learn.microsoft.com/en-us/windows/client-management/mdm/defender-csp#configurationdevicecontrolenabled) |
DefaultEnforcement | Allow | [documentation](https://learn.microsoft.com/en-us/windows/client-management/mdm/defender-csp#configurationdefaultenforcement) |
DataDuplicationDirectory | Enter the directory to store files locally | [documentation](https://learn.microsoft.com/en-us/windows/client-management/mdm/defender-csp#configurationdataduplicationdirectory) |


## Files
This policy is based on information in the following files:

- [windows/device/Group Policy/Any Removable Storage and CD-DVD and WPD Group.xml](/windows/device/Group%20Policy/Any%20Removable%20Storage%20and%20CD-DVD%20and%20WPD%20Group.xml)
- [windows/device/Group Policy/Audit File Information.xml](/windows/device/Group%20Policy/Audit%20File%20Information.xml)


# Deployment Instructions

Device control [policy rules](#policy-rules) and [groups](#groups) can be deployed through the following management tools:


## Windows
- [Intune UX](#intune-ux)
- [Intune Custom Settings](#intune-custom-settings)
- [Group Policy (GPO)](#group-policy-gpo)





## Intune UX

<details>
<summary>Create a reusable setting for Any Removable Storage and CD-DVD and WPD Group_1</summary> 

   1. Navigate to Home > Endpoint Security > Attack Surface Reduction
   2. Click on Reusable Settings
   3. Click (+) Add
   4. Enter the Any Removable Storage and CD-DVD and WPD Group_1 for the name.  
   5. Optionally, enter a description
   6. Click on "Next"
   7. Set the match type toggle to MatchAny
   
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


<details>
<summary>Add a rule for Audit File Information to the policy</summary>


   1. Click on "+ Set reusable settings" under Included Id

   1. Click on *Any Removable Storage and CD-DVD and WPD Group_1*

   1. Click on "Select"


   1. Click on "+ Edit Entry"
   1. Enter *Audit File Information* for the name



   1. Select *Allow* from "Type"
   1. Select *Create file evidence without file* from "Options"
   1. Select ** from "Access mask"


   1. Click "OK"
</details>



## Group Policy (GPO)
<details>
<summary>Define device control policy groups</summary>

   1. Go to Computer Configuration > Administrative Templates > Windows Components > Microsoft Defender Antivirus > Device Control > Define device control policy groups.
   2. Save the XML below to a network share.
```xml
<Groups>
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
	<PolicyRule Id="{b8615f3d-a41e-4c70-a70a-88e7b7aa7768}" >
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7Bb8615f3d-a41e-4c70-a70a-88e7b7aa7768%7D/RuleData -->
		<Name>Audit File Information</Name>
		<IncludedIdList>
			<GroupId>{9b28fae8-72f7-4267-a1a5-685f747a7146}</GroupId>
		</IncludedIdList>
		<ExcludedIdList>
		</ExcludedIdList>
		<Entry Id="{ae40741a-cc96-42b7-9dab-f5ba59adef8a}">
			<Type>Allow</Type>
			<AccessMask>16</AccessMask>
			<Options>16</Options>
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
<summary>Add a row for Audit File Information</summary>  
   
   1. Click "Add"
   2. For Name, enter *Audit File Information*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7Bb8615f3d-a41e-4c70-a70a-88e7b7aa7768%7D/RuleData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  *windows\device\Intune OMA-URI\audit_file_information{b8615f3d-a41e-4c70-a70a-88e7b7aa7768}.xml*
         
   
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
   
   7. For Value, enter *1*
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for DataDuplicationDirectory</summary>  
   
   1. Click "Add"
   2. For Name, enter *DataDuplicationDirectory*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Device/Vendor/MSFT/Defender/Configuration/DataDuplicationDirectory*
   5. For Data type, select *String*
   
   7. For Value, enter *Enter the directory to store files locally*
   
   7. Click "Save"
</details>



