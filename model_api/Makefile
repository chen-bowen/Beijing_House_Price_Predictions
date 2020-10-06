#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_NAME = price_prediction_model_api
CONDA_ENVIRONMENT = price_prediction_model_api
PYTHON_VERSION = Python interpreter (e.g. 3, 3.5, 2.7)
NAME=house-pricing-api
HEROKU_APP_NAME=house-pricing-api
COMMIT_ID=$(shell git rev-parse HEAD)  # REMOVED

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Install Poetry dependencies
poetry-install:
	poetry config virtualenvs.create false \
		&& poetry export --without-hashes -f requirements.txt --dev\
		|  pip install -r /dev/stdin  --use-feature=2020-resolver\
		&& poetry debug

## test model api
test-api:
	pip install pytest
	PYTHONPATH=. python -m pytest -v tests 

build-ml-api-heroku:
	docker build -t registry.heroku.com/$(NAME)/web .

push-ml-api-heroku:
	docker push registry.heroku.com/${HEROKU_APP_NAME}/web:latest
