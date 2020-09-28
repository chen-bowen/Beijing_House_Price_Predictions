import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator


class SelectFeatures(BaseEstimator):
    """ Select only the relevant features"""

    def __init__(self, variables_to_drop=None):
        self.variables = variables_to_drop

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # encode labels
        X.drop(self.variables, axis=1, inplace=True)

        return X
