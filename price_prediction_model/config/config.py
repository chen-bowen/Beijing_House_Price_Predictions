import pathlib
import pandas as pd
import price_prediction_model

pd.options.display.max_rows = 100
pd.options.display.max_columns = 50

PACKAGE_ROOT = pathlib.Path(price_prediction_model.__file__).resolve().parent
TRAINED_MODEL_DIR = PACKAGE_ROOT / "trained_model_files"
DATASET_DIR = PACKAGE_ROOT / "data"
DATA_FILE_NAME = "beijing_house_prices_2012_2017.csv"
DATA_FILE_ENCODING = "gbk"
TRAIN_DATA_PCT = 0.9
VAL_DATA_PCT = 0.01
RANDOM_SEED = 7

# data
TARGET_ORIGINAL = "totalPrice"
TARGET = "totalPricePer10K"

# total price replica
PRICES_PER_AREA = "price"
AREA = "square"

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
    "expAvgPrice3mon",
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

# lightgbm config
EVAL_METRIC = "l2"
EARLY_STOP_RND = 5000
VERBOSE = 0

# categorical variables to encode
CATEGORICAL_VARS = [
    "renovationCondition",
    "buildingStructure",
    "district",
    "floorProximity",
]

# variables to convert to integer
INT_VARS = ["livingRoom", "drawingRoom", "bathRoom"]

# temporal feature
TEMPORAL_VAR_TO_AGE = "constructionTime"

# date features
DATETIME_VAR = "tradeTime"
DATETIME_VAR_YEAR = "tradeYear"
DATETIME_VAR_MONTH = "tradeMonth"

# special encoding variable
RARE_CATEGORY_VAR = "buildingType"
SPECIAL_VAR = "constructionTime"

# impute features
MEDIAN_IMPUTE_VAR = "DOM"
CAT_MEAN_IMPUTE_VAR = "communityAverage"
CAT_VAR = "Cid"
DROP_ROWS_VAR = "fiveYearsProperty"
FILL_0_VAR = "buildingType"

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

NUMERICAL_MIX_TYPE_NOT_ALLOWED = [feature for feature in INT_VARS]

PIPELINE_NAME = "lightgbm_regression"
PIPELINE_SAVE_FILE = f"{PIPELINE_NAME}_model_v"

# used for differential testing
ACCEPTABLE_MODEL_DIFFERENCE = 0.05

# minimum years accepted
MIN_YEARS_ACCEPTED = 2011
