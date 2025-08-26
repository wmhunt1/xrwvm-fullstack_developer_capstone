import os
import requests
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv('backend_url', 'http://localhost:3030')
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    'http://localhost:5050/'
)


def get_request(endpoint, **kwargs):
    """
    Performs a GET request to a specified backend endpoint.

    Args:
        endpoint (str): The API endpoint to send the request to.
        **kwargs: Optional keyword arguments to be included as URL parameters.

    Returns:
        dict: The JSON response from the server, or None if an error occurs.
    """
    request_url = f"{backend_url}{endpoint}"
    print(f"GET from {request_url} with params {kwargs}")
    
    try:
        response = requests.get(request_url, params=kwargs)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Network exception occurred: {e}")
        return None

def analyze_review_sentiments(text):
    """
    Analyzes the sentiment of a given text string.

    Args:
        text (str): The review text to be analyzed.

    Returns:
        dict: The JSON response containing sentiment analysis, or None.
    """
    request_url = f"{sentiment_analyzer_url}analyze/{text}"
    print(f"GET from {request_url}")
    
    try:
        response = requests.get(request_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Network exception occurred: {e}")
        return None

def post_review(data_dict):
    """
    Submits a new review to the backend.

    Args:
        data_dict (dict): A dictionary containing the review data.

    Returns:
        dict: The JSON response from the server after posting, or None.
    """
    request_url = f"{backend_url}/insert_review"
    print(f"POST to {request_url}")
    
    try:
        response = requests.post(request_url, json=data_dict)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Network exception occurred: {e}")
        return None
