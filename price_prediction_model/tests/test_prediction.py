import math

from price_prediction_model.model.predict import make_prediction
from price_prediction_model.utils.utils import load_dataset


def test_make_single_prediction():
    # Given
    test_data = load_dataset(file_name="beijing_house_price_test_data.csv")
    single_test_input = test_data[0:1]

    # When
    subject = make_prediction(input_data=single_test_input)

    # Then
    assert subject is not None
    assert isinstance(subject.get("predictions")[0], float)
    assert math.ceil(subject.get("predictions")[0]) == 531
