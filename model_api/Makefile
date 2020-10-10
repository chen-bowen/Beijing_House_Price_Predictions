#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_NAME = price_prediction_model_api
CONDA_ENVIRONMENT = price_prediction_model_api
PYTHON_VERSION = Python interpreter (e.g. 3, 3.5, 2.7)
NAME=house-pricing-api
AWS_REPO_NAME=house-pricing-model-api
HEROKU_APP_NAME=house-pricing-api
COMMIT_ID=$(shell git rev-parse HEAD)  # REMOVED
CLUSTER_NAME=house-pricing-api-cluster
SERVICE_NAME=house-pricing-api-service
TASK_DEFINITION_NAME=house-pricing-api-task-definition

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Install Poetry dependencies
poetry-install:
	poetry lock
	poetry config virtualenvs.create false \
		&& poetry export --without-hashes -f requirements.txt --dev\
		|  pip install -r /dev/stdin  --use-feature=2020-resolver\
		&& poetry debug

## test model api
test-api:
	pip install pytest
	PYTHONPATH=. python -m pytest -v -m "not differential" tests

build-ml-api-heroku:
	poetry export -f requirements.txt -o requirements.txt
	docker build -t registry.heroku.com/$(NAME)/web .

push-ml-api-heroku:
	docker push registry.heroku.com/${HEROKU_APP_NAME}/web:latest

aws-login:
	aws ecr get-login-password | docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.us-east-1.amazonaws.com

build-ml-api-aws:
	docker build -t $(AWS_REPO_NAME):$(COMMIT_ID) .

push-ml-api-aws:
	docker push ${AWS_ACCOUNT_ID}.dkr.ecr.us-east-1.amazonaws.com/$(AWS_REPO_NAME):$(COMMIT_ID)

tag-ml-api:
	docker tag $(AWS_REPO_NAME):$(COMMIT_ID) ${AWS_ACCOUNT_ID}.dkr.ecr.us-east-1.amazonaws.com/$(AWS_REPO_NAME):$(COMMIT_ID)

update-ec2-service:
	aws ecs update-service --cluster ${CLUSTER_NAME} --service ${SERVICE_NAME} --task-definition  ${TASK_DEFINITION_NAME} --force-new-deployment
