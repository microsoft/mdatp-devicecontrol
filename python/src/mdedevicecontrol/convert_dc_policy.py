#!/usr/bin/env python3

import xml.etree.ElementTree as ET

import logging
logger = logging.getLogger(__name__)

def log_error(text):
    print("\033[0;31m" + text + "\033[00m")

def log_warning(text, strict):
    if strict:
        raise Exception(text)
    else:
        print("\033[0;93m" + text + "\033[00m")

def convert_match_type(match_type, strict):
    match match_type:
        case 'MatchAny':
            return 'or'
        case 'MatchAll':
            return 'and'
        case 'MatchExcludeAll':
            return 'not'
        case 'MatchExcludeAny':
            return 'not'
        case _:
            log_warning(f'Unknown match type {match_type}', strict)
            return None


def convert_primary_id_clause(primary_id, strict):
    clause = {}
    match primary_id:
        case 'RemovableMediaDevices':
            clause["$type"] = "primaryId"
            clause["value"] = "removable_media_devices"
        case 'WpdDevices':
            portable_devices = {}
            portable_devices["$type"] = "primaryId"
            portable_devices["value"] = "portable_devices"

            apple_devices = {}
            apple_devices["$type"] = "primaryId"
            apple_devices["value"] = "apple_devices"

            clause["$type"] = "or"
            clause["query"] = [portable_devices, apple_devices]
        case _:
            log_warning(f"Primary ID [{primary_id}] is not supported on macOS.", strict)
            return None
    
    return clause

def convert_vid_pid_clause(vid_pid, strict):
    vid_pid_split = vid_pid.split('_')
    vid = vid_pid_split[0]
    pid = vid_pid_split[1]

    vendor_id_clause = {}
    vendor_id_clause["$type"] = "vendorId"
    vendor_id_clause["value"] = vid

    product_id_clause = {}
    product_id_clause["$type"] = "productId"
    product_id_clause["value"] = pid

    clause = {}
    clause["$type"] = "and"
    clause["clauses"] = [ vendor_id_clause, product_id_clause ]

    return clause

def convert_serial_number_clause(serial_number, strict):
    clause = {}
    clause["$type"] = "serialNumber"
    clause["value"] = serial_number

    return clause 

def convert_clauses(descriptor_id_list, strict):
    clauses = []

    for descriptor_id in descriptor_id_list:
        match descriptor_id.tag:
            case 'PrimaryId':
                primary_id_clause = convert_primary_id_clause(descriptor_id.text, strict)
                if primary_id_clause is not None:
                    clauses.append(primary_id_clause)
            case 'VID_PID':
                vid_pid_clause = convert_vid_pid_clause(descriptor_id.text, strict)
                if vid_pid_clause is not None:
                    clauses.append(vid_pid_clause)
            case 'SerialNumberId':
                serial_number_clause = convert_serial_number_clause(descriptor_id.text, strict)
                if serial_number_clause is not None:
                    clauses.append(serial_number_clause)
            case _:
                log_warning(f"Unsupported Descriptor ID {descriptor_id.tag}", strict)

    return clauses

def convert_query(match_type, descriptor_id_list, strict):
    query = {}
    
    match match_type:
        case 'MatchAny':
            query["$type"] = 'or'
            query["clauses"] = convert_clauses(descriptor_id_list, strict)
        case 'MatchAll':
            query["$type"] = 'and'
            query["clauses"] = convert_clauses(descriptor_id_list, strict)
        case 'MatchExcludeAll':
            query["$type"] = 'not'
            query["query"] = convert_query("MatchAll, descriptor_id_list, strict")
        case 'MatchExcludeAny':
            query["$type"] = 'not'
            query["query"] = convert_query("MatchAny, descriptor_id_list, strict")
        case _:
            log_warning(f'Unknown match type {match_type}', strict)
            return None

    return query


