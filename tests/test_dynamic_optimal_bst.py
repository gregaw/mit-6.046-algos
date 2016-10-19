import pytest

from algos.j2_dynamic_optimal_bst import Tree, optimal_bst


@pytest.mark.parametrize(
    "l,result", [
        ([1], (1, Tree(None, 0, None))),
        ([1, 2], (4, Tree(Tree(None, 0, None), 1, None))),
        ([1, 2, 1], (6, Tree(Tree(None, 0, None), 1, Tree(None, 2, None)))),
        ([2, 1, 1], (7, Tree(None, 0, Tree(None, 1, Tree(None, 2, None))))),
        ([1, 1, 2], (7, Tree(Tree(None, 0, None), 1, Tree(None, 2, None)))),
    ]
)
def test_optimal_bst(l, result):
    run = optimal_bst(l)
    actual = run[0], Tree.pretty(run[1])
    expected = result[0], Tree.pretty(result[1])
    try:
        assert actual == expected
    except:
        print 'actual:\n' + actual[1]
        print 'expected:\n' + expected[1]
        raise
