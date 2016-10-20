import pytest

from algos.k_graph_shortest_paths import dynamic_shortest_path_all, dijkstra_shortest_path_all
from tests.utils.graph import create_vertices_from_string, create_matrix_from_vertices, matrix_to_string, \
    generate_random_graph


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
    graph_nodes = create_vertices_from_string(graph)

    assert matrix_to_string(dynamic_shortest_path_all(graph_nodes)) == expected.replace(' ', '')
    assert matrix_to_string(dijkstra_shortest_path_all(graph_nodes)) == expected.replace(' ', '')


def test_random_graph():
    vertices = generate_random_graph(3, 2, 10)
    try:
        assert matrix_to_string(dynamic_shortest_path_all(vertices)) == matrix_to_string(
            dijkstra_shortest_path_all(vertices))
    except:
        print matrix_to_string(create_matrix_from_vertices(vertices))
        raise
