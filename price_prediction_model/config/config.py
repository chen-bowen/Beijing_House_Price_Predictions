import pathlib

import price_prediction_moddel

import pandas as pd


pd.options.display.max_rows = 100
pd.options.display.max_columns = 50

PACKAGE_ROOT = pathlib.Path(price_prediction_moddel.__file__).resolve().parent
TRAINED_MODEL_DIR = PACKAGE_ROOT / "trained_model_files"
DATASET_DIR = PACKAGE_ROOT / "data"


# data
TESTING_DATA_FILE = "test.csv"
TRAINING_DATA_FILE = "train.csv"
TARGET_ORIGINAL = "totalPrice"
TARGET = "totalPrice_per_10000"

# features
FEATURES = [
    "Lng",
    "Lat",
    "DOM",
    "followers",
    "square",
    "livingRoom",
    "drawingRoom",
    "kitchen",
    "bathRoom",
    "buildingType",
    "renovationCondition",
    "buildingStructure",
    "ladderRatio",
    "elevator",
    "fiveYearsProperty",
    "subway",
    "district",
    "communityAverage",
    "buildingTotalFloors",
    "floorProximity",
    "houseAgeYears",
    "tradeYear",
    "tradeMonth",
    "3_month_avg_price",
]

# hyperparameters
HYPER_PARAMS = {
    "boosting_type": "gbdt",
    "colsample_bytree": 0.9,
    "importance_type": "split",
    "learning_rate": 0.1,
    "max_depth": -1,
    "min_child_samples": 20,
    "min_child_weight": 0.001,
    "min_split_gain": 0.2,
    "n_estimators": 100,
    "n_jobs": -1,
    "num_leaves": 50,
    "objective": "regression",
    "random_state": 7,
    "reg_alpha": 0.0,
    "reg_lambda": 0.0,
    "silent": True,
    "subsample": 1.0,
    "subsample_for_bin": 500000,
    "subsample_freq": 0,
}


# categorical variables to encode
CATEGORICAL_VARS = [
    "renovationCondition",
    "buildingStructure",
    "district",
    "floorProximity",
]

# variables to convert to integer
TO_INT_VARS = ["livingRoom", "drawingRoom", "bathRoom"]

# temporal feature
TEMPORAL_VAR_TO_REPLACE = "constructionTime"
TEMPORAL_SPECIAL_VALUES_HANDLING = {"2018": ["0", "未知"], "2017": "1"}
TEMPORAL_TRANSFORMED_VAR = "houseAgeYears"

# date features
DATETIME_VAR = "tradeTime"
DATETIME_VAR_YEAR = "tradeYear"
DATETIME_VAR_MONTH = "tradeMonth"

# drop features
DROP_FEATURES = [
    "url",
    "id",
    "Cid",
    "year",
    "tradeTime",
    "floor",
    "price",
    "constructionTime",
]

# variable contains non-unicode string
NON_UNICODE_VAR = "floor"
NON_UNICODE_TRANSFORMED_VARS = ["floorProximity", "buildingTotalFloors"]
NON_UNICODE_MAPPING = {"顶": "5", "高": "4", "中": "3", "低": "2", "底": "1", "未知": "0"}

NUMERICAL_NA_NOT_ALLOWED = [
    feature for feature in FEATURES if feature not in CATEGORICAL_VARS
]

PIPELINE_NAME = "lightgbm_regression"
PIPELINE_SAVE_FILE = f"{PIPELINE_NAME}_model_v"

# used for differential testing
ACCEPTABLE_MODEL_DIFFERENCE = 0.05
