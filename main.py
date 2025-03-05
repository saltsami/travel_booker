#!/usr/bin/env python3
"""
Travel Booker MVP - Main Entry Point
"""
import os
import sys
import typer
import importlib
from typing import Optional
from dotenv import load_dotenv

# Load environment variables from .env file if present
load_dotenv()

# Initialize CLI app
app = typer.Typer(help="Travel Booker - Book flights and hotels using natural language")

def setup_environment():
    """
    Check and setup the required environment variables and dependencies
    """
    # Check if OpenAI API key is available
    if not os.getenv("OPENAI_API_KEY"):
        typer.echo("Error: OPENAI_API_KEY environment variable is not set.")
        typer.echo("Please set it using:")
        typer.echo("  export OPENAI_API_KEY=your-api-key")
        return False

    # Check if browser-use is installed
    try:
        importlib.import_module('browser_use')
    except ImportError:
        typer.echo("Error: browser-use package is not installed.")
        typer.echo("Please install it using:")
        typer.echo("  pip install browser-use")
        return False

    return True

@app.command()
def book_flight(
    request: Optional[str] = typer.Argument(
        None,
        help="Natural language description of flight booking requirements"
    )
):
    """
    Book a flight using natural language description
    """
    from travel_booker.core.ai_parser import parse_flight_request
    from travel_booker.browser_automation.flight_booker import book_flight

    # If no request provided via argument, prompt for it
    if not request:
        request = typer.prompt("Please describe your flight booking request")

    # Parse the flight booking request
    booking_details = parse_flight_request(request)
    if not booking_details:
        typer.echo("Failed to parse flight booking request.")
        return

    # Book the flight
    result = book_flight(booking_details)
    if result:
        typer.echo("Flight booking completed successfully!")
        typer.echo(f"Details: {result}")
    else:
        typer.echo("Flight booking failed.")

@app.command()
def book_hotel(
    request: Optional[str] = typer.Argument(
        None,
        help="Natural language description of hotel booking requirements"
    )
):
    """
    Book a hotel using natural language description
    """
    from travel_booker.core.ai_parser import parse_hotel_request
    from travel_booker.browser_automation.hotel_booker import book_hotel

    # If no request provided via argument, prompt for it
    if not request:
        request = typer.prompt("Please describe your hotel booking request")

    # Parse the hotel booking request
    booking_details = parse_hotel_request(request)
    if not booking_details:
        typer.echo("Failed to parse hotel booking request.")
        return

    # Book the hotel
    result = book_hotel(booking_details)
    if result:
        typer.echo("Hotel booking completed successfully!")
        typer.echo(f"Details: {result}")
    else:
        typer.echo("Hotel booking failed.")

def main():
    """
    Main entry point for the application
    """
    # Check environment setup
    if not setup_environment():
        sys.exit(1)
    
    # Run the CLI app
    app()

if __name__ == "__main__":
    main() 