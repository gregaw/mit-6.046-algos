def dynamic_shortest_path_all(vertices):
    """
        acyclic or non-negative
    :param vertices:
    :return:
    """

    cache = {}

    def shortest_path(a, b, k):

        if k == 0:
            return float('inf')

        if cache.has_key((a, b, k)):
            return cache[(a, b, k)]

        if a == b:
            return 0

        best = float('inf')
        for e in a.edges:
            new_weight = shortest_path(e.finish, b, k - 1) + e.weight
            if new_weight < best:
                best = new_weight

        cache[(a, b, k)] = best
        return best

    output = [[None] * len(vertices) for x in xrange(0, len(vertices))]

    for row, start in enumerate(vertices):
        for column, finish in enumerate(vertices):
            output[row][column] = shortest_path(start, finish, len(vertices))

    return output


def dijkstra_shortest_path_all(vertices):
    shortest = {}

    class Entry:
        def __init__(self, vertex, path_weight):
            self.path_weight = path_weight
            self.vertex = vertex

    for v in vertices:
        queue = [Entry(v, 0)]
        while queue:

            current = min(queue, key=lambda x: x.path_weight)

            if shortest.has_key((v, current.vertex)):
                queue.remove(current)
            else:
                shortest[(v, current.vertex)] = current.path_weight

                queue.remove(current)

                for neighbour in current.vertex.edges:
                    queue.append(Entry(neighbour.finish, current.path_weight + neighbour.weight))

    def convert_to_matrix(dictionary):
        def find_ix(vertex):
            for ix, v in enumerate(vertices):
                if v == vertex:
                    return ix
            return None

        output = [[float('inf')] * len(vertices) for x in xrange(0, len(vertices))]
        for key, path_weight in dictionary.iteritems():
            output[find_ix(key[0])][find_ix(key[1])] = path_weight

        return output

    return convert_to_matrix(shortest)
