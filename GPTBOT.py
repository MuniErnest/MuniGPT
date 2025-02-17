import google.generativeai as genai
from flask import Flask, request, jsonify

app = Flask(__name__)

# Set up Gemini API Key
genai.configure(api_key="AIzaSyAxgLyoaj3D4RSRdFpekLc1jF1eYTy2jAs")  # Replace with your actual key

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_input = request.json.get("message")

        # Send request to Google Gemini AI
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(user_input)

        return jsonify({"response": response.text})  # Get AI-generated text

    except Exception as e:
        print(f"🚨 Error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5000, debug=True)
