import requests

def get_response(user_query):
    """
    Sends the user query to the Gemini API (gemini-2.0-flash model) and returns the response.
    """
    # Gemini API endpoint
    api_url = "https://api.gemini.ai/v1/chat/completions"

    # Your Gemini API key
    api_key = "your-gemini-api-key"  # Replace with your actual API key

    # Prepare the request payload
    payload = {
        "model": "gemini-2.0-flash",  # Specify the gemini-2.0-flash model
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_query}
        ]
    }

    # Set the headers
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    try:
        # Make the POST request to the Gemini API
        response = requests.post(api_url, json=payload, headers=headers)
        response.raise_for_status()  # Raise an error for HTTP errors

        # Parse the response JSON
        response_data = response.json()
        return response_data["choices"][0]["message"]["content"]

    except requests.exceptions.RequestException as e:
        # Handle errors (e.g., network issues, invalid API key)
        return f"Error: Unable to fetch response from Gemini API. Details: {e}"

def handle_user_query(user_query):
    # Process the user query and return the simulated response
    response = get_response(user_query)
    return response