from sklearn.pipeline import Pipeline
import lightgbm as lgbm

from price_prediction_model.preprocessing.data_type_conversion import (
    ToCategories,
    ToInt,
)

from price_prediction_model.preprocessing.missing_data_imputer import (
    VariableMedianImputer,
    ZeroImputer,
    CategoricalMeanImputer,
)

from price_prediction_model.preprocessing.special_value_encoding import (
    EncodeSpecialValueEncoder,
    RareCategoryEncoder,
)

from price_prediction_model.features.floors import FloorFeaturesCreation
from price_prediction_model.features.moving_average import ExponentialWeightedAvgPrice
from price_prediction_model.features.select_features import SelectFeatures
from price_prediction_model.features.target_var import TargetVarCreation
from price_prediction_model.features.year_month_from_date import (
    HouseAgeYears,
    TradeYearMonth,
)

from price_prediction_model.config import config

import logging


_logger = logging.getLogger(__name__)


class ModelPipeline:
    """ model pipeline building, training and prediction """

    def __init__(self):
        self.build_model()

    def build_model(self):
        self.model_pipeline = Pipeline(
            [
                (
                    "Rare Category Encoding",
                    RareCategoryEncoder(variable_to_encode=config.RARE_CATEGORY_VAR),
                ),
                (
                    "Special Value Encoding",
                    EncodeSpecialValueEncoder(variable_to_encode=config.SPECIAL_VAR),
                ),
                (
                    "Missing Data Imputation, Column Median",
                    VariableMedianImputer(
                        variables_to_impute=[config.MEDIAN_IMPUTE_VAR]
                    ),
                ),
                (
                    "Missing Data Imputation, Categorical Mean",
                    CategoricalMeanImputer(
                        category_variable_pair=[
                            (config.CAT_MEAN_IMPUTE_VAR, config.CAT_VAR)
                        ]
                    ),
                ),
                (
                    "Missing Data Imputation, Fill 0",
                    ZeroImputer(variables_to_impute=[config.FILL_0_VAR]),
                ),
                (
                    "Trade Year Month from Date",
                    TradeYearMonth(date=config.DATETIME_VAR),
                ),
                (
                    "House Age Month from Date",
                    HouseAgeYears(datetime=config.TEMPORAL_VAR_TO_AGE),
                ),
                (
                    "Create Floors Feature",
                    FloorFeaturesCreation(variable_to_replace=config.NON_UNICODE_VAR),
                ),
                (
                    "Create Moving Average Price Feature",
                    ExponentialWeightedAvgPrice(
                        target_sale_year=config.DATETIME_VAR_YEAR,
                        target_sale_month=config.DATETIME_VAR_MONTH,
                        prices=config.PRICES_PER_AREA,
                        areas=config.AREA,
                    ),
                ),
                (
                    "Create Target Variable",
                    TargetVarCreation(
                        target_var=config.TARGET, target_var_orig=config.TARGET_ORIGINAL
                    ),
                ),
                (
                    "Data Type Conversion, To Categories",
                    ToCategories(variables_to_convert=config.CATEGORICAL_VARS),
                ),
                (
                    "Data Type Conversion, To Int",
                    ToInt(variables_to_convert=config.INT_VARS),
                ),
                (
                    "Select Final Features Set",
                    SelectFeatures(variables_to_select=config.FEATURES),
                ),
                ("LightGBM", lgbm.LGBMRegressor(**config.HYPER_PARAMS)),
            ]
        )

    def train(self, X_train, y_train):
        """ Train the model using the pipeline constructed """

        self.model_pipeline.fit(X_train, y_train)

    def predict(self, X):
        """ Predict with the pipeline created and return the predictions"""

        y_pred = self.model_pipeline.predict(X)
        return y_pred
