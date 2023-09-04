"""
testing the main module
"""

import src.main


def test_function_one():
    """tests function_one in main
    """
    assert src.main.function_one(3, 5) == 15


def test_function_two():
    """tests function_two in main
    """
    assert src.main.function_two(3, 0) == 3
