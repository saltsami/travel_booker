# Travel Booker MVP

An autonomous tool designed to simplify booking flights with Finnair and hotels with Booking.com using natural language instructions and browser automation.

## Features

- Natural language processing for travel requests
- Automated flight booking on Finnair
- Automated hotel booking on Booking.com
- CLI interface for easy interaction
- Browser automation using browser-use Python package
- Demo mode with mock implementations

## Requirements

- Python 3.8+
- OpenAI API key (optional for demo mode)
- Browser (Chrome or Firefox) installed on your system

## Installation

```bash
# Clone the repository
git clone https://github.com/your-repo/travel-booker.git
cd travel-booker

# Run the installation script
python install.py

# OR install manually
pip install -r requirements.txt
pip install browser-use
```

## Usage

### Production Mode (requires OpenAI API key)

```bash
# Set your OpenAI API key
export OPENAI_API_KEY=your-api-key  # Linux/Mac
# OR
set OPENAI_API_KEY=your-api-key     # Windows

# Run the travel booker
python -m travel_booker.main
```

### Demo Mode

For demonstration purposes, you can set the API key to a special value to use the mock implementation:

```bash
# Set the mock API key
export OPENAI_API_KEY=sk-mock-testing-key  # Linux/Mac
# OR
set OPENAI_API_KEY=sk-mock-testing-key     # Windows
```

### Command Examples

```bash
# Book a flight
python -m travel_booker.main book-flight "Book a flight from Helsinki to New York on 2023-07-01 for 2 adults"

# Book a hotel
python -m travel_booker.main book-hotel "Book a hotel in New York from 2023-07-01 to 2023-07-05 for 2 adults"
```

## How It Works

1. User enters travel requirements in natural language
2. AI interprets the input and extracts structured data
3. Browser automation navigates to Finnair or Booking.com
4. The tool fills in forms and makes selections automatically
5. Booking confirmation details are displayed to the user

## Using browser-use

This application leverages the browser-use Python package for browser automation. The browser-use library provides a Python interface to control and automate web browsers.

Key components:
- `Browser` - Manages browser instances
- `Agent` - Provides higher-level browser automation capabilities

## Recent Improvements

- Fixed CLI command parsing for natural language inputs
- Added demo mode with mock implementations
- Improved error handling throughout the application
- Updated browser automation code to work with the latest browser-use API
- Added better debugging and user feedback

## Limitations

This is an MVP with the following limitations:
- Stops before the actual payment step
- Limited error handling
- No credential storage
- Hardcoded selectors that may break if websites change 

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. 