from flask import Blueprint, request, jsonify
from price_prediction_model.model.predict import make_prediction
from price_prediction_model import __version__ as _version
import os
from werkzeug.utils import secure_filename

from api.config import get_logger, UPLOAD_FOLDER
from api.validation import validate_inputs, allowed_file
from api import __version__ as api_version

_logger = get_logger(logger_name=__name__)


prediction_app = Blueprint("prediction_app", __name__)


@prediction_app.route("/", methods=["GET"])
def default_page():
    if request.method == "GET":
        _logger.info("health status OK")
        return "Your Beijing House Price Predictions Model API is Starting"


@prediction_app.route("/health", methods=["GET"])
def health():
    if request.method == "GET":
        _logger.info("health status OK")
        return "ok"


@prediction_app.route("/version", methods=["GET"])
def version():
    if request.method == "GET":
        return jsonify({"model_version": _version, "api_version": api_version})


@prediction_app.route("/v1/predict/model", methods=["POST"])
def predict():
    if request.method == "POST":
        # Step 1: Extract POST data from request body as JSON
        json_data = request.get_json()
        _logger.debug(f"Inputs: {json_data}")

        # Step 2: Validate the input using marshmallow schema
        # input_data, errors = validate_inputs(input_data=json_data)
        input_data = json_data
        errors = []

        # Step 3: Model prediction
        response = make_prediction(input_data=input_data)
        _logger.debug(f"Outputs: {response}")

        # Step 4: Convert numpy ndarray to list
        predictions = response.get("predictions").tolist()
        version = response.get("version")

        # Step 5: Return the response as JSON
        return jsonify(
            {"predictions": predictions, "version": version, "errors": errors}
        )
