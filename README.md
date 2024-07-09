# Chatbot with Model Selector

This is a Streamlit application that allows users to select from different NLP models and generate text based on their inputs. The models are hosted on Hugging Face Spaces.

## Features

- Select from multiple NLP models such as GPT-2, BERT, and RoBERTa.
- Generate text based on user input prompts.
- Display responses in a user-friendly interface.

## Setup

### Prerequisites

- Python 3.7 or later
- Streamlit
- Requests library
- Hugging Face API

## Running the App
Run the Streamlit app with the following command:


streamlit run app.py


## Usage
Open the Streamlit app in your browser.
Select a model from the dropdown menu.
Enter a prompt in the text area.
Click the "Generate" button to get the model's response.
## Troubleshooting
If you encounter any errors, ensure that:

The Hugging Face space URL is correctly specified in the app.py file.
The .env file is correctly set up with your Hugging Face API key.
All required Python packages are installed.

## License
This project is licensed under the MIT License. See the LICENSE file for details.



