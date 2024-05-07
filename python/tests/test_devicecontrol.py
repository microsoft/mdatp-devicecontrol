import mdedevicecontrol as dc

def test1():

    api = dc.api()


def test2():

    api = dc.api()

    vid_pid = api.createProperty(dc.Group.WindowsDeviceVendorProductProperty,"05AC_12AB")
    properties = [vid_pid]

    g1 = api.createGroup(name="Allowed Devices",
                         group_type=dc.Group.WindowsDeviceGroupType,
                         match_type=dc.MatchType.Any,
                         properties=properties)

    print(str(g1))