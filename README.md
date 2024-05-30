# Gemini Pro LTS Rest API (Deprecated Dependencies)

## Run in local environment
1. Setup your local environment for running Python app
2. Download the Repo
3. Add a `.env` file inside the folder and add `GOOGLE_API_KEY=replace_me_with_gemini_Key`
4. Install dependencies
```
pip install Flask
pip install python-dotenv
pip install google-ai-generativelanguage==0.6.2
pip install google-generativeai==0.5.2
```
5. For running the server use `flask run`

## Deploy to Render

1. Create a render account `https://render.com/`
2. Create a new Web Service
3. Build and deploy from a Git repository
4. Use Public Git repository or Sign in with your personal repo

```
Runtime: Python 3
Build Command: pip install -r requirements.txt
Start Command: gunicorn app:app
add a .env file and inside GOOGLE_API_KEY=replace_me_with_gemini_Key
```

# *Works with Google's deprecated dependencies