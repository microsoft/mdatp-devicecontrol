#!/usr/bin/env python3

import xml.etree.ElementTree as ET
import argparse
import os, sys
import pandas as pd
import jinja2
import pathlib
import copy
import json

from devicecontrol import Group, PolicyRule, Entry, Settings, Setting, IntuneCustomRow, Support, IntuneUXFeature, WindowsFeature
import convert_dc_policy as mac 

Default_Settings = Settings(
    {
        Setting.DefaultEnforcement: "Deny",
        Setting.DeviceControlEnabled: True
    }
)

def full_stack():
    import traceback, sys
    exc = sys.exc_info()[0]
    stack = traceback.extract_stack()[:-1]  # last one would be full_stack()
    if exc is not None:  # i.e. an exception is present
        del stack[-1]       # remove call of full_stack, the printed exception
                            # will contain the caught exception caller instead
    trc = 'Traceback (most recent call last):\n'
    stackstr = trc + ''.join(traceback.format_list(stack))
    if exc is not None:
         stackstr += '  ' + traceback.format_exc().lstrip(trc)
    return stackstr


def clean_up_name(name, new_space = "-"):

    clean_name = name
    clean_name = str(clean_name).lstrip()
    clean_name = str(clean_name).rstrip()
    clean_name = str(clean_name).lower()
    clean_name = str(clean_name).replace(" ",new_space)
    clean_name = str(clean_name).replace("(","")
    clean_name = str(clean_name).replace(")","")
    clean_name = str(clean_name).replace(",","")

    return clean_name




class Helper:

    def get_section_title_for_object(object):
        return clean_up_name(object.name)
    
    true_icons = {
        PolicyRule.Allow:":white_check_mark:",
        PolicyRule.AuditAllowed:":page_facing_up:",
        PolicyRule.Deny:":x:",
        PolicyRule.AuditDenied:":page_facing_up:"
    }

    def get_permission_icons(entry):

        if entry.format == "mac":

            permission_icons = {}
            for permission in entry.all_permissions:
                enabled = permission in entry.access
                if enabled:
                    permission_icons[permission] = Helper.true_icons[entry.enforcement]
                else:
                    permission_icons[permission] = "-"

        else:

            permission_icons = {
            }

            for mask in entry.entry_type.access_masks:
                if mask & int(entry.access_mask):
                    permission_icons[mask] = Helper.true_icons[entry.enforcement]
                else:
                    permission_icons[mask] = "-"   

        return permission_icons
    
    def generate_clause_table(group):

        clauses = group.clauses
        clause_table = Helper.generate_table_for_clauses(clauses)
        return clause_table

    def generate_table_for_clauses(clauses,offset=1):
        table = []
        for clause in clauses:
            if len(clause.sub_clauses) > 0:
                sub_table = Helper.generate_clause_table(clause.sub_clauses,offset+1)
                for row in sub_table:
                    row = []*offset + row
                    table.append(row)
            else:
                for property in clause._properties:
                    operator = ""
                    if len(table) > 0:
                        operator = clause.clause_type
                    else:
                        operator = ""

                    row = ["-"]*offset + [property.name,property.value]
                    row[offset-1] = operator

                    table.append(row)

        return table




