import random

import pytest

from algos.k_graph_shortest_paths import Vertex, Edge, dynamic_shortest_path_all, dijkstra_shortest_path_all


def create_nodes_from_string(text):
    rows = text.replace(' ', '').split('\n')
    vertices = [Vertex([]) for row in rows]
    for ix, row in enumerate(rows):
        vertex = vertices[ix]
        vertex.edges = [Edge(vertex, vertices[to_ix], int(weight)) for to_ix, weight in enumerate(row.split(',')) if
                        len(weight)]

    return vertices


def create_matrix_from_vertices(vertices):
    def find_ix(vertex):
        for ix, v in enumerate(vertices):
            if v == vertex:
                return ix
        return None

    output = []
    for v in vertices:
        row = [float('inf')] * len(vertices)
        for e in v.edges:
            row[find_ix(e.finish)] = e.weight
        output.append(row)

    return output


def matrix_to_string(matrix):
    return '\n'.join([','.join([str(cell) if cell != float('inf') else '' for cell in row]) for row in matrix])


@pytest.mark.parametrize(
    "graph,expected", [
        ("""   ,  1,
               ,   ,  2
               ,   ,   """,
         """  0,  1,  3
               ,  0,  2
               ,   ,  0 """),
        ("""   ,  2,
              1,   ,  2
               ,   ,   """,
         """  0,  2,  4
              1,  0,  2
               ,   ,  0 """),
        ("""   ,  8,  4
              5,   ,  1
              9,  5,    """,
         """  0,  8,  4
              5,  0,  1
              9,  5,  0 """
         )
    ]
)
def test_shortest_path(graph, expected):
    graph_nodes = create_nodes_from_string(graph)

    assert matrix_to_string(dynamic_shortest_path_all(graph_nodes)) == expected.replace(' ', '')
    assert matrix_to_string(dijkstra_shortest_path_all(graph_nodes)) == expected.replace(' ', '')


def test_random_graph():
    def generate_random_graph(size, max_edges_per_node, max_weight):
        vertices = [Vertex([]) for x in xrange(size)]

        for v in vertices:
            v.edges = [Edge(v, x, random.randint(1, max_weight)) for x in
                       random.sample(vertices, random.randint(0, max_edges_per_node)) if x != v]

        return vertices

    vertices = generate_random_graph(3, 2, 10)
    try:
        assert matrix_to_string(dynamic_shortest_path_all(vertices)) == matrix_to_string(
            dijkstra_shortest_path_all(vertices))
    except:
        print matrix_to_string(create_matrix_from_vertices(vertices))
        raise
