class DataStructures:
    """
    A collection of methods demonstrating basic operations
    on Python data structures such as lists, tuples, and dictionaries.

    This class is intended as a learning exercise for practicing
    simple data manipulation tasks in Python.
    """

    @staticmethod
    def get_tuple_of_sorted_squared_values(value_1, value_2, value_3):
        """
        Return a tuple containing the squared values of the three inputs,
        sorted in ascending order.

        Parameters
        ----------
        value_1 : int or float
            First value.
        value_2 : int or float
            Second value.
        value_3 : int or float
            Third value.

        Returns
        -------
        tuple of int or float
            A tuple with squared values of the inputs, sorted in ascending order.

        Examples
        --------
        >>> DataStructures.get_tuple_of_sorted_squared_values(3, 1, 2)
        (1, 4, 9)
        """
        # TODO - BLOCK START
        # TASK#2
        pass
        # TODO - BLOCK END

    @staticmethod
    def get_values_as_sorted_list(value_1, value_2, value_3):
        """
        Return a sorted list created from the three input values.

        Parameters
        ----------
        value_1 : int or float
            First value.
        value_2 : int or float
            Second value.
        value_3 : int or float
            Third value.

        Returns
        -------
        list of int or float
            A sorted list containing the three values.

        Examples
        --------
        >>> DataStructures.get_values_as_sorted_list(3, 1, 2)
        [1, 2, 3]
        """
        # TODO - BLOCK START
        # TASK#3
        pass
        # TODO - BLOCK END

    @staticmethod
    def count_unique_values_from_list(lst):
        """
        Count the number of unique values in a list.

        Parameters
        ----------
        lst : list
            Input list. If None, returns 0.

        Returns
        -------
        int
            Number of unique values in the list.

        Examples
        --------
        >>> DataStructures.count_unique_values_from_list([1, 2, 2, 3, 4, 4])
        4
        """
        # TODO - BLOCK START
        # TASK#4
        pass
        # TODO - BLOCK END

    @staticmethod
    def dictionary_from_values(value_1, value_2, key_1="a", key_2="b"):
        """
        Create a dictionary from two values with specified keys.

        Parameters
        ----------
        value_1 : any
            Value for the first key.
        value_2 : any
            Value for the second key.
        key_1 : str, default="a"
            Key for the first value.
        key_2 : str, default="b"
            Key for the second value.

        Returns
        -------
        dict
            Dictionary with two key-value pairs.

        Examples
        --------
        >>> DataStructures.dictionary_from_values(10, 20)
        {'a': 10, 'b': 20}
        >>> DataStructures.dictionary_from_values(10, 20, key_1="x", key_2="y")
        {'x': 10, 'y': 20}
        """
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