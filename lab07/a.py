from enum import Enum

from typing import Any
from typing import Dict, List
from typing import Optional
from lab02 import Queue as test


class EdgeType(Enum):
    directed = 1
    undirected = 2


class Vertex:
    data: Any
    index: int

    def __init__(self, data, ind):
        self.data = data
        self.index = ind

    def __repr__(self):
        return f'{self.data}:v{self.index}'


class Edge:
    source: Vertex
    destination: Vertex
    weight: Optional[float]

    def __init__(self, s, d, w):
        self.source = s
        self.destination = d
        self.weight = w

    def __repr__(self):
        return f'{self.destination}'


class Graph:
    adjacencies: Dict[Vertex, List[Edge]]

    def __init__(self):
        self.adjacencies = dict()

    def __repr__(self):
        stirng = ""
        for data in self.adjacencies:
            stirng += f'- {data} ->{self.adjacencies[data]}\n'
        return stirng

    def create_vertex(self, data: Any):
        self.adjacencies[Vertex(data, len(self.adjacencies))] = list()

    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None):
        graph.adjacencies[source].append(Edge(source, destination, weight))

    def add_undirected_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None):
        graph.adjacencies[source].append(Edge(source, destination, weight))
        graph.adjacencies[destination].append(Edge(destination, source, weight))

    def add(self, edge: EdgeType, source: Vertex, destination: Vertex, weight: Optional[float] = None):
        if edge.name == "directed":
            self.add_directed_edge(source, destination, weight)
        else:
            self.add_undirected_edge(source, destination, weight)

    def traverse_breadth_first(self, visit):
        list_keys = [x for x in self.adjacencies.keys()]
        list_visited = []
        queue = test.Queue()
        queue.enqueue(list_keys[0])
        while (len(queue) != 0):
            new = queue.dequeue()
            list_visited.append(new)
            visit(new)
            for new_neighbour in self.adjacencies[new]:
                if new_neighbour.destination in list_visited:
                    True
                else:
                    queue.enqueue(new_neighbour.destination)

    def traverse_depth_first(self, visit):
        list_keys = [x for x in self.adjacencies.keys()]
        list_visited = []
        self._dfs(list_keys[0], list_visited, visit)

    def _dfs(self, v: Vertex, visited: List[Vertex], visit):
        visit(v)
        visited.append(v)
        for new_neighbour in self.adjacencies[v]:
            if new_neighbour.destination in visited:
                True
            else:
                self._dfs(new_neighbour.destination, visited, visit)


graph = Graph()
graph.create_vertex("0")
graph.create_vertex("1")
graph.create_vertex("2")
graph.create_vertex("3")
graph.create_vertex("4")
graph.create_vertex("5")
graph.create_vertex("6")
list = graph.adjacencies.keys()
list_keys = [x for x in list]
graph.add(EdgeType(1), list_keys[0], list_keys[2], 13)
graph.add(EdgeType(1), list_keys[0], list_keys[6], 8)
graph.add(EdgeType(1), list_keys[1], list_keys[3], 14)
graph.add(EdgeType(1), list_keys[1], list_keys[2], 15)
graph.add(EdgeType(1), list_keys[1], list_keys[6], 9)
graph.add(EdgeType(1), list_keys[2], list_keys[4], 14)
graph.add(EdgeType(1), list_keys[2], list_keys[6], 13)
graph.add(EdgeType(1), list_keys[3], list_keys[4], 6)
graph.add(EdgeType(1), list_keys[4], list_keys[5], 6)
graph.add(EdgeType(1), list_keys[5], list_keys[6], 14)
print()
print(graph)
