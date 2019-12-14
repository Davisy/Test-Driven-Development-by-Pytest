# Test Driven Development by Pytest

pytest is a framework that makes building simple and scalable tests easy. Tests are expressive and readable.

Install pytest by running the following command **"pip install -U pytest"**

## Basic Commands
- **pytest -V** = increases the verbosity.
- **pytest test_class.py -v** = the command will execute the tests only from file test_class.py.
- **pytest -m set1 -v** = Run all test with a market called set1
- To run tests in parallel install **pytest-xdist** and then write this command **pytest -n <num>** example pytest -n 3
