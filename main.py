import requests, os, time
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

CANVAS_API_URL = os.environ.get('CANVAS_API_URL')
CANVAS_API_TOKEN = os.environ.get('CANVAS_API_TOKEN')
CANVAS_DEVELOPER_KEY = os.environ.get('CANVAS_DEVELOPER_KEY')

canvas_url = f'{CANVAS_API_URL}/users?enrollment_type=teacher&per_page=50'

def get_canvas_data(url):
    data_set = []
    total_start_time = time.time()
    total_items = 0
    
    while url:
        start_time = time.time()
        headers = {
            'Authorization' : f'Bearer {CANVAS_API_TOKEN}'
        }
        print("Sending request...")
        response = requests.get(url, headers=headers)
    
        if response.status_code == 200:
            link_header = response.headers.get('Link')
            url = get_next_link(link_header)
            data = response.json()
            data_set.extend(data)
            request_time = time.time() - start_time
            print(f"Fetched {len(data)} items in {request_time:.2f} seconds.")
            total_items += len(data)
        else:
            raise Exception(f'Error fetching Canvas data: {response.status_code}, {response.text}')
    total_time = time.time() - total_start_time
    print(f"Total time taken to fetch {total_items} items: {total_time:.2f} seconds.")
    return data_set


def get_next_link(link_header):
    if not link_header:
        return None
    
    links = {}
    for part in link_header.split(','):
        section = part.split(';')
        url = section[0].strip()[1:-1] # Remove the angle brackets
        rel = section[1].strip().split('=')[1].strip('"')
        links[rel] = url
    return links.get('next')


df = pd.DataFrame(get_canvas_data(canvas_url))

df.to_csv('data.csv', index=False)