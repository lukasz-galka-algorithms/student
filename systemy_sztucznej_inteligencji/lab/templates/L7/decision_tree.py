import numpy as np

from decision_tree_node import CustomDecisionTreeNode

class CustomDecisionTree:
    """
    A minimal decision tree using pluggable split strategies.

    The tree grows recursively until a stopping criterion is met and then
    stores the majority class in a leaf. Prediction routes samples through
    learned splits to reach a leaf and returns its label.
    """

    def __init__(self, max_depth=None, split_strategy="gini", strategy_params=None, min_samples_split=2):
        """
        Initialize the custom decision tree.

        Parameters
        ----------
        max_depth : int or None, default=None
        Maximum tree depth. If None, unlimited.
        split_strategy : {"gini", "clustering"}, default="gini"
        Strategy name used at each internal node.
        strategy_params : dict or None, default=None
        Parameters passed to strategy constructors.
        min_samples_split : int, default=2
        Minimum number of samples required to attempt a split.
        """
        self._max_depth = max_depth
        self._split_strategy = split_strategy
        self._strategy_params = strategy_params or {}
        self._min_samples_split = min_samples_split
        self._root = None

    def fit(self, X, y):
        """
        Train the decision tree on the given dataset.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
        Training features.
        y : array-like of shape (n_samples,)
        Training labels.

        Returns
        -------
        None
        """
        # TODO - BLOCK START
        # TASK#7
        pass
        # TODO - BLOCK END

    def _predict_batch(self, X, node):
        """
        Recursively predict labels for a batch of samples from a given node.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
        Samples to classify.
        node : CustomDecisionTreeNode
        Current node to route samples through.

        Returns
        -------
        ndarray of shape (n_samples,)
        Predicted labels for each sample in `X`.
        """
        # TODO - BLOCK START
        # TASK#8
        pass
        # TODO - BLOCK END

    def predict(self, X):
        """
        Predict class labels for the input samples.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
        Samples to classify.

        Returns
        -------
        ndarray of shape (n_samples,)
        Predicted labels.
        """
        return self._predict_batch(np.asarray(X), self._root)

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