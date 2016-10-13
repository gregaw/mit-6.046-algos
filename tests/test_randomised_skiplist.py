import random

import pytest

from algos.g_randomised_skiplist import SkipListStatic, SkipListRandomised


@pytest.mark.parametrize(
    "l", [
        # [2, 1],
        # [4, 1],
        [0, 2, 4, 6, 8, 10, 12, 14, 16, 18],
        random.sample(xrange(0, 100), 50),
    ]
)
def test_skip_list_static(l):
    assert_skip_list_ok(SkipListStatic(l), l)
    assert_skip_list_ok(SkipListRandomised(l), l)


def assert_skip_list_ok(skip_list, original_list):
    for value in xrange(min(original_list), max(original_list) + 1):
        assert skip_list.contains(value) == (value in original_list)
