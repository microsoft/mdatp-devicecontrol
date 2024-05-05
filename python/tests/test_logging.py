import logging

import unittest
import pathlib as pl

from tests import check_path

def test_mdedevicecontrol_logging():

    import logging.config
    logging.config.fileConfig("logging.conf")

    logger = logging.getLogger("mdedevicecontrol.devicecontrol")
    logger.info("Info message for mdedevicecontrol.devicecontrol")
    logger.warning("Warning message for mdedevicecontrol.devicecontrol")
    logger.error("Error message for mdedevicecontrol.devicecontrol")

    check_path("mdedevicecontrol.log")