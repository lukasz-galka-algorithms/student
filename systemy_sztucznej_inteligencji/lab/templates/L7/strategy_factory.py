from clustering_strategy import ClusterStrategy
from gini_strategy import GiniStrategy


class StrategyFactory:
    """
    Factory for creating split strategies by string identifier.
    """

    @staticmethod
    def create_strategy(model_type="gini", model_params=None):
        """
        Create and return a split strategy instance.

        Parameters
        ----------
        model_type : {"gini", "clustering"}, default="gini"
        Type of splitting strategy to instantiate.
        model_params : dict or None, default=None
        Keyword arguments passed to the strategy constructor.

        Returns
        -------
        SplitStrategy
        A new strategy instance.

        Raises
        ------
        ValueError
        If `model_type` is not recognized.
        """
        params = model_params or {}

        # TODO - BLOCK START
        # TASK#5
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