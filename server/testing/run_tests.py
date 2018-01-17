# testing/run_tests.py

""" Set up env for tests and run each one"""

import sys
import os
from os.path import join, dirname
from dotenv import load_dotenv

DOTENV_PATH = join(dirname(__file__), '.test_env')
load_dotenv(DOTENV_PATH)

# Add the app module to sys paths
sys.path.append(os.getenv('APP_MODULE'))

# Run the unit tests
os.system("python -m unittest discover")
