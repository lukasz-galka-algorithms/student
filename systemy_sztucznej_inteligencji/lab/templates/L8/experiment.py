# TODO - BLOCK START

# TODO - BLOCK END

from model_factory import ModelFactory
from classification_metrics import ClassificationMetrics
from threshold_determination import ThresholdDetermination

class Experiment:
    """
    A class to run classification experiments.
    """

    def __init__(self, df, target_column):
        """
        Initialize the experiment with a dataframe and target column.

        Parameters
        ----------
        df : pd.DataFrame
            Input data containing features and target.
        target_column : str
            Name of the target column.
        """
        self.df = df
        self.target_column = target_column
        self.X_train = self.X_test = None
        self.y_train = self.y_test = None
        self.model = None

    def run_experiment(self, steps):
        """
        Run a series of classification steps.

        Parameters
        ----------
        steps : list of tuples
            A list of steps to perform, where each tuple contains:
            - step name (str)
            - step parameters (dict)

            Supported steps:
            - 'split'                   : train/test split
            - 'model'                   : build (and fit if split already done)
            - 'run_confusion_matrix'    : confusion matrix analysis
            - 'run_metrics_analysis'    : base metrics analysis
            - 'run_threshold_analysis'  : optimal thresholds determination
            - 'run_advanced_metrics_analysis' : advanced metrics analysis

        Returns
        -------
        list[tuple[str, any]]
            Sequence of (step_name, result/info).
        """
        results = []
        for step, params in steps:
            if step == 'split':
                X = self.df.drop(columns=[self.target_column])
                y = self.df[self.target_column]
                test_size = params.get('test_size', 0.2)
                random_state = params.get('random_state', 42)
                strat = y if params.get('stratify', True) else None

                # TODO - BLOCK START
                # TASK#12
                pass
                # TODO - BLOCK END
                results.append((step, "Done"))

            elif step == 'model':
                model_type = params.get('model_type', None)
                model_params = params.get('model_params', None)
                if model_type is not None:
                    # TODO - BLOCK START
                    # TASK#13
                    pass
                    # TODO - BLOCK END
                else:
                    # TODO - BLOCK START
                    # TASK#14
                    pass
                    # TODO - BLOCK END
                if self.X_train is not None and self.y_train is not None:
                    self.clf.fit(self.X_train, self.y_train)
                    results.append((step, "Done"))
                else:
                    results.append((step, "Error: No training data"))

            elif step == 'run_confusion_matrix':
                if self.clf is None or self.X_test is None:
                    results.append((step, "Error: Model not trained or data not split."))
                else:
                    # TODO - BLOCK START
                    # TASK#15
                    confusion_matrix = None
                    # TODO - BLOCK END
                    results.append((step, {"confusion_matrix": confusion_matrix}))

            elif step == 'run_metrics_analysis':
                if self.clf is None or self.X_test is None:
                    results.append((step, "Error: Model not trained or data not split."))
                else:
                    # TODO - BLOCK START
                    # TASK#16
                    accuracy = None
                    precision = None
                    recall = None
                    f1 = None
                    # TODO - BLOCK END
                    results.append((step, {"accuracy": accuracy, "precision": precision, "recall": recall, "f1_score": f1}))

            elif step == 'run_threshold_analysis':
                if self.clf is None or not hasattr(self.clf, "predict_proba"):
                    results.append((step, "Error: Model does not support 'predict_proba', cannot perform threshold analysis."))
                else:
                    # TODO - BLOCK START
                    # TASK#17
                    threshold_min_dist = None
                    threshold_max_youden = None
                    # TODO - BLOCK END
                    results.append((step, {"min_dist_threshold": threshold_min_dist,
                                           "max_youden_threshold": threshold_max_youden}))

            elif step == 'run_advanced_metrics_analysis':
                if self.clf is None or not hasattr(self.clf, "predict_proba"):
                    results.append((step, "Error: Model does not support 'predict_proba', cannot perform advanced analysis."))
                else:
                    # TODO - BLOCK START
                    # TASK#18
                    roc_auc = None
                    pr_auc = None
                    # TODO - BLOCK END
                    results.append((step, {"roc_auc": roc_auc, "pr_auc": pr_auc}))
            else:
                raise ValueError(f"Unknown step: {step}")

        return results

    @staticmethod
    def example_experiment_1(df, target_column):
        """
        Example of an advanced metrics experiment:
        - Data split (test_size=0.3, random_state=13, stratify=True)
        - Train SVM classifier with model_params (probability=True)
        - Run threshold analysis
        - Run advanced metrics analysis
        """
        # TODO - BLOCK START
        # TASK#19
        steps = []
        # TODO - BLOCK END
        experiment = Experiment(df, target_column)
        return experiment.run_experiment(steps)

    @staticmethod
    def example_experiment_2(df, target_column):
        """
        Example of a basic metrics and confusion matrix experiment:
        - Data split with default parameters
        - Train RandomForestClassifier with default parameters
        - Run basic metrics analysis
        - Run confusion matrix analysis
        """
        # TODO - BLOCK START
        # TASK#20
        steps = []
        # TODO - BLOCK END
        experiment = Experiment(df, target_column)
        return experiment.run_experiment(steps)

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