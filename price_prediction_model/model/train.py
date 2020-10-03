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
import os


_logger = logging.getLogger(__name__)


def train_model() -> None:
    """Train the model."""

    # read training data
    house_dataset = load_dataset(file_name=config.DATA_FILE_NAME)

    # sklearn pipelines doesn't support row operations, we have to alter it here
    house_dataset = house_dataset[
        house_dataset["tradeTime"] >= str(config.MIN_YEARS_ACCEPTED)
    ]
    house_dataset = house_dataset.dropna(subset=["fiveYearsProperty"])

    # divide train, validation and test
    X_train, y_train, X_val, y_val = train_test_validation_split(
        data=house_dataset,
        time_col=config.DATETIME_VAR,
        target_col=config.TARGET_ORIGINAL,
    )
    save_file_name = f"{config.PIPELINE_SAVE_FILE}{_version}.pkl"
    save_path = config.TRAINED_MODEL_DIR / save_file_name

    if os.path.exists(save_path):
        _logger.info(f"Found existing model version: {_version}")
        return

    # initialize and train the model
    model = ModelPipeline()
    model.train(X_train, y_train)

    _logger.info(f"saving model version: {_version}")
    save_pipeline(pipeline_to_persist=model.model_pipeline)


if __name__ == "__main__":
    train_model()
