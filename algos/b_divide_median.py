from itertools import imap, chain, ifilter
import math
from itertools import islice


def median_std(numbers):
    """
        find a median (or upper/lower median)
        O(n*log(n))
    :param numbers: [1,4,2,3...]
    :return: (1,2) or (1,1) (lower, upper median
    """

    ordered = sorted(numbers)
    lower = int(math.floor((len(numbers) + 1.0) / 2)) - 1
    higher = int(math.ceil((len(numbers) + 1.0) / 2)) - 1
    return ordered[lower], ordered[higher]


def median_o_n(numbers):
    """
        find a median (or upper/lower median)
        O(n)
        a lot of copying which implied a big O(n) multiplier, but O(n) nevertheless
        check out the performance test - the n multiplier is so large, that it looses up till at least 10000

    :param numbers: [1,4,2,3...]
    :return: (1,2) or (1,1) (lower, upper median)
    """

    def rec(nums, rank):
        """
            returns an index in the nums of the element ranked with rank
        :param nums:
        :param rank: 1-based rank
        :return:
        """
        if len(nums) <= 5:
            return sorted(nums)[rank - 1]

        # sort in 5-columns
        columns = sorted(list(islice(nums, x, y)) for (x, y) in imap(lambda x: (x, x + 5), xrange(0, len(nums), 5)))

        # find recursively median of medians
        medians = map(lambda x: x[2] if len(x) > 2 else x[0], columns)
        median = rec(medians, 1 + len(medians) / 2)

        # find the median's rank
        median_rank = sum(map(lambda x: 1 if x <= median else 0, nums))

        # find recursively for adjusted rank in limited list
        if median_rank == rank:
            return median
        elif median_rank > rank:
            limited_list = list(ifilter(lambda x: x < median, nums))
            return rec(limited_list, rank)
        else:
            limited_list = list(ifilter(lambda x: x > median, nums))
            return rec(limited_list, rank - median_rank)

    upper_median = rec(numbers, 1 + len(numbers) / 2)

    if len(numbers) % 2 == 1:
        return upper_median, upper_median
    else:
        lower_median = max(ifilter(lambda x: x < upper_median, numbers))
        return lower_median, upper_median
