#!/usr/bin/env python3

import xml.etree.ElementTree as ET
import argparse
import os
import pandas as pd
import jinja2
import pathlib
import urllib.parse


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

        self.properties = []
        descriptors = root.findall("./DescriptorIdList//")
        for descriptor in descriptors:
            self.properties.append({descriptor.tag: descriptor.text})
        return


    def toXML(self,indent = "\t"):

        out = indent + "<Group Id=\""+self.id+"\" Type=\""+self.type+"\">\n"
        out +=indent + "\t<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/"+urllib.parse.quote_plus(self.id)+"/GroupData -->\n"
        out +=indent + "\t<Name>"+self.name+"</Name>\n"
        out +=indent + "\t<MatchType>"+self.match_type+"</MatchType>\n"
        out +=indent + "\t<DescriptorIdList>\n"
        
        for property in self.properties:
            tag = list(property.keys())[0]
            text = property[tag]

            out += indent +"\t\t<"+tag+">"+text+"</"+tag+">\n"

        out += indent +"\t</DescriptorIdList>\n"
        out += indent +"</Group>"

        return out

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

    def toXML(self,indent = "\t"):

        out = indent + "<PolicyRule Id=\""+self.id+"\" >\n"
        out +=indent + "\t<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/"+urllib.parse.quote_plus(self.id)+"/RuleData -->\n"
        out +=indent + "\t<Name>"+self.name+"</Name>\n"
        
        out +=indent + "\t<IncludedIdList>\n"
        for group in self.included_groups:
            out += indent +"\t\t<GroupId>"+group+"</GroupId>\n"
        out +=indent + "\t</IncludedIdList>\n"

        out += indent +"\t<ExcludedIdList>\n"
        for group in self.excluded_groups:
            out += indent +"\t\t<GroupId>"+group+"</GroupId>\n"
        out += indent +"\t</ExcludedIdList>\n"

        for entry in self.entries:

            out += entry.toXML(indent+"\t")


        out += indent +"</PolicyRule>"

        return out
class Entry:



    access_masks = {
        0x01: "Disk Read",
        0x02: "Disk Write",
        0x04: "Disk Execute",
        0x08: "File Read",
        0x10: "File Write",
        0x20: "File Execute",
        0x40: "Print"
    }

    allow_notification_masks = {
        0x04: "Disable",
        0x08: "Create File Evidence"
    }

    deny_notification_masks = {
        0x04: "Disable"
    }

    audit_allowed_notification_masks = {
        0x01: "Nothing",
        0x02: "Send Event"
    }

    audit_denied_notification_masks = {
        0x01: "Show Notification",
        0x02: "Send Event"
    }

    notification_masks = {
        "Allow": allow_notification_masks,
        "AuditAllowed": audit_allowed_notification_masks,
        "Deny": deny_notification_masks,
        "AuditDenied": audit_denied_notification_masks
    }


    def __init__(self,entry):
        self.id = entry.attrib["Id"]
        self.type = entry.find("./Type").text
        self.options = entry.find("./Options").text
        self.access_mask = entry.find("./AccessMask").text

        self.permissions = []
        self.notifications = []

        for mask in Entry.access_masks.keys():
            if int(self.access_mask) & mask:
                self.permissions.append(Entry.access_masks[mask])

        notification_masks = Entry.notification_masks[self.type]
        for mask in notification_masks:
            if int(self.options) & mask:
                self.notifications.append(notification_masks[mask])
        
        if len(self.notifications) == 0:
            self.notifications.append("Nothing")

        sid = entry.find("./Sid")
        if sid is not None:
            self.sid = sid.text
        else:
            self.sid = "All Users"

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
    
    def toXML(self,indent):

        out = indent + "<Entry>\n"
        out += indent +"\t<Type>"+self.type+"</Type>\n"
        out += indent +"\t<AccessMake>"+self.access_mask+"</AccessMask>\n"
        out += indent +"\t<Options>"+self.options+"</Options>\n"

        if self.sid is not "All Users":
            out += indent +"\t<Sid>"+self.sid+"</Sid>\n"

        if self.parameters is not None:
            out += self.parameters.toXML(indent+"\t")
            

        out += indent +"</Entry>\n"

        return out
        
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

    def toXML(self,indent):

        out = indent + "<Parameters MatchType=\""+self.match_type+"\">\n"

        for condition in self.conditions:
            out += condition.toXML(indent+"\t")

        out += indent + "</Parameters>\n"

        return out

class Condition:
    def __init__(self,condition):
        self.match_type = condition.attrib['MatchType']
        self.groups = []
        self.tag = condition.tag
        self.condition_type = condition.tag
        for group in condition.findall(".//GroupId"):
            self.groups.append(group.text)

    def get_group_ids(self):
        return self.groups
    
    def toXML(self,indent):
        out = indent + "<"+self.tag+" MatchType=\""+self.match_type+"\">\n"

        for group in self.groups:
            out += indent +"\t<GroupId>"+group+"</GroupId>\n"

        out += indent + "</"+self.tag+">\n"

        return out


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
            print ("Error in "+xml_path+": "+str(e))
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
    groupsXML = "<Groups>"
    rulesXML  = "<PolicyRules>"

    for ind in filtered_rules.index:
        rule = filtered_rules['object'][ind]
        rules[rule.id] = rule
        rulesXML += "\n"+rule.toXML()
        groups_for_rule = inventory.get_groups_for_rule(rule)
        for group in groups_for_rule:
            groups[group] = groups_for_rule[group]
            groupsXML += "\n"+groups[group].toXML()

    groupsXML += "\n</Groups>"
    rulesXML += "\n</PolicyRules>"

    if args.format == "text":
        templatePath = pathlib.Path(__file__).parent.resolve()
        templateLoader = jinja2.FileSystemLoader(searchpath=templatePath)
        templateEnv = jinja2.Environment(loader=templateLoader)
        TEMPLATE_FILE = args.template
        template = templateEnv.get_template(TEMPLATE_FILE)
        out = template.render({"rules":rules,"groups":groups, "groupsXML": groupsXML, "rulesXML":rulesXML})
        with open(args.out_path,"w") as out_path:
            out_path.write(out)
            out_path.close()