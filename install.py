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

def check_node_installed():
    """Check if Node.js is installed."""
    try:
        subprocess.run(["node", "--version"], check=True, capture_output=True)
        return True
    except (subprocess.SubprocessError, FileNotFoundError):
        print("Error: Node.js is not installed or not in PATH.")
        print("Please install Node.js from https://nodejs.org/")
        return False

def install_python_dependencies():
    """Install Python dependencies."""
    print("Installing Python dependencies...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
        print("Python dependencies installed successfully.")
        return True
    except subprocess.SubprocessError as e:
        print(f"Error installing Python dependencies: {e}")
        return False

def install_node_dependencies():
    """Install Node.js dependencies."""
    print("Installing Node.js dependencies...")
    try:
        subprocess.run(["npm", "install"], check=True)
        print("Node.js dependencies installed successfully.")
        return True
    except subprocess.SubprocessError as e:
        print(f"Error installing Node.js dependencies: {e}")
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
    if not check_python_version() or not check_node_installed():
        sys.exit(1)
    
    # Install dependencies
    if not install_python_dependencies() or not install_node_dependencies():
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