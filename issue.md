# Device Control Policy: Issue with User Policies

## Policy Rules
<table>
    <tr>
        <th rowspan="2" valign="top">Name</th>
        <th rowspan="2" valign="top">Devices</th>
        <th rowspan="2" valign="top">Excluding</th>
        <th rowspan="2" valign="top">Rule Type</th>
        <th colspan="7" valign="top"><center>Access</center></th>
        <th rowspan="2" valign="top">Notification</th>
        <th rowspan="2" valign="top">User SID</th>
        <th rowspan="2" valign="top">Conditions</th>
    </tr>
    <tr>
		<th>Disk Read</th>
		<th>Disk Write</th>
		<th>Disk Execute</th>
		<th>File Read</th>
		<th>File Write</th>
		<th>File Execute</th>
		<th>Print</th>
	</tr><tr>
            <td rowspan="2"><b>Allow Read,Write, Execute Access to removable devices</b></td>
            <td rowspan="2 valign="top">
                <ul><li>Global-Removable_Group_Baseline (1)_3<a href="#global-removable_group_baseline-1_3" title="[{'HardwareId': 'USBSTOR\\DiskKingstonDTVaultPrivacy30PMAP'}, {'HardwareId': 'USBSTOR\\CdRomKingstonDTVaultPrivacy30PMAP'}, {'HardwareId': 'USBSTOR\\DiskHypertecEncryptPlusV2___1.21'}, {'HardwareId': 'USBSTOR\\CdRomHypertecEncryptPlusV2___1.21'}, {'HardwareId': 'USBSTOR\\DiskKingstonDataTraveler_3.0PMAP'}]">(details)</a></ul>
            </td>
            <td rowspan="2" valign="top">
                <ul></ul>
            </td>
            <td>Allow</td>
            <td>:white_check_mark:</td>
            <td>:white_check_mark:</td>
            <td>:white_check_mark:</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>None (0)</td> 
            <td>S-1-5-21-602162358-1563985344-839522115-286197</td>
            <td>
                <ul>
                </ul>
            </td>
        </tr><tr>
            <td>Audit Allowed</td>
            <td>-</td>
            <td>:page_facing_up:</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>None and Send event (3)</td>
            <td>All Users</td>
            <td>
                <ul>
                </ul>
            </td>
        </tr><tr>
            <td rowspan="2"><b>Allow Read,Execute Access to non-encrypted removable devices</b></td>
            <td rowspan="2 valign="top">
                <ul><li>Global-Removable_Group_Baseline (1)_2<a href="#global-removable_group_baseline-1_2" title="[{'HardwareId': 'USBSTOR\\DiskKingstonDTVaultPrivacy30PMAP'}, {'HardwareId': 'USBSTOR\\CdRomKingstonDTVaultPrivacy30PMAP'}, {'HardwareId': 'USBSTOR\\DiskHypertecEncryptPlusV2___1.21'}, {'HardwareId': 'USBSTOR\\CdRomHypertecEncryptPlusV2___1.21'}, {'HardwareId': 'USBSTOR\\DiskKingstonDataTraveler_3.0PMAP'}]">(details)</a></ul>
            </td>
            <td rowspan="2" valign="top">
                <ul></ul>
            </td>
            <td>Deny</td>
            <td>-</td>
            <td>:x:</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>None (0)</td> 
            <td>S-1-5-21-602162358-1563985344-839522115-286196</td>
            <td>
                <ul>
                </ul>
            </td>
        </tr><tr>
            <td>Audit Denied</td>
            <td>-</td>
            <td>:page_facing_up:</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>Show notification and Send event (3)</td>
            <td>All Users</td>
            <td>
                <ul>
                </ul>
            </td>
        </tr><tr>
            <td rowspan="2"><b>Allow Read,Write, Execute Access to encrypted removable devices</b></td>
            <td rowspan="2 valign="top">
                <ul><li>Global-Removable_Group_Baseline (1)_3<a href="#global-removable_group_baseline-1_3" title="[{'HardwareId': 'USBSTOR\\DiskKingstonDTVaultPrivacy30PMAP'}, {'HardwareId': 'USBSTOR\\CdRomKingstonDTVaultPrivacy30PMAP'}, {'HardwareId': 'USBSTOR\\DiskHypertecEncryptPlusV2___1.21'}, {'HardwareId': 'USBSTOR\\CdRomHypertecEncryptPlusV2___1.21'}, {'HardwareId': 'USBSTOR\\DiskKingstonDataTraveler_3.0PMAP'}]">(details)</a></ul>
            </td>
            <td rowspan="2" valign="top">
                <ul></ul>
            </td>
            <td>Allow</td>
            <td>:white_check_mark:</td>
            <td>:white_check_mark:</td>
            <td>:white_check_mark:</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>None (0)</td> 
            <td>S-1-5-21-602162358-1563985344-839522115-288583</td>
            <td>
                <ul>
                </ul>
            </td>
        </tr><tr>
            <td>Audit Allowed</td>
            <td>-</td>
            <td>:page_facing_up:</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>None and Send event (3)</td>
            <td>All Users</td>
            <td>
                <ul>
                </ul>
            </td>
        </tr><tr>
            <td rowspan="2"><b>Block Read,Write,Execute Access to all removable devices</b></td>
            <td rowspan="2 valign="top">
                <ul><li>Global-Removable_Group_Baseline (1)_1<a href="#global-removable_group_baseline-1_1" title="[{'PrimaryId': 'RemovableMediaDevices'}, {'PrimaryId': 'CdRomDevices'}, {'PrimaryId': 'WpdDevices'}]">(details)</a></ul>
            </td>
            <td rowspan="2" valign="top">
                <ul><li>Global-Removable_Group_Baseline (1)_2<a href="#global-removable_group_baseline-1_2" title="[{'HardwareId': 'USBSTOR\\DiskKingstonDTVaultPrivacy30PMAP'}, {'HardwareId': 'USBSTOR\\CdRomKingstonDTVaultPrivacy30PMAP'}, {'HardwareId': 'USBSTOR\\DiskHypertecEncryptPlusV2___1.21'}, {'HardwareId': 'USBSTOR\\CdRomHypertecEncryptPlusV2___1.21'}, {'HardwareId': 'USBSTOR\\DiskKingstonDataTraveler_3.0PMAP'}]">(details)</a><li>Global-Removable_Group_Baseline (1)_3<a href="#global-removable_group_baseline-1_3" title="[{'HardwareId': 'USBSTOR\\DiskKingstonDTVaultPrivacy30PMAP'}, {'HardwareId': 'USBSTOR\\CdRomKingstonDTVaultPrivacy30PMAP'}, {'HardwareId': 'USBSTOR\\DiskHypertecEncryptPlusV2___1.21'}, {'HardwareId': 'USBSTOR\\CdRomHypertecEncryptPlusV2___1.21'}, {'HardwareId': 'USBSTOR\\DiskKingstonDataTraveler_3.0PMAP'}]">(details)</a></ul>
            </td>
            <td>Deny</td>
            <td>:x:</td>
            <td>:x:</td>
            <td>:x:</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>None (0)</td> 
            <td>All Users</td>
            <td>
                <ul>
                </ul>
            </td>
        </tr><tr>
            <td>Audit Denied</td>
            <td>:page_facing_up:</td>
            <td>:page_facing_up:</td>
            <td>:page_facing_up:</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>Show notification and Send event (3)</td>
            <td>All Users</td>
            <td>
                <ul>
                </ul>
            </td>
        </tr></table>

