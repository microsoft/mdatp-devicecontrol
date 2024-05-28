import unittest
import pathlib as pl
import hashlib


root_dir = pl.Path(__file__).parent.parent.parent.absolute()

def check_path(path):
    if not pl.Path("mdedevicecontrol.log").resolve().is_file():
        raise AssertionError("File does not exist: %s" % str(path))


def hash(value):
    return hashlib.sha256(value.encode()).hexdigest()