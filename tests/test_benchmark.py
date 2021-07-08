import math

from factorial import factorial

from .conftest import FACTORIALS


def run_benchmark(benchmark, func):
    result = benchmark.pedantic(
        lambda: [func(input) for input in range(0, 17)],
        rounds=100,
        iterations=100,
        warmup_rounds=1000,
    )
    assert result == FACTORIALS


def test_py_naive(benchmark):
    """Benchmark naive Python implementation."""

    def factorial_naive(input):
        if input < 0 or input > 16:
            raise TypeError("Invalid input")
        result = 1
        for i in range(1, input + 1):
            result *= i
        return result

    run_benchmark(benchmark, factorial_naive)


def test_py_lookup(benchmark):
    """Benchmark lookup Python implementation."""

    def factorial_lookup(input):
        try:
            return FACTORIALS[input]
        except IndexError:
            raise TypeError("Invalid input")

    run_benchmark(benchmark, factorial_lookup)


def test_py_builtin(benchmark):
    """Benchmark built in Python implementation."""
    run_benchmark(benchmark, math.factorial)


def test_c(benchmark):
    """Benchmark C implementation."""
    run_benchmark(benchmark, factorial)