## Groups


### Global-Removable_Group_Baseline (1)_3
[{'HardwareId': 'USBSTOR\\DiskKingstonDTVaultPrivacy30PMAP'}, {'HardwareId': 'USBSTOR\\CdRomKingstonDTVaultPrivacy30PMAP'}, {'HardwareId': 'USBSTOR\\DiskHypertecEncryptPlusV2___1.21'}, {'HardwareId': 'USBSTOR\\CdRomHypertecEncryptPlusV2___1.21'}, {'HardwareId': 'USBSTOR\\DiskKingstonDataTraveler_3.0PMAP'}]

### Global-Removable_Group_Baseline (1)_2
[{'HardwareId': 'USBSTOR\\DiskKingstonDTVaultPrivacy30PMAP'}, {'HardwareId': 'USBSTOR\\CdRomKingstonDTVaultPrivacy30PMAP'}, {'HardwareId': 'USBSTOR\\DiskHypertecEncryptPlusV2___1.21'}, {'HardwareId': 'USBSTOR\\CdRomHypertecEncryptPlusV2___1.21'}, {'HardwareId': 'USBSTOR\\DiskKingstonDataTraveler_3.0PMAP'}]

### Global-Removable_Group_Baseline (1)_1
[{'PrimaryId': 'RemovableMediaDevices'}, {'PrimaryId': 'CdRomDevices'}, {'PrimaryId': 'WpdDevices'}]


