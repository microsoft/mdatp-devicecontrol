#!/usr/bin/env python3

import xml.etree.ElementTree as ET
import argparse
import os
import pandas as pd
import jinja2
import pathlib


class Group:

    def __init__(self,root):
        self.id = root.attrib["Id"]
        if "Type" in root.attrib.keys():
            self.type = root.attrib["Type"]
        else:
            self.type = "Device"

        name_node = root.find(".//Name")
        if name_node is None:
            self.name = "?"
        else:
            self.name = name_node.text

        match_node = root.find(".//MatchType")
        if match_node is None:
            if "MatchType" in root.attrib.keys():
                self.match_type = root.attrib["MatchType"]
            else:
                self.match_type = "?"
        else:
            self.match_type = match_node.text

        self.properties = {}
        descriptors = root.findall("./DescriptorIdList//")
        for descriptor in descriptors:
            self.properties[descriptor.tag] = descriptor.text
        return

class PolicyRule:

    def __init__(self,root):
        self.id = root.attrib["Id"]
        name_node = root.find(".//Name")
        if name_node is None:
            self.name = "?"
        else:
            self.name = name_node.text

        self.included_groups = []
        self.excluded_groups = []
        self.entries = []

        included_groups_node = root.find(".//IncludedIdList")
        if not included_groups_node is None:
            groups = included_groups_node.findall(".//GroupId")
            for group in groups:
                self.included_groups.append(group.text)

        excluded_groups_node = root.find(".//ExcludedIdList")
        if not excluded_groups_node is None:
            groups = excluded_groups_node.findall(".//GroupId")
            for group in groups:
                self.excluded_groups.append(group.text)

        for entry in root.findall(".//Entry"):
            self.entries.append(Entry(entry))        

        return

class Entry:

    def __init__(self,entry):
        self.id = entry.attrib["Id"]
        self.type = entry.find("./Type").text
        self.options = entry.find("./Options").text
        self.access_mask = entry.find("./AccessMask").text

        sid = entry.find("./Sid")
        if sid is not None:
            self.sid = sid.text
        else:
            self.sid = None

        parameters = entry.find("./Parameters")
        if parameters is not None:
            self.parameters = Parameters(parameters)
        else:
            self.parameters = None
        return
    
    def get_group_ids(self):
        if self.parameters is not None:
            return self.parameters.get_group_ids()
        else:
            return []
    
class Parameters:

    def __init__(self,parameters):
        self.match_type = parameters.attrib['MatchType']
        self.conditions = []
        for condition in parameters.findall("./"):
            match condition.tag:
                case "Network":
                    self.conditions.append(Condition(condition))
                case "VPNConnection":
                    self.conditions.append(Condition(condition))
                case "File":
                    self.conditions.append(Condition(condition))
                case "Parameters":
                    self.conditions.append(Parameters(condition))
                case other:
                    raise Exception('Unknown condition '+condition.tag)

    def get_group_ids(self):
        groups = []
        for condition in self.conditions:
            group_ids = condition.get_group_ids()
            for group_id in group_ids:
                groups.append(group_id)

        return groups


class Condition:
    def __init__(self,condition):
        self.match_type = condition.attrib['MatchType']
        self.groups = []
        self.condition_type = condition.tag
        for group in condition.findall(".//GroupId"):
            self.groups.append(group.text)

    def get_group_ids(self):
        return self.groups


