from sklearn.base import BaseEstimator
from itertools import islice
import logging
import pandas as pd

_logger = logging.getLogger(__name__)


class ExponentialWeightedAvgPrice(BaseEstimator):
    """ Create exponentially weighted average price as a feature from target sale year and month """

    def __init__(
        self, target_sale_year=None, target_sale_month=None, prices=None, areas=None
    ):
        self.year = target_sale_year
        self.month = target_sale_month
        self.prices = prices
        self.areas = areas

    def fit(self, X, y=None):
        """ fit to get the average prices of a given month, year"""
        # calculate the EWMA price
        X["totalPrice"] = X[self.prices] * X[self.areas] // 10000

        average_prices = pd.DataFrame(
            X.groupby([self.year, self.month]).mean()["totalPrice"]
        )

        X.drop("totalPrice", axis=1, inplace=True)

        # convert and save the
        self.avg_price_map = average_prices.ewm(span=3).mean().to_dict()["totalPrice"]

        _logger.info(
            f"""
                Created price map \n
                first 3 values: {dict(islice(self.avg_price_map.items(), 3))} \n
            """
        )

        return self

    def transform(self, X):
        # self.fit(X)

        # create 3 month average price
        X["expAvgPrice3mon"] = X.apply(
            lambda row: self.avg_price_map[(row[self.year], row[self.month])], axis=1
        )

        # after log
        _logger.info(
            f"""
                Created 3 month average prices \n
                expAvgPrice3mon feature: {X["expAvgPrice3mon"]
                                                .head()
                                                .to_dict()} \n
                
            """
        )

        return X
