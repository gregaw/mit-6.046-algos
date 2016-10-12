from itertools import permutations
import random
import timeit
from algos.a_dynamic_interval_scheduling import interval_scheduling, interval_scheduling_optimised, \
    interval_scheduling_weighted_recursion, interval_scheduling_weighted_dynamic_programming, \
    interval_scheduling_weighted_dynamic_programming2
import pytest


@pytest.mark.parametrize(
    "intervals,result", [
        ([(0, 1), (1, 2)], [1, 2]),
        ([(0, 1), (2, 3), (1, 3)], [1, 3]),
        ([(1, 2), (0, 1)], [1, 2]),
        ([(1, 2), (0, 1), (1, 3)], [1, 2]),
        ([(1, 2), (0, 1), (0, 2)], [1, 2]),
        ([(1, 2), (0, 1), (2, 4), (0, 4), (0, 2), (2, 5)], [1, 2, 4]),
    ]
)
def test_interval_scheduling(intervals, result):
    assert interval_scheduling(intervals) == result
    assert interval_scheduling_optimised(intervals) == result


@pytest.mark.parametrize(
    "intervals,result", [
        ([(0, 5, 10), (1, 2, 2), (3, 4, 2)], [(0, 5, 10)]),
        ([(0, 5, 1), (1, 2, 2), (3, 4, 2)], [(1, 2, 2), (3, 4, 2)]),
        ([(0, 5, 1), (1, 2, 2), (3, 4, 2), (3, 4, 1)], [(1, 2, 2), (3, 4, 2)]),
        ([(0, 5, 1), (1, 2, 5), (3, 4, 2), (3, 4, 1)], [(1, 2, 5), (3, 4, 2)]),
    ]
)
def test_interval_scheduling_weighted_recursion(intervals, result):
    for permutation in permutations(intervals):
        assert set(interval_scheduling_weighted_recursion(permutation)) == set(result)
        assert set(interval_scheduling_weighted_dynamic_programming(permutation)) == set(result)
        assert set(interval_scheduling_weighted_dynamic_programming2(permutation)) == set(result)


def random_intervals(count, start, end):
    for i in xrange(0, count):
        s = random.randint(start, end - 1)
        e = random.randint(s + 1, end)
        w = random.randint(1, 10)
        yield (s, e, w)


def test_cross_interval_scheduling():
    def add_weights(tuples):
        return sum(map(lambda tuple: tuple[2], tuples))

    for i in xrange(1, 25):
        intervals = list(random_intervals(i, 1, 1000))
        assert add_weights(interval_scheduling_weighted_recursion(intervals)) == add_weights(
            interval_scheduling_weighted_dynamic_programming2(intervals))


def run_dynamic(size):
    interval_scheduling_weighted_dynamic_programming2(random_intervals(size, 1, 1000))


def run_recursive(size):
    interval_scheduling_weighted_recursion(list(random_intervals(size, 1, 1000)))


def tooslow_test_performance_dynamic():
    assert timeit.timeit(stmt="run_dynamic(3000)", setup="from tests.test_dynamic_interval_scheduling import run_dynamic",
                         number=10) < \
           timeit.timeit(stmt="run_recursive(30)", setup="from tests.test_dynamic_interval_scheduling import run_recursive",
                         number=10)
