from revChatGPT.V1 import Chatbot

def get_response(user_query):
    """
    Sends the user query to ChatGPT and returns the response.
    """
#     chatbot = Chatbot(config={
#     "session_token": "your-session-token"  # Replace with your session token
# })
    chatbot = Chatbot(config={
        "email": "your-email@example.com",  # Replace with your OpenAI email
        "password": "your-password"         # Replace with your OpenAI password
    })

    response = ""
    for data in chatbot.ask(user_query):
        response = data["message"]

    return response

def handle_user_query(user_query):
    # Process the user query and return the simulated response
    response = get_response(user_query)
    return response