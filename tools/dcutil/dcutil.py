#!/usr/bin/env python3

import xml.etree.ElementTree as ET
import argparse
import os
import pandas as pd


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
        self.type = entry.find(".//Type").text
        self.options = entry.find(".//Options").text
        self.access_mask = entry.find(".//AccessMask").text

        parameters = entry.find(".//Parameters")
        if parameters is not None:
            print(parameters)
        return
    
class Inventory:

 
    def __init__(self,source_path):
        self.paths = source_path

        group_columns = {
            "type":[],
            "path":[],
            "name":[],
            "id":[],
            "match_type":[]
        }

        rule_columns = {
            "path":[],
            "name":[],
            "id":[],
            "included_groups":[],
            "excluded_groups":[]
        }

        self.groups = pd.DataFrame(group_columns)
        self.policy_rules = pd.DataFrame(rule_columns)

        self.load_inventory()

        print(self.groups)

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
                print (root.tag)
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
            return

    def addGroup(self,group,path):

        new_row = pd.DataFrame([{
            "type":group.type,
            "path":path,
            "name":group.name,
            "id":group.id,
            "match_type":group.match_type
        }])

        self.groups = pd.concat([self.groups,new_row],ignore_index=True)

    def addPolicyRule(self,rule,path):

        new_row = pd.DataFrame([{
            "path":path,
            "name":rule.name,
            "id":rule.id,
            "included_groups":rule.included_groups,
            "excluded_groups":rule.excluded_groups
        }])

        self.policy_rules = pd.concat([self.policy_rules,new_row],ignore_index=True)

        return


def dir_path(string):
    paths = string.split(os.pathsep)
    for path in paths:
        if os.path.isdir(path):
            continue
        else:
            raise NotADirectoryError(path)
    return paths

if __name__ == '__main__':

    arg_parser = argparse.ArgumentParser(
        description='Utility for importing/exporting device control policies.')

    arg_parser.add_argument('-p', '--path', type=dir_path, dest="source_path", help='The path to search for source files',default=".")

    args = arg_parser.parse_args()

    inventory = Inventory(args.source_path)