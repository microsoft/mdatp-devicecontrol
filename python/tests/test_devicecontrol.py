import mdedevicecontrol as dc

def test_create_api():

    api = dc.api()


def test_create_group():

    api = dc.api()

    vid_pid = api.createProperty(dc.Group.WindowsDeviceVendorProductProperty,"05AC_12AB")
    properties = [vid_pid]

    g1 = api.createGroup(name="Allowed Devices",
                         group_type=dc.Group.WindowsDeviceGroupType,
                         match_type=dc.MatchType.Any,
                         properties=properties)

    print(str(g1))


def test_create_entry():

    api = dc.api()

    entry = api.createEntry()

def test_create_rule():

    api = dc.api()

    rule = api.createRule("Test Rule")