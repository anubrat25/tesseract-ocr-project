import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variable
api_key = os.getenv('API_KEY')

# Use the API key in your application
print(f"Your API key is: {api_key}")

