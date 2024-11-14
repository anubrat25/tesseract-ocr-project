import requests
from bs4 import BeautifulSoup

def get_relevant_articles(keywords):
    # News API endpoint
    endpoint = "https://newsapi.org/v1/everything"
    api_key = "14ade100cceb421499d0418149172372"
    # Define query parameters
    params = {
        "q": keywords,
        "language": "en",
        "pageSize": 10,  # Number of articles to retrieve
        "apiKey": api_key
    }
    
    # Make the GET request to the News API
    response = requests.get(endpoint, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        results = response.json().get("articles", [])
        
        # Collect and aggregate article content
        all_content = ""
        
        for article in results:
            url = article["url"]
            content = article.get("content", "")
            
            # Fetch full content if partial content is provided
            if not content:
                try:
                    content = fetch_article_content(url)
                except Exception as e:
                    print(f"Could not retrieve content for {url}: {e}")
                    content = ""
            
            # Add article title and content to the overall content
            all_content += f"Title: {article['title']}\nContent:\n{content}\n\n"
        
        return all_content
    else:
        print("Error:", response.status_code, response.text)
        return ""

def fetch_article_content(url):
    # Fetch and parse the main content from the article URL using BeautifulSoup
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Extract text from paragraph tags
    paragraphs = soup.find_all("p")
    content = "\n".join([p.get_text() for p in paragraphs])
    
    return content if content else "Content not available."



