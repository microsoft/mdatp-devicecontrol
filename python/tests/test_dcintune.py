import mdedevicecontrol.dcintune

def test_rule_xml():

    rule = dcintune.DeviceControlPolicyTemplate.DeviceControlRule()
    rule.id = "12345"
    rule.name = "Test"
    rule.included_groups = ["group1","group2"]
    
    out =str(rule)
    print(out)
