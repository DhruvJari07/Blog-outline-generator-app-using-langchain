from langchain_community.llms import HuggingFaceEndpoint
from langchain import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

Huggingface_api = os.getenv("Huggingface_api")

repo_id = "mistralai/Mistral-7B-Instruct-v0.2"
llm = HuggingFaceEndpoint(repo_id=repo_id, huggingfacehub_api_token=Huggingface_api, temperature=0.3)

template = "As an experienced technical writer and expert on a subject, generate an outline on a blog about {topic}."
prompt = PromptTemplate(input_variables = ['topic'], template=template)

topic = "Ecommerce Business"

prompt_query = prompt.format(topic=topic)

response = llm.invoke(prompt_query)

print(response)

