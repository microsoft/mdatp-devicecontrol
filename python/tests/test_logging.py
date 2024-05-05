import logging

import unittest
import pathlib as pl

def check_path(path):
    if not pl.Path("mdedevicecontrol.log").resolve().is_file():
        raise AssertionError("File does not exist: %s" % str(path))

def test_mdedevicecontrol_logging():
    logger = logging.getLogger("mdedevicecontrol.devicecontrol")
    logger.info("Info message for mdedevicecontrol.devicecontrol")
    logger.warning("Warning message for mdedevicecontrol.devicecontrol")
    logger.error("Error message for mdedevicecontrol.devicecontrol")

    check_path("mdedevicecontrol.log")