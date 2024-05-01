# Device control - Python

Useful python scripts for interacting with Device Control

## Getting started

1. Install [python 3.10](https://www.python.org/downloads/release/python-3100/) or greater
2. Install the package locally

```
python3 -m pip install --upgrade build
python3 -m build
pip3 install -e
```

This will create the link to the command line tools

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


## devicecontrol.py

Python API for device control files.