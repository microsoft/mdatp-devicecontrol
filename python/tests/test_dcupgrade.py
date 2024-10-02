import mdedevicecontrol.upgrade_dc_policy as dc_upgrade
import os
import json
from tests import root_dir

def test_updgade_v1():

    samples = ["deny_all_mount.mobileconfig","mount_allowlist.mobileconfig"]
    v1_samples_dir = os.path.join(str(root_dir),"macOS","mobileconfig","v1")
    for sample in samples:
        sample_file = open(os.path.join(v1_samples_dir,sample),"rb")
        upgraded_policy = dc_upgrade.upgrade_v1_policy(sample_file)
        print(json.dumps(upgraded_policy, indent=2))
    
    return