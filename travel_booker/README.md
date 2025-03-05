# Travel Booker MVP

An autonomous tool designed to simplify booking flights with Finnair and hotels with Booking.com using natural language instructions and browser automation.

## Features

- Natural language processing for travel requests
- Automated flight booking on Finnair
- Automated hotel booking on Booking.com
- CLI interface for easy interaction

## Requirements

- Python 3.8+
- Node.js (for browser-use)
- OpenAI API key

## Installation

```bash
pip install git+https://github.com/your-repo/travel-booker.git
```

## Usage

```bash
# Set your OpenAI API key
export OPENAI_API_KEY=your-api-key

# Run the travel booker
travel-booker
```

Then follow the CLI prompts to input your travel details.

Example commands:
- "Book a flight from Helsinki to New York on 2023-07-01 for 2 adults"
- "Book a hotel in New York from 2023-07-01 to 2023-07-05 for 2 adults"

## How It Works

1. User enters travel requirements in natural language
2. AI interprets the input and extracts structured data
3. Browser automation navigates to Finnair or Booking.com
4. The tool fills in forms and makes selections automatically
5. Booking confirmation details are displayed to the user

## Limitations

This is an MVP with the following limitations:
- Stops before the actual payment step
- Limited error handling
- No credential storage
- Hardcoded selectors that may break if websites change