class Inventory:

 
    def __init__(self,source_path):
        self.paths = source_path

        group_columns = {
            "type":[],
            "path":[],
            "name":[],
            "id":[],
            "match_type":[],
            "object":[]
        }

        rule_columns = {
            "path":[],
            "name":[],
            "id":[],
            "included_groups":[],
            "excluded_groups":[],
            "object":[]
        }

        self.groups = pd.DataFrame(group_columns)
        self.policy_rules = pd.DataFrame(rule_columns)

        self.load_inventory()

        

    def load_inventory(self):
        for path in self.paths:
            for dir in os.walk(top=path):
                files = dir[2]
                for file in files:
                    if str(file).endswith(".xml"):
                        xml_path = dir[0]+os.sep+file
                        self.load_file(xml_path)

    def load_file(self,xml_path):
        try:
            with open(xml_path) as file:
                root = ET.fromstring(file.read())
                match root.tag:
                    case "Group":
                        self.addGroup(Group(root),xml_path)
                    case "Groups":
                        for group in root.findall(".//Group"):
                            self.addGroup(Group(group),xml_path)
                    case "PolicyRule":
                        self.addPolicyRule(PolicyRule(root),xml_path)
                    case "PolicyRules":
                        for policyRule in root.findall(".//PolicyRule"):
                            self.addPolicyRule(PolicyRule(policyRule),xml_path)

                return root

        except Exception as e:
            print ("Error in "+xml_path+": "+e.msg)
            return

    def addGroup(self,group,path):

        new_row = pd.DataFrame([{
            "type":group.type,
            "path":path,
            "name":group.name,
            "id":group.id,
            "match_type":group.match_type,
            "object": group
        }])

        self.groups = pd.concat([self.groups,new_row],ignore_index=True)

    def addPolicyRule(self,rule,path):

        new_row = pd.DataFrame([{
            "path":path,
            "name":rule.name,
            "id":rule.id,
            "included_groups":rule.included_groups,
            "excluded_groups":rule.excluded_groups,
            "object": rule
        }])

        self.policy_rules = pd.concat([self.policy_rules,new_row],ignore_index=True)

        return
    
    def get_groups_for_rule(self,rule):
        groups_for_rule = {}
        for included_group in rule.included_groups:
            g = self.get_group_by_id(included_group)
            groups_for_rule[g.id] = g

        for excluded_group in rule.excluded_groups:
            g = self.get_group_by_id(excluded_group)
            groups_for_rule[g.id] = g

        for entry in rule.entries:
            groups = entry.get_group_ids()
            for entry_group in groups:
                g = self.get_group_by_id(entry_group)
                groups_for_rule[g.id] = g
        
        return groups_for_rule


    def get_group_by_id(self,group_id):
        group_frame = self.groups.query("id == '"+group_id+"'")
        return group_frame.iloc[0]["object"]


def dir_path(string):
    paths = string.split(os.pathsep)
    for path in paths:
        if os.path.isdir(path):
            continue
        else:
            raise NotADirectoryError(path)
    return paths

def format(string):
    match string:
        case "text":
            return string
        case other:
            raise argparse.ArgumentError("Invalid format "+string)

if __name__ == '__main__':

    arg_parser = argparse.ArgumentParser(
        description='Utility for importing/exporting device control policies.')

    arg_parser.add_argument('-p', '--path', type=dir_path, dest="source_path", help='The path to search for source files',default=".")
    arg_parser.add_argument('-q','--query',dest="query",help='The query to retrieve the policy rules to process',default='path.str.contains(".xml")')
    arg_parser.add_argument('-f','--format',type=format, dest="format",help="The format of the output (text)",default="text")
    arg_parser.add_argument('-o','--output',dest="out_path",help="The output path",default="dcutil.out")
    arg_parser.add_argument('-t','--template',dest="template",help="Jinja template to use to generate output",default="dcutil.out.tmpl")

    args = arg_parser.parse_args()

    inventory = Inventory(args.source_path)

    filtered_rules = inventory.policy_rules.query(args.query, engine='python')

    rules = {}
    groups = {}
    for ind in filtered_rules.index:
        rule = filtered_rules['object'][ind]
        rules[rule.id] = rule
        groups_for_rule = inventory.get_groups_for_rule(rule)
        for group in groups_for_rule:
            groups[group] = groups_for_rule[group]

    if args.format == "text":
        templatePath = pathlib.Path(__file__).parent.resolve()
        templateLoader = jinja2.FileSystemLoader(searchpath=templatePath)
        templateEnv = jinja2.Environment(loader=templateLoader)
        TEMPLATE_FILE = args.template
        template = templateEnv.get_template(TEMPLATE_FILE)
        out = template.render({"rules":rules,"groups":groups})
        with open(args.out_path,"w") as out_path:
            out_path.write(out)
            out_path.close()