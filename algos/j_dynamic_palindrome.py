from collections import defaultdict


def longest_palindromic_sequence(values):
    """
        Given: A string X[1...n], n >= 1
        To find: Longest palindrome that is a subsequence
        Example: Given "character" output "c a r a c"
    :param values:
    :return:
    """

    if not values:
        return ''

    cache = defaultdict(list)

    def rec(a, b):
        """

        :param a: start inclusive
        :param b: end inclusive
        :return: spalindrome: string
        """

        if cache[(a, b)]:
            return cache[(a, b)]

        if a == b:

            ret = values[a:b + 1]

        elif a == b - 1:

            if values[a] == values[b]:
                ret = values[a:b + 1]
            else:
                ret = values[a:a + 1]

        elif values[a] == values[b]:

            ret = values[a:a + 1] + rec(a + 1, b - 1) + values[b:b + 1]

        else:

            left = rec(a, b - 1)
            right = rec(a + 1, b)
            ret = left if len(left) >= len(right) else right

        cache[(a, b)] = ret
        return ret

    return rec(0, len(values) - 1)
