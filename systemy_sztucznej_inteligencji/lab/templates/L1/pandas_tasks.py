import pandas as pd

class PandasTasks:
    """
    A collection of methods demonstrating the use of Pandas for data manipulation.
    """

    @staticmethod
    def create_dataframe_from_lists(names, ages):
        """
        Create a Pandas DataFrame from two lists: one for names and one for ages.

        Parameters
        ----------
        names : list of str
            List of names.
        ages : list of int
            List of ages.

        Returns
        -------
        pandas.DataFrame
            A DataFrame with two columns: 'Name' and 'Age'.

        Examples
        --------
        >>> PandasTasks.create_dataframe_from_lists(['Alice', 'Bob'], [24, 30])
        Name   Age
        0  Alice   24
        1    Bob   30
        """
        # TODO - BLOCK START
        # TASK#13
        pass
        # TODO - BLOCK END

    @staticmethod
    def filter_by_age(df, age_limit):
        """
        Filter rows in a DataFrame where the age is greater than the given age limit.

        Parameters
        ----------
        df : pandas.DataFrame
            Input DataFrame with 'Age' column.
        age_limit : int
            The minimum age for the filter.

        Returns
        -------
        pandas.DataFrame
            A DataFrame with only the rows where 'Age' > age_limit.

        Examples
        --------
        >>> df = PandasTasks.create_dataframe_from_lists(['Alice', 'Bob'], [24, 30])
        >>> PandasTasks.filter_by_age(df, 25)
        Name   Age
        1  Bob   30
        """
        # TODO - BLOCK START
        # TASK#14
        pass
        # TODO - BLOCK END

    @staticmethod
    def group_by_age(df):
        """
        Group the DataFrame by the 'Age' column and return the grouped data.

        Parameters
        ----------
        df : pandas.DataFrame
            Input DataFrame with 'Age' column.

        Returns
        -------
        pandas.core.groupby.generic.DataFrameGroupBy
            A GroupBy object, where you can perform aggregation on the grouped data.

        Examples
        --------
        >>> df = PandasTasks.create_dataframe_from_lists(['Alice', 'Bob', 'Charlie'], [24, 30, 30])
        >>> grouped = PandasTasks.group_by_age(df)
        >>> grouped.size()
        Age
        24    1
        30    2
        dtype: int64
        """
        # TODO - BLOCK START
        # TASK#15
        pass
        # TODO - BLOCK END

    @staticmethod
    def calculate_average_age(df):
        """
        Calculate the average age from the 'Age' column.

        Parameters
        ----------
        df : pandas.DataFrame
            Input DataFrame with 'Age' column.

        Returns
        -------
        float
            The average age.

        Examples
        --------
        >>> df = PandasTasks.create_dataframe_from_lists(['Alice', 'Bob'], [24, 30])
        >>> PandasTasks.calculate_average_age(df)
        27.0
        """
        # TODO - BLOCK START
        # TASK#16
        pass
        # TODO - BLOCK END

    @staticmethod
    def sort_by_name(df):
        """
        Sort the DataFrame by the 'Name' column in ascending order.

        Parameters
        ----------
        df : pandas.DataFrame
            Input DataFrame with 'Name' column.

        Returns
        -------
        pandas.DataFrame
            The DataFrame sorted by 'Name'.

        Examples
        --------
        >>> df = PandasTasks.create_dataframe_from_lists(['Alice', 'Bob'], [24, 30])
        >>> PandasTasks.sort_by_name(df)
        Name   Age
        0  Alice   24
        1    Bob   30
        """
        # TODO - BLOCK START
        # TASK#17
        pass
        # TODO - BLOCK END

    @staticmethod
    def get_top_n_ages(df, n=5):
        """
        Get the top 'n' oldest individuals from the DataFrame.

        Parameters
        ----------
        df : pandas.DataFrame
            Input DataFrame with 'Age' column.
        n : int, default=5
            The number of top individuals to return.

        Returns
        -------
        pandas.DataFrame
            A DataFrame containing the top 'n' oldest individuals.

        Examples
        --------
        >>> df = PandasTasks.create_dataframe_from_lists(['Alice', 'Bob', 'Charlie'], [24, 30, 35])
        >>> PandasTasks.get_top_n_ages(df, 2)
        Name   Age
        2  Charlie   35
        1    Bob   30
        """
        # TODO - BLOCK START
        # TASK#18
        pass
        # TODO - BLOCK END

    @staticmethod
    def add_new_column(df, column_name, values):
        """
        Add a new column to the DataFrame.

        Parameters
        ----------
        df : pandas.DataFrame
            Input DataFrame.
        column_name : str
            The name of the new column.
        values : list
            A list of values to populate the new column.

        Returns
        -------
        pandas.DataFrame
            The updated DataFrame with the new column.

        Examples
        --------
        >>> df = PandasTasks.create_dataframe_from_lists(['Alice', 'Bob'], [24, 30])
        >>> PandasTasks.add_new_column(df, 'Gender', ['F', 'M'])
        Name   Age Gender
        0  Alice   24      F
        1    Bob   30      M
        """
        # TODO - BLOCK START
        # TASK#19
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