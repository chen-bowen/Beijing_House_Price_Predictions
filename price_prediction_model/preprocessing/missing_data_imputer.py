from sklearn.base import BaseEstimator
import logging

_logger = logging.getLogger(__name__)


class VariableMedianImputer(BaseEstimator):
    """ Impute the missing data with the median of the variable median """

    def __init__(self, variables_to_impute=None):
        self.variables = variables_to_impute

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # before log
        _logger.info(
            f"""Before VariableMedianImputer Transformation: \n
                data null counts: {X[[self.variables]]
                                    .isnull()
                                    .sum()
                                    .to_dict()}\n
            """
        )
        # transformation
        for var in self.variables:
            X[var] = X[var].fillna(X[var].median())

        # after log
        _logger.info(
            f"""After VariableMedianImputer Transformation: \n
                data null counts: {X[[self.variables]]
                                    .isnull()
                                    .sum()
                                    .to_dict()}\n
            """
        )
        return X


class ZeroImputer(BaseEstimator):
    """ Impute the missing data with 0 """

    def __init__(self, variables_to_impute=None):
        self.variables = variables_to_impute

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # before log
        _logger.info(
            f"""Before ZeroImputer Transformation: \n
                data null counts: {X[[self.variables]]
                                    .isnull()
                                    .sum()
                                    .to_dict()}\n
            """
        )

        for var in self.variables:
            X[var] = X[var].fillna(0)

        # after log
        _logger.info(
            f"""After ZeroImputer Transformation: \n
                data null counts: {X[[self.variables]]
                                    .isnull()
                                    .sum()
                                    .to_dict()}\n
            """
        )
        return X


class CategoricalMeanImputer(BaseEstimator):
    """ Impute the missing data with mean of a certain category """

    def __init__(self, category_variable_pair=None):
        self.category_variable_pair = category_variable_pair

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        for category, var in self.category_variable_pair:
            # before log
            _logger.info(
                f"""Before CategoricalMeanImputer Transformation: \n
                    data null counts: {X[[self.var]]
                                        .isnull()
                                        .sum()
                                        .to_dict()}\n
            """
            )

            X[var] = X.groupby(category).transform(lambda x: x.fillna(x.mean()))

            # after log
            _logger.info(
                f"""After CategoricalMeanImputer Transformation: \n
                    data null counts: {X[[self.var]]
                                        .isnull()
                                        .sum()
                                        .to_dict()}\n
                """
            )

        return X


class DropMissingDataRows(BaseEstimator):
    """ Drop rows if the variable value is missing in that row """

    def __init__(self, variables_to_impute=None):
        self.category_variable_pair = category_variable_pair

    def fit(self, X, y=None):
        return self

    def transform(self, X):

        # before log
        _logger.info(
            f"""Before DropMissingDataRows Transformation: \n
                data rows: {X.shape[0]}\n
                data null counts: {X[[self.variables]]
                                    .isnull()
                                    .sum()
                                    .to_dict()}\n
            """
        )

        for var in self.variables:
            X.dropna(subset=[var], inplace=True)

        # after log
        _logger.info(
            f"""After DropMissingDataRows Transformation: \n
                data rows: {X.shape[0]}\n
                data null counts: {X[[self.variables]]
                                    .isnull()
                                    .sum()
                                    .to_dict()}\n
            """
        )
        return X
