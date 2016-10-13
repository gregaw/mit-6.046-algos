import abc
import math


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

        node = self.skips
        last_node = node
        while node:
            if node.value == value:
                return True
            elif node.value > value:
                if last_node.follow_down:
                    node = last_node.follow_down
                    last_node = node
                else:
                    return False
            else:
                last_node = node
                node = node.follow

        return False
