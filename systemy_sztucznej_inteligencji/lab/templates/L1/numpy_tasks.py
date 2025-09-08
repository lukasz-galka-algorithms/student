import numpy as np

class NumpyTasks:
    """
    A collection of methods demonstrating the use of NumPy for
    array creation, statistics, elementwise operations, dot products,
    and pairwise distance calculations.
    """

    @staticmethod
    def create_array_from_list(values):
        """
        Convert a Python list into a NumPy array.

        Parameters
        ----------
        values : list or ndarray
            Input sequence.

        Returns
        -------
        numpy.ndarray
            A NumPy array view/copy of the input.

        Examples
        --------
        >>> NumpyTasks.create_array_from_list([1, 2, 3])
        array([1, 2, 3])
        """
        # TODO - BLOCK START
        # TASK#6
        pass
        # TODO - BLOCK END

    @staticmethod
    def compute_mean(values):
        """
        Compute the mean (average) of the given values.

        Parameters
        ----------
        values : list or ndarray
            Input data.

        Returns
        -------
        float
            Mean value. Returns 0.0 for empty input.

        Examples
        --------
        >>> NumpyTasks.compute_mean([1, 2, 3, 4])
        2.5
        """
        # TODO - BLOCK START
        # TASK#7
        pass
        # TODO - BLOCK END

    @staticmethod
    def compute_median(values):
        """
        Compute the median of the given values.

        Parameters
        ----------
        values : list or ndarray
            Input data.

        Returns
        -------
        float
            Median value. Returns 0.0 for empty input.

        Examples
        --------
        >>> NumpyTasks.compute_median([1, 3, 2])
        2.0
        """
        # TODO - BLOCK START
        # TASK#8
        pass
        # TODO - BLOCK END

    @staticmethod
    def compute_standard_deviation(values):
        """
        Compute the standard deviation of the given values.

        Parameters
        ----------
        values : list or ndarray
            Input data.

        Returns
        -------
        float
            Standard deviation. Returns 0.0 for empty input.

        Examples
        --------
        >>> round(NumpyTasks.compute_standard_deviation([1, 2, 3]), 6)
        0.816497
        """
        # TODO - BLOCK START
        # TASK#9
        pass
        # TODO - BLOCK END

    @staticmethod
    def elementwise_square(values):
        """
        Square each element of the input.

        Parameters
        ----------
        values : list or ndarray
            Input data.

        Returns
        -------
        numpy.ndarray
            Array with squared values.

        Examples
        --------
        >>> NumpyTasks.elementwise_square([1, 2, 3])
        array([1, 4, 9])
        """
        # TODO - BLOCK START
        # TASK#10
        pass
        # TODO - BLOCK END

    @staticmethod
    def dot_product(values1, values2):
        """
        Compute the dot product of two 1D arrays.

        Parameters
        ----------
        values1 : list or ndarray
            First vector.
        values2 : list or ndarray
            Second vector.

        Returns
        -------
        float
            Dot product.

        Examples
        --------
        >>> NumpyTasks.dot_product([1, 2], [3, 4])
        11
        """
        # TODO - BLOCK START
        # TASK#11
        pass
        # TODO - BLOCK END

    @staticmethod
    def pairwise_distances(values):
        """
        Compute pairwise Euclidean distances between all elements of a 1D array.

        Parameters
        ----------
        values : list or ndarray
            One-dimensional input.

        Returns
        -------
        numpy.ndarray
            A 2D matrix D of shape (n, n) where D[i, j] = |values[i] - values[j]|.

        Examples
        --------
        >>> NumpyTasks.pairwise_distances([1, 3, 7])
        array([[0., 2., 6.],
               [2., 0., 4.],
               [6., 4., 0.]])
        """
        # TODO - BLOCK START
        # TASK#12
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