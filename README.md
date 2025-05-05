# TRMNL Boston Time Plugin

A simple TRMNL plugin that displays the current time in Boston.

## Files

- `boston-time.html` - The TRMNL plugin template
- `time-data.json` - The data file that TRMNL will poll

## Setup

1. In TRMNL's web interface:
   - Create a new Private Plugin
   - Set Strategy to "Polling"
   - Set Polling URL to: `https://raw.githubusercontent.com/YOUR_USERNAME/trmnl-boston-time/main/time-data.json`
   - Upload the `boston-time.html` template
   - Save and add to your device

## Raw JSON URL

The JSON file is available at:
```
https://raw.githubusercontent.com/YOUR_USERNAME/trmnl-boston-time/main/time-data.json
```

Replace `YOUR_USERNAME` with your GitHub username. 