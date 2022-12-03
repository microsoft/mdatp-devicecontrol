# Device Control for macOS Deployment

## demo.mobileconfig

An example mobileconfig file demonstrating how to deploy a DC policy.

### DC_in_dlp

The v2 Device Control implementation is gated behind a feature flag while in preview.  The feature will be disabled unless set in the MDE settings (com.microsoft.wdav preference domain):

```xml
    <key>dlp</key>
    <dict>
        <key>features</key>
        <dict>
            <key>name</key>
            <string>DC_in_dlp</string>
            <key>state</key>
            <string>enabled</string>
        </dict>
    </dict>
```

_Note: This will not be needed after public release._

### Device Control policy

The v2 Device Control policy is now set via the `deviceControl/policy` key.  The policy is no longer directly embedded within the MDE settings, but instead indirectly stored as a string.

```xml
    <key>deviceControl</key>
    <dict>
        <key>policy</key>
        <string>
            policy text here
        </string>
    </dict>
```

## schema.json

The [mdatp-xplat](https://github.com/microsoft/mdatp-xplat) repo's [schema.json](https://github.com/microsoft/mdatp-xplat/blob/master/macos/schema/schema.json) has been updated to expose both the `deviceControl/policy` and `dlp/features` configurations.