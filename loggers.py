import os
from distutils.util import strtobool as sb
from logging import requests, INFO, basicConfig, getLogger
from logging import DEBUG, WARNING, basicConfig, getLogger, INFO
from logging.handlers import RotatingFileHandler
import logging
ENV = os.environ.get("ENV", False)
ENV = os.environ.get("ENV", False)
if bool(ENV):
    CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

    if CONSOLE_LOGGER_VERBOSE:
        basicConfig(
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            level=debug,
        )
    else:
        basicConfig(
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=INFO
        )
    logger = getLogger(__name__)
