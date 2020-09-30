from price_prediction_model.config import config

import pandas as pd


def validate_inputs(input_data: pd.DataFrame) -> pd.DataFrame:
    """Check model inputs for unprocessable values."""

    validated_data = input_data.copy()

    # check for numerical variables with NA not seen during training
    for var in config.NUMERICAL_MIX_TYPE_NOT_ALLOWED:
        for i, item in enumerate(validated_data[var]):
            try:
                validated_data[config.NUMERICAL_MIX_TYPE_NOT_ALLOWED].astype(int)

            except:
                validated_data = validated_data.drop(index=i, axis=0, subset=[var])

    return validated_data