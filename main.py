import requests, os
from dotenv import load_dotenv

load_dotenv()

CANVAS_API_URL = os.environ.get('CANVAS_API_URL')
CANVAS_API_TOKEN = os.environ.get('CANVAS_API_TOKEN')
CANVAS_DEVELOPER_KEY = os.environ.get('CANVAS_DEVELOPER_KEY')


def get_canvas_data():
    headers = {
        'Authorization' : f'Bearer {CANVAS_API_TOKEN}'
    }
    response = requests.get(f'{CANVAS_API_URL}/users', headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f'Error fetching Canvas data: {response.status_code}, {response.text}')

print(get_canvas_data())