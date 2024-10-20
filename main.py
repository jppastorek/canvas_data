import requests, os
from dotenv import load_dotenv

load_dotenv()

CANVAS_URL = os.environ.get('CANVAS_URL')
CANVAS_API_KEY = os.environ.get('CANVAS_API_KEY')

response = requests.get(f'{CANVAS_URL}')