class Inventory:

    
    def __init__(self,source_path,generated_files_locations_by_format={},dest="."):
        self.paths = source_path
        self.generated_files_locations_by_format = generated_files_locations_by_format
        if self.generated_files_locations_by_format is None:
            self.generated_files_locations_by_format = {}
       
        self.dest_dir = dest

        group_columns = {
            "type":[],
            "path":[],
            "format":[],
            "name":[],
            "id":[],
            "match_type":[],
            "object":[]
        }

        rule_columns = {
            "path":[],
            "format":[],
            "name":[],
            "id":[],
            "included_groups":[],
            "excluded_groups":[],
            "object":[],
            "rule_index":[]
        }

        group_rule_columns = {
            "groupId":[],
            "ruleId": [],
            "type":[]
        }

        self.groups = pd.DataFrame(group_columns)
        self.policy_rules = pd.DataFrame(rule_columns)
        self.group_rules = pd.DataFrame(group_rule_columns)

       
        self.load_inventory()

        

    def load_inventory(self):
        for path in self.paths:
            for dir in os.walk(top=path):
                files = dir[2]
                for file in files:
                    if str(file).endswith(".xml"):
                        xml_path = dir[0]+os.sep+file
                        self.load_xml_file(xml_path)
                    if str(file).endswith(".json"):
                        json_path = dir[0]+os.sep+file
                        self.load_json_file(json_path)

    
    
    def load_json_file(self,json_path):
        try:
            with open(json_path) as file:
                json_object = json.load(file)

                if "groups" in json_object.keys():
                    group_index = 1
                    for group in json_object["groups"]:
                        self.addGroup(Group(group,"mac",json_path),group_index)
                        group_index=group_index+1

                if "rules" in json_object.keys():
                    rule_index = 1
                    for rule in json_object["rules"]:
                        self.addPolicyRule(PolicyRule(rule,"mac",json_path,rule_index))

            return
        except Exception as e:
            print(full_stack())
            print ("Error in "+json_path+": "+str(e))
            return
    
    def load_xml_file(self,xml_path):
        try:
            with open(xml_path) as file:
                root = ET.fromstring(file.read())
                match root.tag:
                    case "Group":
                        self.addGroup(Group(root,"oma-uri",xml_path))
                    case "Groups":
                        group_index = 1
                        for group in root.findall(".//Group"):
                            self.addGroup(Group(group,"gpo",xml_path), group_index)
                            group_index=group_index+1
                    case "PolicyGroups":
                        #This is what Intune UX looks like on disk
                        group_index = 1
                        for group in root.findall(".//Group"):
                            self.addGroup(Group(group,"gpo",xml_path), group_index)
                            group_index=group_index+1
                    case "PolicyRule":
                        self.addPolicyRule(PolicyRule(root,"oma-uri",xml_path))
                    case "PolicyRules":
                        rule_index = 1
                        for policyRule in root.findall(".//PolicyRule"):
                            self.addPolicyRule(PolicyRule(policyRule,"gpo",xml_path,rule_index))
                            rule_index= rule_index + 1

                return root

        except Exception as e:
            print(full_stack())
            print ("Error in "+xml_path+": "+str(e))
            return

    def addGroup(self,group, group_index=0):

        
        path = group.path
        format = group.format

        if group.name == "?":
            paths = str(path).split(os.sep)
            last_path = paths[-1]
            fileWithoutExtension = last_path.split(".")[0]
            group.name = fileWithoutExtension+"_"+str(int(group_index))


        #Could check for Intune UX support
        new_row = pd.DataFrame([{
            "type":group.type,
            "path":path,
            "format":format,
            "name":group.name,
            "id":group.id,
            "match_type":group.match_type,
            "object": group
        }])

        self.groups = pd.concat([self.groups,new_row],ignore_index=True)

    def addPolicyRule(self,rule):

        path = rule.path
        format = rule.format
        rule_index = rule.rule_index

        if rule.id is None:
            return

        new_row = pd.DataFrame([{
            "path":path,
            "format":format,
            "name":rule.name,
            "id":rule.id,
            "included_groups":rule.included_groups,
            "excluded_groups":rule.excluded_groups,
            "object": rule,
            "rule_index": rule_index
        }])

        self.policy_rules = pd.concat([self.policy_rules,new_row],ignore_index=True)

    
    def get_groups_for_rule(self,rule):
        groups_for_rule = {
            "gpo":[],
            "oma-uri":[],
            "mac":[],
            "included":[],
            "excluded":[],
            "entries":[]
        }
        for included_group in rule.included_groups:
            g = self.get_group_by_id(included_group)
            if g is not None:
                groups_for_rule["gpo"] += g["gpo"] 
                groups_for_rule["mac"] += g["mac"]
                groups_for_rule["oma-uri"] += g["oma-uri"]
                groups_for_rule["included"]+= g[rule.format]

        for excluded_group in rule.excluded_groups:
            g = self.get_group_by_id(excluded_group)
            if g is not None:
                groups_for_rule["gpo"] += g["gpo"]
                groups_for_rule["oma-uri"] += g["oma-uri"]
                groups_for_rule["mac"] += g["mac"]
                groups_for_rule["excluded"]+= g[rule.format]

        for entry in rule.entries:
            groups = entry.get_group_ids()
            for entry_group in groups:
                g = self.get_group_by_id(entry_group)
                if g is not None:
                    groups_for_rule["gpo"] += g["gpo"]
                    groups_for_rule["oma-uri"] += g["oma-uri"]
                    groups_for_rule["entries"]+= g[rule.format]
                    #Groups in entries not supported on mac
                    #groups_for_rule["mac"] += g["mac"]
        
        return groups_for_rule


    def get_group_by_id(self,group_id):
        group_frame = self.groups.query("id == '"+group_id+"'")
        if group_frame.size == 0:
            print ("No group found for "+group_id)
            return None
        else:
            groups = {
                "gpo":[],
                "oma-uri":[],
                "mac":[]
            }
            
            for i in range(0,group_frame.index.size):
                group = group_frame.iloc[i]["object"]
                format = group_frame.iloc[i]["format"]
                path = group_frame.iloc[i]["path"]
                if group in groups[format]:
                    continue
                elif len(groups[format]) == 0:
                    groups[format].append(group)
                else:
                    print("Conflicting groups for "+group_id+" at "+path+"\n"+str(group) +"\n!=\n" +str(groups[format][0]))

            #Use either GPO or Mac, to create an OMA-URI group
            if len(groups["oma-uri"]) == 0:
                oma_uri_group = None
                if len(groups["gpo"]) > 0:
                    oma_uri_group = self.missing_oma_uri(groups["gpo"][0])
                elif len(groups["mac"]) >0:
                    oma_uri_group = self.missing_oma_uri(groups["mac"][0])

                if oma_uri_group is not None:
                    groups["oma-uri"].append(oma_uri_group)

            return groups
    
    def get_path_for_group(self,group_id):
        group_frame = self.groups.query("id == '"+group_id+"'")
        return group_frame.iloc[0]["path"]
    

    def query_policy_rules(self,query):
        rules = {
            "gpo":{},
            "oma-uri":{},
            "mac":{},
            "all":[]
        }

        query = str(query).encode('unicode-escape').decode()
        
        rule_frame = self.policy_rules.query(query, engine='python')
        rule_frame = rule_frame.sort_values("rule_index", ascending=True)
        for i in range(0,rule_frame.index.size):
            rule = rule_frame.iloc[i]["object"]
            format = rule_frame.iloc[i]["format"]
            rule_index = rule_frame.iloc[i]["rule_index"]
            rule_id = rule.id

            if format == "oma-uri":
                rule_id = rule.get_oma_uri()

            rules_for_format = rules[format]
            if rule_id in rules_for_format:
                existing_rule = rules_for_format[rule_id]
                if existing_rule != rule:
                    print ("Conflicting rules for id "+rule.id+"\n"+str(rule)+"\n!=\n"+str(existing_rule))
            elif format == "oma-uri":
                rules[format][rule_id] = IntuneCustomRow(rule)
            else:
                rules[format][rule_id] = rule 

            rules["all"].append(rule)

        rules["all"] = list(set(rules["all"]))
        rules["all"].sort(key= lambda x: x.rule_index)

        #check for missing oma-uri rules
        for rule in rules["all"]:
            if not rule.get_oma_uri() in rules["oma-uri"]:
                oma_uri_rule = self.missing_oma_uri(rules[rule.format][rule.id])
                if oma_uri_rule is not None:
                    rules["oma-uri"][rule.get_oma_uri()] = IntuneCustomRow(oma_uri_rule)

        return rules
    

    def missing_oma_uri(self,object):
        print("Missing oma-uri for id "+object.id)
        oma_uri_object = copy.copy(object)
        oma_uri_object.format = "oma-uri"


        if "oma-uri" in self.generated_files_locations_by_format.keys():
            
            path = self.generated_files_locations_by_format["oma-uri"] + os.sep + clean_up_name(oma_uri_object.name,"_")+oma_uri_object.id + ".xml"
            oma_uri_object.set_path(path)
            with open(path,"w") as generated_file:
                generated_file.write(oma_uri_object.toXML(""))
                generated_file.close()

        else:
            oma_uri_object.set_path(None)

        return oma_uri_object
    
    def process_query(self,query):

        if query is None:
            query="path.str.contains('(.*)')"

        filtered_rules = self.query_policy_rules(query)

        result = {}

        rules = {}
        groups = {}
        paths = []

        intune_ux_support = Support()
        windows_support = Support()
        mac_support = Support()

        groupsXML = "<Groups>"
        rulesXML  = "<PolicyRules>"
        mac_policy = {
            "groups":[],
            "rules":[]
        }
        oma_uri = filtered_rules["oma-uri"]
        entry_type = None
        has_mixed_entry_type = False

        for rule in filtered_rules["all"]:

            if rule.id in rules:
                print ("Conflicting rules "+rules[rule.id].toXML()+" in "+rules[rule.id].path+" != "+rule.toXML()+" in "+rule.path)
                continue
        
            rules[rule.id] = rule
            paths.append(rule.path)
            mac_policy["rules"].append(rule.toJSON())

            #sets the entry type to the Generic
            #if the query returns more than 1
            if entry_type is None:
                entry_type = rule.entry_type
            elif entry_type is not rule.entry_type:
                if not has_mixed_entry_type:
                    if rule.format == "mac":
                        entry_type = Entry.AppleGeneric
                    else:
                        entry_type = Entry.WindowsGeneric

                    has_mixed_entry_type = True


            intune_ux_support += IntuneUXFeature.get_support_for(rule)
            windows_support += WindowsFeature.get_support_for(rule)

            rulesXML += "\n"+rule.toXML()
            groups_for_rule = self.get_groups_for_rule(rule)
            all_groups = set(groups_for_rule["gpo"]+groups_for_rule["oma-uri"])
            for group in all_groups:
                if group.id not in groups:
                    groupsXML += "\n"+group.toXML()
                    groups[group.id] = group
                    paths.append(group.path)
                    mac_policy["groups"].append(group.toJSON())

                    intune_ux_support += IntuneUXFeature.get_support_for(group)
                    windows_support += WindowsFeature.get_support_for(group)
            
            for oma_uri_group in groups_for_rule["oma-uri"]:
                oma_uri[oma_uri_group.get_oma_uri()] = IntuneCustomRow(oma_uri_group)
        

        groupsXML += "\n</Groups>"
        rulesXML += "\n</PolicyRules>"

        #remove duplicates from paths
        paths = list(set(paths))
        web_paths = []
        for path in paths:
            if str(path).startswith(".\\"):
                path = path[2:]
            path = str(path).replace("\\","/")
            web_paths.append(path)

        try:
            
            mac_error = None
            if entry_type not in Entry.MacEntryTypes:
                mac_policy["groups"] = mac.convert_groups(ET.fromstring(groupsXML),True)
                mac_policy["rules"] = mac.convert_rules(ET.fromstring(rulesXML),True)
        except Exception as e:
            mac.log_error("Failed to convert policy to Mac:")
            mac.log_error(str(e))
            mac_policy = None
            mac_error = str(e)
    
        #Gather result
        result["oma_uri"] = oma_uri
        result["web_paths"] = web_paths
        result["rules"] = rules
        result["groups"] = groups
        result["intune_ux_support"] = intune_ux_support
        result["groupsXML"] = groupsXML
        result["rulesXML"] = rulesXML
        result["mac_policy"] = mac_policy
        result["mac_error"] = mac_error
        result["windows_support"] = windows_support 
        result["entry_type"] = entry_type

        return result    

    def generate_csv(self,dest):
        self.groups.to_csv(dest+os.sep+"dc_groups.csv",sep=",")
        self.policy_rules.to_csv(dest+os.sep+"dc_rules.csv",sep=",")

        #create the list of group-rule-mappings
        for i in range(0,self.policy_rules.index.size):
            rule = self.policy_rules.iloc[i]["object"]
            groups = self.get_groups_for_rule(rule)
            
            for group_rule_type in ["included","excluded","entries"]:
                if group_rule_type in groups.keys():
                    for included_group in groups[group_rule_type]:
                        new_row = pd.DataFrame([{
                            "type":group_rule_type,
                            "groupId": included_group.id,
                            "ruleId": rule.id
                        }])

                        self.group_rules = pd.concat([self.group_rules,new_row],ignore_index=True)
            
            
            

        self.group_rules.to_csv(dest+os.sep+"dc_group_rules.csv",sep=",")


    def generate_text(self,result,dest,file,title, description="A sample policy", settings = None ):
        
        if settings is not None:
            custom_settings_values = settings.getIntuneCustomValues()
            for custom_settings_value in custom_settings_values:
                result["oma_uri"][custom_settings_value] = custom_settings_values[custom_settings_value] 

            if result["mac_policy"] is not None:
                mac_policy = result["mac_policy"]
                mac_policy["settings"] = settings.get_mac_settings()
                result["mac_policy"] = mac_policy

        
        if result["mac_policy"] is not None:
            result["mac_policy"] = json.dumps(result["mac_policy"],indent=4)

        templatePath = pathlib.Path(__file__ ).parent.resolve() 
        templatePath = pathlib.Path(str(templatePath)+ os.sep + "templates").resolve()
        templateLoader = jinja2.FileSystemLoader(searchpath=templatePath)
        templateEnv = jinja2.Environment(loader=templateLoader)
        TEMPLATE_FILE = args.template
        template = templateEnv.get_template(TEMPLATE_FILE)
        out = template.render(
            {"intuneCustomSettings":result["oma_uri"],
             "paths":result["web_paths"],
             "rules":result["rules"],
             "groups":result["groups"], 
             "intune_ux_support":result["intune_ux_support"],
             "windows_support": result["windows_support"],
             "groupsXML": result["groupsXML"], 
             "rulesXML":result["rulesXML"],
             "macPolicy":result["mac_policy"],
             "macError": result["mac_error"],
             "entry_type": result["entry_type"],
             "description": description,
             "settings": settings,
             "env":os.environ,
             "Helper":Helper,
             "title":title})
        

        with open(dest+os.sep+file,"w") as out_file:
            out_file.write(out)
            out_file.close()



