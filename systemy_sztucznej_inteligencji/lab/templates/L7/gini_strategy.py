import numpy as np

class GiniStrategy:
    """
    Binary split that minimizes class impurity using the Gini criterion.
    """

    def __init__(self):
        """
        Initialize an unfitted Gini-based split strategy.
        """
        self._best_feature = None
        self._best_threshold = None

    def fit(self, X, y):
        """
        Find the best (feature, threshold) for a binary split using Gini impurity.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
        Node samples.
        y : array-like of shape (n_samples,)
        Class labels for the samples.

        Returns
        -------
        None
        """

        n_samples, n_features = X.shape
        best_gini = float('inf')

        # TODO - BLOCK START
        # TASK#2
        pass
        # TODO - BLOCK END

    def get_nodes_number(self):
        """
        Number of children produced by the best split.

        Returns
        -------
        int
        2 if a valid split was found in `fit`, otherwise 0.
        """
        return 2 if self._best_feature is not None else 0

    def predict(self, X):
        """
        Route samples to left (0) or right (1) child according to the split.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
        Samples to route.

        Returns
        -------
        ndarray of shape (n_samples,)
        0 for samples where feature <= threshold, 1 otherwise.

        Raises
        ------
        ValueError
        If called before `fit`.
        """
        if self._best_feature is None:
            raise ValueError("Split strategy has not been fitted.")
        return (X[:, self._best_feature] > self._best_threshold).astype(int)

    def _calculate_gini(self, left_y, right_y):
        """
        Compute weighted Gini impurity of the two partitions.

        Parameters
        ----------
        left_y : array-like of shape (n_left,)
        Labels of the left partition.
        right_y : array-like of shape (n_right,)
        Labels of the right partition.

        Returns
        -------
        float
        Weighted Gini impurity: (n_left/N)*Gini(left) + (n_right/N)*Gini(right).
        """
        n_left = len(left_y)
        n_right = len(right_y)
        n_total = n_left + n_right

        def gpart(y):
            if len(y) == 0:
                return 0.0
            classes, counts = np.unique(y, return_counts=True)
            p = counts / counts.sum()
            return 1.0 - np.sum(p ** 2)

        return (n_left / n_total) * gpart(left_y) + (n_right / n_total) * gpart(right_y)

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