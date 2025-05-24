import os  # load all variables from env file and save in os

from dotenv import load_dotenv

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
gemini_api_model = os.getenv("GEMINI_API_MODEL")
gemini_api_url = os.getenv("GEMINI_BASE_URL")

if not gemini_api_key or not gemini_api_url or not gemini_api_model:
    print("please set envirement variables")
    exit(1)


class Secrets:
    def __init__(self):
        self.gemini_api_key = gemini_api_key
        self.gemini_api_url = gemini_api_url
        self.gemini_api_model = gemini_api_model
