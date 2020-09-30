from sklearn.base import BaseEstimator
import logging

_logger = logging.getLogger(__name__)


class SelectRows(BaseEstimator):
    """ Select only the relevant features"""

    def __init__(self, variables_to_filter_on=None, bound=None):
        self.variable = variables_to_filter_on
        self.bound = bound

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # before log
        _logger.info(
            f"""
                Before SelectRows Transformation:
                Shape: {X.shape}\n
            """
        )

        # transformation
        X = X[X[self.variable] >= self.bound]

        # after log
        _logger.info(
            f"""
                After SelectRows Transformation: \n
                Shape: {X.shape}\n 
            """
        )

        return X