## Files
This policy is based on information in the following files:

- C:\Users\joshbregman\Downloads\device control\Global-Removable_Group_Baseline (1).xml
- C:\Users\joshbregman\Downloads\device control\Global-Removable_Policy_Baseline (1).xml


## Intune UX

- Create a reusable setting for Global-Removable_Group_Baseline (1)_3  
   1. Navigate to Home > Endpoint Security > Attack Surface Reduction
   2. Click on Reusable Settings
   3. Click (+) Add
   4. Enter the Global-Removable_Group_Baseline (1)_3 for the name.  
   5. Optionally, enter a description
   6. Click on "Next"
   7. Set the match type toggle to MatchAny
   
      
   8. Add a Removable Storage object for HardwareId
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Edit Instance"    
        4. Enter *HardwareId* for Name
        5. Enter *USBSTOR\DiskKingstonDTVaultPrivacy30PMAP* for HardwareId
        6. Click "Save"
    
   
      
   8. Add a Removable Storage object for HardwareId
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Edit Instance"    
        4. Enter *HardwareId* for Name
        5. Enter *USBSTOR\CdRomKingstonDTVaultPrivacy30PMAP* for HardwareId
        6. Click "Save"
    
   
      
   8. Add a Removable Storage object for HardwareId
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Edit Instance"    
        4. Enter *HardwareId* for Name
        5. Enter *USBSTOR\DiskHypertecEncryptPlusV2___1.21* for HardwareId
        6. Click "Save"
    
   
      
   8. Add a Removable Storage object for HardwareId
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Edit Instance"    
        4. Enter *HardwareId* for Name
        5. Enter *USBSTOR\CdRomHypertecEncryptPlusV2___1.21* for HardwareId
        6. Click "Save"
    
   
      
   8. Add a Removable Storage object for HardwareId
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Edit Instance"    
        4. Enter *HardwareId* for Name
        5. Enter *USBSTOR\DiskKingstonDataTraveler_3.0PMAP* for HardwareId
        6. Click "Save"
    
   
   8. Click "Next"
   9. Click "Add"
- Create a reusable setting for Global-Removable_Group_Baseline (1)_2  
   1. Navigate to Home > Endpoint Security > Attack Surface Reduction
   2. Click on Reusable Settings
   3. Click (+) Add
   4. Enter the Global-Removable_Group_Baseline (1)_2 for the name.  
   5. Optionally, enter a description
   6. Click on "Next"
   7. Set the match type toggle to MatchAny
   
      
   8. Add a Removable Storage object for HardwareId
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Edit Instance"    
        4. Enter *HardwareId* for Name
        5. Enter *USBSTOR\DiskKingstonDTVaultPrivacy30PMAP* for HardwareId
        6. Click "Save"
    
   
      
   8. Add a Removable Storage object for HardwareId
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Edit Instance"    
        4. Enter *HardwareId* for Name
        5. Enter *USBSTOR\CdRomKingstonDTVaultPrivacy30PMAP* for HardwareId
        6. Click "Save"
    
   
      
   8. Add a Removable Storage object for HardwareId
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Edit Instance"    
        4. Enter *HardwareId* for Name
        5. Enter *USBSTOR\DiskHypertecEncryptPlusV2___1.21* for HardwareId
        6. Click "Save"
    
   
      
   8. Add a Removable Storage object for HardwareId
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Edit Instance"    
        4. Enter *HardwareId* for Name
        5. Enter *USBSTOR\CdRomHypertecEncryptPlusV2___1.21* for HardwareId
        6. Click "Save"
    
   
      
   8. Add a Removable Storage object for HardwareId
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Edit Instance"    
        4. Enter *HardwareId* for Name
        5. Enter *USBSTOR\DiskKingstonDataTraveler_3.0PMAP* for HardwareId
        6. Click "Save"
    
   
   8. Click "Next"
   9. Click "Add"
