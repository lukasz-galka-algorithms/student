# TODO - BLOCK START

# TODO - BLOCK END

class ClassificationMetrics:
    """
    A class containing static methods for calculating various classification metrics.
    """

    @staticmethod
    def accuracy(y_true, y_pred):
        """
        Calculates the accuracy score.

        Accuracy is the proportion of correctly classified instances.

        Parameters
        ----------
        y_true : np.ndarray
            True labels.
        y_pred : np.ndarray
            Predicted labels.

        Returns
        -------
        float
            The accuracy score.
        """
        # TODO - BLOCK START
        # TASK#3
        pass
        # TODO - BLOCK END

    @staticmethod
    def precision(y_true, y_pred, average='binary', pos_label=1):
        """
        Calculates the precision score.

        Precision is the ratio of correctly predicted positive observations
        to the total predicted positive observations.

        Parameters
        ----------
        y_true : np.ndarray
            True labels.
        y_pred : np.ndarray
            Predicted labels.
        average : str, default='binary'
            This parameter is required for multi-class and multi-label targets.
            'binary': Only reports results for the class specified by pos_label.
            'macro': Calculate metrics for each label, and find their unweighted mean.
                     This does not take label imbalance into account.
        pos_label : int or str, default=1
            The label of the positive class. Used only when average='binary'.

        Returns
        -------
        float or np.ndarray
            The precision score.
        """
        # TODO - BLOCK START
        # TASK#4
        pass
        # TODO - BLOCK END

    @staticmethod
    def recall(y_true, y_pred, average='binary', pos_label=1):
        """
        Calculates the recall score.

        Recall is the ratio of correctly predicted positive observations
        to the all observations in the actual class.

        Parameters
        ----------
        y_true : np.ndarray
            True labels.
        y_pred : np.ndarray
            Predicted labels.
        average : str, default='binary'
            This parameter is required for multi-class and multi-label targets.
            'binary': Only reports results for the class specified by pos_label.
            'macro': Calculate metrics for each label, and find their unweighted mean.
                     This does not take label imbalance into account.
        pos_label : int or str, default=1
            The label of the positive class. Used only when average='binary'.

        Returns
        -------
        float or np.ndarray
            The recall score.
        """
        # TODO - BLOCK START
        # TASK#5
        pass
        # TODO - BLOCK END

    @staticmethod
    def f1_score(y_true, y_pred, average='binary', pos_label=1):
        """
        Calculates the F1 score.

        The F1 score is the weighted average of Precision and Recall.

        Parameters
        ----------
        y_true : np.ndarray
            True labels.
        y_pred : np.ndarray
            Predicted labels.
        average : str, default='binary'
            This parameter is required for multi-class and multi-label targets.
            'binary': Only reports results for the class specified by pos_label.
            'macro': Calculate metrics for each label, and find their unweighted mean.
                     This does not take label imbalance into account.
        pos_label : int or str, default=1
            The label of the positive class. Used only when average='binary'.

        Returns
        -------
        float or np.ndarray
            The F1 score.
        """
        # TODO - BLOCK START
        # TASK#6
        pass
        # TODO - BLOCK END

    @staticmethod
    def confusion_matrix(y_true, y_pred):
        """
        Computes the confusion matrix.

        A confusion matrix is a table that is often used to describe the
        performance of a classification model on a set of test data for which
        the true values are known.

        Parameters
        ----------
        y_true : np.ndarray
            True labels.
        y_pred : np.ndarray
            Predicted labels.

        Returns
        -------
        np.ndarray
            The confusion matrix.
        """
        # TODO - BLOCK START
        # TASK#7
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
        # TASK#8
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