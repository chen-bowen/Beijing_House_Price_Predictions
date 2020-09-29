from sklearn.base import BaseEstimator
import logging

_logger = logging.getLogger(__name__)


class EncodeSpecialValueEncoder(BaseEstimator):
    """ encode outlier values to sensible range """

    def __init__(self, variables_to_encode=None):
        self.variable = variables_to_encode

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # before log
        _logger.info(
            f"""
                Before EncodeSpecialValueEncoder Transformation: \n
                data categories count: {X[[self.variable]]
                                        .value_counts(sort=False)
                                        .to_dict()}\n
            """
        )

        # encode construction years 0 and 未知 as 2018, 1 as 2017
        X[self.variable] = X[self.variable].astype("str")
        X.loc[
            (X[self.variable] == "0") | (X[self.variable] == "未知"), self.variable
        ] = "2018"
        X.loc[X[self.variable] == "1", self.variable] = "2017"

        # after log
        _logger.info(
            f"""
                After EncodeSpecialValueEncoder Transformation: \n
                data categories count: {X[[self.variable]]
                                        .value_counts(sort=False)
                                        .to_dict()} \n
            """
        )

        return X


class RareCategoryEncoder(BaseEstimator):
    """ Encode rare labels"""

    def __init__(self, variables_to_encode=None):
        self.variable = variables_to_encode

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # before log
        _logger.info(
            f"""
                Before RareCategoryEncoder Transformation: \n
                data categories count: {X[[self.variable]]
                                        .value_counts(sort=False)
                                        .to_dict()}\n
            """
        )

        # encode range below 1 to be 1
        X[self.variable] = X[self.variable].apply(lambda x: 1 if x < 1 else x)

        # after log
        _logger.info(
            f"""
                After EncodeSpecialValueEncoder Transformation: \n
                data categories count: {X[[self.variable]]
                                        .value_counts(sort=False)
                                        .to_dict()} \n
            """
        )

        return X
