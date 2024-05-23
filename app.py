import os
from flask import Flask, jsonify, json
from dotenv import load_dotenv
import google.generativeai as genai
import google.ai.generativelanguage as glm

app = Flask(__name__)


description = {
    'Language-Model': 'gemini-1.5-pro-latest or gemini-1.5-flash-latest',
    'version': 'v1beta',
    'language': 'python (flask)',
    'routes': ['/top10movies'],
    'comment': 'language model response time not reliable but right now response type json configurable'
}

# test_api_url = "https://jsonplaceholder.typicode.com/todos/1"
# x = requests.get(test_api_url)
# db = description.json()

@app.route("/")
def home():
    return description



@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"status": 404, "message": "Not Found"}), 404

def call_api():

    load_dotenv()
    # Replace with your actual Google API key
    apiKey = os.getenv('GOOGLE_API_KEY')

    jsonSchema = {
    "title": "top 10 movie name from IMDB",
    "description": "Return the current top 10 movie name from IMDB",
    "type": "array",
        "properties": {
            "Movie_Name": {"type": "string"},
            "IMDB_link": {"type": "string"},
            "Movie_Rating": {"type": "string"}
        }
    }
    prompt = f"Follow JSON schema.<JSONSchema>{json.dumps(jsonSchema)}</JSONSchema>"
    genai.configure(api_key=apiKey)
    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro-latest", # or use gemini-1.5-flash-latest
        generation_config=glm.GenerationConfig(response_mime_type="application/json"),
    )
    response = model.generate_content(prompt)
    print(response.text)
    
    getText=response.text
    print(response.text)
    getjsonformate=json.loads(getText)
    
    # if type(getText) is list:
    #     print("ïts showing array")
    #     getjsonformate=json.loads(getText)

    #     return getjsonformate
    # else:
    #     print("ïts showing text___________")
    
    return getjsonformate
        
        

@app.route("/top10movies")
def testalp():
    return call_api()

