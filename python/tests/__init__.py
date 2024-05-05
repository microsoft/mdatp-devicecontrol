import unittest
import pathlib as pl

def check_path(path):
    if not pl.Path("mdedevicecontrol.log").resolve().is_file():
        raise AssertionError("File does not exist: %s" % str(path))
