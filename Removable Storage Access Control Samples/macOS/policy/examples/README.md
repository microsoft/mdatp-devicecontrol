# Device Control for macOS Example Policies

Example policies to demonstrate the capabilities of the Device Control for macOS policy format.

## groups / rules

Contains 'translations' of the existing Device Control for Windows examples found in [Group Policy](/Removable%20Storage%20Access%20Control%20Samples/Group%20Policy/).  The file names (normalized) correspond to existing files within that location.

The translation is best effort as macOS only supports a subset of the existing functionality of the Windows implementation.

_Note: These json files are not valid Device Control for macOS policy files._

## *.json

Contains full policy samples for simple scenarios for each of the device types supported by macOS.

|Device Type|Example Policy|
|-----------|--------------|
|iOS devices|[audit_all_apple_devices.json](./audit_all_apple_devices.json)|
|bluetooth devices|[deny_all_bluetooth_devices_except_samsung.json](./deny_all_bluetooth_devices_except_samsung.json)|
|portable devices|[deny_debug_on_android.json](./deny_debug_on_android.json)|
|removable media|[deny_removable_media_except_kingston.json](./deny_removable_media_except_kingston.json)|