#!/usr/bin/env python3

import uuid

def log_error(text):
    print("\033[0;31m" + text + "\033[00m")

def log_warning(text):
    print("\033[0;93m" + text + "\033[00m")

def upgrade_settings(navigation_target):
    upgraded_settings = {
        "features": {
            "removableMedia": {
                "disable": False
            }
        }
    }

    if navigation_target is not None:
        upgraded_settings['ux']= {
            "navigationTarget": navigation_target
        }

    return upgraded_settings

def convert_permissions(permissions):
    access = ["read", "write", "execute"]

    if "none" in permissions:
        return access

    for permission in permissions:
        match permission:
            case "read":
                access.remove("read")
            case "write":
                access.remove("write")
            case "execute":
                access.remove("execute")
            case _:
                log_warning(f"Unsupported permission: [{permission}")

    return access

def add_deny_entries(rule, permissions):
    access = convert_permissions(permissions)

    if len(access) > 0:
        # Deny everything we don't have permission for
        deny_entry_id = str(uuid.uuid4())
        deny_entry = {
            "$type": "removableMedia",
            "id": deny_entry_id,
            "enforcement": {
                "$type": "deny"
            },
            "access": access
        }

        # Make sure to send telemetry and show ux
        audit_deny_entry_id = str(uuid.uuid4())
        audit_deny_entry = {
            "$type": "removableMedia",
            "id": audit_deny_entry_id,
            "enforcement": {
                "$type": "auditDeny",
                "options": [
                    "send_event",
                    "show_notification"
                ]
            },
            "access": access
        }

        rule["entries"].append(deny_entry)
        rule["entries"].append(audit_deny_entry)

    if len(access) < 3:
        # Allow everything that makes it past the deny entry
        # Otherwise, this device may match another group/rule
        allow_entry_id = str(uuid.uuid4())
        allow_entry = {
            "$type": "removableMedia",
            "id": allow_entry_id,
            "enforcement": {
                "$type": "allow"
            },
            "access": [
                "read",
                "write",
                "execute"
            ]
        }

        rule["entries"].append(allow_entry)

def add_allow_entries(rule, permissions):
    access = convert_permissions(permissions)

    # Allow all permissions, so that only this rule gets evaluated
    allow_entry_id = str(uuid.uuid4())
    allow_entry = {
        "$type": "removableMedia",
        "id": audit_allow_entry_id,
        "enforcement": {
            "$type": "allow"
        },
        "access": [
            "read",
            "write",
            "execute"
        ]
    }

    # Only send telemetry on items that would be blocked
    audit_allow_entry_id = str(uuid.uuid4())
    audit_allow_entry = {
        "$type": "removableMedia",
        "id": audit_allow_entry_id,
        "enforcement": {
            "$type": "auditAllow",
            "options": [
                "send_event"
            ]
        },
        "access": access
    }

    rule["entries"].append(allow_entry)
    rule["entries"].append(audit_allow_entry)

def add_entries(rule, permissions, block):
    if block:
        add_deny_entries(rule, permissions)
    else:
        add_allow_entries(rule, permissions)

def add_serial_number_rule(upgraded_policy, vendor_id, product_id, serial_numbers, block):
    for serial_number in serial_numbers:
        print('Adding rule for Serial Number: ' + serial_number)
        permissions = serial_numbers[serial_number]

        group_id = str(uuid.uuid4())
        group = {
            "$type": "device",
            "id": group_id,
            "name": "Removable Storage Devices: Vendor " + vendor_id + ", Product " + product_id + ", Serial Number " + serial_number,
            "query": {
                "$type": "and",
                "clauses": [
                    {
                        "$type": "primaryId",
                        "value": "removable_media_devices"
                    },
                    {
                        "$type": "vendorId",
                        "value": vendor_id
                    },
                    {
                        "$type": "productId",
                        "value": product_id
                    },
                    {
                        "$type": "serialNumber",
                        "value": serial_number
                    }
                ]
            }
        }

        rule_id = str(uuid.uuid4())
        rule = {
            "id": rule_id,
            "name": "Removable Storage Devices: Vendor " + vendor_id + ", Product " + product_id + ", Serial Number " + serial_number,
            "includeGroups": [
                group_id
            ],
            "entries": []
        }

        add_entries(rule, permissions, block)

        upgraded_policy["groups"].append(group)
        upgraded_policy["rules"].append(rule)


