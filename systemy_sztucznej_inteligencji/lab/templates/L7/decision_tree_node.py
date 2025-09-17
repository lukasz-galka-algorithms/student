import numpy as np

from strategy_factory import StrategyFactory

class CustomDecisionTreeNode:
    """
    Recursive node for the custom decision tree.

    Each node owns a split strategy (unless it is a leaf), a mapping of
    child index -> child node, and optionally a `value` for leaf prediction.
    """

    def __init__(self, split_strategy="gini", model_params=None):
        """
        Initialize a decision tree node.

        Parameters
        ----------
        split_strategy : {"gini", "clustering"}, default="gini"
        Strategy name used to split at this node (when not a leaf).
        model_params : dict or None, default=None
        Parameters passed to the strategy constructor.
        """
        self.split_strategy = split_strategy
        self.model_params = model_params or {}
        self.strategy = StrategyFactory.create_strategy(split_strategy, self.model_params)
        self.children = {}
        self.value = None

    def _majority(self, y):
        """
        Compute the majority class label in `y`.

        Parameters
        ----------
        y : array-like of shape (n_samples,)
        Labels at the current node.

        Returns
        -------
        hashable
        Most frequent label (ties broken by `np.argmax`).
        """
        vals, counts = np.unique(y, return_counts=True)
        return vals[np.argmax(counts)]

    def fit(self, X, y, max_depth=None, depth=0, min_samples_split=2):
        """
        Grow the subtree rooted at this node.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
        Samples at this node.
        y : array-like of shape (n_samples,)
        Labels at this node.
        max_depth : int or None, default=None
        Maximum depth of the tree. If None, unlimited.
        depth : int, default=0
        Current recursion depth (managed internally).
        min_samples_split : int, default=2
        Minimum number of samples required to attempt a split.

        Returns
        -------
        None
        The node mutates into a leaf or internal node with children.
        """
        if (max_depth is not None and depth >= max_depth) or len(np.unique(y)) <= 1 or len(y) < min_samples_split:
            self.value = self._majority(y)
            self.strategy = None
            self.children = {}
            return

        self.strategy.fit(X, y)
        k = self.strategy.get_nodes_number()
        if k < 2:
            self.value = self._majority(y)
            self.strategy = None
            self.children = {}
            return

        labels = self.strategy.predict(X)

        for child_idx in range(k):
            if np.sum(labels == child_idx) == 0:
                self.value = self._majority(y)
                self.strategy = None
                self.children = {}
                return

        for child_idx in range(k):
            # TODO - BLOCK START
            # TASK#6
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