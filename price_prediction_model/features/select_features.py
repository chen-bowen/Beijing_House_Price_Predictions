from sklearn.base import BaseEstimator
import logging

_logger = logging.getLogger(__name__)


class SelectFeatures(BaseEstimator):
    """ Select only the relevant features"""

    def __init__(self, variables_to_select=None):
        self.variables = variables_to_drop

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # before log
        _logger.info(
            f"""Before Select Features Transformation: \n
                Shape: {X.shape}\n 
                Columns: {list(X.columns)}
            """
        )

        # transformation
        X = X[[self.variables]]

        # after log
        _logger.info(
            f"""After Select Features Transformation: \n
                Shape: {X.shape}\n 
                Columns: {list(X.columns)}
            """
        )

        return X
