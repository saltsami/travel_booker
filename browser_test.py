#!/usr/bin/env python3
"""
Test script for browser-use API
"""
from browser_use import Browser, BrowserConfig, Agent

def main():
    """
    Print out the available methods and attributes of Browser and BrowserConfig classes
    """
    print("Browser methods and attributes:")
    print(dir(Browser))
    
    print("\nBrowserConfig methods and attributes:")
    print(dir(BrowserConfig))
    
    print("\nAgent methods and attributes:")
    print(dir(Agent))
    
    # Create a browser instance and print its methods
    browser_config = BrowserConfig()
    print("\nBrowserConfig instance properties:")
    print(browser_config.__dict__)
    
    browser = Browser(browser_config)
    print("\nBrowser instance methods and attributes:")
    print(dir(browser))
    
    # Print documentation if available
    print("\nBrowser class docstring:")
    print(Browser.__doc__)

if __name__ == "__main__":
    main() 