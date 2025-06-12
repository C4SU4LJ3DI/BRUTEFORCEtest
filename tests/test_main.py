import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from utils import brute_force_search, brute_force_password_multithreaded

def test_found():
    data = [1, 2, 3, 42, 5]
    assert brute_force_search(data, 42) == 3

def test_not_found():
    data = [1, 2, 3, 4, 5]
    assert brute_force_search(data, 999) == -1

def test_brute_force_password_lowercase():
    assert brute_force_password_multithreaded("abc", charset="ascii_lowercase", max_length=3, num_threads=2) == "abc"

def test_brute_force_password_digit():
    assert brute_force_password_multithreaded("5", charset="digits", max_length=1, num_threads=2) == "5"

def test_brute_force_password_special():
    assert brute_force_password_multithreaded("!", charset="ascii_lowercase_digits_special", max_length=1, num_threads=2) == "!"

def test_brute_force_password_not_found():
    # Should return None if impossible to find in given max_length
    assert brute_force_password_multithreaded("abcd", charset="ascii_lowercase", max_length=2, num_threads=2) is None
