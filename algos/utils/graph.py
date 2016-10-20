__author__ = 'gregaw'


class Edge:
    def __init__(self, start, finish, weight):
        self.weight = weight
        self.finish = finish
        self.start = start


class Vertex:
    def __init__(self, edges):
        self.edges = edges
