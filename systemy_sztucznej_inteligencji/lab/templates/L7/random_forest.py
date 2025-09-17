import numpy as np
from decision_tree import CustomDecisionTree

class CustomRandomForest:
    """
    Minimal random forest built from `CustomDecisionTree` base learners.

    Each tree is trained on a (possibly bootstrapped) subsample of the
    training set. Final predictions are obtained by majority voting across
    the ensemble.
    """

    def __init__(self, n_estimators=100, samples_per_tree=None, split_strategy="gini", strategy_params=None,
                 max_depth=None, min_samples_split=2):
        """
        Initialize the random forest ensemble.

        Parameters
        ----------
        n_estimators : int, default=100
        Number of trees in the forest.
        samples_per_tree : int or None, default=None
        Number of samples to draw per tree. If None, use all samples.
        split_strategy : {"gini", "clustering"}, default="gini"
        Strategy name for all trees.
        strategy_params : dict or None, default=None
        Parameters passed to the split strategy constructor.
        max_depth : int or None, default=None
        Maximum depth of each tree.
        min_samples_split : int, default=2
        Minimum number of samples required to attempt a split.
        """
        self.n_estimators = int(n_estimators)
        self.samples_per_tree = samples_per_tree
        self.split_strategy = split_strategy
        self.strategy_params = strategy_params or {}
        self.max_depth = max_depth
        self.min_samples_split = int(min_samples_split)
        self.trees = []

    def fit(self, X, y):
        """
        Train the forest by fitting each tree on a (sub)sample of the data.

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
        X = np.asarray(X)
        y = np.asarray(y)
        n, _ = X.shape
        self.trees = []

        # TODO - BLOCK START
        # TASK#9
        pass
        # TODO - BLOCK END

    def predict(self, X):
        """
        Predict class labels by majority vote across trees.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
        Samples to classify.

        Returns
        -------
        ndarray of shape (n_samples,)
        Predicted labels from the ensemble.
        """
        X = np.asarray(X)
        votes = np.vstack([t.predict(X) for t in self.trees])
        N = X.shape[0]
        out = np.empty(N, dtype=votes.dtype)
        for i in range(N):
            counts = np.bincount(votes[:, i])
            out[i] = np.argmax(counts)
        return out

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