FROM python:3.7.6

# Create the user that will run the app
RUN adduser --disabled-password --gecos '' model-api-user

WORKDIR /app

ARG PIP_EXTRA_INDEX_URL
ENV FLASK_APP run.py

# Install requirements, including from Gemfury
ADD . /app

RUN pip install --upgrade pip
RUN pip install poetry
RUN make poetry-install

RUN chmod +x run.sh
RUN chown -R model-api-user:model-api-user ./

USER model-api-user

EXPOSE 5000

CMD ["bash", "./run.sh"]