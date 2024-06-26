import mdedevicecontrol.dcdoc as doc
import os
import xml.etree.ElementTree as ET

import pathlib as pl

from tests import check_path, root_dir


mac_samples_dir = os.path.join(root_dir,"macOS","policy","samples")


class DcDocArgs: 

    def __init__(self):

        self.query = None
        self.scenarios = None
        self.in_file = None

        self.source_path = doc.dir_path(".")
        self.format = "text"
        self.out_file = None
        self.dest = doc.dir(".")

        self.loggingConf = doc.file("logging.conf")

        self.templates_path = doc.path_array("templates")
        self.template = "dcutil.j2"
        self.readme_template = "readme.j2"
        self.description_template = "description.j2"
        self.readme_file = "readme.md"
        
        self.generated_files_locations = None
        
        
    def set_source_path(self,path):
        self.source_path = doc.dir_path(path)

    
    def set_dest(self,dest):
        self.dest = doc.dir(dest)

    def set_templates_path(self,templates_path):
        self.templates_path = doc.path_array(templates_path)

    
        

        

def test_generate_mac_docs():
        
    args = DcDocArgs()
    args.set_source_path(str(mac_samples_dir))
    args.scenarios = os.path.join(mac_samples_dir,"scenarios.json")
    

    doc.process_args(args)

    check_path(os.path.join(str(os.getcwd()),"allow_all_removable_media_except_smi_instaview.md"))
    check_path(os.path.join(str(os.getcwd()),"readme.md"))
    
    
    
