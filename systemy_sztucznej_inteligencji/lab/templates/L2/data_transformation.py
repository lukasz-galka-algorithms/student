import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler, PowerTransformer, RobustScaler
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

class DataTransformer:
    """
    A class for performing various data transformations such as:
    - Normalization
    - Standardization
    - Log transformation
    - Power transformation
    - Robust scaling
    - PCA (Principal Component Analysis)
    - Encoding categorical variables
    - Feature selection and extraction
    """

    NUMERIC_COLUMNS = ['number', 'float64', 'int64', 'int32', 'float32']

    @staticmethod
    def normalize_data(df):
        """
        Normalize the numerical data using Min-Max normalization.

        Parameters
        ----------
        df : pd.DataFrame
            The input dataframe with numerical data.

        Returns
        -------
        pd.DataFrame
            DataFrame with normalized values in the range [0, 1].
        """
        # TODO - BLOCK START
        # TASK#6
        pass
        # TODO - BLOCK END

    @staticmethod
    def standardize_data(df):
        """
        Standardize the numerical data using z-score standardization.

        Parameters
        ----------
        df : pd.DataFrame
            The input dataframe with numerical data.

        Returns
        -------
        pd.DataFrame
            DataFrame with standardized values (mean=0, std=1).
        """
        # TODO - BLOCK START
        # TASK#7
        pass
        # TODO - BLOCK END

    @staticmethod
    def log_transform(df):
        """
        Apply a logarithmic transformation to the numerical data.

        Parameters
        ----------
        df : pd.DataFrame
            The input dataframe with numerical data.

        Returns
        -------
        pd.DataFrame
            DataFrame with logarithmic transformation applied (log(x + 1) to handle 0 values).
        """
        # TODO - BLOCK START
        # TASK#8
        pass
        # TODO - BLOCK END

    @staticmethod
    def power_transform(df):
        """
        Apply a power transformation to the numerical data to make the data more Gaussian-like.

        Parameters
        ----------
        df : pd.DataFrame
            The input dataframe with numerical data.

        Returns
        -------
        pd.DataFrame
            DataFrame with power transformation applied.
        """
        # TODO - BLOCK START
        # TASK#9
        pass
        # TODO - BLOCK END

    @staticmethod
    def robust_scale_data(df):
        """
        Scale the data using Robust Scaling, which is less sensitive to outliers.

        Parameters
        ----------
        df : pd.DataFrame
            The input dataframe with numerical data.

        Returns
        -------
        pd.DataFrame
            DataFrame with robust scaling applied.
        """
        # TODO - BLOCK START
        # TASK#10
        pass
        # TODO - BLOCK END

    @staticmethod
    def apply_pca(df, n_components=2):
        """
        Apply PCA (Principal Component Analysis) for dimensionality reduction.

        Parameters
        ----------
        df : pd.DataFrame
            The input dataframe with numerical data.
        n_components : int, optional
            The number of components to reduce to, by default 2.

        Returns
        -------
        pd.DataFrame
            DataFrame with reduced dimensions.
        """
        # TODO - BLOCK START
        # TASK#11
        pass
        # TODO - BLOCK END

    @staticmethod
    def encode_categorical_data(df, method='label_encoding'):
        """
        Encode categorical variables using a specified encoding method.

        Parameters
        ----------
        df : pd.DataFrame
            The input dataframe containing categorical data.
        method : str, default='label_encoding'
            The encoding method to use. Options are:
            - 'label_encoding': Converts each category to a number.
            - 'one_hot_encoding': Creates binary columns for each category represented by dense matrix.

        Returns
        -------
        pd.DataFrame
            DataFrame with encoded categorical variables.
        """
        # TODO - BLOCK START
        # TASK#12
        pass
        # TODO - BLOCK END

    @staticmethod
    def select_important_features(df, target_column, method='correlation', threshold=0.1):
        """
        Select important features using correlation or mutual information methods.

        Parameters
        ----------
        df : pd.DataFrame
            The input dataframe.
        target_column : str
            The column name of the target variable.
        method : str, default='correlation'
            The method for feature selection. Options are 'correlation' or 'mutual_information'.
        threshold : float, default=0.1
            The threshold for selecting important features.

        Returns
        -------
        pd.DataFrame
            DataFrame with selected features.
        """
        # TODO - BLOCK START
        # TASK#13
        pass
        # TODO - BLOCK END

    @staticmethod
    def transform_data(df, steps):
        """
        Perform a series of transformations on the dataframe based on the specified steps.

        Parameters
        ----------
        df : pd.DataFrame
            The input dataframe with numerical or categorical data.
        steps : list of tuples
            A list of tuples where each tuple contains:
            - step name (str)
            - step parameters (dict)

            Example: [ ('normalize_data', {}),
                      ('standardize_data', {}),
                      ('log_transform', {}),
                      ('apply_pca', {'n_components': 2}) ]

        Returns
        -------
        pd.DataFrame
            DataFrame after all transformations have been applied.
        """
        for step, params in steps:
            if step == 'normalize_data':
                df = DataTransformer.normalize_data(df)
            elif step == 'standardize_data':
                df = DataTransformer.standardize_data(df)
            elif step == 'log_transform':
                df = DataTransformer.log_transform(df)
            elif step == 'power_transform':
                df = DataTransformer.power_transform(df)
            elif step == 'robust_scale_data':
                df = DataTransformer.robust_scale_data(df)
            elif step == 'apply_pca':
                n_components = params.get('n_components', 2)
                df = DataTransformer.apply_pca(df, n_components=n_components)
            elif step == 'encode_categorical_data':
                method = params.get('method', 'label_encoding')
                df = DataTransformer.encode_categorical_data(df, method=method)
            elif step == 'select_important_features':
                target_column = params.get('target_column')
                method = params.get('method', 'correlation')
                threshold = params.get('threshold', 0.1)
                df = DataTransformer.select_important_features(df, target_column, method, threshold)
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