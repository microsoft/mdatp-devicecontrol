# Device control - Python

Utilities for Device Control

## Getting Started

- Fork the repo

### Install the tools

1. Install [python 3.12](https://www.python.org/downloads/release/python-3120/) or greater
2. Install the package locally

On macOS on Linux
```
python3 -m pip install --upgrade build
python3 -m build
pip3 install -e .
```

On Windows
```
py -m pip install --upgrade build
py -m build
pip install -e .
```

> [!NOTE]
> On Windows, long paths need to be enabled 
>  1.  Open the Registry Editor: Press Win + R, type regedit, and press Enter.
>  2.  Navigate to the Key: Go to:
>            `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem`
>  3. Modify the Value: Find the `LongPathsEnabled` DWORD in the right pane. Double-click on it and change the value from 0 to 1.
>  4. Restart Your Computer: For the changes to take effect, restart your computer.

The follow shortcuts should be created:

   - ```dc``` - [Creating and deploying device control policies](#dc)
   - ```dcconvert``` - [Converting Windows XML to macOS JSON formats](#dcconvert)
   - ```dcupgrade``` - [Upgrade macOS v1 policies to v2](#dcupgrade)
   - ```dcdoc``` - [Generate documentation for device control policies](#dcdoc)

### Deploy a sample using dc
- [Configure the environment for dc](#setting-up-the-environment-for-dc)
- To deploy an example, go to one of the directories in the [deployable examples](../deployable%20examples/), and type ```dc apply -a``` if you're using an application identity or ```dc apply -u``` if you're using a user identity

### Create a new example using dc
- To import a configuration from an Excel file *<xlsx-file>* and deploy it to Intune:
    -   Create a directory for the project called *<package-dir>*
    -   ```cd package-dir```
    -   ```dc init xlsx --name <name of the project> --description <description for the project> --os [windows|macOs] --version [v1|v2] xlsx --file <xlsx file>```
    -  ```dc apply --user```




## dc
```
usage: dc [-h] {init,validate,apply,delete} ...

Utility for device control

positional arguments:
  {init,validate,apply,delete}
                        The operation to perform on the package
    init                Initialize the package
    validate            Validate the configuration
    apply               Apply the package to Intune
    delete              Delete the package from Intune
    patch-graph         Patches the graph SDK to work with dc


options:
  -h, --help            show this help message and exit
```

### Setting up the environment for dc


> [!IMPORTANT]
> ```dc``` can use either a user `-u` or application `-a` identity to connect to the Graph API. The instructions for authenticating as the logged in user (user credentials) are found [here](https://learn.microsoft.com/en-us/graph/tutorials/python?tabs=aad&tutorial-step=1).  The instructions for authenticating as an application are found here [here](https://learn.microsoft.com/en-us/graph/tutorials/python-app-only?tabs=aad&tutorial-step=1)<BR>
> ```dc``` uses the ```DeviceManagementConfiguration.ReadWrite.All Directory.Read.All``` scopes to read information from Entra Id, and read/write information to Intune.<BR>
> ```dc``` reads the credentials information from the environment variables.

Set the following environment variables

| Environment Variable | Description |
|---                   |---
| DC_CONFIG_PATH       | Path to the ```mdedevicecontrol.conf```
| DC_LOG_PATH          | Path to for the ```dc.log```
| DC_CLIENT_ID         | The ```client_id``` used to connect to the Graph API |
| DC_TENANT_ID         | The ```tenant_id``` of the tenant |
| DC_CLIENT_SECRET     | The ```client_secret_id ``` used by the application to authenticate to the Graph API|

Here's an example on Linux/Mac

```
export DC_CONFIG_PATH=/workspaces/mdatp-devicecontrol/python/mdedevicecontrol.conf
export DC_LOG_PATH=/workspaces/mdatp-devicecontrol/Examples/dc.log
export DC_CLIENT_ID=09df2e26-5097-4912-95f5-XXXXXXXXXXXX
export DC_TENANT_ID=5abce36e-7d75-4ce7-a04d-XXXXXXXXXXXX
export DC_CLIENT_SECRET=xxxxxx
```

On Windows
```
setx DC_CONFIG_PATH c:\Users\xxxxx\OneDrive\Documents\GitHub\mdatp-devicecontrol\python\mdedevicecontrol.conf
setx DC_LOG_PATH c:\\Users\\xxxxx\\OneDrive\\Documents\\dc.log
setx DC_CLIENT_ID 09df2e26-5097-4912-95f5-XXXXXXXXXXXX
setx DC_TENANT_ID=5abce36e-7d75-4ce7-a04d-XXXXXXXXXXXX
setx DC_CLIENT_SECRET=xxxxxx
```

> [!NOTE]
> On Windows, opening a new command shell is required for settings to take effect<BR>
> On Windows, Double shlashes - `\\` are required in the value of `DC_LOG_PATH`<BR>
> If `dc` is connecting as a user, then set `DC_CLIENT_SECRET` to an empty value




### dc init

Initializes the directory optionally from an external source.

```
usage: dc init [-h] [-n NAME] {intune,xlsx} ...

positional arguments:
  {intune,xlsx}         source

options:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  The name of the package
```

```dc``` uses a standard directory structure for organizing a device control deployment

```
   .
   |-package.json
   |-metadata.json
   |-src
   |-macOS
   |---devicecontrol
   |-----policies
   |-windows
   |---devicecontrol
   |-----groups
   |-----rules
```

| Path | Description |
|----  |----
| .    | The root directory of the package
| package.json | Information about the ```policies``` and ```settings``` |
| metadata.json | Information about the deployment in Intune |
| src | A directory containing files that was used to create the directory |
| macOS/devicecontrol/policies | A directory containing the ```.json``` policy files for macOS | 
| windows/devicecontrol/groups | A directory contaning the ```.xml``` files for groups |
| windows/devicecontrol/rules | A directory contaning the ```.xml``` files for rules |

### dc init xlsx

Initializes a directory from an Excel spreadsheet

```
usage: dc init xlsx [-h] -f FILE -n NAME
                    [-d DESCRIPTION] -o OS -v VERSION

options:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  xlsx file to import
  -n NAME, --name NAME  name of the policy
  -d DESCRIPTION, --description DESCRIPTION
                        description of the policy
  -o OS, --os OS
  -v VERSION, --version VERSION
```
Notes:
-   The sheets of the Excel spreadsheet contains information about the rules, groups, and entries to be imported.
-   The ```--os``` value is either ```windows``` or ```macOS```
-   The ```--version``` values is either ```v1``` or ```v2```.  ```v1``` for macOS is custom mobilconfig.  ```v1``` for windows is OMA-URI.  ```v2``` is the settings catalog that the Intune UX uses.   
-   Not all features are supported on all OS and versions

The xlsx import uses the following sheets:

| Sheet | Description |
|---    |---
| Entries | Rows of entries to be used in rules |
| Groups  | Rows of groups to be used in rules.  |
| Rules   | Rows of the information used by rules |
| *group name*| A sheet that contains the group data for a group |
| Settings | Rows on settings and their values

#### Example Group Data sheet

| Descriptor Value Name| VID_PID |
|--- |---
| Device A | 0000_1111
| Device B | 1111_2222

>[!NOTE]
> - The column names are **exactly** the descriptorIds for the groups XML
> - The **Descriptor Value Name** is used to provide a more descriptive name for the entry in reusable settings

#### Example Rules sheet


| Name | Description | Included Groups | Excluded Groups | Entries |
|---   |---          |---              |---              |---      |
| Allow access to allowed USBs | Allow full access and audit write |Allowed USBs||Allow full access,Audit write access |
| Allowed USBs | Allow full access,Audit write access |All Removable Media Devices|Allowed USBs|Deny all access, Audit deny  all access and block|

Note:  
- The name of the groups are comma delimited and **must** match the name of the sheet containing the group data
- The values in the entries are comma delimited and **must** match the name inf the Entries sheet


#### Example Entries sheet


| Name |Type |Disk Read | Disk Write | Disk Execute| File Read| File Write |File Execute |Notification|
|---   |---  |---       |---         |---          |---       |---        |---          |---
Allow full access| Allow |X |X |X |  |  |  |0|
Audit write access| AuditAllowed| | X| | | | |2|

#### Example Groups sheet
| Name | Type | Match |
|---   |---   |---
| Allowed USBs | Device | MatchAll |
| All Removable Media | Device | MatchAll|

 Note:  the name of the group **must** match the name of the sheet containing the group data

 ### Example Settings sheet

 | Setting | Value |
 |---      |---
 | DefaultEnforcement | Allow |
 | DeduplicateAccessEvents | TRUE |

A example spreadsheet is [here](../deployable%20examples/deduplicate_access_events/src/deduplicate_audit_example.xlsx)

### dc init intune

Initializes a directory from Intune

```
usage: dc init intune [-h] -n NAME [-d DESCRIPTION] [-o OS] [-v VERSION] [-p POLICIES]
                      (-u | -a)

options:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  name of the package
  -d DESCRIPTION, --description DESCRIPTION
                        description of the package
  -o OS, --os OS
  -v VERSION, --version VERSION
  -p POLICIES, --policies POLICIES
                        command separated list of policy names to export
  -u, --user            authenticate as the logged in user to the graph API
  -a, --application     authenticate as the application to the graph API
```

### dc validate graph

Validates the connection to the graph API

```
usage: dc validate graph [-h] (-u | -a) {user,application} ...

positional arguments:
  {user,application}  The type of authentication to the graph

options:
  -h, --help          show this help message and exit
  -u, --user
  -a, --application
```

Note:
-  The ```--user``` option will test connectivity for the logged in user.
-  The ```---application``` option will test connectivity for the configure application.

### dc apply

Applies the configuration to Intune

```
usage: dc apply [-h] (-u | -a)

options:
  -h, --help         show this help message and exit
  -u, --user         authenticate as the logged in user to the graph API
  -a, --application  authenticate as the application to the graph API
```

## dc delete

Deletes the objects from Intune

```
usage: dc delete [-h] (-u | -a) [-s]

options:
  -h, --help         show this help message and exit
  -u, --user         authenticate as the logged in user to the graph API
  -a, --application  authenticate as the application to the graph API
  -s, --silent       don't prompt the user to confirm delete
```

## dc patch-graph

Patches issues with the generated graph sdk to work with dc 

```
usage:  dc patch-graph
```

### Known Issues
- The *device_management_reusable_policy_setting_item_request_builder_patch.py* fixes the issue that there is no PUT function on [msgraph_beta/generated/device_management/reusable_settings/item/device_management_configuration_setting_definition_item_request_builder.py](https://github.com/microsoftgraph/msgraph-beta-sdk-python/blob/main/msgraph_beta/generated/device_management/reusable_settings/item/device_management_configuration_setting_definition_item_request_builder.py)

## dcconvert

Converts Windows DC policy XML into equivalent macOS policy JSON.

```
usage: dcconvert [--groups=groups.xml][--rules=rules.xml][--strict][--o=outfile]
```

<details>
<summary>Visual Studio Code configuration</summary>

```json
{
    "name": "Python: Convert device control policy",
    "type": "python",
    "request": "launch",
    "program": "${workspaceFolder}\\python\\convert_dc_policy.py",
    "console": "integratedTerminal",
    "justMyCode": true,
    "args":[
        "--groups=${file}",
        "-o${workspaceFolder}\\Examples\\converted.json"
    ]
}
```
</details>


> [!NOTE]  
> Not all Windows policies can be converted to Mac.  

## dcupgrade

Used to update v1 macOS DC policy plists into the new JSON policy format.

```
usage: dcupgrade [-h] [-o OUTPUT_FILE]
                            v1_policy
```

for example:

```
dcupgrade /workspaces/mdatp-devicecontrol/macOS/mobileconfig/v1/deny_all_mount.mobileconfig
```
Gerenates the following in ``dc_policy.json``

```json
{
  "groups": [
    {
      "$type": "device",
      "id": "9eb96f56-a517-4ab0-9615-d0f0b0bf51be",
      "name": "Removable Storage Devices: All",
      "query": {
        "$type": "and",
        "clauses": [
          {
            "$type": "primaryId",
            "value": "removable_media_devices"
          }
        ]
      }
    }
  ],
  "rules": [
    {
      "id": "38075d0a-77f7-4f61-880b-5014ec900c19",
      "name": "Removable Storage Devices: All",
      "includeGroups": [
        "9eb96f56-a517-4ab0-9615-d0f0b0bf51be"
      ],
      "entries": [
        {
          "$type": "removableMedia",
          "id": "b604eccd-5bd6-4232-ba63-81ecd7801d23",
          "enforcement": {
            "$type": "deny"
          },
          "access": [
            "read",
            "write",
            "execute"
          ]
        },
        {
          "$type": "removableMedia",
          "id": "435b62a4-adf4-4578-abdb-ffecc2b0e4d9",
          "enforcement": {
            "$type": "auditDeny",
            "options": [
              "send_event",
              "show_notification"
            ]
          },
          "access": [
            "read",
            "write",
            "execute"
          ]
        }
      ]
    }
  ],
  "settings": {
    "features": {
      "removableMedia": {
        "disable": false
      }
    },
    "ux": {
      "navigationTarget": "https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/mac-device-control-overview?view=o365-worldwide"
    }
  }
```
<details>
<summary>Visual Studio Code configuration</summary>

```json

        {
            "name": "Convert the v1 file to v2",
            "type": "debugpy",
            "request": "launch",
            "program": "${workspaceFolder}/python/src/mdedevicecontrol/upgrade_dc_policy.py",
            "console": "integratedTerminal",
            "args": [
                "${file}"
            ]
        }
```
</details>


## dcdoc

Used to generate documentaion on device control policies

```
usage: dcdoc [-h] [-q QUERY | -s SCENARIOS | -i IN_FILE]
                [-p SOURCE_PATH] [-f FORMAT] [-o OUT_FILE]
                [-d DEST] [-g GENERATED_FILES_LOCATIONS]
                [-t TEMPLATE] [-rt README_TEMPLATE]
                [-r README_FILE] [-tp TEMPLATES_PATH]

Utility for generating documentation for device control
policies.

options:
  -h, --help            show this help message and exit
  -q QUERY, --query QUERY
                        The query to retrieve the policy
                        rules to process
  -s SCENARIOS, --scenarios SCENARIOS
                        A JSON file that contains a list of
                        scenarios to process
  -i IN_FILE, --input IN_FILE
                        A policy rule to process
  -p SOURCE_PATH, --path SOURCE_PATH
                        The path to search for source files.
                        Defaults to current working
                        directory.
  -f FORMAT, --format FORMAT
                        The format of the output. Defaults    
                        to text.
  -o OUT_FILE, --output OUT_FILE
                        The output file
  -d DEST, --dest DEST  The output directory. Defaults to     
                        current working directory.
  -g GENERATED_FILES_LOCATIONS, --generate GENERATED_FILES_LOCATIONS
                        Generates files for other formats     
  -t TEMPLATE, --template TEMPLATE
                        Jinja2 template to use to generate    
                        output. Defaults to dcutil.j2.        
  -rt README_TEMPLATE, --readme_template README_TEMPLATE      
                        Jinja2 template to use for the        
                        readme. Defaults to readme.j2.        
  -r README_FILE, --readme README_FILE
                        The readme file to generate.
                        Defaults to readme.md.
  -tp TEMPLATES_PATH, --templates_path TEMPLATES_PATH
                        path to Jinja2 templates. Defaults    
                        to templates.
```

```dcdoc``` loads all of the group and policy files found in the ```SOURCE_PATH``` into an inventory.

It then selects files from that inventory for processing. 
-  Select a single file  ```IN_FILE```.
-  Select files defined in a scenario file ```SCENARIOS```.  
   - See [Windows Device Scenarios](/windows/device/scenarios.json), [Windows Printer Scenarios](/windows/printer/scenarios.json), [Windows Getting Started](/windows/Getting%20Started/scenarios.json) or [Mac Scenarios](/macOS/policy/samples/scenarios.json) for examples
-  Select files from the inventory using a query ```QUERY```.  The query uses the [pandas query](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html) syntax.  

The query is run.  As part of running the query, ```dcdoc``` will attempt to generate files in other formats.  The ```GENERATED_FILES_LOCATION``` controls which format of files are generated and where they are saved.  This parameter is a comma delimited list of ```format```:```path``` values (e.g ```oma-uri:c:\dcdoc\output```)

The result of the query is coverted to a ```FORMAT``` - either ```csv``` or ```txt```.  

The ```csv``` option generates a ```dc_rules.csv``` and ```dc_groups.csv``` with the contents of the queries inventory.  

- See the [rules for the examples in this repo](/dc_rules.csv) and [groups for the examples in this repo](/dc_rules.csv) for the format of the files

The  ```txt``` option uses the ```TEMPLATE``` in the [templates](templates/) directory to format the content.  

If the files were defined using ```SCENARIOS```, then a [readme.md](templates/readme.j2) is generated as well.
- See [Windows Device Examples README](/windows/device/readme.md), [Windows Printer Examples README](/windows/printer/readme.md), [Windows Getting Started README](/windows/Getting%20Started/readme.md) or [Mac Samples README](/macOS/policy/samples/README.md) for examples

The output is stored in the ```DEST``` directory.  The name of the file created can be changed from the default using the ```OUT_FILE``` parameter.

### Example Visual Studio Code configurations

The example are [VS Code Python configurations](https://code.visualstudio.com/docs/python/debugging#_additional-configurations).  They can be added to ```launch.json```

<details>
<summary>Generate documentation for a single file</summary>

```json
{
"name": "Python: dcdoc - single file",
"type": "python",
"request": "launch",
"program": "${workspaceFolder}\\python\\src\\mdedevicecontrol\\dcdoc.py",
"args": [
    "--path=${fileDirname}",
    "--input=${relativeFile}",
    "--dest=${workspaceFolder}\\Examples"
],
"console": "integratedTerminal",
"justMyCode": true,
}

```
</details>

<details>
<summary>Generate documentation based on scenarios</summary>

```json
{
"name": "Python: dcdoc with scenarios",
    "type": "python",
    "request": "launch",
    "program": "${workspaceFolder}\\python\\src\\mdedevicecontrol\\dcdoc.py",
    "args": [
        "--path=${fileDirname}",
        "--template=dcutil.j2",
        "--scenarios=${file}",
        "--generate=oma-uri:${fileDirname}\\Intune OMA-URI",
        "--dest=${fileDirname}"
    ],
    "console": "integratedTerminal",
    "justMyCode": true,
}
```
</details>

<details>
<summary>Generate csv report on files</summary>

```json
{
    "name": "Python: dcdoc csv report",
    "type": "python",
    "request": "launch",
    "program": "${workspaceFolder}\\python\\src\\mdedevicecontrol\\dcdoc.py",
    "args": [
        "--path=${workspaceFolder}\\windows;${workspaceFolder}\\macOS",
        "--format=csv",
        "--dest=${workspaceFolder}"
    ],
    "console": "integratedTerminal",
    "justMyCode": true,
}
```
        
</details>

