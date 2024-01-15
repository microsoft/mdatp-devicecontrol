# Device Control for macOS Policy

Contains information and resources for creating and validating Device Control for macOS policy json.

## Policy

The new DC for macOS policy schema is intended to align to the existing structure of the Windows format.

### Limitations

* macOS uses JSON instead of XML
* macOS only supports a subset of the Window’s policy functionality
  + Windows specific items
  + Items not yet implemented in macOS
* The macOS policy restructures some of the elements from the Windows policy to more cleanly deserialize and validate.
  + For example, on Windows an entry has a ‘Type’ and an ‘Options’ field that has bit flags for various operations.  Only certain bit flags are valid for certain types.  On macOS the options are represented by a JSON enum instead of bit flag for easier readability.  In addition, each entry type is a unique JSON type with a specific options enum limited to the valid values for that type.

### Additional Capabilities

The macOS policy does support additional capabilities not currently in the Windows policy

* Subqueries
  + macOS policy can define an arbitrarily complex query by composing `and`, `or`, and `not` queries.
  + Windows has recently implemented ‘subgroups’ which is an equivalent feature, but requires defining a new group for each individual query. So, this requires manually creating/assembling the query hierarchy.
* Bluetooth Devices
* Granular permissions
  + Windows entries have limited options for AccessMask –-> RWX, FS RWX
  + Since macOS DC operates in a different manner from Windows, individual device types have more granular controls associated with them.  For example, Android devices have download_files, transfer_files, download_photos, and debug permissions that can be individual restricted or allowed.  
  + There is also generic_read, generic_write, and generic_execute permissions which are then mapped to the granular controls, to provide equivalent usage as the Windows AccessMask.
* Settings
  + The Windows policy format only includes groups and rules sections.  The macOS policy format adds a new ‘settings’ section to control the overall behavior of DC.
  + This keeps the settings together with the policy.
  + On Windows such settings are currently separate configurations.

## Policy Schema

The Device Control Policy schema is defined in [device_control_policy_schema.json](./device_control_policy_schema.json).  This schema can be used to validate device control policies prior to deployment.

**Links**
* [https://www.jsonschemavalidator.net/](www.jsonschemavalidator.net)

## Examples

The [examples](./examples/) directory contains a variety of example device control policies.

## Scripts

The [scripts](./scripts/) directory contains useful scripts for manipulating the policy JSON.