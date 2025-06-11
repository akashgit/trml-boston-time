# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a TRMNL plugin for displaying real-time MBTA train times at Porter Square station. The project consists of a Python backend that fetches data from the MBTA API and HTML templates that render the information in TRMNL's terminal display format.

## Development Commands

### Environment Setup
```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

### Running the Application
```bash
# Test MBTA API integration
python test_mbta.py
```

## Architecture

### Data Flow
1. **API Integration**: `test_mbta.py` fetches real-time predictions from MBTA API v3 for Porter Square station (`place-portr`)
2. **Template Processing**: TRMNL processes the HTML template (`trmnl_template.html`) with Liquid templating to display train data
3. **Display Rendering**: The plugin renders on TRMNL terminal devices with timezone-aware formatting

### Key Components
- **`test_mbta.py`**: Core API client that fetches train predictions, includes trip and route data via `include` parameter
- **`trmnl_template.html`**: Main display template with bidirectional train listings (inbound to Alewife, outbound to Ashmont/Braintree)
- **`trmnl_template_vertical.html`**: Alternative vertical layout template
- **`trmnl_docs.md`**: Comprehensive TRMNL development guide with Liquid templating patterns

### TRMNL Integration
- Uses TRMNL's timezone system (`trmnl.user.utc_offset`) for time calculations
- Implements status indicators (✓ on-time, ! delayed, ✗ cancelled) based on API response
- Handles route identification for Red Line and Commuter Rail services
- Calculates relative arrival times in minutes from current timestamp

### API Configuration
- Targets Porter Square station specifically
- Filters for transit types 0,1,2 (subway/light rail, heavy rail, commuter rail)
- Sorts by arrival time with 6-result limit
- Includes relationship data for routes and trips

## Environment Variables
- `MBTA_API_KEY`: Required for MBTA API access (stored in `.env`)