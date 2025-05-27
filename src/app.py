from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

# ✅ Replace with your actual GAT API key here
GAT_API_KEY = "AIzaSyC4XgT1kHag2bNEAKi1ghNPDI035uU18RU"

# ✅ Configure GAT (Gemini) API
genai.configure(api_key=GAT_API_KEY)

# ✅ Load Gemini/GAT model
model = genai.GenerativeModel("models/gemini-2.0-flash")

# ✅ Initialize Flask app
app = Flask(__name__)
CORS(app)  # Allow frontend access from different origin (localhost:3000)

@app.route("/query", methods=["POST"])
def query():
    try:
        data = request.get_json()
        user_query = data.get("query", "").strip()

        if not user_query:
            return jsonify({"response": "⚠️ Query cannot be empty."}), 400

        # Gemini (GAT) API call
        response = model.generate_content(
            contents=[{"role": "user", "parts": [{"text": user_query}]}]
        )
        chatbot_reply = response.candidates[0].content.parts[0].text.strip()

        return jsonify({"response": chatbot_reply})

    except Exception as e:
        return jsonify({"response": f"[Error] {str(e)}"}), 500

# ✅ Run the app
if __name__ == "__main__":
    app.run(debug=True)
