import pytest

from algos.g_randomised_skiplist import SkipListStatic


@pytest.mark.parametrize(
    "l", [
        # [2, 1],
        # [4, 1],
        [0, 2, 4, 6, 8, 10, 12, 14, 16, 18],
    ]
)
def test_skip_list_static(l):
    skip_list = SkipListStatic(l)
    for value in xrange(min(l), max(l) + 1):
        assert skip_list.contains(value) == (value in l)
