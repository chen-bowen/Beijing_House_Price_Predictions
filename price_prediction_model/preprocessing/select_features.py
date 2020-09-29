from sklearn.base import BaseEstimator


class SelectFeatures(BaseEstimator):
    """ Select only the relevant features"""

    def __init__(self, variables_to_select=None):
        self.variables = variables_to_drop

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # encode labels
        X = X[[self.variables]]

        return X
