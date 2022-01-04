from logging_func import setup_logger

# first file logger
logger = setup_logger("first_logger", "first_logfile.log")
logger.info("This is just info message")

# second file logger
super_logger = setup_logger("second_logger", "second_logfile.log")
super_logger.error("This is an error message")


def another_method():
    # using logger defined above also works here
    logger.info("Inside method")
