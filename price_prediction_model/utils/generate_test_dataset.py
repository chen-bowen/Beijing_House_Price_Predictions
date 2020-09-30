import sys

sys.path.append(".")

from price_prediction_model.config import config
from price_prediction_model.utils.utils import load_dataset
import pandas as pd


def generate_test_dataset():
    """ save part of the original dataset to csv as test dataset """

    # read training data
    data = load_dataset(file_name=config.DATA_FILE_NAME)

    split_index = int(len(data) * (config.TRAIN_DATA_PCT + config.VAL_DATA_PCT))

    # data splits
    data = data.sample(frac=1, random_state=config.RANDOM_SEED).reset_index(drop=True)
    data["year"] = pd.to_datetime(data[config.DATETIME_VAR]).dt.year
    data.sort_values(by="year", inplace=True)
    data.drop("year", axis=1, inplace=True)

    # get test data and write to data directory
    test_data = data.iloc[split_index:]
    test_data.to_csv(
        f"{config.DATASET_DIR}/beijing_house_price_test_data.csv", index=False
    )


if __name__ == "__main__":
    generate_test_dataset()