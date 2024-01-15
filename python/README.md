# Device control - Python

Useful python scripts for interacting with Device Control

## Getting started

1. Install [python 3.10](https://www.python.org/downloads/release/python-3100/) or greater
2. Install the required python libraries

```
pip3 install -r requirements.txt
```

## convert_dc_policy.py

Used to convert Windows DC policy XML into equivalent macOS policy JSON.

```
usage: convert_dc_policy.py [--groups=groups.xml][--rules=rules.xml][--strict][--o=outfile]
```

> [!NOTE]  
> Not all Windows policies can be converted to Mac.  

## upgrade_dc_policy.py

Used to update v1 macOS DC policy plists into the new JSON policy format.

```
usage: upgrade_dc_policy.py [-h] [-o OUTPUT_FILE]
                            v1_policy
```

## dcutil.py

Used to generate documentaion on device control files

## devicecontrol.py

Python API for device control files.