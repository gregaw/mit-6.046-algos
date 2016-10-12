from bitarray import bitarray
import math


class Tree():
    """
        Implementation of a bitset with with a successor
    """

    @staticmethod
    def create(max_value):
        if max_value <= 16:
            return RegularTree(max_value)
        else:
            return VanEmdeBoasTree(max_value)


class RegularTree(Tree):
    def __init__(self, max_value):
        self.v = bitarray('0') * max_value

    def get(self, ix):
        return self.v[ix]

    def put(self, ix, value):
        self.v[ix] = value

    def successor(self, ix):

        for i in xrange(ix + 1, len(self.v)):
            if self.v[i]:
                return i

        return -1

    def is_empty(self):
        return not max(self.v)


class VanEmdeBoasTree(Tree):
    """
        non-clustering: O(sqrt(u))
        Insert, delete = log(u), successor = log(u)^log(3)

        remember min/max in each cluster to get additional loglog(u) !
    """
    def __init__(self, max_value):
        self.block_size = math.sqrt(max_value)
        assert self.block_size == int(self.block_size)
        self.block_size = int(self.block_size)

        #   v[k][j] == 1 iff element j i kth block has been set
        self.v = [Tree.create(self.block_size) for i in xrange(0, self.block_size)]

        #   summary[k] == 1 iff v[k*block_size .. +block_size] contains a value
        self.summary = Tree.create(self.block_size)

    def _highlow(self, ix):
        return self._high(ix), self._low(ix)

    def _high(self, ix):
        return ix / self.block_size

    def _low(self, ix):
        return ix % self.block_size

    def _ix(self, high, low):
        return high * self.block_size + low

    def get(self, ix):
        return self.v[self._high(ix)].get(self._low(ix))

    def put(self, ix, value):

        high, low = self._highlow(ix)

        # update v
        self.v[high].put(low, value)

        # update summary
        if value:
            self.summary.put(high, True)
        else:
            self.summary.put(high, not self.v[high].is_empty())

    def is_empty(self):
        for t in self.v:
            if not t.is_empty():
                return False
        return True

    def successor(self, ix):
        high, low = self._highlow(ix)

        local_block_low_ix = self.v[high].successor(low)
        if local_block_low_ix == -1:
            next_block_high_ix = self.summary.successor(high)
            if next_block_high_ix == -1:
                return -1
            else:
                return self._ix(next_block_high_ix, self.v[next_block_high_ix].successor(-1))
        else:
            return self._ix(high, local_block_low_ix)
