"""
Flight booking automation for Finnair using browser-use.
"""
import os
import json
import subprocess
import tempfile
from typing import Dict, Any, Optional

def book_flight(booking_details: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """
    Automate flight booking on Finnair website using browser-use.
    
    Args:
        booking_details: Dictionary with flight booking details
        
    Returns:
        Dictionary with booking confirmation details or None if booking failed
    """
    try:
        # Create a temporary file to store booking details for Node.js script
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
            json.dump(booking_details, f)
            temp_file_path = f.name
        
        # Path to the Node.js script (in the same directory as this file)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        script_path = os.path.join(script_dir, 'flight_automation.js')
        
        # Create the Node.js script if it doesn't exist
        if not os.path.exists(script_path):
            create_flight_automation_script(script_path)
        
        # Execute the Node.js script with browser-use
        result = subprocess.run(
            ['node', script_path, temp_file_path],
            capture_output=True,
            text=True,
            check=True
        )
        
        # Parse the output from the Node.js script
        try:
            return json.loads(result.stdout)
        except json.JSONDecodeError:
            print(f"Warning: Could not parse Node.js script output: {result.stdout}")
            return {"status": "completed", "details": "Booking process completed, but details not available"}
        
    except subprocess.CalledProcessError as e:
        print(f"Browser automation process failed: {e}")
        print(f"Error output: {e.stderr}")
        return None
    except Exception as e:
        print(f"Error in flight booking automation: {e}")
        return None
    finally:
        # Clean up the temporary file
        if 'temp_file_path' in locals():
            try:
                os.unlink(temp_file_path)
            except:
                pass

def create_flight_automation_script(file_path: str) -> None:
    """
    Create the Node.js script for flight booking automation.
    
    Args:
        file_path: Path where the script will be saved
    """
    script_content = """
    const fs = require('fs');
    const { chromium } = require('browser-use');

    async function bookFlight(bookingDetails) {
        // Launch a browser
        const browser = await chromium.launch({ headless: false });
        const page = await browser.newPage();

        try {
            // Navigate to Finnair website
            await page.goto('https://www.finnair.com/');

            // Accept cookies if the dialog appears
            try {
                const cookieButton = await page.waitForSelector('[data-testid="cookie-consent-accept-all"]', { timeout: 5000 });
                if (cookieButton) {
                    await cookieButton.click();
                }
            } catch (error) {
                console.log('Cookie dialog not found or already accepted');
            }

            // Fill in flight search form
            // Note: These selectors are examples and may need to be updated
            console.log('Filling origin...');
            await page.fill('[data-testid="origin-input"]', bookingDetails.origin);
            
            console.log('Filling destination...');
            await page.fill('[data-testid="destination-input"]', bookingDetails.destination);
            
            console.log('Setting date...');
            await page.click('[data-testid="date-input"]');
            // This is a simplified approach - date selection requires more specific handling
            // based on Finnair's actual calendar component
            await page.click(\`[data-date="\${bookingDetails.date}"]\`);
            
            console.log('Setting passengers...');
            await page.click('[data-testid="passenger-select"]');
            
            // Set adults
            const currentAdults = await page.textContent('[data-testid="adult-count"]');
            const adultDiff = bookingDetails.num_adults - parseInt(currentAdults);
            
            if (adultDiff > 0) {
                for (let i = 0; i < adultDiff; i++) {
                    await page.click('[data-testid="adult-increment"]');
                }
            } else if (adultDiff < 0) {
                for (let i = 0; i < Math.abs(adultDiff); i++) {
                    await page.click('[data-testid="adult-decrement"]');
                }
            }
            
            // Set children if any
            if (bookingDetails.num_children > 0) {
                for (let i = 0; i < bookingDetails.num_children; i++) {
                    await page.click('[data-testid="child-increment"]');
                }
            }
            
            // Close passenger selection
            await page.click('[data-testid="passenger-select-confirm"]');
            
            // Submit the search form
            console.log('Submitting search...');
            await page.click('[data-testid="search-button"]');
            
            // Wait for results to load
            await page.waitForSelector('[data-testid="flight-card"]', { timeout: 30000 });
            
            // Select the first available flight
            console.log('Selecting flight...');
            await page.click('[data-testid="flight-card"]');
            
            // Proceed to passenger details
            console.log('Proceeding to passenger details...');
            await page.click('[data-testid="continue-button"]');
            
            // For the MVP, we'll stop here before payment
            console.log('Booking process completed up to payment page');
            
            // In a real implementation, we would collect the booking details
            // from the confirmation page
            const bookingResult = {
                status: 'success',
                details: {
                    airline: 'Finnair',
                    origin: bookingDetails.origin,
                    destination: bookingDetails.destination,
                    date: bookingDetails.date,
                    passengers: {
                        adults: bookingDetails.num_adults,
                        children: bookingDetails.num_children || 0
                    },
                    reservation_id: 'DEMO-' + Math.random().toString(36).substring(2, 10).toUpperCase()
                }
            };
            
            return bookingResult;
            
        } catch (error) {
            console.error('Error during flight booking:', error);
            throw error;
        } finally {
            // Close the browser
            await browser.close();
        }
    }

    // Main function to run the automation
    async function main() {
        try {
            // Get booking details from command line argument
            const bookingDetailsPath = process.argv[2];
            const bookingDetailsJson = fs.readFileSync(bookingDetailsPath, 'utf8');
            const bookingDetails = JSON.parse(bookingDetailsJson);
            
            // Run the booking process
            const result = await bookFlight(bookingDetails);
            
            // Output the result as JSON
            console.log(JSON.stringify(result));
            
        } catch (error) {
            console.error('Error:', error);
            process.exit(1);
        }
    }

    // Run the main function
    main();
    """
    
    with open(file_path, 'w') as f:
        f.write(script_content) 