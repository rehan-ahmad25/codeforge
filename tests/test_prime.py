# tests/test_prime.py
"""Tests for the ``is_prime`` function in ``prime_utils``.

The test suite covers:

* Correct detection of prime numbers.
* Correct detection of composite numbers.
* Edge cases (the smallest prime, numbers just below the prime threshold).
* Input validation – ensuring ``TypeError`` for non‑integer inputs and ``ValueError``
  for integers less than 2.
"""

import pytest
from prime_utils import is_prime

# Valid prime numbers
@pytest.mark.parametrize("n", [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71])
def test_primes(n):
    assert is_prime(n) is True

# Valid composite numbers
@pytest.mark.parametrize("n", [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36, 38, 39, 40, 42, 44, 45, 46, 48, 49, 50])
def test_composites(n):
    assert is_prime(n) is False

# Edge cases – values below the allowed range
@pytest.mark.parametrize("n", [0, 1, -1, -10])
def test_invalid_range(n):
    with pytest.raises(ValueError):
        is_prime(n)

# Invalid type inputs
@pytest.mark.parametrize("n", [2.5, "13", None, [7], {11: "eleven"}])
def test_invalid_type(n):
    with pytest.raises(TypeError):
        is_prime(n)
