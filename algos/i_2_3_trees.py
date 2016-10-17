class Tree23:
    """
        no dups
        as much as possible in-place for efficiency
    """

    def __init__(self, left, data1, middle, data2, right):
        self.middle = middle
        self.data2 = data2
        self.right = right
        self.left = left
        self.data1 = data1

    @staticmethod
    def create(values):
        tree = Tree23.empty()
        for value in values:
            tree = tree.insert(value)
        return tree

    @staticmethod
    def empty():
        return Tree23(None, None, None, None, None)

    @staticmethod
    def leaf(value):
        return Tree23(None, value, None, None, None)

    @staticmethod
    def node2(t1, d2, t3):
        return Tree23(t1, d2, t3, None, None)

    def contains(self, value):
        if self.data1 == value or self.data2 == value:
            return True
        elif self.left:
            if value < self.data1:
                return self.left.contains(value)
            elif self.data2 is None or value < self.data2:
                return self.middle.contains(value)
            elif self.right is not None:
                return self.right.contains(value)
            else:
                return False
        else:
            return False

    def insert(self, value):
        tup = self._insert(value)
        if len(tup) == 1:
            return tup[0]
        else:
            return Tree23.node2(tup[0], tup[1], tup[2])

    def _insert(self, value):

        if self.data1 == value or self.data2 == value:
            return self,
        elif self.data1 is None:
            # empty node
            self.data1 = value
            return self,
        elif self.data2 is None and self.left is None:
            # 2 node - leaf
            if value > self.data1:
                self.data2 = value
                return self,
            else:
                self.data2 = self.data1
                self.data1 = value
                return self,
        elif self.data2 is None and self.left is not None:
            # 2 node - internal
            if value < self.data1:
                tup = self.left._insert(value)
                if len(tup) > 1:
                    self.left, self.data1, self.middle, self.data2, self.right = tup[0], tup[1], tup[
                        2], self.data1, self.middle
                return self,
            else:
                tup = self.middle._insert(value)
                if len(tup) > 1:
                    self.middle, self.data2, self.right = tup[0], tup[1], tup[2]
                return self,

        elif self.left is None:
            # 3 node - leaf
            if value < self.data1:
                d1, d2, d3 = value, self.data1, self.data2
            elif value < self.data2:
                d1, d2, d3 = self.data1, value, self.data2
            else:
                d1, d2, d3 = self.data1, self.data2, value

            return self.leaf(d1), d2, self.leaf(d3)
        else:
            # 3 node - non-leaf
            if value < self.data1:
                tup = self.left._insert(value)
                if len(tup) == 1:
                    return self,
                else:
                    tree_left, data, tree_right = tup
                    return Tree23.node2(tree_left, data, tree_right), self.data1, Tree23.node2(self.middle, self.data2,
                                                                                               self.right)
            elif value < self.data2:
                tup = self.middle._insert(value)
                if len(tup) == 1:
                    return self,
                else:
                    tree_left, data, tree_right = tup
                    return Tree23.node2(self.left, self.data1, tree_left), data, Tree23.node2(tree_right, self.data2,
                                                                                              self.right)

            else:
                tup = self.right._insert(value)
                if len(tup) == 1:
                    return self,
                else:
                    tree_left, data, tree_right = tup
                    return Tree23.node2(self.left, self.data1, self.middle), self.data2, Tree23.node2(tree_left, data,
                                                                                                      tree_right)
