from sklearn.base import BaseEstimator
import pandas as pd
import datetime as dt


class TradeYearMonth(BaseEstimator):
    """ Create trade year and trade month features """

    def __init__(self, date=None):
        self.date = date

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X["tradeYear"] = pd.to_datetime(X[self.date]).dt.year
        X["tradeMonth"] = pd.to_datetime(X[self.date]).dt.month
        return X


class HouseAgeYears(BaseEstimator):
    """ Create house age years feature """

    def __init__(self, datetime=None):
        self.datetime = datetime

    def fit(self, X, y=None):
        return self

    def transform(self, X):

        X["year"] = pd.to_datetime(X[self.datetime])
        X["houseAgeYears"] = round(
            (dt.datetime.today() - X["year"]).dt.days / 365
        ).astype(int)

        X.drop("year", axis=1, inplace=True)
        return X
