from sklearn.base import BaseEstimator


class CreateTargetVar(BaseEstimator):
    """ Impute the missing data with the median of the variable median """

    def __init__(self, target_var=None, target_var_orig=None):
        self.target_var_orig = target_var_orig
        self.target_var = target_var

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.rename({self.target_var_orig: self.target_var}, axis="columns")
        return X
