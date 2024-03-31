import dcdoc

class TestArgs: 

    def __init__(self):
        self.templates_path = "templates"
        self.source_path = "."
        self.generated_files_locations = None
        self.dest = "."
        self.query = None
        self.out_file = None
        self.scenarios = None
        self.in_file = None
        self.format = None

def test_generate_mac_docs():
    
    args = TestArgs()
    

    dcdoc.main(args)
    return False
    

def test_goodbye():
    return True