def convert_group(group, strict):
    converted_group = {
        "$type": "device"
    }

    id = group.attrib['Id']
    if id is None:
        log_warning("'Id' is not defined for group.", strict)
        return None

    print(f'Converting Group: ID={id}')
    converted_group['id'] = id[1:-1]

    match_type = group.find('MatchType')
    if match_type is None:
        log_warning("Group does not have a MatchType element.")
        return None

    descriptor_id_list = group.find('DescriptorIdList')
    if descriptor_id_list is None:
        log_warning("Group does not have a DescriptorIdList element.")
        return None

    query = convert_query(match_type.text, descriptor_id_list, strict)
    if query is None:
        return None

    converted_group['query'] = query

    return converted_group

def convert_groups(root, strict):
    print('Converting Groups...')

    groups = []

    
    if root.tag != "Groups":
        raise Exception('Invalid Groups XML')

    for group in root:
        if group.tag != "Group":
            log_warning(f"Unknown XML Element: {group.tag}", strict)
            continue

        converted_group = convert_group(group, strict)
        if (converted_group is not None):
            groups.append(converted_group)
    
    return groups

def convert_id_list(id_list, strict):
    groups = []

    for group_id in id_list:
        if group_id.tag != "GroupId":
            log_warning(f"Unknown XML element in IdList {group_id.tag}", strict)
            continue

        groups.append(group_id.text[1:-1])
    
    return groups

def convert_enforcement(entry_type, options, strict):
    enforcement = {}

    match entry_type:
        case "Allow":
            enforcement['$type'] = "allow"

            if options != 0:
                converted_options = []

                if options & 0x4 != 0:
                    converted_options.append('disable_audit_allow')
                    converted_options.append('disable_audit_deny')
                    options = options & ~0x4

                if options != 0:
                    log_warning(f"Unsupported Allow options [{hex(options)}]", strict)

                enforcement['options'] = converted_options
        case "Deny":
            enforcement['$type'] = "deny"

            if options != 0:
                converted_options = []

                if options & 0x4 != 0:
                    converted_options.append('disable_audit_deny')
                    options = options & ~0x4

                if options != 0:
                    log_warning(f"Unsupported Deny options [{hex(options)}]", strict)

                enforcement['options'] = converted_options
        case "AuditAllow":
            enforcement['$type'] = "auditAllow"

            if options != 0:
                converted_options = []

                if options & 0x2 != 0:
                    converted_options.append('send_event')
                    options = options & ~0x2

                if options != 0:
                    log_warning(f"Unsupported AuditAllow options [{hex(options)}]", strict)

                enforcement['options'] = converted_options
        case "AuditDeny":
            enforcement['$type'] = "auditDeny"

            if options != 0:
                converted_options = []

                if options & 0x1 != 0:
                    converted_options.append('show_notification')
                    options = options & ~0x1

                if options & 0x2 != 0:
                    converted_options.append('send_event')
                    options = options & ~0x2

                if options != 0:
                    log_warning(f"Unsupported AuditDeny options [{hex(options)}]", strict)

                enforcement['options'] = converted_options
        case _:
            log_warning(f"Unsupported entry type [{entry_type}]", strict)
    
    return enforcement

def convert_access(access, strict):
    converted_access = []

    if access & 0x1 != 0:
        converted_access.append('generic_read')
        access = access & ~0x1

    if access & 0x2 != 0:
        converted_access.append('generic_write')
        access = access & ~0x2

    if access & 0x4 != 0:
        converted_access.append('generic_execute')
        access = access & ~0x4

    if access != 0:
        log_warning(f"Unsupported AccessMask [{hex(access)}]", strict)

    if len(converted_access) == 0:
        log_warning(f"No valid AccessMask", strict)
        return None


    return converted_access

