""" BEFORE RUNNING THIS SCRIPT
RUN app_testing.py to start the rest api test server """

import unittest

# Import all test modules here
from tests.test_db_connection import *
from tests.test_repositories import *
from tests.test_rest_api import *

if __name__ == "__main__":
    unittest.main()
