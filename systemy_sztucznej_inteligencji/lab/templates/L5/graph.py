class Graph:
    """
    A tiny, DIRECTED graph backed by an adjacency list.
    Edge weights (costs) default to 1.

    What it models
    --------------
    - Nodes can be *any hashable* objects (e.g., str, int, tuples like (r, c)).
    - Edges are *directed* with an optional non-negative weight (cost).
      For an undirected graph, add both directions explicitly.

    Design notes
    ------------
    - Internally we keep:  _adj: dict[node] -> list[(neighbor, cost)]
      This is compact, fast to update, and easy to traverse.
    - We do not de-duplicate edges; adding the same (u, v, cost) twice
      will produce two parallel entries. (That’s fine for most search labs.)

    Doctest-style examples
    ----------------------
    >>> g = Graph()
    >>> g.add_edge('A', 'B')         # cost defaults to 1
    >>> g.add_edge('B', 'C', 3)      # weighted edge
    >>> g.neighbors('B')
    [('C', 3)]
    >>> sorted(g.nodes())
    ['A', 'B', 'C']
    >>> sorted(g.edges())
    [('A', 'B', 1), ('B', 'C', 3)]

    Undirected usage (by adding both directions):
    >>> g2 = Graph()
    >>> g2.add_edge('X', 'Y', 5)
    >>> g2.add_edge('Y', 'X', 5)
    >>> set(g2.neighbors('X')) == {('Y', 5)}
    True
    """

    def __init__(self):
        """
        Initialize an empty adjacency list.

        Attributes
        ----------
        _adj : dict
            Maps a node to a list of (neighbor, cost) tuples.
        """
        # TODO - BLOCK START
        # TASK#2
        pass
        # TODO - BLOCK END

    def add_node(self, u):
        """
        Ensure node `u` exists in the adjacency structure.

        Parameters
        ----------
        u : hashable
            Node identifier (e.g., str, int, tuple).

        Behavior
        --------
        - If `u` is not present, creates an empty neighbor list for it.
        - If `u` already exists, this is a no-op.
        """
        # TODO - BLOCK START
        # TASK#3
        pass
        # TODO - BLOCK END

    def add_edge(self, u, v, cost=1):
        """
        Add a *directed* edge u -> v with a given `cost`.

        Parameters
        ----------
        u, v : hashable
            Endpoints of the edge (nodes). Created on the fly if missing.
        cost : number (default: 1)
            Edge weight (travel cost). For undirected graphs, call twice:
            add_edge(u, v, cost) and add_edge(v, u, cost).

        Notes
        -----
        - Edges are not deduplicated; you can have parallel edges.
        - The class does not validate cost sign.
        """
        # TODO - BLOCK START
        # TASK#4
        pass
        # TODO - BLOCK END

    def neighbors(self, u):
        """
        Return the outgoing neighbors of `u` as a list of (neighbor, cost).

        Parameters
        ----------
        u : hashable

        Returns
        -------
        list[tuple]
            A list like [(v1, c1), (v2, c2), ...]. If `u` is unknown,
            returns an empty list.
        """
        # TODO - BLOCK START
        # TASK#5
        pass
        # TODO - BLOCK END

    def nodes(self):
        """
        Return all nodes currently in the graph.

        Returns
        -------
        list
            A list of node identifiers (the dict keys).
        """
        # TODO - BLOCK START
        # TASK#6
        pass
        # TODO - BLOCK END

    def edges(self):
        """
        Return all directed edges as (u, v, cost) triples.

        Returns
        -------
        list[tuple]
            A flat list of (u, v, cost) for every stored edge.
        """
        # TODO - BLOCK START
        # TASK#7
        pass
        # TODO - BLOCK END

class StudentID:
    """
    Utility class for identifying the student.

    Each student must replace the placeholder return value
    in the `get_ID` method with their own unique student ID.
    """

    @staticmethod
    def get_ID():
        """
        Return the student ID as a string.

        Returns
        -------
        str
            The student ID. Each student must replace "student_ID" with their own ID.

        Examples
        --------
        >>> StudentID.get_ID()
        '123456'
        """
        # TODO - BLOCK START
        # TASK#1
        return "student_ID"
        # TODO - BLOCK END