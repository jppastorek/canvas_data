import requests, os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

CANVAS_API_URL = os.environ.get('CANVAS_API_URL')
CANVAS_API_TOKEN = os.environ.get('CANVAS_API_TOKEN')
CANVAS_DEVELOPER_KEY = os.environ.get('CANVAS_DEVELOPER_KEY')


def get_canvas_data():
    headers = {
        'Authorization' : f'Bearer {CANVAS_API_TOKEN}'
    }
    response = requests.get(f'{CANVAS_API_URL}/users?per_page=1000', headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f'Error fetching Canvas data: {response.status_code}, {response.text}')

df = pd.DataFrame(get_canvas_data())

df.to_csv('data.csv', index=False)