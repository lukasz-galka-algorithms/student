# TODO - BLOCK START

# TODO - BLOCK END

class ModelFactory:
    """
    A factory class to create machine learning models from sklearn library.
    """

    @staticmethod
    def create_model(model_type = "linear_regression",
                     model_params = None):
        """
        Create and return a model based on the specified type.

        Parameters
        ----------
        model_type : str, default='linear_regression'
            The type of model to create. Options are:
            - 'linear_regression'  : Linear Regression
            - 'random_forest'      : Random Forest Regressor
            - 'svm_regressor'      : Support Vector Machine (SVR)
            - 'knn_regressor'      : K-Nearest Neighbors Regressor
        model_params : dict, optional
            Parameters passed to the model constructor.

        Returns
        -------
        model : sklearn estimator
            The created machine learning model.
        """
        params = model_params or {}

        # TODO - BLOCK START
        # TASK#2
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