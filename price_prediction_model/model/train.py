import numpy as np
from sklearn.model_selection import train_test_split

from price_prediction_model.model.model_pipeline import ModelPipeline
from price_prediction_model.utils.utils import (
    load_dataset,
    save_pipeline,
    train_test_validation_split,
)
from price_prediction_model.config import config
from price_prediction_model import __version__ as _version

import logging


_logger = logging.getLogger(__name__)


def train_model() -> None:
    """Train the model."""

    # read training data
    house_dataset = load_dataset(file_name=config.DATA_DIR)

    # divide train, validation and test
    X_train, y_train, X_val, y_val, X_test, y_test = train_test_validation_split(
        data=house_dataset, time_col=config.DATETIME_VAR_YEAR, target_col=config.TARGET
    )
    # initialize and train the model
    model = ModelPipeline()
    model.train(X_train.values, y_train.values, X_val.values, y_val.values)

    _logger.info(f"saving model version: {_version}")
    save_pipeline(pipeline_to_persist=pipeline.price_pipe)


if __name__ == "__main__":
    run_training()
