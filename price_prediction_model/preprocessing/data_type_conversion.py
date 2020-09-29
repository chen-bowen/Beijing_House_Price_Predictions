import pandas as pd
from sklearn.base import BaseEstimator

from price_prediction_moddel.utils.errors import InvalidModelInputError


class ToInt(BaseEstimator):
    """ Convert variables to integer """

    def __init__(self, variables_to_convert=None):
        self.variables = variables_to_convert

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # encode labels
        X[[self.variables]] = X[[self.variables]].astype(int)

        return X


class ToCategories(BaseEstimator):
    """ Convert variables to categories """

    def __init__(self, variables_to_convert=None):
        self.variables = variables_to_convert

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # encode labels
        for var in self.variables:
            X[var] = pd.Series(X[var], dtype="category")

        return X
