k.PHONY: create_environment git

#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_NAME = price_prediction_model
CONDA_ENVIRONMENT = price_prediction_model
PYTHON_VERSION = Python interpreter (e.g. 3, 3.5, 2.7)

#################################################################################
# COMMANDS                                                                      #
#################################################################################

fetch-dataset:
	chmod +x ./scripts/fetch_kaggle_dataset.sh
	./scripts/fetch_kaggle_dataset.sh	

## Install Poetry dependencies
poetry-install:
	poetry lock
	poetry config virtualenvs.create false \
		&& poetry export --without-hashes -f requirements.txt --dev\
		|  pip install -r /dev/stdin \
		&& poetry debug

build-setup:
	pip install dephell
	dephell deps convert

# train model
train:
	PYTHONPATH=.. python ../price_prediction_model/model/train.py

## test price prediction model
test-model:
	pip install pytest==6.1.1
	PYTHONPATH=.. python ../price_prediction_model/utils/generate_test_dataset.py	
	PYTHONPATH=. python -m pytest -v tests 

package:
	pip install twine
	python setup.py sdist
	twine upload --skip-existing dist/*

