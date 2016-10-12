from bitarray import bitarray
import pytest
from algos.d_divide_van_emde_boas import RegularTree, VanEmdeBoasTree


def find_next(bitset, ix):
    for i in xrange(ix + 1, len(bitset)):
        if bitset[i]:
            return i

    return -1

@pytest.mark.parametrize(
    "bitset", [
        bitarray('1000100010001000'),
        bitarray('0000100110001000'),
    ]
)
def test_reg_veb(bitset):
    generic_tree_test(bitset, VanEmdeBoasTree(len(bitset)))
    generic_tree_test(bitset, RegularTree(len(bitset)))

def generic_tree_test(bitset, reg):
    #   put
    for ix in xrange(0, len(bitset)):
        reg.put(ix, bitset[ix])

    #   read
    for ix in xrange(0, len(bitset)):
        assert reg.get(ix) == bitset[ix]

    #   successor
    for ix in xrange(0, len(bitset)):
        assert reg.successor(ix) == find_next(bitset, ix)

    #   delete
    for ix in xrange(0, len(bitset)):
        if bitset[ix]:
            reg.put(ix, False)

    assert reg.is_empty()

    #   read
    for ix in xrange(0, len(bitset)):
        assert reg.get(ix) == False

    assert reg.successor(0) == -1
