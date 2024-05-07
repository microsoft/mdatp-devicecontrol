import mdedevicecontrol as dc

def test1():

    api = dc.api()


def test2():

    api = dc.api()

    vid_pid = api.createProperty(dc.GroupProperty.WindowsDeviceVendorProduct,"05AC_12AB")
    properties = [vid_pid]

    g1 = api.createGroup("g1",dc.MatchType.ANY,properties)

    print(str(g1))