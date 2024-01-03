# Device control policy sample: Scenario 7

Description: A sample policy

A device control policy is a combination of [policy rules](#policy-rules) and [groups](#groups).  
This sample is based on the [sample files](#files).  
To configure the sample, follow the [deployment instructions](#deployment-instructions).  

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
            <td rowspan="2"><b>Deny Wpd Write</b></td>
            <td rowspan="2 valign="top">
                <ul></ul>
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
            <td>All Users</td>
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
        </tr></table>

## Groups



## Files
This policy is based on information in the following files:

- [Intune OMA-URI/Scenario 7 WPD Policy Sample, e.g. iPhone.xml](Intune%20OMA-URI/Scenario%207%20WPD%20Policy%20Sample%2C%20e.g.%20iPhone.xml)


# Deployment Instructions

Device control [policy rules](#policy-rules) and [groups](#groups) can be deployed through the following management tools:

## Windows
- [Intune UX](#intune-ux)
- [Intune Custom Settings](#intune-custom-settings)
- [Group Policy (GPO)](#group-policy-gpo)

## Mac
- [Mac Policy](#mac-policy)

## Intune UX

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
<summary>Add a rule for Deny Wpd Write to the policy</summary>



   1. Click on "+ Edit Entry"
   1. Enter *Deny Wpd Write* for the name



   1. Select *Deny* from "Type"
   1. Select *None* from "Options"
   1. Select *Write* from "Access mask"




   1. Add another entry.  Click on "+ Add"

   1. Select *Audit Denied* from "Type"
   1. Select *Show notification and Send event* from "Options"
   1. Select *Write* from "Access mask"


   1. Click "OK"
</details>



## Group Policy (GPO)
<details>
<summary>Define device control policy groups</summary>

   1. Go to Computer Configuration > Administrative Templates > Windows Components > Microsoft Defender Antivirus > Device Control > Define device control policy groups.
   2. Save the XML below to a network share.
```xml
<Groups>
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
		<Name>Deny Wpd Write</Name>
		<IncludedIdList>
		</IncludedIdList>
		<ExcludedIdList>
		</ExcludedIdList>
		<Entry Id="{ae40741a-cc96-42b7-9dab-f5ba59adef8a}">
			<Type>Deny</Type>
			<AccessMask>2</AccessMask>
			<Options>0</Options>
		</Entry>
		<Entry Id="{ae40741a-cc96-42b7-9dab-f5ba59adef8a}">
			<Type>AuditDenied</Type>
			<AccessMask>2</AccessMask>
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
<summary>Add a row for Deny Wpd Write</summary>  
   
   1. Click "Add"
   2. For Name, enter *Deny Wpd Write*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7Bb8615f3d-a41e-4c70-a70a-88e7b7aa7768%7D/RuleData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  *.\Intune OMA-URI\Scenario 7 WPD Policy Sample, e.g. iPhone.xml*
         
   
   
   7. Click "Save"
</details>


## Mac Policy

This policy is not supported on Mac because Unsupported entry type [AuditDenied]

Learn more
- [Mac device control examples](../Removable%20Storage%20Access%20Control%20Samples/macOS/policy/examples/README.md)