- Create a reusable setting for Global-Removable_Group_Baseline (1)_1  
   1. Navigate to Home > Endpoint Security > Attack Surface Reduction
   2. Click on Reusable Settings
   3. Click (+) Add
   4. Enter the Global-Removable_Group_Baseline (1)_1 for the name.  
   5. Optionally, enter a description
   6. Click on "Next"
   7. Set the match type toggle to MatchAny
   
      
   8. Add a Removable Storage object for PrimaryId
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Edit Instance"    
        4. Enter *PrimaryId* for Name
        5. Enter *RemovableMediaDevices* for PrimaryId
        6. Click "Save"
    
   
      
   8. Add a Removable Storage object for PrimaryId
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Edit Instance"    
        4. Enter *PrimaryId* for Name
        5. Enter *CdRomDevices* for PrimaryId
        6. Click "Save"
    
   
      
   8. Add a Removable Storage object for PrimaryId
        1. Click (+) Add
        2. Select "Reusable storage"
        3. Click on "Edit Instance"    
        4. Enter *PrimaryId* for Name
        5. Enter *WpdDevices* for PrimaryId
        6. Click "Save"
    
   
   8. Click "Next"
   9. Click "Add"
- Create a Device Control Rules configuration profile   
   1. Navigate to Home > Endpoint Security > Attack Surface Reduction
   2. Click on "Create Policy"
   3. Under Platform, select "Windows 10 and later"
   4. Under Profile, select "Device Control Rules"
   5. Click "Create"
   6. Under Name, enter *Issue with User Policies*
   7. Optionally, enter a description
   8. Click "Next"

- Add a rule for Allow Read,Write, Execute Access to removable devices to the policy

   1. Click on "+ Set reusable settings" under Included Id

   1. Click on *Global-Removable_Group_Baseline (1)_3*

   1. Click on "Select"


   1. Click on "+ Edit Entry"
   1. Enter *Allow Read,Write, Execute Access to removable devices* for the name



   1. Select *Allow* from "Type"
   1. Select *None* from "Options"
   1. Select *Read, Write and Execute* from "Access mask"

   1. Enter *S-1-5-21-602162358-1563985344-839522115-286197* for "Sid"




   1. Click on "+ Add"

   1. Select *Audit Allowed* from "Type"
   1. Select *None and Send event* from "Options"
   1. Select *Write* from "Access mask"


- Add a rule for Allow Read,Execute Access to non-encrypted removable devices to the policy

   1. Click on "+ Set reusable settings" under Included Id

   1. Click on *Global-Removable_Group_Baseline (1)_2*

   1. Click on "Select"


   1. Click on "+ Edit Entry"
   1. Enter *Allow Read,Execute Access to non-encrypted removable devices* for the name



   1. Select *Deny* from "Type"
   1. Select *None* from "Options"
   1. Select *Write* from "Access mask"

   1. Enter *S-1-5-21-602162358-1563985344-839522115-286196* for "Sid"




   1. Click on "+ Add"

   1. Select *Audit Denied* from "Type"
   1. Select *Show notification and Send event* from "Options"
   1. Select *Write* from "Access mask"


