# Use the official Python image from the Docker Hub as the base image
FROM python:3.11-slim

RUN apt update
RUN apt-get -y install gcc

# Set the working directory in the container
WORKDIR /app

RUN pip install poetry

COPY pyproject.toml pyproject.toml

RUN poetry install 

COPY . .

CMD ["dvc", "repro" "--force"]
