from itertools import permutations
import random
import timeit

import pytest

from algos.b_divide_median import median_std, median_o_n


@pytest.mark.parametrize(
    "numbers,result", [
        ([1, 2, 3, 4], (2, 3)),
        ([1, 2, 3, 4, 5], (3, 3)),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], (5, 5)),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], (5, 6)),
        ([1, 2], (1, 2)),
        ([1], (1, 1)),
    ]
)
def test_divide_median(numbers, result):
    for nums in random.sample(list(permutations(numbers)), min(10, len(numbers))):
        assert median_std(nums) == result
        assert median_o_n(nums) == result


def test_random_cross():
    for size in xrange(1, 100, 50):
        numbers = random_list(size)
        assert median_o_n(numbers) == median_std(numbers)


def random_list(size):
    random.seed(13)
    return list(random.sample(xrange(1, size * 10), size))


def run_o_n(size):
    median_o_n(random_list(size))


def run_o_nlogn(size):
    median_std(random_list(size))


# for sizes < 10000 our nlogn solution wins hands down - the o(n) solution is pretty heavy
def too_slow_test_performance_nlogn_wins():
    assert timeit.timeit(stmt="run_o_n(1000)",
                         setup="from tests.test_divide_median import run_o_n",
                         number=10) > \
           timeit.timeit(stmt="run_o_nlogn(1000)",
                         setup="from tests.test_divide_median import run_o_nlogn",
                         number=10)
