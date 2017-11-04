"""Directed graph data structure."""


class Graph(object):
    """Create graph class."""

    def __init__(self):
        """Initialize graph instance."""
        self._graph = {}
        self._edges = []

    def add_node(self, val):
        """Add a node to the graph."""
        if not self.has_node(val):
            self._graph[val] = []
        else:
            raise ValueError("Value already in graph.")

    def has_node(self, val):
        """Return true if graph contains node with val."""
        return val in self._graph

    def add_edge(self, val, edge):
        """Add an edge to a node, create node if not exists."""
        if [val, edge] not in self._edges:
            if self.has_node(val) and self.has_node(edge):
                self._graph[val].append(edge)
            elif self.has_node(val) and not self.has_node(edge):
                self.add_node(edge)
                self._graph[val].append(edge)
            elif not self.has_node(val) and self.has_node(edge):
                self.add_node(val)
                self._graph[val].append(edge)
            else:
                self.add_node(val)
                self.add_node(edge)
                self._graph[val].append(edge)
            self._edges.append([val, edge])

    def nodes(self):
        """Return list of all nodes in graph."""
        return [node for node in self._graph]

    def edges(self):
        """Return list of all edges in graph."""
        return self._edges

    def del_node(self, val):
        """Remove a node and associated edges from graph."""
        try:
            self._graph.pop(val)
            for node, edges in self._graph.items():
                try:
                    edges.remove(val)
                except ValueError:
                    continue
            self._edges = [edge for edge in self._edges if val not in edge]  # lambda filter
        except KeyError:
            raise ValueError("Value not in graph.")

    def del_edge(self, val1, val2):
        """Remove an edge from the graph."""
        try:
            self._edges.remove([val1, val2])
            self._graph[val1].remove(val2)
        except ValueError:
            raise ValueError("Edge not in graph.")

    def neighbors(self, val):
        """Return values node is connected to."""
        return self._graph[val]

    def adjacent(self, val1, val2):
        """Return true if val1 and val2 are connected by an edge."""
        if self.has_node(val1) and self.has_node(val2):
            return val2 in self._graph[val1] or val1 in self._graph[val2]
        else:
            raise ValueError("Supplied value not in graph.")
