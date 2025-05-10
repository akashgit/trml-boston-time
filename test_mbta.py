import requests
import json
from datetime import datetime

def get_mbta_data():
    url = 'https://api-v3.mbta.com/predictions'
    params = {
        'filter[stop]': 'place-portr',
        'sort': 'arrival_time',
        'include': 'trip,route',
        'page[limit]': 6,
        'filter[route_type]': '0,1,2'  # Include all transit types
    }
    
    response = requests.get(url, params=params)
    print(json.dumps(response.json(), indent=2))

if __name__ == '__main__':
    get_mbta_data() 