def add_product_rules(upgraded_policy, vendor_id, products, block):
    for product_id in products:
        print('Adding rule for product: ' + product_id)
        product = products[product_id]

        group_id = str(uuid.uuid4())
        group = {
            "$type": "device",
            "id": group_id,
            "name": "Removable Storage Devices: Vendor " + vendor_id + ", Product " + product_id,
            "query": {
                "$type": "and",
                "clauses": [
                    {
                        "$type": "primaryId",
                        "value": "removable_media_devices"
                    },
                    {
                        "$type": "vendorId",
                        "value": vendor_id
                    },
                    {
                        "$type": "productId",
                        "value": product_id
                    }
                ]
            }
        }

        rule_id = str(uuid.uuid4())
        rule = {
            "id": rule_id,
            "name": "Removable Storage Devices: Vendor " + vendor_id + ", Product " + product_id,
            "includeGroups": [
                group_id
            ],
            "entries": []
        }

        permissions = product["permission"]

        add_entries(rule, permissions, block)

        upgraded_policy["groups"].append(group)
        upgraded_policy["rules"].append(rule)

        if 'serialNumbers' in product:
            add_serial_number_rule(upgraded_policy, vendor_id, product_id, product['serialNumbers'], block)


def add_vendor_rules(upgraded_policy, vendors, block):
    for vendor_id in vendors:
        print('Adding rule for vendor: ' + vendor_id)
        vendor = vendors[vendor_id]

        group_id = str(uuid.uuid4())
        group = {
            "$type": "device",
            "id": group_id,
            "name": "Removable Storage Devices: Vendor " + vendor_id,
            "query": {
                "$type": "and",
                "clauses": [
                    {
                        "$type": "primaryId",
                        "value": "removable_media_devices"
                    },
                    {
                        "$type": "vendorId",
                        "value": vendor_id
                    }
                ]
            }
        }

        rule_id = str(uuid.uuid4())
        rule = {
            "id": rule_id,
            "name": "Removable Storage Devices: Vendor " + vendor_id,
            "includeGroups": [
                group_id
            ],
            "entries": []
        }

        permissions = vendor["permission"]

        add_entries(rule, permissions, block)

        upgraded_policy["groups"].append(group)
        upgraded_policy["rules"].append(rule)

        if 'products' in vendor:
            add_product_rules(upgraded_policy, vendor_id, vendor['products'], block)


def add_global_rule(upgraded_policy, block, removable_media_policy):
    print("Adding global rule")
    group_id = str(uuid.uuid4())
    group = {
        "$type": "device",
        "id": group_id,
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

    rule_id = str(uuid.uuid4())
    rule = {
        "id": rule_id,
        "name": "Removable Storage Devices: All",
        "includeGroups": [
            group_id
        ],
        "entries": []
    }

    permissions = removable_media_policy["permission"]

    add_entries(rule, permissions, block)

    upgraded_policy['groups'].append(group)
    upgraded_policy['rules'].append(rule)

    if 'vendors' in removable_media_policy:
        add_vendor_rules(upgraded_policy, removable_media_policy["vendors"], block)

def upgrade_removable_media_policy(removable_media_policy):
    upgraded_policy = {
        "groups": [],
        "rules": []
    }

    if 'enforcementLevel' not in removable_media_policy:
        raise Exception("'removableMediaPolicy' does not contain an 'enforcementLevel' key")

    block = removable_media_policy["enforcementLevel"] == "block"

    if 'permission' not in removable_media_policy:
        raise Exception("'removableMediaPolicy' does not contain a 'permission' key")

    add_global_rule(upgraded_policy, block, removable_media_policy)

    # Reverse the rules so they go from most specific to least specific
    upgraded_policy["rules"].reverse()

    return upgraded_policy


def upgrade_v1_policy(v1_policy):
    import plistlib 

    policy = plistlib.load(v1_policy)

    if 'deviceControl' not in policy:
        raise Exception("Policy does not contain a 'deviceControl' key")
        
    device_control = policy['deviceControl']
        
    if 'removableMediaPolicy' not in device_control:
        raise Exception("'deviceControl' key does not contain a 'removableMediaPolicy'")

    removable_media_policy = device_control['removableMediaPolicy']
    
    upgraded_policy = upgrade_removable_media_policy(removable_media_policy)

    upgraded_policy["settings"] = upgrade_settings(device_control.get('navigationTarget'))

    return upgraded_policy



def main():
    import argparse
    import json

    arg_parser = argparse.ArgumentParser(
        description='Upgrades an existing Device Control for macOS v1 policy into a Device Control for macOS v2 policy.')

    arg_parser.add_argument(type=argparse.FileType('rb'), dest="v1_policy", help='The v1 policy plist')
    arg_parser.add_argument('-o', '--output', type=argparse.FileType('w', encoding='UTF-8'), default='dc_policy.json', dest="output_file", help='Specify the output file.  Defaults to dc_policy.json.')

    args = arg_parser.parse_args()

    try:
        upgraded_policy = upgrade_v1_policy(args.v1_policy)

        args.output_file.write(json.dumps(upgraded_policy, indent=2))
    except Exception as e:
        log_error("Failed to convert policy:")
        log_error(str(e))

if __name__ == '__main__':
    main()