import streamlit as st
from langchain_community.llms import HuggingFaceEndpoint
from langchain import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

Huggingface_api = os.getenv("Huggingface_api")

# Configuring the page and setting the title of the Streamlit web app.
st.set_page_config(page_title="🦜🔗 Blog Outline Generator App")
st.title('🦜🔗 Blog Outline Generator App')


# Function to generate a blog outline based on a given topic.
def generate_response(topic):
    repo_id = "mistralai/Mistral-7B-Instruct-v0.2"
    llm = HuggingFaceEndpoint(repo_id=repo_id, huggingfacehub_api_token=Huggingface_api, temperature=0.3)
    # Creating a prompt template for the blog outline.
    template = 'As an experienced technical writer and expert on a subject, generate an outline on a blog about {topic}.'
    prompt = PromptTemplate(input_variables=['topic'], template=template)
    prompt_query = prompt.format(topic=topic)
    # Running the model with the prompt and displaying the response.
    response = llm.invoke(prompt_query)
    return st.info(response)

# Creating a form for user input.
with st.form('myform'):
    # Text input field for the blog topic.
    topic_text = st.text_input('Enter keyword:', placeholder="Ecommerce Business, Data Science, Machine Learning, etc")
    # Button to submit the form.
    submitted = st.form_submit_button('Submit')
    # Processing the form submission and generating a response.
    if submitted:
        generate_response(topic_text)