- Add a rule for Allow Read,Write, Execute Access to encrypted removable devices to the policy

   1. Click on "+ Set reusable settings" under Included Id

   1. Click on *Global-Removable_Group_Baseline (1)_3*

   1. Click on "Select"


   1. Click on "+ Edit Entry"
   1. Enter *Allow Read,Write, Execute Access to encrypted removable devices* for the name



   1. Select *Allow* from "Type"
   1. Select *None* from "Options"
   1. Select *Read, Write and Execute* from "Access mask"

   1. Enter *S-1-5-21-602162358-1563985344-839522115-288583* for "Sid"




   1. Click on "+ Add"

   1. Select *Audit Allowed* from "Type"
   1. Select *None and Send event* from "Options"
   1. Select *Write* from "Access mask"


- Add a rule for Block Read,Write,Execute Access to all removable devices to the policy

   1. Click on "+ Set reusable settings" under Included Id

   1. Click on *Global-Removable_Group_Baseline (1)_1*

   1. Click on "Select"


   1. Click on "+ Set reusable settings" under Excluded Id

   1. Click on *Global-Removable_Group_Baseline (1)_2*

   1. Click on *Global-Removable_Group_Baseline (1)_3*

   1. Click on "Select"

   1. Click on "+ Edit Entry"
   1. Enter *Block Read,Write,Execute Access to all removable devices* for the name



   1. Select *Deny* from "Type"
   1. Select *None* from "Options"
   1. Select *Read, Write and Execute* from "Access mask"




   1. Click on "+ Add"

   1. Select *Audit Denied* from "Type"
   1. Select *Show notification and Send event* from "Options"
   1. Select *Read, Write and Execute* from "Access mask"





