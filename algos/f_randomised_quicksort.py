import random


def quicksort_simple(nums):
    """
        duplicates, not in place
    :param nums:
    :return:
    """

    def qs(ns):
        """
        :return: sorted ns
        """

        if len(ns) <= 1:
            return ns

        # divide into Less Equal Greater
        ix = random.randint(0, len(ns) - 1)
        val = ns[ix]
        L = filter(lambda x: x < val, ns)
        G = filter(lambda x: x > val, ns)
        E = [val] * (len(ns) - len(L) - len(G))

        # recursive for Less Greater
        return qs(L) + E + qs(G)

    return qs(nums)


def quicksort_inplace(nums):
    def qs(a, b):
        """
            no duplicates, in place
        :param a: 0based index of first element
        :param b: 0based indexo of last element
        :return:
        """
        if a >= b:
            return

            # pick random element
        ix = random.randint(a, b)
        val = nums[ix]
        # pivot in place around it (Less, Equal, Greater)
        start = a
        end = b
        while start < end:
            # invariant: all before start index are < val, all after end > val
            if nums[start] >= val >= nums[end]:
                tmp = nums[start]
                nums[start] = nums[end]
                nums[end] = tmp
                if nums[start] != val:
                    start += 1
                else:
                    end -= 1
            elif val < nums[end]:
                end -= 1
            elif nums[start] < val:
                start += 1

        # use recursion to sort the Less and Greater
        qs(a, start - 1)
        qs(start, b)

    qs(0, len(nums) - 1)

    return nums
