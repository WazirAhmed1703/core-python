import os
from dotenv import load_dotenv

# load variable to env
load_dotenv()

BASE_URL = 'https://gorest.co.in/'
BASE_PATH = 'public/'
VERSION = 'v3/'

USERS = 'users'

def users():
    return BASE_URL + BASE_PATH + VERSION + USERS

def access_token():
    token = os.getenv("API_ACCESS_TOKEN")
    if not token:
        raise ValueError("Missing API_ACCESS_TOKEN. Check your .env file.") 
    return token