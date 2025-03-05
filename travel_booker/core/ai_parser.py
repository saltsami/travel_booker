"""
AI parser for interpreting natural language booking requests.
"""
import os
import json
from typing import Dict, Any, Optional
import openai

# Get OpenAI API key from environment
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = openai.OpenAI(api_key=OPENAI_API_KEY)

def parse_flight_request(request: str) -> Optional[Dict[str, Any]]:
    """
    Parse a natural language flight booking request into structured data.
    
    Args:
        request: Natural language request string
        
    Returns:
        Dictionary with structured booking data or None if parsing failed
    """
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
