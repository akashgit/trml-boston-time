from flask import Flask, render_template, jsonify
import requests
import json
import schedule
import time
import os
from datetime import datetime
from dotenv import load_dotenv
import threading
import pytz

# Load environment variables
load_dotenv()

app = Flask(__name__)

# MBTA API configuration
MBTA_API_KEY = os.getenv('MBTA_API_KEY', '')
STOP_ID = 'place-portr'  # Porter Square stop ID

# Headers for MBTA API requests
headers = {
    'x-api-key': MBTA_API_KEY,
    'Accept': 'application/vnd.api+json'
}

def get_red_line_stops():
    """Fetch all stops for the Red Line"""
    try:
        response = requests.get(
            'https://api-v3.mbta.com/stops',
            params={
                'filter[route]': 'Red',
                'sort': 'name'
            },
            headers=headers
        )
        
        response.raise_for_status()
        return response.json()['data']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching stops: {e}")
        return []

# Global variable to store train data
train_data = {
    "current_time": "",
    "timezone": "America/New_York",
    "inbound_trains": [],
    "outbound_trains": []
}

def get_next_trains():
    """Fetch next train predictions from MBTA API"""
    try:
        # Make request to MBTA API with minimal parameters
        url = 'https://api-v3.mbta.com/predictions'
        params = {
            'filter[stop]': STOP_ID,
            'filter[route]': 'Red',
            'include': 'trip,schedule,vehicle',
            'sort': 'arrival_time'
        }
        
        response = requests.get(url, headers=headers, params=params)
        
        response.raise_for_status()
        data = response.json()

        # Process the data
        inbound_trains = []
        outbound_trains = []
        
        for pred in data.get('data', []):
            # Get the trip data
            trip_id = pred['relationships']['trip']['data']['id']
            trip = next((t for t in data['included'] if t['type'] == 'trip' and t['id'] == trip_id), None)
            
            if trip:
                # Calculate minutes until arrival
                arrival_time = datetime.fromisoformat(pred['attributes']['arrival_time'].replace('Z', '+00:00'))
                now = datetime.now(pytz.UTC)
                minutes_away = int((arrival_time - now).total_seconds() / 60)
                
                # Only include trains that haven't arrived yet
                if minutes_away >= 0:
                    train_info = {
                        'id': pred['id'],
                        'direction': trip['attributes']['direction_id'],
                        'destination': trip['attributes']['headsign'],
                        'minutes_away': minutes_away,
                        'arrival_time': arrival_time.strftime('%I:%M %p'),
                        'status': pred['attributes']['status']
                    }
                    
                    # Determine direction based on destination
                    destination = trip['attributes']['headsign'].lower()
                    if 'alewife' in destination:
                        inbound_trains.append(train_info)
                    else:
                        outbound_trains.append(train_info)

        # Update global variable
        train_data['current_time'] = datetime.now().strftime('%I:%M %p')
        train_data['inbound_trains'] = inbound_trains[:5]  # Limit to 5 trains per direction
        train_data['outbound_trains'] = outbound_trains[:5]
        print(f"Successfully processed {len(inbound_trains)} inbound and {len(outbound_trains)} outbound trains")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching train data: {e}")
        # Keep existing data if there's an error

def run_schedule():
    """Run the scheduler in a separate thread"""
    while True:
        schedule.run_pending()
        time.sleep(1)

# Schedule the train data update
schedule.every(1).minutes.do(get_next_trains)

# Start the scheduler in a separate thread
scheduler_thread = threading.Thread(target=run_schedule)
scheduler_thread.daemon = True
scheduler_thread.start()

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html', train_data=train_data)

@app.route('/stops')
def stops():
    """Display all Red Line stops"""
    stops = get_red_line_stops()
    return render_template('stops.html', stops=stops)

@app.route('/api/trains')
def get_trains():
    """API endpoint to get train data"""
    return jsonify(train_data)

if __name__ == '__main__':
    # Initial data fetch
    get_next_trains()
    # Run the Flask app
    app.run(host='0.0.0.0', port=3000, debug=True) 