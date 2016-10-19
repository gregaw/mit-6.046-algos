import random

import pytest

from algos.j_dynamic_alternating_coin_game import alternating_coin_game


@pytest.mark.parametrize(
    "values,expected", [
        ([1], (1, 1)),
        ([1, 2], (2, 2)),
        ([4, 42, 39, 17, 25, 6], (4, 68)),
    ]
)
def test_alternating_coin_game(values, expected):
    assert alternating_coin_game(values) == expected


def test_alternating_coin_game_performance():
    # should be quick, an exponential algo wouldn't survive this...
    alternating_coin_game([random.randint(1, 10) for x in xrange(0, 100)])
