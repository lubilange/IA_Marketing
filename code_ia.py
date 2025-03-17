from flask import Flask, request, jsonify
import os
import google.generativeai as genai

# Initialize the Flask app
app = Flask(__name__)

# Load the API key from an environment variable for security
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable is not set")

# Configure the Google Generative AI library with the API key
genai.configure(api_key=API_KEY)

# Define a system prompt to guide the AI's behavior
SYSTEM_PROMPT = "You are a helpful assistant."

@app.route('/query', methods=['POST'])
def handle_query():
    """
    Handle POST requests to /query, process the user's query with Gemini,
    and return the response as JSON.
    """
    # Get the JSON data from the request
    data = request.get_json()
    if not data or 'query' not in data:
        return jsonify({"status": "error", "message": "Missing 'query' in request body"}), 400
    
    user_query = data['query']

    # Create a model instance with the system instruction
    model = genai.GenerativeModel(
        model_name="models/gemini-1.5-flash",  # Adjust model name as needed
        system_instruction=SYSTEM_PROMPT
    )

    try:
        # Generate content using the Gemini model
        response = model.generate_content(user_query)
        model_response = response.text  # Extract the generated text

        # Return the response as JSON
        return jsonify({"status": "success", "result": model_response})

    except Exception as e:
        # Handle any errors and return them as JSON
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)