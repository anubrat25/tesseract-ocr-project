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

#taking user details
def enter_details():
    name = input("whats your name: ")
    age = input("enter your age:")
    gender = input("Enter your Gender(Male or Female): ")
    disease= input("Enter the details of any disease you have:") 
    return str('The persons age is: '+ age + ' the patients name is: '+ name + 'the persons gender is: '+ gender +' The details about the persons health conditions: ' +disease)


    
#generating the output
def generate_content(prompt):
    response = client.chat.completions.create(
        
    messages=[
        {"role": "system","content": "you are a health assistant"},
        {"role": "user","content": prompt,}],
        model="gemma-7b-it",# Or "Llama-3-8B" depending on your preference
        )
    return response

#main
image_path = r"C:\Users\vedant raikar\Desktop\ocr health project\tesseract-ocr-project\test files\img4.jpg"
text = perform_ocr(image_path)
text = text.rstrip('\n')
userdetails = enter_details()
output = generate_content("analyse this food ingredients:"+text+"based on these user details: "+userdetails+"And give a personalized response.")
print(output.choices[0].message.content)



