import math

def is_prime(n: int) -> bool:
    """Check if a number is prime.

    Parameters
    ----------
    n : int
        The integer to test for primality.

    Returns
    -------
    bool
        ``True`` if *n* is a prime number, otherwise ``False``.

    Raises
    ------
    TypeError
        If *n* is not an integer.
    ValueError
        If *n* is less than 2 (prime numbers are defined for integers >= 2).

    Examples
    --------
    >>> is_prime(2)
    True
    >>> is_prime(15)
    False
    >>> is_prime(13)
    True
    """
    # Input validation
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 2:
        raise ValueError("n must be greater than or equal to 2")

    # 2 and 3 are prime
    if n in (2, 3):
        return True
    # Eliminate even numbers and multiples of 3 quickly
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Check divisibility up to sqrt(n) using 6k ± 1 optimization
    limit = math.isqrt(n)
    i = 5
    while i <= limit:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
