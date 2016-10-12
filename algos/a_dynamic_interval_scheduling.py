import sys
# Use standard python data structures

def interval_scheduling(tuple_list):
    """Return ending points list of the optimal schedule eg [1,2] in n^2

    :type tuple_list: list of positive int tuples eg [(0,1), (1,2)]
    """

    # we've dealt with all the events beginning < index
    index = 0
    results = []
    filtered = tuple_list
    while filtered:
        x, index = min(filtered, key=lambda (s, e): e)
        results.append(index)
        filtered = filter(lambda (s, e): s >= index, tuple_list)

    return results


def interval_scheduling_optimised(tuple_list):
    """ Return the optimal interval scheduling in n*log(n)

    :param tuple_list: a list of int tuples representing intervals eg [(0,1), (1,2), (2,3)]
    :return: a list of chosen indexes eg [1,2,3]
    """

    ordered = sorted(tuple_list, key=lambda (x, y): (y, x))
    results = []
    index = 0
    for (s, e) in ordered:
        if s >= index:
            index = e
            results.append(index)

    return results


def interval_scheduling_weighted_recursion(tuple_list):
    """
        Return a list of optimally scheduled intervals given weights
        O(2^n)

    :param tuple_list: [(start, end, weight)...]
    :return: [(start, end, weight)...]
    """

    def rec(partial_list, contents):
        """
            return the maximum weighted scheduling for a list l

        :type contents: a set of tuples which are part of the solution already
        :param partial_list:  a list
        :return:    [()...] for the list
        """

        def separate(a, b):
            astart, aend, aweight = a
            bstart, bend, bweight = b
            return astart >= bend or bstart >= aend

        def weight(l):
            return reduce(lambda acc, b: acc + b[2], l, 0)

        if not partial_list:
            return []

        first = partial_list[0]
        with_first = []
        if all([separate(x, first) for x in contents]):
            with_first = [first]
            with_first.extend(rec(partial_list[1:], contents + [first]))

        without_first = rec(partial_list[1:], contents)

        if weight(with_first) >= weight(without_first):
            return with_first
        else:
            return without_first

    return rec(tuple_list, [])


def interval_scheduling_weighted_dynamic_programming(tuple_list):
    """
        use dynamic programming going from the end of time, memoizing best fits as we go
        O(n*log(n) + m), n- intervals, m- times

    :param tuple_list: [(start, end, weight)...]
    :return: [(start, end, weight)...]
    """

    ordered = sorted(tuple_list, key=lambda (start, end, weight): start, reverse=True)
    min_start = min(tuple_list, key=lambda (start, end, weight): start)[0]
    max_end = max(tuple_list, key=lambda (start, end, weight): end)[1]

    def ix(time):
        return time - min_start

    mem = [(None, 0)] * (max_end - min_start + 1)

    last_start = max_end
    mem[ix(last_start)] = (None, 0)

    for interval in ordered:
        # invariant: mem[ix(last_start)] and up contain the optimal (interval, weight)
        start, end, weight = interval

        # fill the best weights from my-start - if not filled yet
        for i in xrange(start, last_start):
            if mem[ix(i)][0] is None:
                mem[ix(i)] = mem[ix(last_start)]

        # calculate my best weight
        best_weight_from_start = weight + mem[ix(end)][1]

        # record if better than anything so far
        if best_weight_from_start > mem[ix(start)][1]:
            mem[ix(start)] = (interval, best_weight_from_start)

        last_start = start

    results = []
    item = mem[ix(min_start)]
    while item[0]:
        results.append(item[0])
        item = mem[ix(item[0][1])]

    return results

class Interval:
    def __init__(self, start, end, weight):
        self.weight = weight
        self.end = end
        self.start = start
        assert end > start

    def to_tuple(self):
        return self.start, self.end, self.weight

class Mem:
    def __init__(self, start, end):
        self.end = end
        self.start = start
        self.mem = [(None, 0)] * (end - start + 1)

    def get(self, t):
        return self.mem[t - self.start]

    def set(self, t, value):
        self.mem[t - self.start] = value



def interval_scheduling_weighted_dynamic_programming2(intervals):
    """
    :param intervals: [(start, end, weight)]
    :return: [(start, end, weight)]
    """

    # sort intervals by start time - reverse
    intervals = map(lambda tuple: Interval(tuple[0], tuple[1], tuple[2]), intervals)
    ordered = sorted(intervals, key=lambda i: i.start, reverse=True)
    min_start = min(intervals, key=lambda i: i.start).start
    max_end = max(intervals, key=lambda i: i.end).end

    mem = Mem(min_start, max_end)
    last_start = max_end
    # iterate
    for interval in ordered:
        # start invariant: last_start and up contain the optimal schedules

        # fill down the optimal mems till interval.start - if better
        for t in xrange(interval.start, last_start):
            if mem.get(t)[1] < mem.get(last_start)[1]:
                mem.set(t, mem.get(last_start))

        # find the value with interval and set to mem[start] if improved
        my_best_weight = interval.weight + mem.get(interval.end)[1]
        if my_best_weight > mem.get(interval.start)[1]:
            mem.set(interval.start, (interval, my_best_weight))

        # set last_start to start
        last_start = interval.start

        # end invariant: start and up contain the optimal schedules

    results = []
    tuple = mem.get(min_start)
    while tuple[0]:
        results.append(tuple[0].to_tuple())
        tuple = mem.get(tuple[0].end)

    return results