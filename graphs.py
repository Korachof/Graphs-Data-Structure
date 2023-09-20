class Graph:
    def __init__(self):
        self.adjacency_data = {}

    def add_vertex(self, vertex):
        """
        Add new vertex to the graph
        :param vertex: the vertex to be added
        :return: Bool (True if the vertex is not already in the graph, False otherwise)
        """
        if vertex not in self.adjacency_data.keys():
            self.adjacency_data[vertex] = []
            return True

        return False

    def add_edge(self, vertex1, vertex2):
        """
        Add a new edge between two existing vertices
        :param vertex1: The first vertex for the edge
        :param vertex2: The second vertex for the edge
        :return: Bool (True if both vertices exist and the edge is added, False otherwise)
        """
        if vertex1 in self.adjacency_data.keys() and vertex2 in self.adjacency_data.keys():
            self.adjacency_data[vertex1].append(vertex2)
            self.adjacency_data[vertex2].append(vertex1)
            return True

        return False

    def remove_edge(self, vertex1, vertex2):
        """
        Remove an existing edge from the graph
        :param vertex1: The first vertex of the edge
        :param vertex2: The second vertext of the edge
        :return: Bool (True if both vertices exist, the edge exists, and it was removed, False Otherwise)
        """
        if vertex1 in self.adjacency_data.keys() and vertex2 in self.adjacency_data.keys():
            try:
                self.adjacency_data[vertex1].remove(vertex2)
                self.adjacency_data[vertex2].remove(vertex1)
                return True
            except ValueError:
                pass

        return False

    def remove_vertex(self, vertex):
        """
        Remove an existing vertex from the graph
        :param vertex: The vertex to be removed
        :return: Bool (True if the vertex exists and is removed, False otherwise)
        """
        if vertex in self.adjacency_data.keys():
            for edge in self.adjacency_data[vertex]:
                self.remove_edge(vertex, edge)
            del self.adjacency_data[vertex]
            return True

        return False