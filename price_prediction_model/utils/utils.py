import pandas as pd
import joblib
from sklearn.pipeline import Pipeline

from price_prediction_model.config import config
from price_prediction_model import __version__ as _version

import logging
import typing as t


_logger = logging.getLogger(__name__)


def train_test_validation_split(data, time_col, target_col):
    """

    Perform train test validation split based on time,
    returns splitted data in form of X,y dataframes

    """
    # get split points
    train_split_index = int(len(data) * config.TRAIN_DATA_PCT)
    val_split_index = int(len(data) * (config.TRAIN_DATA_PCT + config.VAL_DATA_PCT))

    # data splits
    data = data.sample(frac=1, random_state=config.RANDOM_SEED).reset_index(drop=True)
    data["year"] = pd.to_datetime(data[time_col]).dt.year
    data.sort_values(by="year", inplace=True)
    data.drop("year", axis=1, inplace=True)

    training_data = data.iloc[:train_split_index]
    validation_data = data.iloc[train_split_index:val_split_index]
    test_data = data.iloc[val_split_index:]

    # split into X, y
    X_train, y_train = (
        training_data.drop([target_col], axis=1),
        training_data[target_col],
    )

    X_val, y_val = (
        validation_data.drop([target_col], axis=1),
        validation_data[target_col],
    )

    return X_train, y_train, X_val, y_val


def load_dataset(*, file_name: str) -> pd.DataFrame:
    """ load the dataset """
    _data = pd.read_csv(
        f"{config.DATASET_DIR}/{file_name}",
        encoding=config.DATA_FILE_ENCODING,
        low_memory=False,
    )
    return _data


def save_pipeline(*, pipeline_to_persist) -> None:
    """
    Persist the pipeline.
    Saves the versioned model, and overwrites any previous
    saved models. This ensures that when the package is
    published, there is only one trained model that can be
    called, and we know exactly how it was built.

    """

    # Prepare versioned save file name
    save_file_name = f"{config.PIPELINE_SAVE_FILE}{_version}.pkl"
    save_path = config.TRAINED_MODEL_DIR / save_file_name

    if not os.path.exists(config.TRAINED_MODEL_DIR):
        os.makedirs(config.TRAINED_MODEL_DIR)

    remove_old_pipelines(files_to_keep=[save_file_name])
    joblib.dump(pipeline_to_persist, save_path)
    _logger.info(f"saved pipeline: {save_file_name}")


def load_pipeline(*, file_name: str) -> Pipeline:
    """Load a persisted pipeline."""

    file_path = config.TRAINED_MODEL_DIR / file_name
    trained_model = joblib.load(filename=file_path)
    return trained_model


def remove_old_pipelines(*, files_to_keep: t.List[str]) -> None:
    """
    Remove old model pipelines.

    This is to ensure there is a simple one-to-one
    mapping between the package version and the model
    version to be imported and used by other applications.
    However, we do also include the immediate previous
    pipeline version for differential testing purposes.
    """
    do_not_delete = files_to_keep + ["__init__.py"]
    for model_file in config.TRAINED_MODEL_DIR.iterdir():
        if model_file.name not in do_not_delete:
            model_file.unlink()
