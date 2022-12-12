from codefellows.dsa.queue import Queue


class Graph:
    def __init__(self):

        self._adjacency_list = {}

    def add_node(self, value):

        v = Vertex(value)

        self._adjacency_list[v] = []

        return v

    def size(self):
        return len(self._adjacency_list)

    def add_edge(self, start_vertex, end_vertex, weight=0, undirected=False):

        if start_vertex not in self._adjacency_list:
            raise KeyError("Start Vertex not found in graph")

        if end_vertex not in self._adjacency_list:
            raise KeyError("End Vertex not found in graph")

        adjacencies = self._adjacency_list[start_vertex]

        adjacencies.append(Edge(end_vertex, weight))

        if undirected:

            adjacencies = self._adjacency_list[end_vertex]

            adjacencies.append(Edge(start_vertex, weight))

    def get_nodes(self):
        return list(self._adjacency_list.keys())

    def get_neighbors(self, vertex):
        return self._adjacency_list.get(vertex, [])

    def breadth_first_search(self, start_vertex, action=(lambda x: None)):

        queue = Queue()

        visited = set()

        queue.enqueue(start_vertex)

        visited.add(start_vertex)

        while len(queue):

            current_vertex = queue.dequeue()

            action(current_vertex)

            neighbors = self.get_neighbors(current_vertex)

            for neighbor in neighbors:

                neighbor_vertex = neighbor.vertex

                if neighbor_vertex not in visited:

                    visited.add(neighbor_vertex)

                    queue.enqueue(neighbor_vertex)


class Vertex:
    def __init__(self, value):
        self.value = value


class Edge:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight
