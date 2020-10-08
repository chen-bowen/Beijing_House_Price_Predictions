import typing as t

from marshmallow import Schema, fields
from marshmallow import ValidationError

from api import config


class InvalidInputError(Exception):
    """Invalid model input."""


class HouseDataRequestSchema(Schema):
    url = fields.Str()
    id = fields.Int()
    Lng = fields.Float()
    Lat = fields.Float()
    Cid = fields.Int()
    tradeTime = fields.Str()
    DOM = fields.Float(allow_none=True)
    followers = fields.Int()
    price = fields.Int()
    square = fields.Float()
    livingRoom = fields.Int()
    drawingRoom = fields.Int()
    kitchen = fields.Int()
    bathRoom = fields.Int()
    floor = fields.Str()
    buildingType = fields.Float(allow_none=True)
    constructionTime = fields.Str()
    renovationCondition = fields.Int()
    buildingStructure = fields.Int()
    ladderRatio = fields.Float()
    elevator = fields.Float()
    fiveYearsProperty = fields.Float()
    subway = fields.Float(allow_none=True)
    district = fields.Int()
    communityAverage = fields.Float()


def _filter_error_rows(errors: dict, validated_input: t.List[dict]) -> t.List[dict]:
    """Remove input data rows with errors."""

    indexes = errors.keys()
    # delete them in reverse order so that you
    # don't throw off the subsequent indexes.
    for index in sorted(indexes, reverse=True):
        del validated_input[index]

    return validated_input


def validate_inputs(input_data):
    """Check prediction inputs against schema."""

    # set many=True to allow passing in a list
    schema = HouseDataRequestSchema(strict=True, many=True)

    errors = None
    try:
        schema.load(input_data)
    except ValidationError as exc:
        errors = exc.messages

    if errors:
        validated_input = _filter_error_rows(errors=errors, validated_input=input_data)
    else:
        validated_input = input_data

    return validated_input, errors
