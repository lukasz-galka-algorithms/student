# TODO - BLOCK START

# TODO - BLOCK END

from model_factory import ModelFactory

class RegressionModel:
    """
    A class for handling the regression task.
    """

    def __init__(self, model_type="random_forest", model_params=None):
        """
        Initialize the regression model using ModelFactory.
        """
        # TODO - BLOCK START
        # TASK#3
        pass
        # TODO - BLOCK END

    def get_model_params(self, deep = True):
        """
        Return model parameters.

        Parameters
        ----------
        deep : bool, default=True
            If True, also include params of nested estimators.

        Returns
        -------
        dict
            Dictionary of model parameters.
        """
        return self.model.get_params(deep=deep)

    def fit(self, X_train, y_train):
        """Fit the model to the training data."""
        # TODO - BLOCK START
        # TASK#4
        pass
        # TODO - BLOCK END

    def predict(self, X_test):
        """Predict values for the test data."""
        # TODO - BLOCK START
        # TASK#5
        pass
        # TODO - BLOCK END

    def evaluate_performance(self, X_test, y_test):
        """
        Evaluate the performance of the model using Mean Squared Error and R-squared.

        Returns
        -------
        dict
            Dictionary with MSE and R-squared scores.
        """
        # TODO - BLOCK START
        # TASK#6
        mse = 0.0
        r2 = 0.0
        # TODO - BLOCK END
        return {"mse": mse, "r2": r2}

    def cross_validate(self, X, y, cv=5):
        """
        Perform cross-validation to evaluate model performance.

        Returns
        -------
        dict
            Mean MSE and R-squared across folds.
        """
        # TODO - BLOCK START
        # TASK#7
        mean_neg_mse = 0.0
        mean_r2 = 0.0
        # TODO - BLOCK END
        return {"mean_neg_mse": mean_neg_mse, "mean_r2": mean_r2}

    def grid_search(self, X_train, y_train, param_grid, cv=5, n_jobs=-1):
        """
        Perform Grid Search for hyperparameter tuning.

        Parameters
        ----------
        X_train : array-like
            Training features.
        y_train : array-like
            Training values.
        param_grid : dict
            Dictionary of parameters with lists of values to try.
        cv : int, default=5
            Number of cross-validation folds.
        n_jobs : int, default=-1
            Number of CPU cores to use (-1 = all cores).

        Side effects
        ------------
        Updates self.model to the best estimator found, based on the 'neg_mean_squared_error' metric.
        """
        # TODO - BLOCK START
        # TASK#8
        pass
        # TODO - BLOCK END

    def randomized_search(self, X_train, y_train, param_dist, n_iter=100, cv=5, n_jobs=-1):
        """
        Perform Randomized Search for hyperparameter tuning.

        Parameters
        ----------
        X_train : array-like
            Training features.
        y_train : array-like
            Training values.
        param_dist : dict
            Dictionary with parameters and their possible values or distributions.
        n_iter : int, default=100
            Number of random parameter settings sampled.
        cv : int, default=5
            Number of cross-validation folds.
        n_jobs : int, default=-1
            Number of CPU cores to use (-1 = all cores).

        Side effects
        ------------
        Updates self.model to the best estimator found, based on the 'neg_mean_squared_error' metric.
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