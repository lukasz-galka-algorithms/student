# TODO - BLOCK START

# TODO - BLOCK END

class AnomalyDetectionMetrics:
    """
    A class containing static methods for calculating various anomaly detection classification metrics.
    """

    @staticmethod
    def f1_score(y_true, y_pred, pos_label=1):
        """
        Calculates the F1 score.

        The F1 score is the weighted average of Precision and Recall.

        Parameters
        ----------
        y_true : np.ndarray
            True labels.
        y_pred : np.ndarray
            Predicted labels.
        pos_label : int or str, default=1
            The label of the positive class.

        Returns
        -------
        float or np.ndarray
            The F1 score.
        """
        # TODO - BLOCK START
        # TASK#3
        pass
        # TODO - BLOCK END

    @staticmethod
    def roc_auc_score(y_true, y_score, pos_label=1):
        """
        Calculates the Area Under the Receiver Operating Characteristic Curve (ROC AUC).

        This metric is used for binary classification problems. It calculates
        the area under the curve that plots the True Positive Rate (TPR)
        against the False Positive Rate (FPR) at various threshold settings.

        Parameters
        ----------
        y_true : np.ndarray
            True labels.
        y_score : np.ndarray
            Target scores for the positive class, typically probability estimates.
            This should be a 1D array.
        pos_label : int or str, default=1
            The label of the positive class.

        Returns
        -------
        float
            The ROC AUC score.
        """
        # TODO - BLOCK START
        # TASK#4
        pass
        # TODO - BLOCK END

    @staticmethod
    def pr_auc_score(y_true, y_score, pos_label=1):
        """
        Calculates the Area Under the Precision-Recall Curve (PR AUC).

        This metric is especially useful for binary classification problems with
        imbalanced datasets, as it focuses on the performance of the positive class.
        The score is the area under the curve that plots Precision against Recall.

        Parameters
        ----------
        y_true : np.ndarray
            True labels.
        y_score : np.ndarray
            Target scores for the positive class, typically probability estimates.
            This should be a 1D array.
        pos_label : int or str, default=1
            The label of the positive class.

        Returns
        -------
        float
            The PR AUC score.
        """
        # TODO - BLOCK START
        # TASK#5
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