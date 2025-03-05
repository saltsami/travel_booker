from setuptools import setup, find_packages

setup(
    name="travel-booker",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "openai",  # OpenAI API client
        "python-dotenv",  # For environment variables
        "requests",  # HTTP requests
        "typer",  # CLI interface
        "pydantic",  # Data validation
    ],
    extras_require={
        "browser": ["nodejs"],  # Node.js for browser-use
    },
    entry_points={
        "console_scripts": [
            "travel-booker = travel_booker.main:main",
        ],
    },
    description="Autonomous travel booking tool using AI and browser automation",
    author="Travel Booker Team",
    python_requires=">=3.8",
) 