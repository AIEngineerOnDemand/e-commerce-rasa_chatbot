# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy only requirements to cache them in docker layer
COPY pyproject.toml poetry.lock* /app/

# Project initialization:
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

# Add the current directory contents into the container at /app
ADD . /app

# Switch to root user
USER root

# Train the Rasa NLU model
RUN rasa train nlu

# Change permissions of the config.yml file
RUN chmod 666 config.yml

# Use an unprivileged user
USER 1001

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Run rasa when the container launches
ENTRYPOINT ["rasa"]
CMD ["run", "--enable-api", "--port","8080"]