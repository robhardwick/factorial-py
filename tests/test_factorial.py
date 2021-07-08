import pytest

from factorial import factorial

from .conftest import FACTORIALS


def test_validation():
    """Ensure factorial only accepts integers ≥ 1 and ≤ 16"""
    with pytest.raises(TypeError):
        factorial()

    with pytest.raises(TypeError):
        factorial(1, 2)

    with pytest.raises(TypeError):
        factorial("invalid")

    with pytest.raises(TypeError):
        factorial(-1)

    with pytest.raises(TypeError):
        factorial(100)


def test_factorial():
    """Ensure factorial produces correct result"""
    for input, output in enumerate(FACTORIALS):
        assert factorial(input) == output
