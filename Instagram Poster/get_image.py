# Imports
import requests
from dotenv import load_dotenv
import os
from urllib.parse import quote_plus

# Load Bing API
load_dotenv()
BING_SEARCH_URL = "https://api.bing.microsoft.com/v7.0/images/search"

# Function to get car image URL using Bing Image Search API
def get_car_image_bing(query):
    
    # Get API key
    api_key = os.getenv("BING_API_KEY")

    # Properly format query string for URL search
    search_query = quote_plus(query)

    # Set headers with API key
    headers = {
        "Ocp-Apim-Subscription-Key": api_key
    }

    # Send request to Bing Image Search API
    params = {"q": search_query, "count": 1, "imageType": "photo"}
    response = requests.get(BING_SEARCH_URL, headers=headers, params=params)

    if response.status_code == 200:

        # Parse response and get image URL
        data = response.json()

        if "value" in data and len(data["value"]) > 0:
            image_url = data["value"][0]["contentUrl"]
            return image_url
        
        else:
            return "No image found"
        
    else:
        return f"Error fetching image: {response.status_code}"
