from price_prediction_model.preprocessing.data_type_conversion import (
    ToCategories,
    ToInt,
)

from price_prediction_model.preprocessing.missing_data_imputer import (
    VariableMedianImputer,
    ZeroImputer,
    CategoricalMeanImputer,
    DropMissingDataRows,
)

from price_prediction_model.preprocessing.select_rows import SelectRows
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
                    "Select Rows",
                    SelectRows(
                        variables_to_filter_on=config.DATETIME_VAR_YEAR,
                        bound=config.MIN_YEARS_ACCEPTED,
                    ),
                ),
                ("Data Type Conversion, To Int", ToInt(variables=config.INT_VARS)),
                (
                    "Rare Category Encoding",
                    RareCategoryEncoder(variables_to_encode=config.RARE_CATEGORY_VAR),
                ),
                (
                    "Special Value Encoding",
                    EncodeSpecialValueEncoder(variables_to_encode=config.SPECIAL_VAR),
                ),
                (
                    "Missing Data Imputation, Column Median",
                    VariableMedianImputer(variables_to_impute=config.MEDIAN_IMPUTE_VAR),
                ),
                (
                    "Missing Data Imputation, Categorical Mean",
                    CategoricalMeanImputer(
                        variables_to_impute=(config.CAT_MEAN_IMPUTE_VAR, config.CAT_VAR)
                    ),
                ),
                (
                    "Missing Data Imputation, Fill 0",
                    ZeroImputer(variables_to_impute=config.FILL_0_VAR),
                ),
                (
                    "Missing Data Imputation, Drop Rows",
                    DropMissingDataRows(variables_to_impute=config.DROP_ROWS_VAR),
                ),
                (
                    "Trade Year Month from Date",
                    TradeYearMonth(date=config.DATETIME_VAR),
                ),
                (
                    "House Age Month from Date",
                    HouseAgeYears(date=config.TEMPORAL_VAR_TO_AGE),
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
                        prices=config.TARGET,
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
                    ToCategories(variables=config.CATEGORICAL_VARS),
                ),
                (
                    "Select Final Features Set",
                    SelectFeatures(variables_to_select=config.FEATURES),
                ),
                ("LightGBM Model", lgbm.LGBMRegressor(**hyper_params)),
            ]
        )

    def train(self, X_train, y_train, X_val, y_val):
        """ Train the model using the pipeline constructed """

        self.model_pipeline.fit(
            X_train,
            y_train,
            eval_metric=config.EVAL_METRIC,
            eval_set=[(X_val, y_val)],
            early_stopping_rounds=config.EARLY_STOP_RND,
            verbose=0,
        )

    def predict(self, X):
        """ Predict with the pipeline created and return the predictions"""

        y_pred = self.model_pipeline.predict(X)
        return y_pred
