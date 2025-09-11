import heapq

class Search:
    """
    Canonical shortest-path search routines on graphs with non-negative edge weights.

    What it provides
    ----------------
    - Dijkstra (Uniform-Cost Search) for optimal paths on non-negative weights.
    - A* Search with a user-supplied heuristic `h(n)`; if `h=None`, behaves like Dijkstra.

    Return format
    -------------
    Both algorithms return a dict:
      {
        'path':   [start, ..., goal]      # empty list if unreachable
        'cost':   total_path_cost         # float('inf') if unreachable
        'visited': [n1, n2, ...]          # order in which nodes were expanded
      }
    """

    @staticmethod
    def _iter_neighbors(graph, node):
        """
        Unified neighbor iterator.

        Accepts either:
          - graph.neighbors(node) -> [(neighbor, weight), ...]
          - graph.neighbors(node) -> [neighbor, ...]   (weight implicitly 1)

        Yields
        ------
        (neighbor, edge_weight) tuples.
        """
        for item in graph.neighbors(node):
            if isinstance(item, tuple) and len(item) == 2:
                neighbor, edge_weight = item
            else:
                neighbor, edge_weight = item, 1
            yield neighbor, edge_weight

    @staticmethod
    def _reconstruct_path(predecessor, start, goal):
        """
        Rebuild a path from `start` to `goal` using a predecessor map.

        Parameters
        ----------
        predecessor : dict
            Maps each reached node to its immediate predecessor on the best-known path.
        start : hashable
            Start node.
        goal : hashable
            Goal node.

        Returns
        -------
        list
            [start, ..., goal] if connected; [] if no path exists.

        Notes
        -----
        - If start == goal, returns [start].
        - If `goal` is not present in `predecessor`, returns [].
        """
        if start == goal:
            return [start]
        if goal not in predecessor:
            return []
        path = [goal]
        current = goal
        while current != start:
            current = predecessor.get(current)
            if current is None:
                return []
            path.append(current)
        path.reverse()
        return path

    @staticmethod
    def dijkstra(graph, start, goal):
        """
        Dijkstra's algorithm (Uniform-Cost Search) for non-negative weights.

        Parameters
        ----------
        graph : object
            Provides `neighbors(u)` as described in the class docstring.
        start : hashable
            Start node.
        goal : hashable
            Goal node.

        Returns
        -------
        dict
            {
              'path': [start, ..., goal] or [],
              'cost': total_cost or float('inf'),
              'visited': expansion_order_list
            }

        Raises
        ------
        ValueError
            If a negative edge weight is encountered.
        """
        # priority queue holds pairs (g_cost, node)
        priority_queue = [(0, start)]
        # best known g(n) cost to each node
        best_g = {start: 0}
        # predecessor on the best-known path
        predecessor = {}
        # expansion order (useful for tests/analysis)
        expanded_order = []

        while priority_queue:
            g_current, current = heapq.heappop(priority_queue)

            # Skip stale entries (a better cost has been found)
            if g_current != best_g.get(current, float('inf')):
                continue

            expanded_order.append(current)

            # TODO - BLOCK START
            # TASK#10
            pass
            # TODO - BLOCK END

            for neighbor, edge_weight in Search._iter_neighbors(graph, current):
                if edge_weight < 0:
                    raise ValueError("Dijkstra requires non-negative edge weights.")
                # TODO - BLOCK START
                # TASK#11
                pass
                # TODO - BLOCK END

        return {'path': [], 'cost': float('inf'), 'visited': expanded_order}

    @staticmethod
    def astar(graph, start, goal, h=None):
        """
        A* search with heuristic h(n). With h=None, behaves exactly like Dijkstra.

        Parameters
        ----------
        graph : object
            Provides `neighbors(u)` as described in the class docstring.
        start : hashable
            Start node.
        goal : hashable
            Goal node.
        h : callable or None
            Heuristic function `h(n) -> non-negative estimate`. If None, `h(n)=0`.

        Returns
        -------
        dict
            {
              'path': [start, ..., goal] or [],
              'cost': total_cost or float('inf'),
              'visited': expansion_order_list
            }

        Raises
        ------
        ValueError
            If a negative edge weight is encountered.
        """
        if h is None:
            def h(_):  # default to 0 → A* reduces to Dijkstra
                return 0

        # priority queue holds triples (f=g+h, g, node)
        priority_queue = [(h(start), 0, start)]
        best_g = {start: 0}
        predecessor = {}
        expanded_order = []

        while priority_queue:
            f_current, g_current, current = heapq.heappop(priority_queue)

            # Skip stale entries (a better g has been found)
            if g_current != best_g.get(current, float('inf')):
                continue

            expanded_order.append(current)

            # TODO - BLOCK START
            # TASK#12
            pass
            # TODO - BLOCK END

            for neighbor, edge_weight in Search._iter_neighbors(graph, current):
                if edge_weight < 0:
                    raise ValueError("A* requires non-negative edge weights.")
                # TODO - BLOCK START
                # TASK#13
                pass
                # TODO - BLOCK END

        return {'path': [], 'cost': float('inf'), 'visited': expanded_order}

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