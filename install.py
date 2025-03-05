#!/usr/bin/env python3
"""
Installation script for the Travel Booker application.
"""
import os
import sys
import subprocess
import shutil

def check_python_version():
    """Check if Python version is 3.8 or higher."""
    if sys.version_info < (3, 8):
        print("Error: Python 3.8 or higher is required.")
        return False
    return True

def install_python_dependencies():
    """Install Python dependencies including browser-use."""
    print("Installing Python dependencies...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
        print("Python dependencies installed successfully.")
        
        # Ensure browser-use is installed
        try:
            import browser_use
            print("browser-use is already installed.")
        except ImportError:
            print("Installing browser-use package...")
            subprocess.run([sys.executable, "-m", "pip", "install", "browser-use"], check=True)
            print("browser-use installed successfully.")
        
        return True
    except subprocess.SubprocessError as e:
        print(f"Error installing Python dependencies: {e}")
        return False

def setup_env_file():
    """Create .env file from .env.example if it doesn't exist."""
    if not os.path.exists(".env") and os.path.exists(".env.example"):
        print("Creating .env file from .env.example...")
        shutil.copy(".env.example", ".env")
        print("Please edit the .env file to add your OpenAI API key.")
    elif not os.path.exists(".env.example"):
        print("Warning: .env.example file not found.")
    else:
        print(".env file already exists.")

def main():
    """Run the installation process."""
    print("=== Travel Booker Installation ===")
    
    # Check requirements
    if not check_python_version():
        sys.exit(1)
    
    # Install dependencies
    if not install_python_dependencies():
        sys.exit(1)
    
    # Setup environment file
    setup_env_file()
    
    print("\nInstallation completed successfully!")
    print("To use the Travel Booker, make sure to:")
    print("1. Set your OpenAI API key in the .env file")
    print("2. Run the application with: python -m travel_booker.main")
    print("   or use the example script: python example.py")

if __name__ == "__main__":
    main() 