def dir_path(string):
    paths = string.split(os.pathsep)
    for path in paths:
        if os.path.isdir(path):
            continue
        else:
            raise NotADirectoryError(path)
    return paths

def dir(path):
    if os.path.isdir(path):
        return path
    else:
        raise NotADirectoryError(path)

def file(path):
    if os.path.isfile(path):
        return path
    else:
        raise argparse.ArgumentError("Not a file "+path)

def format(string):
    match string:
        case "text":
            return string
        case "csv":
            return string
        case other:
            raise argparse.ArgumentError("Invalid format "+string)

def generate_files_format(format_strings):

    generated_files_locations_by_format = {}
    format_string = format_strings.split(",")
    for format_string in format_string:
        
        format_string_values = format_string.split(":")
        format = format_string_values[0]
        location = ":".join(format_string_values[1:])

        if format in ["oma-uri","mac","gpo"]:
            if os.path.isdir(location):
                generated_files_locations_by_format[format] = location
                continue
            else:
                raise argparse.ArgumentError("Invalid location to save generated files"+location)

        else:
            raise argparse.ArgumentError("Invalid format "+format)

    return generated_files_locations_by_format

def parse_in_file(in_file):
    query = "path.str.contains('"+in_file+"',regex=False)"
    title = str(in_file.split(os.sep)[-1]).split(".")[0]
    outfile = title+".md"
    settings = Default_Settings

    #check the settings for the file
    if in_file.endswith(".json"):
         p = pathlib.PurePath(in_file)
         with open(in_file,"r") as json_file:
            mac_policy = json.loads(json_file.read())
            mac_settings = Settings.generate_settings_from_mac_policy(mac_policy)
            if mac_settings is not None:
                settings = mac_settings

            json_file.close()
            

    return query,title,outfile,settings

