from sklearn.cluster import KMeans

class ClusterStrategy:
    """
    Multiway split based on k-means clustering.
    """

    def __init__(self, n_clusters=2, random_state=0):
        """
        Initialize the clustering-based split strategy.

        Parameters
        ----------
        n_clusters : int, default=2
        Number of clusters (child nodes) to form.
        random_state : int, RandomState instance or None, default=0
        Controls the randomness of KMeans.
        """
        self._n_clusters = int(n_clusters)
        self._kmeans = None
        self._random_state = random_state

    def fit(self, X, y=None):
        """
        Learn cluster centroids on the node's data (labels are ignored).

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
        Feature matrix for samples at the node.
        y : array-like of shape (n_samples,), optional
        Unused; present for API compatibility with supervised strategies.

        Returns
        -------
        None
        """
        # TODO - BLOCK START
        # TASK#3
        pass
        # TODO - BLOCK END

    def get_nodes_number(self):
        """
        Number of child nodes produced by this strategy.

        Returns
        -------
        int
        `n_clusters` if fitted, else 0.
        """
        # TODO - BLOCK START
        # TASK#4
        pass
        # TODO - BLOCK END

    def predict(self, X):
        """
        Route samples to child indices using the trained KMeans model.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
        Samples to assign to clusters.

        Returns
        -------
        ndarray of shape (n_samples,)
        Cluster labels in the range [0, n_clusters-1].

        Raises
        ------
        ValueError
        If called before `fit`.
        """
        if self._kmeans is None:
            raise ValueError("Split strategy has not been fitted.")
        return self._kmeans.predict(X)

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