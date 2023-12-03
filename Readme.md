# E-Commerce Chatbot

This repository hosts the code for an e-commerce chatbot built with Rasa, a leading open-source conversational AI library.

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


## Usage

You can interact with the chatbot through the command line or through a web interface (if available). To interact through the command line, use `rasa shell` after starting the chatbot.

## Contributing

Contributions to this project are welcome. Please ensure you read the [contributing guidelines](CONTRIBUTING.md) before making a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.