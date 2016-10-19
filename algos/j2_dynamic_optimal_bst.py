class Tree:
    def __init__(self, left, value, right):
        self.right = right
        self.value = value
        self.left = left

    @staticmethod
    def pretty(tree, prefix='-'):
        if not tree:
            return prefix + '.'
        return '{}{}\n{}\n{}'.format(
            prefix,
            tree.value,
            Tree.pretty(tree.left, prefix=' ' + prefix),
            Tree.pretty(tree.right, prefix=' ' + prefix),
        )


def optimal_bst(weights):
    """

    :param weights:
    :return: (weight, tree)
    """

    cache = {}

    def rec(a, b):
        """

        :param a: inclusive
        :param b: inclusive
        :return: (weight, tree)
        """

        if cache.has_key((a, b)):
            return cache[(a, b)]

        if a > b:
            ret = 0, None
        elif a == b:
            ret = weights[a], Tree(None, a, None)
        else:
            best = (float('inf'), None)
            for root_ix in xrange(a, b + 1):
                left = rec(a, root_ix - 1)
                right = rec(root_ix + 1, b)
                weight = left[0] + right[0] + sum(weights[a:b + 1])
                if weight < best[0]:
                    best = (weight, Tree(left[1], root_ix, right[1]))

            ret = best

        cache[(a, b)] = ret
        return ret

    return rec(0, len(weights) - 1)
