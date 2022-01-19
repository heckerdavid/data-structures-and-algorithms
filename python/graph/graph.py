
class Graph:
    def __init__(self) -> None:
        self.length = 0
        self.vertex_list = {}

    def size(self):
        return self.length

    def get_nodes(self):
        return list(self.vertex_list.keys())

    def add_node(self, value):
        vertex = Vertex(value)
        self.length += 1
        self.vertex_list[vertex] = []
        return vertex

    def add_edge(self, start, end, weight=0):
        self.vertex_list[end]

        self.vertex_list[start].append(Edge(end, weight))

    def get_neighbors(self, vertex):
        return self.vertex_list[vertex]

class Edge:
    def __init__(self, vertex, weight=0) -> None:
        self.vertex = vertex
        self.weight = weight

class Vertex:
    def __init__(self, value) -> None:
        self.value = value
