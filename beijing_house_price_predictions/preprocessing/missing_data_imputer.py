import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator


class VariableMedianImputer(BaseEstimator):
    """ Impute the missing data with the median of the variable median """

    def __init__(self, variables_to_impute=None):
        self.variables = variables_to_impute

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        for var in self.variables:
            X[var] = X[var].fillna(X[var].median())
        return X


class ZeroImputer(BaseEstimator):
    """ Impute the missing data with 0 """

    def __init__(self, variables_to_impute=None):
        self.variables = variables_to_impute

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        for var in self.variables:
            X[var] = X[var].fillna(0)
        return X
