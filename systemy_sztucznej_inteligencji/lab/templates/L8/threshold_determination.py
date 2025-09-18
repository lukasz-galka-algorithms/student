# TODO - BLOCK START

# TODO - BLOCK END

class ThresholdDetermination:
    """
    A class for finding optimal classification thresholds based on the ROC curve.
    """

    @staticmethod
    def find_min_distance_threshold(y_true, y_score, pos_label=1):
        """
        Finds the optimal threshold with the minimum Euclidean distance to the ideal point (0, 1) on the ROC curve.

        This point represents a perfect classifier with a False Positive Rate of 0 and a True Positive Rate of 1.

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
            The optimal threshold value.
        """
        # TODO - BLOCK START
        # TASK#10
        pass
        # TODO - BLOCK END

    @staticmethod
    def find_max_youden_threshold(y_true, y_score, pos_label=1):
        """
        Finds the optimal threshold that maximizes the distance from the random detection line (y = x).

        This is equivalent to maximizing the difference between TPR and FPR, often known as the Youden's J statistic.

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
            The optimal threshold value.
        """
        # TODO - BLOCK START
        # TASK#11
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