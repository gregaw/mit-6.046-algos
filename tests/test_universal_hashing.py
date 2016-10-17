import random

import pytest

from algos.h_universal_hashing import UniversalHashSet


@pytest.mark.parametrize(
    "l", [
        [2, 1],
        [4, 1],
        [0, 2, 4, 6, 8, 10, 12, 14, 16, 18],
        random.sample(xrange(0, 1000), 200),
    ]
)
def test_universal_list_static(l):
    myset = UniversalHashSet(l)
    assert_universal_set_ok(myset, l)
    for value in list(l):
        myset.remove(value)
        l.remove(value)
        assert_universal_set_ok(myset, l)


def assert_universal_set_ok(lut, original_list):
    lowest = min(original_list) if original_list else 0
    highest = max(original_list) + 1 if original_list else 10
    for value in xrange(lowest, highest):
        assert lut.contains(value) == (value in original_list)


def test_universal_set_show_distribution():
    """
        estimated size of underlying lists should be uniform
    """

    def show_sizes(myset):
        sizes = map(lambda x: len(x) if x else 0, myset.hash_set)
        print min(sizes), max(sizes)

    show_sizes(UniversalHashSet(random.sample(xrange(0, 100000), 10000)))
    show_sizes(UniversalHashSet(list(xrange(0, 10000))))
    show_sizes(UniversalHashSet([113 * x for x in xrange(0, 10000)]))
