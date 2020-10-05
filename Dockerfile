FROM python:3.7.6

# Create the user that will run the app
RUN adduser --disabled-password --gecos '' model-api-user

WORKDIR /app/model_api

ARG PIP_EXTRA_INDEX_URL
ENV FLASK_APP run.py

# Install requirements, including from Gemfury
ADD ./model_api /app/model_api/

RUN pip install --upgrade pip
RUN cd ./app/model_api && make poetry-install

RUN chmod +x /app/ml_api/run.sh
RUN chown -R model-api-user:model-api-user ./

USER model-api-user

EXPOSE 5000

CMD ["bash", "./run.sh"]