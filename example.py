#!/usr/bin/env python3
"""
Example script to demonstrate the Travel Booker functionality.
"""
import os
import importlib
from dotenv import load_dotenv
from travel_booker.core.ai_parser import parse_flight_request, parse_hotel_request
from travel_booker.browser_automation.flight_booker import book_flight
from travel_booker.browser_automation.hotel_booker import book_hotel

# Load environment variables from .env file if present
load_dotenv()

def main():
    """
    Run example booking scenarios.
    """
    # Check if OpenAI API key is available
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY environment variable is not set.")
        print("Please set it using:")
        print("  export OPENAI_API_KEY=your-api-key")
        return

    # Check if browser-use is installed
    try:
        importlib.import_module('browser_use')
    except ImportError:
        print("Error: browser-use package is not installed.")
        print("Please install it using:")
        print("  pip install browser-use")
        return

    # Example 1: Book a flight
    flight_request = "Book a flight from Helsinki to New York on 2023-07-01 for 2 adults"
    print(f"\nProcessing flight request: '{flight_request}'")
    
    # Parse the flight booking request
    flight_details = parse_flight_request(flight_request)
    if flight_details:
        print(f"Parsed flight details: {flight_details}")
        
        # Book the flight
        print("Booking flight...")
        result = book_flight(flight_details)
        if result:
            print("Flight booking completed successfully!")
            print(f"Details: {result}")
        else:
            print("Flight booking failed.")
    else:
        print("Failed to parse flight booking request.")

    # Example 2: Book a hotel
    hotel_request = "Book a hotel in New York from 2023-07-01 to 2023-07-05 for 2 adults"
    print(f"\nProcessing hotel request: '{hotel_request}'")
    
    # Parse the hotel booking request
    hotel_details = parse_hotel_request(hotel_request)
    if hotel_details:
        print(f"Parsed hotel details: {hotel_details}")
        
        # Book the hotel
        print("Booking hotel...")
        result = book_hotel(hotel_details)
        if result:
            print("Hotel booking completed successfully!")
            print(f"Details: {result}")
        else:
            print("Hotel booking failed.")
    else:
        print("Failed to parse hotel booking request.")

if __name__ == "__main__":
    main() 