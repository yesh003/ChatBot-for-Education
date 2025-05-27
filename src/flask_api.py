from flask import Flask, request, jsonify
from flask_cors import CORS
from response_handler import handle_user_query  # your existing backend logic

app = Flask(__name__)
CORS(app)  # Allow requests from React frontend

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_query = data.get('query')
    if not user_query:
        return jsonify({"error": "No query provided"}), 400
    try:
        answer = handle_user_query(user_query)
        return jsonify({"response": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5000, debug=True)
