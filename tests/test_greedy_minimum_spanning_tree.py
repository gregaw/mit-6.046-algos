import pytest

from algos.l_greedy_minimum_spanning_tree import mst_kruskal
from tests.utils.graph import create_vertices_edges_from_string


@pytest.mark.parametrize(
    "graph,expected", [
        ("""   ,  1,
               ,   ,  2
               ,   ,   """,
         3),
        ("""   ,  1,  1
               ,   ,  2
               ,   ,   """,
         2),
        ("""   ,  1,
               ,   ,  2
              1,   ,   """,
         2),
    ]
)
def test_shortest_path(graph, expected):
    vertices, edges = create_vertices_edges_from_string(graph)

    assert sum(map(lambda x: x.weight, mst_kruskal(vertices, edges))) == expected

# def test_random_graph():
#     vertices = generate_random_graph(3, 2, 10)
#     try:
#         assert matrix_to_string(dynamic_shortest_path_all(vertices)) == matrix_to_string(
#             dijkstra_shortest_path_all(vertices))
#     except:
#         print matrix_to_string(create_matrix_from_vertices(vertices))
#         raise