def convert_entry(entry, strict):
    converted_entry = {}

    converted_entry['$type'] = "generic"

    id = entry.attrib['Id']
    if id is None:
        log_warning("'Id' is not defined for rule.", strict)
        return None
    
    converted_entry['id'] = id[1:-1]

    entry_type = entry.find("Type")
    if entry_type is None:
        log_warning("Entry does not contain a Type element.", strict)
        return None
    
    options_element = entry.find("Options")
    if options_element is not None:
        options = int(options_element.text)
    else:
        options = 0

    enforcement = convert_enforcement(entry_type.text, options, strict)
    if enforcement is None:
        return None
    
    converted_entry["enforcement"] = enforcement

    access_element = entry.find("AccessMask")
    if access_element is None:
        log_warning("Entry does not contain an AccessMask element.")
        return None

    converted_access = convert_access(int(access_element.text), strict)
    if converted_access is None:
        return None
    
    converted_entry["access"] = converted_access

    return converted_entry

def convert_entries(entries, strict):
    converted_entries = []

    for entry in entries:
        converted_entry = convert_entry(entry, strict)
        if converted_entry is not None:
            converted_entries.append(converted_entry)
            
    if len(converted_entries) == 0:
        log_warning(f"No valid entries", strict)
        return None
        
    return converted_entries
        

def convert_rule(rule, strict):
    converted_rule = {}

    id = rule.attrib['Id']
    if id is None:
        log_warning("'Id' is not defined for rule.", strict)
        return None

    print(f'Converting Rule: ID={id}')
    converted_rule['id'] = id[1:-1]

    name = rule.find('Name')
    if name is None:
        log_warning("Rule does not have a Name element.")
        return None

    converted_rule['name'] = name.text

    included_id_list = rule.find('IncludedIdList')
    include_groups = convert_id_list(included_id_list, strict)
    if include_groups is not None:
        converted_rule['includeGroups'] = include_groups

    exluded_id_list = rule.find('ExcludedIdList')
    if exluded_id_list is not None:
        exclude_groups = convert_id_list(exluded_id_list, strict)
        if exclude_groups is not None:
            converted_rule['excludeGroups'] = exclude_groups

    entries = rule.findall('Entry')
    if entries is None:
        log_warning('Rule does not have any Entry elements.')
        return None

    converted_entries = convert_entries(entries, strict)
    if converted_entries is None:
        return None

    converted_rule['entries'] = converted_entries
    
    return converted_rule

def convert_rules(root, strict):
    print('Converting Rules...')
    
    rules = []

    if root.tag != "PolicyRules":
        raise Exception('Invalid Groups XML')

    for rule in root:
        if rule.tag != "PolicyRule":
            log_warning(f"Unknown XML Element: {rule.tag}", strict)
            continue

        converted_rule = convert_rule(rule, strict)
        if (converted_rule is not None):
            rules.append(converted_rule)

    return rules

def main():
    import argparse
    import json

    arg_parser = argparse.ArgumentParser(
        description='Converts an existing DC policy written for Windows into an equivalent policy for macOS.')

    arg_parser.add_argument('-g', '--groups', type=argparse.FileType('r', encoding='UTF-8'), dest="groups_file", help='The Windows DC policy group definitions xml')
    arg_parser.add_argument('-r', '--rules', type=argparse.FileType('r', encoding='UTF-8'), dest="rules_file", help='The Windows DC policy rule definitions xml')
    arg_parser.add_argument('-s', '--strict', action='store_true', help='Fail conversion if any unsupported elements are encountered.')
    arg_parser.add_argument('-o', '--output', type=argparse.FileType('w', encoding='UTF-8'), default='dc_policy.json', dest="output_file", help='Specify the output file.  Defaults to dc_policy.json.')

    args = arg_parser.parse_args()

    try:
        if args.groups_file is None and args.rules_file is None:
            raise Exception('At least --groups or --rules must be specified')

        converted_policy = {}

        if args.groups_file is not None:
            groups_root = ET.fromstring(args.groups_file.read())
            converted_policy["groups"] = convert_groups(groups_root, args.strict)

        if args.rules_file is not None:
            rules_root = ET.fromstring(args.rules_file.read())
            converted_policy["rules"] = convert_rules(rules_root, args.strict)

        args.output_file.write(json.dumps(converted_policy, indent=2))
    except Exception as e:
        log_error("Failed to convert policy:")
        log_error(str(e))

if __name__ == '__main__':
    main()