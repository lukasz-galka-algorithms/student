# TODO - BLOCK START

# TODO - BLOCK END


class ModelFactoryForAnomaly:
    """
    A factory class to create anomaly detection models from scikit-learn.

    Supported model types
    ---------------------
    - 'isolation_forest'   : sklearn.ensemble.IsolationForest
    - 'one_class_svm'      : sklearn.svm.OneClassSVM
    - 'lof'                : sklearn.neighbors.LocalOutlierFactor
                             (created with novelty=True by default to allow predict on new data)
    - 'elliptic_envelope'  : sklearn.covariance.EllipticEnvelope
    """

    @staticmethod
    def create_model(model_type: str = "isolation_forest",
                     model_params: dict | None = None):
        """
        Create and return an anomaly detector based on the specified type.

        Parameters
        ----------
        model_type : str, default='isolation_forest'
            The type of anomaly detector to create. Options are:
            - 'isolation_forest'   : IsolationForest
            - 'one_class_svm'      : OneClassSVM
            - 'lof'                : LocalOutlierFactor (with novelty=True by default)
            - 'elliptic_envelope'  : EllipticEnvelope
        model_params : dict, optional
            Parameters passed to the underlying sklearn estimator constructor.

        Returns
        -------
        sklearn estimator
            The created anomaly detection model.
        """
        params = dict(model_params or {})

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