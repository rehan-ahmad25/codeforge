# prime_utils.py
"""Utility functions for prime number operations.

This module provides a single public function ``is_prime`` that checks whether a
given integer is a prime number. The function includes input validation and a
clear, comprehensive docstring with usage examples.

Example
-------
>>> from prime_utils import is_prime
>>> is_prime(2)
True
>>> is_prime(15)
False
>>> is_prime(17)
True
"""

import math
from typing import Any


def is_prime(n: Any) -> bool:
    """Return ``True`` if *n* is a prime number, ``False`` otherwise.

    Parameters
    ----------
    n : int
        The number to test for primality.

    Returns
    -------
    bool
        ``True`` if *n* is prime, ``False`` otherwise.

    Raises
    ------
    TypeError
        If *n* is not an instance of :class:`int`.
    ValueError
        If *n* is less than ``2`` – the smallest prime number.

    Notes
    -----
    The implementation uses trial division up to ``sqrt(n)``. For ``n`` less
    than ``4`` the result is known immediately. For larger numbers we test
    divisibility by ``2`` and then only odd candidates up to the integer square
    root of ``n``.

    Examples
    --------
    >>> is_prime(2)
    True
    >>> is_prime(4)
    False
    >>> is_prime(13)
    True
    >>> is_prime(0)
    Traceback (most recent call last):
        ...
    ValueError: n must be greater than or equal to 2
    >>> is_prime(3.14)
    Traceback (most recent call last):
        ...
    TypeError: n must be an integer
    """
    # Input type validation
    if not isinstance(n, int):
        raise TypeError("n must be an integer")

    # Input value validation
    if n < 2:
        raise ValueError("n must be greater than or equal to 2")

    # Quick handling for the first two primes
    if n in (2, 3):
        return True

    # Even numbers greater than 2 are not prime
    if n % 2 == 0:
        return False

    # Only need to test odd divisors up to sqrt(n)
    limit = int(math.isqrt(n))  # math.isqrt returns floor(sqrt(n)) without floating point
    for divisor in range(3, limit + 1, 2):
        if n % divisor == 0:
            return False
    return True


if __name__ == "__main__":
    # Simple manual testing when the module is executed directly.
    test_numbers = [2, 3, 4, 9, 11, 15, 17, 19, 20, 23, 24, 29, 31, 37, 41, 42]
    for num in test_numbers:
        print(f"{num}: {'prime' if is_prime(num) else 'composite'}")
