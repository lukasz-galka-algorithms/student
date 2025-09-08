import pandas as pd
from data_cleaning import DataCleaner
from data_transformation import DataTransformer

class Experiment:
    """
    A class to run a series of data preprocessing and modeling experiments.
    """

    def __init__(self, df):
        """
        Initialize the experiment with a dataframe.

        Parameters
        ----------
        df : pd.DataFrame
            The input dataframe with data to process.
        """
        self.df = df

    def run_experiment(self, steps):
        """
        Run a series of data cleaning, transformation steps.

        Parameters
        ----------
        steps : list of tuples
            A list of steps to perform, where each tuple contains:
            - step name (str)
            - step parameters (dict)

            Example: [ ('cleaning', {'remove_duplicates': {}}),
                       ('transform', {'normalize_data': {}}) ]

        Returns
        -------
        pd.DataFrame
            The transformed dataframe after all steps have been applied.
        """
        temp_df = self.df
        for step, params in steps:
            if step == 'cleaning':
                temp_df = DataCleaner.clean_data(temp_df, params)

            elif step == 'transform':
                temp_df = DataTransformer.transform_data(temp_df, params)

            else:
                raise ValueError(f"Unknown step: {step}")

        return temp_df

    @staticmethod
    def example_experiment_1(df):
        """
        Example of the first experiment:
        - Remove duplicates
        - Impute missing values with the mean
        - Remove outliers using IQR method with threshold 1.5
        - Drop 'sepal width (cm)' columns
        """
        # TODO - BLOCK START
        # TASK#14
        steps = []
        # TODO - BLOCK END
        experiment = Experiment(df)
        return experiment.run_experiment(steps)

    @staticmethod
    def example_experiment_2(df):
        """
        Example of the second experiment:
        - Apply One-Hot Encoding
        - Remove duplicates
        - Impute missing values with the most frequent value
        - Remove outliers using IQR method with threshold 1.5
        - Standardize data
        - Apply PCA for dimensionality reduction with n_components = 2
        """
        # TODO - BLOCK START
        # TASK#15
        steps = []
        # TODO - BLOCK END
        experiment = Experiment(df)
        return experiment.run_experiment(steps)

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