#!/usr/bin/env python3
"""Script to run the CLI Todo application directly."""

import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Change to the project directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Import and run the main CLI function
from src.todo_app.cli.main import main

if __name__ == "__main__":
    main()