"""Main entry point for the Todo CLI application."""

import sys
import os
# Add the current directory to the path so we can import todo_app
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from todo_app.cli.main import main

if __name__ == '__main__':
    main()