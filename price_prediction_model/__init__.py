import logging
from price_prediction_model.config import config, logging_config
from price_prediction_model import utils, preprocessing, features, model
import poetry_version


# Configure logger for use in package
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging_config.get_console_handler())
logger.propagate = False


__version__ = poetry_version.extract(source_file=__file__)
