import pytest
from prime_checker.is_prime import is_prime

@pytest.mark.parametrize("prime", [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47])
def test_is_prime_valid_primes(prime):
    assert is_prime(prime) is True

@pytest.mark.parametrize("composite", [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 27, 28, 30, 32, 33, 34, 35, 36, 38, 39, 40])
def test_is_prime_valid_composites(composite):
    assert is_prime(composite) is False

def test_is_prime_type_error():
    with pytest.raises(TypeError):
        is_prime(3.14)
    with pytest.raises(TypeError):
        is_prime("7")
    with pytest.raises(TypeError):
        is_prime([2])

def test_is_prime_value_error():
    with pytest.raises(ValueError):
        is_prime(0)
    with pytest.raises(ValueError):
        is_prime(1)
    with pytest.raises(ValueError):
        is_prime(-5)
