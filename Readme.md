# E-Commerce Chatbot

This repository hosts the code for an e-commerce chatbot built with Rasa, a leading open-source conversational AI library.

## Running the Code

We have updated our execution process. Now, we run the code through `rasa_host.py`. To execute the code, use the following command:

```bash
python rasa_host.py
```

## Data Tracking

We are now tracking data to a PostgreSQL datastore. If you want to run this locally, you can spin up a PostgreSQL instance using Docker. Here's a basic command to get you started:

```bash
docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres
```

Replace `mysecretpassword` with a password of your choice. This will start a new PostgreSQL instance that you can connect to.

## Project Overview

The chatbot is designed to assist users in navigating an e-commerce platform. It can perform tasks such as:
- Answering queries about products
- Providing product recommendations
- Guiding users through the purchasing process

## File Structure

- `actions.py`: This file contains custom actions that the Rasa chatbot can perform. These actions can interact with the user, call APIs, or modify the state of the conversation.
## Project Overview

The chatbot is designed to assist users in navigating an e-commerce platform. It can perform tasks such as:
- Answering queries about products
- Providing product recommendations
- Guiding users through the purchasing process

## File Structure

- `actions.py`: This file contains custom actions that the Rasa chatbot can perform. These actions can interact with the user, call APIs, or modify the state of the conversation.

## Installation

Follow these steps to set up and run the project:

1. Clone this repository to your local machine.
2. Install the dependencies. This project uses Poetry for dependency management. If you have Poetry installed, you can install the dependencies with `poetry install`.
3. Ensure Rasa is installed. If not, you can install it with `pip install rasa`.
4. Train the chatbot model with `rasa train`.
5. Start the chatbot with `rasa run`.

## Docker Image

A Docker image of the application has been created and is available on Docker Hub.

You can pull the Docker image using the following command:
