from collections import defaultdict


def mst_kruskal(vertices, edges):
    """

    :param vertices:
    :param edges:
    :return:    [edge1, edge2]
    """

    edges_sorted = list(sorted(edges, key=lambda x: x.weight))  # E log E

    output = []

    vertices_sets = defaultdict(set)
    for e in edges:
        vertices_sets[e.start].add(e.finish)
        vertices_sets[e.finish].add(e.start)

    # while vertices not full  E
    for edge in edges_sorted:
        left = vertices_sets[edge.start]
        right = vertices_sets[edge.finish]
        if len(left.symmetric_difference(right)) > 0:
            both = left.union(right)
            vertices_sets[edge.start] = both
            vertices_sets[edge.finish] = both
            output.append(edge)

    return output
