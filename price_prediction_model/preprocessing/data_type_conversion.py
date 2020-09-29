import pandas as pd
from sklearn.base import BaseEstimator

from price_prediction_moddel.utils.errors import InvalidModelInputError
import logging

_logger = logging.getLogger(__name__)


class ToInt(BaseEstimator):
    """ Convert variables to integer """

    def __init__(self, variables_to_convert=None):
        self.variables = variables_to_convert

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # before log
        _logger.info(
            f"""Before ToInt Transformation: \n
                data types: {X[[self.variables]].dtypes.to_dict()}\n
            """
        )

        # transformation
        X[[self.variables]] = X[[self.variables]].astype(int)

        # after log
        _logger.info(
            f"""After ToInt Transformation: \n
                data types: {X[[self.variables]].dtypes.to_dict()}\n
            """
        )

        return X


class ToCategories(BaseEstimator):
    """ Convert variables to categories """

    def __init__(self, variables_to_convert=None):
        self.variables = variables_to_convert

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # before log
        _logger.info(
            f"""Before ToCategories Transformation: \n
                data types: {X[[self.variables]].dtypes.to_dict()}\n
            """
        )

        # transformation
        for var in self.variables:
            X[var] = pd.Series(X[var], dtype="category")

        # after log
        _logger.info(
            f"""After ToCategories Transformation: \n
                data types: {X[[self.variables]].dtypes.to_dict()}\n
            """
        )

        return X
