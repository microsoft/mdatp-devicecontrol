# Device control - Python

Utilities for Device Control

## Getting Started

- Fork the repo
- [Install and Configure](#installation-and-configuration) ```dc``` including configuring the connection to the graph API.
- To deploy an example, go to one of the directories in the ```deployable examples```, and type ```dc apply```
- To import a configuration from an Excel file *<xlsx-file>* and deploy it to Intune:
    -   Create a directory for the project called *<package-dir>*
    -   ```cd package-dir```
    -   ```dc init xlsx --file <xlsx-file> --name <name of the project> --description <description for the project> --os [windows|macOs] --version [v1|v2]```
    -  ```dc apply --user```

## Installation and Configuration

1. Install [python 3.10](https://www.python.org/downloads/release/python-3100/) or greater
2. Install the package locally

```
python3 -m pip install --upgrade build
python3 -m build
pip3 install -e
```

3. Set-up the environment

| Environment Variable | Description |
|---                   |---
| DC_CONFIG_PATH       | Path to the ```mdedevicecontrol.conf```
| DC_LOG_PATH          | Path to for the ```dc.log```
| DC_CLIENT_ID         | The ```client_id``` used to connect to the Graph API |
| DC_TENANT_ID         | The ```tenant_id``` of the tenant |
| DC_CLIENT_SECRET     | The ```client_secret_id ``` used by the application to authenticate to the Graph API|

Note:
- ```dc``` The logging settings are in the ```DC_CONFIG_PATH```
- ```dc``` can use either a user or application identity to connect to the Graph API.  In order to connect to the graph API, ```dc``` needs credentials to connect.  The instructions for authenticating as the logged in user (user credentials) are found [here](https://learn.microsoft.com/en-us/graph/tutorials/python?tabs=aad&tutorial-step=1).  The instructions for authenticating as an application are found here [here](https://learn.microsoft.com/en-us/graph/tutorials/python-app-only?tabs=aad&tutorial-step=1)
- ```dc``` uses the ```DeviceManagementConfiguration.ReadWrite.All Directory.Read.All``` scopes to read information from Entra Id, and read/write information to Intune.
- ```dc``` reads the credentials information from the environment variables.



## dc
```
usage: dc [-h] {init,update,apply,validate} ...

Utility for device control

positional arguments:
  {init,update,apply,validate}
                        The operation
    init                Initialize the directory
    update              Update the configuration from
                        the source
    apply               Apply the configuraion to
                        Intune
    validate            Validate the configuration

options:
  -h, --help            show this help message and exit
```


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
| *<group name>*| A sheet that contains the group data for a group |

#### Example Group Data sheet

| VID_PID |
|---
| 0000_1111
| 1111_2222

Note
- The column names are **exactly** the descriptorIds for the groups XML

#### Example Rules sheet


| Name | Description | Included Groups | Excluded Groups | Entries |
|---   |---          |---              |---              |---      |
| Allow access to allowed USBs | Allow full access and audit write |Allowed USBs||Allow full access,Audit write access |
| Allowed USBs | Allow full access,Audit write access |All Removable Media Devices|Allowed USBs|Deny all access, Audit deny  all access and block|

Note:  
- The name of the groups are comman delimited and **must** match the name of the sheet containing the group data
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

A example spreadsheet is [here](../examples/bitlocker/src/bitllocker_dc_example.xlsx/)


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

<details>
<summary>Visual Studio Code configuration</summary>

```json
 {
     "name": "Python: Upgrade device control Policy",
     "type": "python",
     "request": "launch",
     "program": "${workspaceFolder}\\python\\upgrade_dc_policy.py",
     "console": "integratedTerminal",
     "justMyCode": true,
     "args":[
         "${file}",
         "-o${workspaceFolder}\\Examples\\upgrade.json"
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

