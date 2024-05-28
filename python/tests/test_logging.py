import logging


from tests import check_path

def test_mdedevicecontrol_logging():

    import logging.config
    logging.config.fileConfig("logging.conf")

    logger = logging.getLogger("mdedevicecontrol")
    logger.info("Info message for mdedevicecontrol")
    logger.warning("Warning message for mdedevicecontrol")
    logger.error("Error message for mdedevicecontrol")

    check_path("mdedevicecontrol.log")