import random

import pytest

from algos.f_randomised_quicksort import quicksort_inplace, quicksort_simple


@pytest.mark.parametrize(
    "list,sorted", [
        ([2, 1], [1, 2]),
        ([1, 2], [1, 2]),
        ([1], [1]),
        ([3, 1, 2], [1, 2, 3]),
    ]
)
def test_quicksort(list, sorted):
    assert quicksort_simple(list) == sorted
    quicksort_inplace(list)
    assert list == sorted


def test_randomised():
    for i in xrange(0, 100):
        l = list(xrange(1, 10))
        random.shuffle(l)
        ordered = sorted(l)
        assert quicksort_simple(l) == ordered
        quicksort_inplace(l)
        assert l == ordered
