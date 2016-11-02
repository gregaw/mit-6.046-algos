import pytest

from algos.o_distributed import SpanningTreeSimpleActor


@pytest.mark.parametrize(
    "graph,result", [
        ("0-1", "0-1"),
        ("0-1,1-2,2-3", "0-1,1-2,2-3"),
        ("0-1,1-2,1-4,2-3", "0-1,1-2,1-4,2-3"),
        ("0-1,1-2,0-2", "0-1,0-2"),
        ("0-1,1-2,0-2,1-3", "0-1,0-2,1-3"),
        ("0-1,1-2,0-2,1-3,4-5", "0-1,0-2,1-3"),
    ]
)
def test_spanning_tree_simple_no_cycles(graph, result):
    nodes = []
    try:
        nodes = parse_0graph(graph)

        actual = nodes[0].ask(dict(type='search', parent=None))
        expected = parse_edges_0graph(result) + [(None, 0)]
        assert sorted(actual) == sorted(expected)
    finally:
        if nodes:
            for node in nodes:
                node.stop()


def parse_0graph(graph):
    edges = parse_edges_0graph(graph)
    max_id = max([max(ed) for ed in edges])
    nodes = [SpanningTreeSimpleActor.start(id=x) for x in xrange(0, max_id + 1)]
    for edge in edges:
        nodes[edge[0]].tell(dict(type='add_child', child=nodes[edge[1]]))
    return nodes


def parse_edges_0graph(text):
    return [(int(x[0]), int(x[1])) for x in [ed.split('-') for ed in text.split(',')]]
