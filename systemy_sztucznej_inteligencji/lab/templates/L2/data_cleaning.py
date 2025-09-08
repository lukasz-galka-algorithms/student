import pandas as pd
from sklearn.impute import SimpleImputer

class DataCleaner:
    """
    A class to handle various data cleaning tasks including:
    - Missing value imputation
    - Removing duplicates
    - Handling outliers
    - Dropping unnecessary columns
    """

    @staticmethod
    def handle_missing_values(df, strategy='mean'):
        """
        Handle missing values by imputing them using a specified strategy.

        Parameters
        ----------
        df : pd.DataFrame
            The input dataframe with missing values.
        strategy : str, default='mean'
            The imputation strategy. Options are 'mean', 'median', 'most_frequent'.

        Returns
        -------
        pd.DataFrame
            DataFrame with missing values filled.
        """
        # TODO - BLOCK START
        # TASK#2
        pass
        # TODO - BLOCK END

    @staticmethod
    def remove_duplicates(df):
        """
        Remove duplicate rows from the dataframe.

        Parameters
        ----------
        df : pd.DataFrame
            The input dataframe with potential duplicate rows.

        Returns
        -------
        pd.DataFrame
            DataFrame with duplicates removed.
        """
        # TODO - BLOCK START
        # TASK#3
        pass
        # TODO - BLOCK END

    @staticmethod
    def remove_outliers(df, method='IQR', threshold=1.5):
        """
        Remove outliers from the dataframe using a specified method.

        Parameters
        ----------
        df : pd.DataFrame
            The input dataframe with numerical data.
        method : str, default='IQR'
            The method to use for outlier detection. Options are 'IQR' (Interquartile Range).
        threshold : float, default=1.5
            The threshold for detecting outliers. For IQR, it is multiplied by the IQR.

        Returns
        -------
        pd.DataFrame
            DataFrame with outliers removed.
        """
        # TODO - BLOCK START
        # TASK#4
        pass
        # TODO - BLOCK END

    @staticmethod
    def drop_columns(df, columns):
        """
        Drop specified columns from the dataframe.

        Parameters
        ----------
        df : pd.DataFrame
            The input dataframe.
        columns : list
            List of column names to be dropped.

        Returns
        -------
        pd.DataFrame
            DataFrame with specified columns dropped.
        """
        # TODO - BLOCK START
        # TASK#5
        pass
        # TODO - BLOCK END

    @staticmethod
    def clean_data(df, steps):
        """
        Perform a series of data cleaning operations on the dataframe.

        Parameters
        ----------
        df : pd.DataFrame
            The input dataframe.
        steps : list of tuples
            A list of steps to perform, where each tuple contains:
            - step name (str)
            - step parameters (dict)

            Example: [ ('remove_duplicates', {}),
                      ('handle_missing_values', {'strategy': 'mean'}),
                      ('remove_outliers', {'method': 'IQR', 'threshold': 1.5}),
                      ('drop_columns', {'columns': ['col1', 'col2']}) ]

        Returns
        -------
        pd.DataFrame
            DataFrame after all cleaning steps have been performed.
        """
        for step, params in steps:
            if step == 'remove_duplicates':
                df = DataCleaner.remove_duplicates(df)
            elif step == 'handle_missing_values':
                strategy = params.get('strategy', 'mean')
                df = DataCleaner.handle_missing_values(df, strategy=strategy)
            elif step == 'remove_outliers':
                method = params.get('method', 'IQR')
                threshold = params.get('threshold', 1.5)
                df = DataCleaner.remove_outliers(df, method=method, threshold=threshold)
            elif step == 'drop_columns':
                columns = params.get('columns', [])
                df = DataCleaner.drop_columns(df, columns=columns)
            else:
                raise ValueError(f"Unknown step: {step}")

        return df

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