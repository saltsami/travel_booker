"""
AI parser for interpreting natural language booking requests.
"""
import os
import json
import sys
from typing import Dict, Any, Optional
import openai
from dotenv import load_dotenv

# Reload environment variables to ensure we have the latest
load_dotenv(override=True)

# Get OpenAI API key from environment
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Flag to use mock data for testing
USE_MOCK_DATA = OPENAI_API_KEY == "sk-mock-testing-key" or OPENAI_API_KEY == "sk-your-actual-api-key-here"

if USE_MOCK_DATA:
    print("Using mock data for parsing requests (no API calls)")
else:
    # Check if API key is valid
    if not OPENAI_API_KEY:
        print("Error: Please set a valid OPENAI_API_KEY in your .env file")
        print("You can get an API key from https://platform.openai.com/account/api-keys")
        print("Or use 'sk-mock-testing-key' for testing with mock data")
        sys.exit(1)

    # Initialize OpenAI client
    try:
        client = openai.OpenAI(api_key=OPENAI_API_KEY)
    except Exception as e:
        print(f"Error initializing OpenAI client: {e}")
        sys.exit(1)

def parse_flight_request(request: str) -> Optional[Dict[str, Any]]:
    """
    Parse a natural language flight booking request into structured data.
    
    Args:
        request: Natural language request string
        
    Returns:
        Dictionary with structured booking data or None if parsing failed
    """
    if USE_MOCK_DATA:
        # Mock implementation for testing
        print(f"Mock parsing flight request: '{request}'")
        # Simple parsing based on keywords
        origin = "Helsinki"
        destination = "New York"
        date = "2023-07-01"
        num_adults = 2
        num_children = 0
        
        if "Helsinki to Riika" in request or "Helsinki to Riga" in request:
            destination = "Riga"
        
        if "28.3" in request:
            date = "2023-03-28"
        
        return {
            "origin": origin,
            "destination": destination,
            "date": date,
            "num_adults": num_adults,
            "num_children": num_children
        }
    
    try:
        # Define the system prompt
        system_prompt = """
        You are a flight booking assistant. Extract the following information from the user's request:
        - origin: The departure city/airport
        - destination: The arrival city/airport
        - date: The departure date in YYYY-MM-DD format
        - num_adults: The number of adult travelers
        - num_children: The number of child travelers (0 if not specified)
        
        Return the information as a JSON object with these fields.
        """
        
        # Call OpenAI API to extract information
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": request}
            ],
            response_format={"type": "json_object"}
        )
        
        # Parse the response
        content = response.choices[0].message.content
        return json.loads(content)
    
    except Exception as e:
        print(f"Error parsing flight request: {e}")
        return None


def parse_hotel_request(request: str) -> Optional[Dict[str, Any]]:
    """
    Parse a natural language hotel booking request into structured data.
    
    Args:
        request: Natural language request string
        
    Returns:
        Dictionary with structured booking data or None if parsing failed
    """
    if USE_MOCK_DATA:
        # Mock implementation for testing
        print(f"Mock parsing hotel request: '{request}'")
        # Simple parsing based on keywords
        location = "New York"
        check_in_date = "2023-07-01"
        check_out_date = "2023-07-05"
        num_adults = 2
        num_children = 0
        room_type = "standard"
        
        return {
            "location": location,
            "check_in_date": check_in_date,
            "check_out_date": check_out_date,
            "num_adults": num_adults,
            "num_children": num_children,
            "room_type": room_type
        }
    
    try:
        # Define the system prompt
        system_prompt = """
        You are a hotel booking assistant. Extract the following information from the user's request:
        - location: The city/location for the hotel
        - check_in_date: The check-in date in YYYY-MM-DD format
        - check_out_date: The check-out date in YYYY-MM-DD format
        - num_adults: The number of adult guests
        - num_children: The number of child guests (0 if not specified)
        - room_type: The type of room (if specified, otherwise "standard")
        
        Return the information as a JSON object with these fields.
        """
        
        # Call OpenAI API to extract information
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": request}
            ],
            response_format={"type": "json_object"}
        )
        
        # Parse the response
        content = response.choices[0].message.content
        return json.loads(content)
    
    except Exception as e:
        print(f"Error parsing hotel request: {e}")
        return None
