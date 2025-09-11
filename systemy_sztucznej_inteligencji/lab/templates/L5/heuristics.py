
class Heuristics:
    @staticmethod
    def manhattan(goal):
        """
        Return function h(n) = |r_n - r_g| + |c_n - c_g|.

        Assumes nodes are (row, col) tuples. If the goal or n is invalid,
        returns 0 as a safe fallback.

        Parameters
        ----------
        goal : tuple[int, int]
            Target position (r_g, c_g).

        Returns
        -------
        callable
            A function h(n) taking n=(r_n, c_n).

        Examples
        --------
        >>> h = Heuristics.manhattan((2, 3))
        >>> h((0, 0))
        5
        """
        if isinstance(goal, tuple) and len(goal) == 2:
            gr, gc = goal
        else:
            gr = gc = None

        def h(n):
            if isinstance(n, tuple) and len(n) == 2 and gr is not None:
                r, c = n
                # TODO - BLOCK START
                # TASK#8
                return 0
                # TODO - BLOCK END
            return 0

        return h

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