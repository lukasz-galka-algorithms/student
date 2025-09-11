from graph import Graph

class Maze:
    """
    Grid-based maze with **4-directional** movement (up, down, left, right).

    Legend
    ------
    wall_char  : blocks movement (default '#')
    start_char : optional start (default 'S') → stored in self.start
    goal_char  : optional goal  (default 'G') → stored in self.goal
    cost_of    : dict {char -> enter-cost}; missing chars default to 1

    Edge weight convention
    ----------------------
    Moving u -> v has cost equal to the *destination* tile's cost (default 1 if not specified)

    Readable list-of-lists examples
    ----------------------------------
    Example A (3x3):
        # index map for clarity:
        #          0   1   2
        #     0   [S]  .   .
        #     1    .   #  [G]
        #     2    .   .   .
        grid = [
            ['S', '.', '.'],
            ['.', '#', 'G'],
            ['.', '.', '.'],
        ]

        mz = Maze(grid)            # '#' is a wall, 'S' start, 'G' goal
        mz.start  -> (0, 0)
        mz.goal   -> (1, 2)
        g = mz.to_graph()          # Graph with nodes as (row, col)

    Example B (custom costs; 'm' = mud costs 5 to enter):
        #          0   1   2
        #     0   [S]  .   m
        #     1    .   #  [G]
        #     2    .   .   .
        grid = [
            ['S', '.', 'm'],
            ['.', '#', 'G'],
            ['.', '.', '.'],
        ]
        mz = Maze(grid, cost_of={'m': 5})  # other tiles default to 1

    Notes
    -----
    - This class **does not** perform pathfinding. Use Dijkstra/A* on the
      `Graph` returned by `to_graph()`.
    """

    def __init__(self, grid, start_char='S', goal_char='G', wall_char='#', cost_of=None):
        """
        Build a maze from a rectangular grid (list[list[str]]).

        Parameters
        ----------
        grid : list[list[str]]
            Rectangular grid. Each cell should be a 1-char string.
        start_char, goal_char, wall_char : str
            Special characters used in the grid.
        cost_of : dict or None
            Mapping char -> enter-cost. Missing chars default to cost 1.
            Start and goal also default to cost 1 unless overridden.

        Raises
        ------
        TypeError
            If `grid` is not a list.
        ValueError
            If `grid` is not rectangular (rows have different lengths).
        """
        if not isinstance(grid, list):
            raise TypeError("grid must be a list of lists of chars")

        # Expect list of lists of single-character strings
        self.grid = grid
        self.rows = len(self.grid)
        self.cols = len(self.grid[0]) if self.rows else 0

        # rectangularity check
        for row in self.grid:
            if len(row) != self.cols:
                raise ValueError("grid must be rectangular (all rows same length)")

        self.start_char = start_char
        self.goal_char = goal_char
        self.wall_char = wall_char
        self.cost_of = dict(cost_of or {})

        # Ensure start/goal have a defined cost (default 1) for convenience
        self.cost_of.setdefault(self.start_char, 1)
        self.cost_of.setdefault(self.goal_char, 1)

        # Locate optional start/goal
        self.start = None
        self.goal = None
        self._scan_start_goal()

    def _scan_start_goal(self):
        """
        Scan the grid once to capture the **first occurrence** of start and goal.

        Side effects
        ------------
        - Sets `self.start = (r, c)` if `start_char` is found, else None.
        - Sets `self.goal  = (r, c)` if `goal_char`  is found, else None.

        Notes
        -----
        - If multiple 'S' or 'G' exist, only the **first** one found (row-major)
          is recorded. This keeps behavior deterministic and simple.
        - Having no 'S' or no 'G' is allowed; pathfinding code can use any
          coordinates as (start, goal) if needed.

        Mini-example
        ------------
        grid = [
            ['S', '.', '.'],
            ['.', '#', 'G'],
        ]
        After call:
            self.start == (0, 0)
            self.goal  == (1, 2)
        """
        for r in range(self.rows):
            for c in range(self.cols):
                ch = self.grid[r][c]
                if ch == self.start_char and self.start is None:
                    self.start = (r, c)
                elif ch == self.goal_char and self.goal is None:
                    self.goal = (r, c)

    def in_bounds(self, r, c):
        """
        Check whether (r, c) lies inside the grid bounds.

        Returns
        -------
        bool
            True if 0 <= r < rows and 0 <= c < cols.

        Examples
        --------
        - For a 3x3 grid, (0,0), (2,2) are in bounds; (3,0), (-1,1) are not.
        - Typically used before accessing `grid[r][c]`.
        """
        return 0 <= r < self.rows and 0 <= c < self.cols

    def is_passable(self, r, c):
        """
        Check whether (r, c) is **inside the grid** and **not** a wall tile.

        Returns
        -------
        bool
            True if (r, c) is in bounds and grid[r][c] != wall_char.

        Examples
        --------
        With wall_char = '#':
            grid[r][c] == '#'  → False
            grid[r][c] in {'.','S','G','m', ...} → True (unless it's '#')
        """
        return self.in_bounds(r, c) and self.grid[r][c] != self.wall_char

    def neighbors4(self, r, c):
        """
        Yield passable **4-neighbors** of (r, c): up, down, left, right.

        Yields
        ------
        (nr, nc) : tuple[int, int]
            Coordinates of a neighbor that is in bounds and not a wall.

        Examples
        --------
        Using the grid:
            [['S', '.', '.'],
             ['.', '#', 'G'],
             ['.', '.', '.']]
        neighbors4(0, 0) → (0, 1), (1, 0)
        neighbors4(1, 0) → (0, 0), (2, 0)      # (1,1) is a wall '#'
        neighbors4(1, 2) → (0, 2), (2, 2)      # left (1,1) blocked by '#'
        """
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + dr, c + dc
            if self.is_passable(nr, nc):
                yield (nr, nc)

    def to_graph(self):
        """
        Convert this maze into a `Graph`.

        Nodes
        -----
        All passable cells as (row, col) tuples.

        Edges
        -----
        Between 4-adjacent passable cells.
        Edge cost u->v = enter-cost of cell `v` (defaults to 1 if not provided).

        Quick check (3x3 example)
        -------------------------
        >>> grid = [['S', '.', '.'],
        ...         ['.', '#', 'G'],
        ...         ['.', '.', '.']]
        >>> mz = Maze(grid)
        >>> g = mz.to_graph()
        >>> (0, 0) in g.nodes()
        True
        >>> # entering '.' or 'G' costs 1 by default:
        >>> ((0,0), (0,1), 1) in g.edges()
        True
        """
        # TODO - BLOCK START
        # TASK#9
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