def load_scenarios(scenarios_file):
     with open(scenarios_file) as file:
         scenarios = json.loads(file.read())
         return scenarios
     
def generate_readme(results,dest,title):
    templatePath = pathlib.Path(__file__).parent.resolve()
    templatePath = pathlib.Path(str(templatePath)+ os.sep + "templates").resolve()
    templateLoader = jinja2.FileSystemLoader(searchpath=templatePath)
    templateEnv = jinja2.Environment(loader=templateLoader)
    TEMPLATE_FILE = "readme.j2"
    template = templateEnv.get_template(TEMPLATE_FILE)
    out = template.render(
        {
            "results":results,
            "dest":dest,
            "title":title,
            "env":os.environ
         }
    )

    with open(dest+os.sep+"readme.md","w") as out_file:
        out_file.write(out)
        out_file.close()

if __name__ == '__main__':

    arg_parser = argparse.ArgumentParser(
        description='Utility for generating documentation for device control policies.')

    
    input_group =arg_parser.add_mutually_exclusive_group()
    input_group.add_argument('-q','--query',dest="query",help='The query to retrieve the policy rules to process')
    input_group.add_argument('-s','--scenarios',dest="scenarios",type=file,help='A JSON file that contains a list of scenarios to process')
    input_group.add_argument('-i','--input',dest="in_file",type=file,help='A policy rule to process')


    arg_parser.add_argument('-p', '--path', type=dir_path, dest="source_path", help='The path to search for source files',default=".")
    arg_parser.add_argument('-f','--format',type=format, dest="format",help="The format of the output (text)",default="text")
    arg_parser.add_argument('-o','--output',dest="out_file",help="The output file")
    arg_parser.add_argument('-d','--dest',dest="dest",type=dir,help="The output directory",default=".")
    arg_parser.add_argument('-g','--generate',dest="generated_files_locations", type=generate_files_format, help='Generates files for other formats')
    arg_parser.add_argument('-t','--template',dest="template",help="Jinja2 template to use to generate output",default="dcutil.j2")

    args = arg_parser.parse_args()

    inventory = Inventory(args.source_path,args.generated_files_locations,args.dest)

    query = args.query
    title = None
    if "TITLE" in os.environ.keys():
        title = os.environ["TITLE"]

    out_file = args.out_file

    if args.scenarios is not None:

        scenarios_dir = os.path.dirname(args.scenarios)

        results = {}
        scenarios = load_scenarios(args.scenarios)
        for rule in scenarios["scenarios"]:
            policy_file = rule["file"]

            policy_path = pathlib.PurePath(os.path.join(scenarios_dir,policy_file))
            policy_path = policy_path.relative_to(os.getcwd())
            policy_file = str(policy_path)

            description = "A sample policy"
            
            title = None
            if "description" in rule.keys():
                description = rule["description"]
            if "title" in rule.keys():
                title = rule["title"]
            
            query,default_title,default_outfile,default_settings = parse_in_file(policy_file)
            if "settings" in rule.keys():
                settings = Settings(rule["settings"])
            else:
                settings = default_settings
            
            result = inventory.process_query(query)
            if args.format == "text":
                if title is None:
                    title = default_title
                inventory.generate_text(result,args.dest,default_outfile,title,description,settings)

            results[policy_file] = {
                "result":result,
                "title": title,
                "file": default_outfile
            }

        generate_readme(results,args.dest,scenarios["title"])


    elif query is None:
        if args.in_file is not None:
            query,title,default_outfile,settings = parse_in_file(args.in_file)
            if out_file is None:
                out_file = default_outfile

        if args.format == "text":
            result = inventory.process_query(query)
            inventory.generate_text(result,args.dest,out_file,title,None,settings)
        elif args.format == "csv":
            inventory.generate_csv(args.dest)
        