# TODO - BLOCK START

# TODO - BLOCK END

from classification_model import ClassificationModel

class Experiment:
    """
    A class to run classification experiments using ClassificationModel.
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
        self.clf = None

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
            - 'split'             : train/test split
            - 'model'             : build (and fit if split already done)
            - 'evaluate'          : test accuracy
            - 'cross_validate'    : k-fold CV accuracy
            - 'grid_search'       : GridSearchCV (updates model)
            - 'randomized_search' : RandomizedSearchCV (updates model)

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
                # TASK#10
                pass
                # TODO - BLOCK END
                results.append((step, "Done"))

            elif step == 'model':
                model_type = params.get('model_type', None)
                model_params = params.get('model_params', None)
                if model_type is not None:
                    # TODO - BLOCK START
                    # TASK#11
                    pass
                    # TODO - BLOCK END
                else:
                    # TODO - BLOCK START
                    # TASK#12
                    pass
                    # TODO - BLOCK END
                if self.X_train is not None and self.y_train is not None:
                    # TODO - BLOCK START
                    # TASK#13
                    pass
                    # TODO - BLOCK END
                    results.append((step, "Done"))
                else:
                    results.append((step, "Error: No training data"))

            elif step == 'evaluate':
                if self.clf is None:
                    results.append((step, "Error: No model found"))
                else:
                    if self.X_test is None or self.y_test is None:
                        results.append((step, "Error: No data split performed"))
                    else:
                        # TODO - BLOCK START
                        # TASK#14
                        acc = 0.0
                        # TODO - BLOCK END
                        results.append((step, {"accuracy": acc}))

            elif step == 'cross_validate':
                if self.clf is None:
                    results.append((step, "Error: No model found"))
                else:
                    X = self.df.drop(columns=[self.target_column])
                    y = self.df[self.target_column]
                    cv = params.get('cv', None)
                    if cv is not None:
                        # TODO - BLOCK START
                        # TASK#15
                        cv_mean = 0.0
                        # TODO - BLOCK END
                    else:
                        # TODO - BLOCK START
                        # TASK#16
                        cv_mean = 0.0
                        # TODO - BLOCK END
                    results.append((step, {"cv_mean": cv_mean}))

            elif step == 'grid_search':
                if self.clf is None:
                    results.append((step, "Error: No model found"))
                else:
                    if self.X_train is None or self.y_train is None:
                        results.append((step, "Error: No data split performed"))
                    else:
                        param_grid = params['param_grid']
                        cv = params.get('cv', 5)
                        n_jobs = params.get('n_jobs', -1)
                        # TODO - BLOCK START
                        # TASK#17
                        pass
                        # TODO - BLOCK END
                        results.append((step, "Done"))

            elif step == 'randomized_search':
                if self.clf is None:
                    results.append((step, "Error: No model found"))
                else:
                    if self.X_train is None or self.y_train is None:
                        results.append((step, "Error: No data split performed"))
                    else:
                        param_dist = params['param_dist']
                        n_iter = params.get('n_iter', 100)
                        cv = params.get('cv', 5)
                        n_jobs = params.get('n_jobs', -1)
                        # TODO - BLOCK START
                        # TASK#18
                        pass
                        # TODO - BLOCK END
                        results.append((step, "Done"))

            else:
                raise ValueError(f"Unknown step: {step}")

        return results

    @staticmethod
    def example_experiment_1(df, target_column):
        """
        Example of the first experiment:
        - Split data (test_size=0.25, random_state=42, stratify=True)
        - Train Random Forest classifier with default parameters
        - Optimize hyperparameters using GridSearchCV (n_estimators=[100, 200], max_depth=[None, 5, 10], cv=5, n_jobs=-1)
        - Evaluate accuracy on test data
        - Perform 5-fold cross-validation (cv=5)
        - Optimize hyperparameters using RandomizedSearchCV (n_estimators=[50, 100, 200, 300], max_depth=[None, 5, 10, 15], min_samples_split=[2, 5, 10], n_iter=10, cv=5, n_jobs=-1)
        - Evaluate accuracy on test data
        - Perform 5-fold cross-validation (cv=5)
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
        Example of the second experiment:
        - Split data (test_size=0.2, random_state=13, stratify=True)
        - Train K-Nearest Neighbors (default parameters)
        - Optimize hyperparameters using GridSearchCV (n_neighbors=[3, 5, 7, 9], weights=['uniform', 'distance'], p=[1, 2], cv=5, n_jobs=-1)
        - Evaluate accuracy on test data
        - Perform 5-fold cross-validation (cv=5)
        - Optimize hyperparameters using RandomizedSearchCV (n_neighbors=[3..31 step 2], weights=['uniform','distance'], p=[1,2], leaf_size=[10, 20, 30, 40, 50], algorithm=['auto','ball_tree','kd_tree'], n_iter=20, cv=5, n_jobs=-1)
        - Evaluate accuracy on test data
        - Perform 5-fold cross-validation (cv=5)
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