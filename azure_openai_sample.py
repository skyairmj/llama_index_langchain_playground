from dotenv import load_dotenv
import os
import openai

#load environment variables
load_dotenv()

openai.api_type = "azure"
openai.api_base = os.getenv("AZURE_OPENAI_API_ENDPOINT") 
openai.api_version = os.getenv("AZURE_OPENAI_API_VERSION") 
openai.api_key = os.getenv("AZURE_OPENAI_API_KEY")

deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")

response = openai.ChatCompletion.create(
    engine=deployment_name,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},
        {"role": "assistant", "content": "Yes, customer managed keys are supported by Azure OpenAI."},
        {"role": "user", "content": "Do other Azure Cognitive Services support this too?"}
    ]
)

print(response)
print(response['choices'][0]['message']['content'])