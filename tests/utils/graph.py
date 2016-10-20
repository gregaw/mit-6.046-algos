import random

from algos.utils.graph import Edge, Vertex


def create_vertices_from_string(text):
    rows = text.replace(' ', '').split('\n')
    vertices = [Vertex([]) for row in rows]
    for ix, row in enumerate(rows):
        vertex = vertices[ix]
        vertex.edges = [Edge(vertex, vertices[to_ix], int(weight)) for to_ix, weight in enumerate(row.split(',')) if
                        len(weight)]

    return vertices


def create_vertices_edges_from_string(text):
    rows = text.replace(' ', '').split('\n')
    vertices = list(xrange(0, len(rows)))
    edges = []
    for ix, row in enumerate(rows):
        vertex = vertices[ix]
        for to_ix, weight in enumerate(row.split(',')):
            if len(weight):
                edges.append(Edge(vertex, vertices[to_ix], int(weight)))

    return vertices, edges


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


def generate_random_graph(size, max_edges_per_node, max_weight):
    vertices = [Vertex([]) for x in xrange(size)]

    for v in vertices:
        v.edges = [Edge(v, x, random.randint(1, max_weight)) for x in
                   random.sample(vertices, random.randint(0, max_edges_per_node)) if x != v]

    return vertices
