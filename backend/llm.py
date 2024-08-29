from groq import Groq
from ocr import perform_ocr
import os
from dotenv import load_dotenv
import json 

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variable
key = os.getenv('API_KEY')
client = Groq(api_key=key)

def generate_content(prompt):
    response = client.chat.completions.create(
        
    messages=[
        {
            "role": "system",
            "content": "you are a health assistant"
        },
        
        {"role": "user",
               "content": prompt,}

    ],

    model="gemma-7b-it",# Or "Llama-3-8B" depending on your preference

    )
    return response

image_path = r"C:\Users\vedant raikar\Desktop\ocr health project\tesseract-ocr-project\test files\img4.jpg"
text = perform_ocr(image_path)
text = text.rstrip('\n')
output = generate_content("analyse this food ingredients:"+text)
print(output)


