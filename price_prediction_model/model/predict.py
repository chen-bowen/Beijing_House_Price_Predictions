import numpy as np
import pandas as pd

from price_prediction_model.utils.utils import load_pipeline
from price_prediction_model.config import config

from price_prediction_model.utils.validation import validate_inputs
from price_prediction_model import __version__ as _version

import logging
import typing as t

_logger = logging.getLogger(__name__)

pipeline_file_name = f"{config.PIPELINE_SAVE_FILE}{_version}.pkl"
model_pipeline = load_pipeline(file_name=pipeline_file_name)


def make_prediction(*, input_data: t.Union[pd.DataFrame, dict]) -> dict:
    """Make a prediction using a saved model pipeline.

    Args:
        input_data: Array of model prediction inputs.

    Returns:
        Predictions for each input row, as well as the model version.
    """

    data = pd.DataFrame(input_data)
    validated_data = validate_inputs(input_data=data)

    prediction = model_pipeline.predict(validated_data)

    response = {"predictions": prediction, "version": _version}

    _logger.info(
        f"Making predictions with model version: {_version} "
        f"Inputs: {validated_data} "
        f"Predictions: {response}"
    )

    return response
