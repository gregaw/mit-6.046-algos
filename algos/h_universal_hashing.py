import random
import itertools

# must be prime
m = 113
#  m^r >= max value, for a long key: m^r > 1e20, 113^10
r = 10
seed = [random.randint(0, m - 1) for x in xrange(0, r)]


def convert_to_m_base(value):
    ret = [0] * m
    i = 0
    while i < m and value >= 1:
        ret[i] = value % m
        i += 1
        value /= m
    return ret


def universal_hash(value):
    return sum(itertools.imap(lambda x, y: (x * y) % m, convert_to_m_base(value), seed)) % m


class UniversalHashSet:
    hash_set = [None] * m

    def __init__(self, values):
        for i in xrange(0, len(self.hash_set)):
            self.hash_set[i] = []

        for value in values:
            self.insert(value)

    def insert(self, value):
        l = self.hash_set[universal_hash(value)]
        if value not in l:
            l.append(value)

    def remove(self, value):
        l = self.hash_set[universal_hash(value)]
        if value in l:
            l.remove(value)

    def contains(self, value):
        l = self.hash_set[universal_hash(value)]
        return value in l
