import abc
import math
import random


class SkipList():
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def insert(self, value):
        """
            insert value into the list
        :param value:
        :return: Nothing
        """
        pass

    @abc.abstractmethod
    def remove(self, value):
        """
            remove value from the list
        :param value:
        :return:
        """
        pass

    @abc.abstractmethod
    def contains(self, value):
        """
        :param value:
        :return: True if value exists, otherwise False
        """
        return None


class Node():
    value = None
    follow = None
    follow_down = None

    def __init__(self, value, follow, follow_down):
        self.follow_down = follow_down
        self.follow = follow
        self.value = value

    @classmethod
    def create(cls, values):
        node = None
        for value in reversed(values):
            node = Node(value, node, None)

        return node

    @classmethod
    def summarise(cls, skips, skip_value):
        """
            creates a new Node list, linked to the skips Node list every skip_value and ending with the last element
        """
        assert skips
        cur = Node(skips.value, None, skips)
        first = cur
        last = skips
        cur_skips = skips.follow
        i = 1
        while cur_skips:
            # invariant: ret contains all the correct nodes up till cur_skips
            if i % skip_value == 0:
                cur_new = Node(cur_skips.value, None, cur_skips)
                cur.follow = cur_new
                cur = cur_new

            last = cur_skips
            cur_skips = cur_skips.follow
            i += 1

        if cur.value != last.value:
            cur.follow = Node(last.value, None, last)

        return first

    @classmethod
    def contains(cls, skips, value):
        contains, path = Node.contains_tuple(skips, value)

        return contains

    @classmethod
    def contains_tuple(cls, skips, value):

        node = skips
        last_node = node
        path = []
        while node:
            path.append(node)
            if node.value == value:
                return True, path
            elif node.value > value:
                if last_node.follow_down:
                    node = last_node.follow_down
                    last_node = node
                else:
                    return False, path
            else:
                last_node = node
                node = node.follow

        return False, path


class SkipListStatic(SkipList):
    """
        creation: nlogn (due to sorting
        contains: log(n)
        doesn't support insert or removal, just create it out of a list and use contains
    """

    def __init__(self, values):
        self.skips = SkipListStatic.create_skips(values)

    @classmethod
    def create_skips(cls, values):
        skips = Node.create(sorted(values))

        summary_count = int(math.sqrt(len(values)))
        while summary_count > 2:
            skips = Node.summarise(skips, summary_count)
            summary_count = int(math.sqrt(summary_count))

        return skips

    def insert(self, value):
        raise NotImplementedError()

    def remove(self, value):
        raise NotImplementedError()

    def contains(self, value):
        return Node.contains(self.skips, value)


class SkipListRandomised(SkipList):
    """
        insert, delete, contains: O(logn) with high probability

    """

    def __init__(self, values=[]):
        self.skips = None
        for value in values:
            self.insert(value)

    def contains(self, value):
        return Node.contains(self.skips, value)

    def remove(self, value):

        raise NotImplementedError()

    def insert(self, value):
        """
            recursively create a summary node with probability 1/2
        :param value:
        :return:
        """

        if not self.skips:
            self.skips = Node(value, None, None)
            return

        contains, path = Node.contains_tuple(self.skips, value)

        if value < path[0].value:

            # inserting the smallest so far

            self.skips = Node(value, self.skips, None)
            current = self.skips
            while current.follow.follow_down:
                # invariant: all inserted at the current level
                new_current = Node(value, current.follow.follow_down, None)
                current.follow_down = new_current
                current = new_current

        elif value > path[-1].value:

            # inserting the greatest so far

            current = self.skips
            while current.follow:
                current = current.follow

            current.follow = Node(value, None, None)
            while current.follow_down:
                current.follow_down.follow = Node(value, None, None)
                current.follow.follow_down = current.follow_down.follow
                current = current.follow_down
        else:

            # inserting in the middle

            # last one's value > value
            path = path[:-1]
            path[-1].follow = Node(value, path[-1].follow, None)
            last_inserted = path[-1].follow
            for ix, current in reversed(list(enumerate(path[:-1]))):

                # only going randomly high
                if random.randint(0, 1) == 1:
                    break

                if current.follow_down == path[ix + 1]:
                    current.follow = Node(value, current.follow, last_inserted)
                    last_inserted = current.follow