## GPO
### Groups
```
<Groups>
	<Group Id="{43786489-56fc-4cb8-98ba-44255de7b8b8}" Type="Device">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B43786489-56fc-4cb8-98ba-44255de7b8b8%7D/GroupData -->
		<Name>Global-Removable_Group_Baseline (1)_3</Name>
		<MatchType>MatchAny</MatchType>
		<DescriptorIdList>
			<HardwareId>USBSTOR\DiskKingstonDTVaultPrivacy30PMAP</HardwareId>
			<HardwareId>USBSTOR\CdRomKingstonDTVaultPrivacy30PMAP</HardwareId>
			<HardwareId>USBSTOR\DiskHypertecEncryptPlusV2___1.21</HardwareId>
			<HardwareId>USBSTOR\CdRomHypertecEncryptPlusV2___1.21</HardwareId>
			<HardwareId>USBSTOR\DiskKingstonDataTraveler_3.0PMAP</HardwareId>
		</DescriptorIdList>
	</Group>
	<Group Id="{6be3d9b7-ec8e-4ab3-862c-023e4a5e0c74}" Type="Device">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B6be3d9b7-ec8e-4ab3-862c-023e4a5e0c74%7D/GroupData -->
		<Name>Global-Removable_Group_Baseline (1)_2</Name>
		<MatchType>MatchAny</MatchType>
		<DescriptorIdList>
			<HardwareId>USBSTOR\DiskKingstonDTVaultPrivacy30PMAP</HardwareId>
			<HardwareId>USBSTOR\CdRomKingstonDTVaultPrivacy30PMAP</HardwareId>
			<HardwareId>USBSTOR\DiskHypertecEncryptPlusV2___1.21</HardwareId>
			<HardwareId>USBSTOR\CdRomHypertecEncryptPlusV2___1.21</HardwareId>
			<HardwareId>USBSTOR\DiskKingstonDataTraveler_3.0PMAP</HardwareId>
		</DescriptorIdList>
	</Group>
	<Group Id="{17319f94-88ee-4b0b-8d43-3a0d277f8dfc}" Type="Device">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B17319f94-88ee-4b0b-8d43-3a0d277f8dfc%7D/GroupData -->
		<Name>Global-Removable_Group_Baseline (1)_1</Name>
		<MatchType>MatchAny</MatchType>
		<DescriptorIdList>
			<PrimaryId>RemovableMediaDevices</PrimaryId>
			<PrimaryId>CdRomDevices</PrimaryId>
			<PrimaryId>WpdDevices</PrimaryId>
		</DescriptorIdList>
	</Group>
</Groups>
```
### Rules
```
<PolicyRules>
	<PolicyRule Id="{dd69607b-15c2-469d-ad1f-3f529e367f0a}" >
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7Bdd69607b-15c2-469d-ad1f-3f529e367f0a%7D/RuleData -->
		<Name>Allow Read,Write, Execute Access to removable devices</Name>
		<IncludedIdList>
			<GroupId>{43786489-56fc-4cb8-98ba-44255de7b8b8}</GroupId>
		</IncludedIdList>
		<ExcludedIdList>
		</ExcludedIdList>
		<Entry>
			<Type>Allow</Type>
			<AccessMask>7</AccessMask>
			<Options>0</Options>
			<Sid>S-1-5-21-602162358-1563985344-839522115-286197</Sid>
		</Entry>
		<Entry>
			<Type>AuditAllowed</Type>
			<AccessMask>2</AccessMask>
			<Options>3</Options>
		</Entry>
	</PolicyRule>
	<PolicyRule Id="{ee022bf3-c61a-4780-92a0-e4f78fd91182}" >
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7Bee022bf3-c61a-4780-92a0-e4f78fd91182%7D/RuleData -->
		<Name>Allow Read,Execute Access to non-encrypted removable devices</Name>
		<IncludedIdList>
			<GroupId>{6be3d9b7-ec8e-4ab3-862c-023e4a5e0c74}</GroupId>
		</IncludedIdList>
		<ExcludedIdList>
		</ExcludedIdList>
		<Entry>
			<Type>Deny</Type>
			<AccessMask>2</AccessMask>
			<Options>0</Options>
			<Sid>S-1-5-21-602162358-1563985344-839522115-286196</Sid>
		</Entry>
		<Entry>
			<Type>AuditDenied</Type>
			<AccessMask>2</AccessMask>
			<Options>3</Options>
		</Entry>
	</PolicyRule>
	<PolicyRule Id="{3ef71340-2d01-404c-bcd8-b966caa14494}" >
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B3ef71340-2d01-404c-bcd8-b966caa14494%7D/RuleData -->
		<Name>Allow Read,Write, Execute Access to encrypted removable devices</Name>
		<IncludedIdList>
			<GroupId>{43786489-56fc-4cb8-98ba-44255de7b8b8}</GroupId>
		</IncludedIdList>
		<ExcludedIdList>
		</ExcludedIdList>
		<Entry>
			<Type>Allow</Type>
			<AccessMask>7</AccessMask>
			<Options>0</Options>
			<Sid>S-1-5-21-602162358-1563985344-839522115-288583</Sid>
		</Entry>
		<Entry>
			<Type>AuditAllowed</Type>
			<AccessMask>2</AccessMask>
			<Options>3</Options>
		</Entry>
	</PolicyRule>
	<PolicyRule Id="{3dbe224a-4bc8-48f6-9e2b-d7b1906b46dd}" >
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7B3dbe224a-4bc8-48f6-9e2b-d7b1906b46dd%7D/RuleData -->
		<Name>Block Read,Write,Execute Access to all removable devices</Name>
		<IncludedIdList>
			<GroupId>{17319f94-88ee-4b0b-8d43-3a0d277f8dfc}</GroupId>
		</IncludedIdList>
		<ExcludedIdList>
			<GroupId>{6be3d9b7-ec8e-4ab3-862c-023e4a5e0c74}</GroupId>
			<GroupId>{43786489-56fc-4cb8-98ba-44255de7b8b8}</GroupId>
		</ExcludedIdList>
		<Entry>
			<Type>Deny</Type>
			<AccessMask>7</AccessMask>
			<Options>0</Options>
		</Entry>
		<Entry>
			<Type>AuditDenied</Type>
			<AccessMask>7</AccessMask>
			<Options>3</Options>
		</Entry>
	</PolicyRule>
</PolicyRules>
```
## Intune Custom Settings

| Name | Description | OMA-URI | Type | Value |
|---  |---          |---      |---   |---    |


## Mac

This policy is not supported on Mac because Unsupported Descriptor ID HardwareId

