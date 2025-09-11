from graph import Graph
from maze import Maze
from search import Search
from heuristics import Heuristics

class Experiment:
    """
    A class to run experiments.
    """

    @staticmethod
    def prepare_maze_example():
        """
        Build and return a **Maze** object.

        Grid spec (5 rows × 7 cols)
        ---------------------------
        Walls '#' form a border; 'S' is start; 'G' is goal; '.' are free cells.
        The S→G path exists along row 1 (left-to-right).

            Row 0: "#######"
            Row 1: "#S...G#"
            Row 2: "#.#.#.#"
            Row 3: "#.....#"
            Row 4: "#######"

        What to return
        --------------
        - A Maze instance constructed from the grid above with:
            start_char = 'S', goal_char = 'G', wall_char = '#'
            cost_of = {'.': 1, 'S': 1, 'G': 1}   (unspecified chars default to 1)
        """
        # TODO - BLOCK START
        # TASK#14
        pass
        # TODO - BLOCK END

    @staticmethod
    def dijkstra_search_example():
        """
        Run Dijkstra on a small **weighted** graph.

        Graph layout (unique shortest A→G is A-B-E-G with total cost 4):
            A -1- B -2- C
            |     |     |
            4     2    10
            |     |     |
            D -1- E -1- G

        Edges (add both directions to emulate undirected):
            (A,B,1), (B,C,2), (A,D,4), (D,E,1), (E,G,1), (B,E,2), (C,G,10)

        Must return
        -----------
        dict:
          - 'path'    : e.g. ['A','B','E','G']
          - 'cost'    : 4
          - 'start'   : 'A'
          - 'goal'    : 'G'
        """
        # TODO - BLOCK START
        # TASK#15
        g, start, goal = None, None, None
        # TODO - BLOCK END
        res = Search.dijkstra(g, start, goal)
        return {
            "path": res["path"],
            "cost": res["cost"],
            "start": start,
            "goal": goal,
        }

    @staticmethod
    def astar_search_example():
        """
        Run A* on a small **coordinate** graph (nodes are (row, col) tuples).

        Why coordinates?
        ----------------
        The provided Manhattan heuristic `Heuristics.manhattan(goal)` expects
        nodes shaped like (r, c). That keeps the example clean and testable.

        Graph spec (a simple corridor with one or two distractors):
            Nodes: (0,0) → (0,1) → (1,1) → (2,1) → (2,2)   [all unit weights]
            Extra detours (higher cost) so the optimal path is unique:
                (0,1) → (0,2) cost 2
                (0,2) → (1,2) cost 2
                (1,2) → (2,2) cost 10
            Make edges bidirectional.

        Start/Goal:
            start = (0,0)
            goal  = (2,2)

        Must return
        -----------
        dict:
          - 'path'    : list of (r,c), e.g. [(0,0),(0,1),(1,1),(2,1),(2,2)]
          - 'cost'    : 4
          - 'start'   : (0,0)
          - 'goal'    : (2,2)
        """
        # TODO - BLOCK START
        # TASK#16
        g, start, goal = None, None, None
        # TODO - BLOCK END
        h = Heuristics.manhattan(goal)
        res = Search.astar(g, start, goal, h=h)

        return {
            "path": res["path"],
            "cost": res["cost"],
            "start": start,
            "goal": goal,
        }

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