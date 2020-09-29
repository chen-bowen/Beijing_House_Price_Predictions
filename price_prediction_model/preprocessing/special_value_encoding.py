from sklearn.base import BaseEstimator
import logging

_logger = logging.getLogger(__name__)


class EncodeSpecialValue(BaseEstimator):
    """ encode outlier values to sensible range """

    def __init__(self, variables_to_encode=None):
        self.variables = variables_to_encode

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # before log
        _logger.info(
            f"""
                Before EncodeSpecialValue Transformation: \n
                data categories count: {X[[self.variables]].value_counts().to_dict()}
            """
        )

        # encode construction years 0 and 未知 as 2018, 1 as 2017
        X[self.variables] = houses[self.variables].astype("str")
        X.loc[
            (X[self.variables] == "0") | (X[self.variables] == "未知"), self.variables
        ] = "2018"
        X.loc[X[self.variables] == "1", self.variables] = "2017"

        # after log
        _logger.info(
            f"""
                After EncodeSpecialValue Transformation: \n
                data categories count: {X[[self.variables]].value_counts().to_dict()}
            """
        )

        return X
