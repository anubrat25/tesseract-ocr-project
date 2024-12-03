import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

def get_kg_terms_and_categories(keyword, limit=20, language='en'):
    """Retrieve terms and categories from Google's Knowledge Graph API."""
    url = "https://kgsearch.googleapis.com/v1/entities:search"
    api_key = os.getenv('gkg_api')
    if not api_key:
        raise ValueError("API key not found. Set the 'gkg_api' environment variable.")
    
    params = {
        'query': keyword,
        'key': api_key,
        'limit': limit,
        'languages': language
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        terms_categories = []
        
        for item in data.get('itemListElement', []):
            result = item.get('result', {})
            name = result.get('name', '')
            categories = result.get('@type', [])
            description = result.get('description', 'No description available')
            
            # Append to results
            terms_categories.append({
                'name': name,
                'categories': categories,
                'description': description
            })
        
        return terms_categories
    else:
        return {"error": f"API request failed with status code {response.status_code}"}

# Example Usage
keyword = "vitamin c"
results = get_kg_terms_and_categories(keyword, limit=5)
print(results)