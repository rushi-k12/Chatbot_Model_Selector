import streamlit as st
import requests
from dotenv import load_dotenv
import os

load_dotenv()

# Streamlit App
def main():
    st.title('Chatbot with Model Selector')
    st.write('Choose a model and enter a prompt to generate text:')

    models = ["gpt2", "gpt2-medium", "bert-base-uncased", "roberta-base", "distilbert-base-uncased"]
    selected_model = st.selectbox("Choose a model", models)

    user_input = st.text_area("You:")

    if st.button("Generate"):
        if user_input:
            try:
                # Use the correct URL
                url = "https://huggingface.co/spaces/rushi-k/app_13"
                response = requests.get(
                    url,
                    params={"model": selected_model, "prompt": user_input}
                )
                response.raise_for_status()  # Check for HTTP request errors
                result = response.json()
                st.write("Bot:")
                st.write(result["generated_text"])
            except requests.HTTPError as http_err:
                st.error(f"HTTP error occurred: {http_err}")
            except Exception as err:
                st.error(f"An error occurred: {err}")
        else:
            st.warning("Please enter a prompt.")

if __name__ == '__main__':
    main()
