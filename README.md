# MBTA Train Times Display

A real-time display of MBTA Red Line train times at Porter Square station, featuring an animated visualization of train movements.

## Features

- Real-time train arrival predictions
- Animated visualization of train movements
- Separate displays for inbound and outbound trains
- Auto-refreshing data
- Clean UI with MBTA branding

## Setup

1. Clone the repository:
```bash
git clone https://github.com/akashgit/trml-boston-time.git
cd trml-boston-time
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your MBTA API key (optional but recommended for higher rate limits):
```
MBTA_API_KEY=your_api_key_here
```

5. Run the application:
```bash
python app.py
```

The application will be available at http://localhost:3000

## Environment Variables

- `MBTA_API_KEY`: Your MBTA API key (optional but recommended for higher rate limits)

## Files

- `app.py`: Main Flask application with MBTA API integration
- `templates/index.html`: Main template with train visualization
- `requirements.txt`: Python dependencies
- `.env`: Environment variables (not tracked in git)

## Contributing

Feel free to submit issues and enhancement requests! 