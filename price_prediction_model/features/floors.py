from sklearn.base import BaseEstimator
import logging

_logger = logging.getLogger(__name__)


class FloorFeaturesCreation(BaseEstimator):
    """ Convert the mixed type feature floor to two features """

    def __init__(self, variable_to_replace=None):
        self.variable = variable_to_replace
        self.height_char_mapping = {
            "顶": "5",
            "高": "4",
            "中": "3",
            "低": "2",
            "底": "1",
            "未知": "0",
        }

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # before log
        _logger.info(
            f"""
                Before FloorFeaturesCreation Transformation: \n
                feature values: {X[[self.variable]].head().to_dict()} \n
            """
        )

        # take the first part of floor and transform is into categories as floorProximity
        X["floorProximity"] = (
            X[self.variable].str.split(" ").str[0].map(self.height_char_mapping)
        )

        # take the second part of floor and transform into a continuous variable as buildingTotalFloors
        X["buildingTotalFloors"] = X[self.variable].str.split(" ").str[1].astype(int)

        # after log
        _logger.info(
            f"""
                After FloorFeaturesCreation Transformation: \n
                floorProximity feature: {X["floorProximity"]
                                            .value_counts(sort=False)
                                            .to_dict()} \n
                
                buildingTotalFloors feature: {X["buildingTotalFloors"]
                                                .head()
                                                .to_dict()} \n
                
            """
        )

        return X
