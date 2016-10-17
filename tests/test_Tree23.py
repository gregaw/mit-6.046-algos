import random

import pytest

from algos.i_2_3_trees import Tree23


@pytest.mark.parametrize(
    "l", [
        [2, 1],
        [4, 1],
        [4, 1, 2],
        [0, 2, 4, 6, 8, 10, 12, 14, 16, 18],
        random.sample(xrange(0, 100), 50),
    ]
)
def test_tree23_static(l):
    tree = Tree23.create(l)
    for value in xrange(min(l), max(l) + 1):
        assert tree.contains(value) == (value in l)
