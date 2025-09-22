# TODO - BLOCK START

# TODO - BLOCK END

from model_factory import ModelFactoryForAnomaly
from anomaly_detection_metrics import AnomalyDetectionMetrics

class Experiment:
    """
    A class to run anomaly detection experiments.
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

    @staticmethod
    def _compute_anomaly_scores(estimator, X):
        """
        Compute anomaly scores where higher = more anomalous.

        Strategy
        --------
        - If estimator has decision_function(X): scores = -decision_function(X)
        - elif has score_samples(X):            scores = -score_samples(X)
        - elif has predict(X):                  scores = 1 for predicted anomalies (-1), else 0
        - else:                                 zeros (fallback)
        """
        if hasattr(estimator, "decision_function"):
            raw = np.asarray(estimator.decision_function(X)).ravel()
            return -raw
        if hasattr(estimator, "score_samples"):
            raw = np.asarray(estimator.score_samples(X)).ravel()
            return -raw
        if hasattr(estimator, "predict"):
            y_tmp = np.asarray(estimator.predict(X)).ravel()
            return (y_tmp == -1).astype(float)
        return np.zeros(len(X), dtype=float)

    @staticmethod
    def _binarize_scores(estimator, X, scores, thresholding):
        """
        Convert continuous scores into binary predictions (1 = anomaly).

        Thresholding methods
        --------------------
        - {'method': 'auto'}:
            use estimator.predict if available (-1 -> 1)
            else fallback to contamination quantile (if available)
        - {'method': 'threshold', 'threshold': float}:
            scores >= threshold -> 1
        - {'method': 'quantile', 'quantile': float in (0,1)}:
            scores >= quantile(scores, q) -> 1
        - {'method': 'top_k', 'top_k': int}:
            mark exactly top-k highest scores as anomalies
        - default fallback:
            if estimator has 'contamination': use (1-contamination) quantile
            elif has predict: map (-1 -> 1)
            else zeros
        """
        method = (thresholding or {}).get('method', None)

        if method == 'auto' and hasattr(estimator, 'predict'):
            y_tmp = np.asarray(estimator.predict(X)).ravel()
            return (y_tmp == -1).astype(int)

        if method == 'threshold':
            thr = float(thresholding.get('threshold'))
            return (scores >= thr).astype(int)

        if method == 'quantile':
            q = float(thresholding.get('quantile', 0.95))
            thr = np.quantile(scores, q)
            return (scores >= thr).astype(int)

        if method == 'top_k':
            k = int(thresholding.get('top_k', 0))
            k = max(0, min(k, scores.size))
            y_pred = np.zeros(scores.size, dtype=int)
            if k > 0:
                idx = np.argpartition(scores, -k)[-k:]
                y_pred[idx] = 1
            return y_pred

        # Fallback
        contamination = getattr(estimator, "contamination", None)
        if contamination is not None:
            q = 1.0 - float(contamination)
            thr = np.quantile(scores, q)
            return (scores >= thr).astype(int)

        if hasattr(estimator, 'predict'):
            y_tmp = np.asarray(estimator.predict(X)).ravel()
            return (y_tmp == -1).astype(int)

        return np.zeros(scores.size, dtype=int)

    def run_experiment(self, steps):
        """
        Run a series of anomaly detection steps.

        Parameters
        ----------
        steps : list of tuples
            A list of steps to perform, where each tuple contains:
            - step name (str)
            - step parameters (dict)

            Supported steps:
            - 'split'                   : train/test split
            - 'model'                   : build (and fit if split already done)
            - 'select_best_model'       : pick best detector by metric (requires labels)
            - 'run_metrics_analysis'    : compute AUCs/F1 (if labels) or just produce scores
            - 'detect_anomalies'        : return indices of anomalies

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
                # TASK#6
                pass
                # TODO - BLOCK END
                results.append((step, "Done"))

            elif step == 'model':
                model_type = params.get('model_type', None)
                model_params = params.get('model_params', None)
                if model_type is not None:
                    # TODO - BLOCK START
                    # TASK#7
                    pass
                    # TODO - BLOCK END
                else:
                    # TODO - BLOCK START
                    # TASK#8
                    pass
                    # TODO - BLOCK END
                if self.X_train is not None:
                    self.clf.fit(self.X_train)  # unsupervised: ignore y
                    results.append((step, "Done"))
                else:
                    results.append((step, "Error: No training data"))

            elif step == 'select_best_model':
                if self.X_train is None or self.X_test is None:
                    results.append((step, "Error: No training/test data"))
                    continue
                if self.y_test is None:
                    results.append((step, "Error: No labels available for model selection."))
                    continue

                candidates = params.get('candidates', [])
                metric = params.get('metric', 'roc_auc')
                pos_label = params.get('pos_label', 1)
                thresholding = params.get('thresholding', None)

                if not candidates:
                    results.append((step, "Error: 'candidates' list is empty."))
                    continue

                best_score = -np.inf
                best_model = None

                for spec in candidates:
                    mt = spec.get('model_type')
                    mp = spec.get('model_params', None)
                    if mt is None:
                        continue

                    mdl = ModelFactoryForAnomaly.create_model(mt, model_params=mp)
                    mdl.fit(self.X_train)

                    # TODO - BLOCK START
                    # TASK#9
                    metric_value = float('nan')
                    # TODO - BLOCK END

                    if np.isfinite(metric_value) and metric_value > best_score:
                        best_score = float(metric_value)
                        best_model = mdl

                if best_model:
                    self.clf = best_model
                    results.append((step, "Done"))
                else:
                    results.append((step, "Error: No best model found."))

            elif step == 'run_metrics_analysis':
                if self.clf is None or self.X_test is None:
                    results.append((step, "Error: Model not trained or data not split."))
                    continue

                pos_label = params.get('pos_label', 1)
                thresholding = params.get('thresholding', None)

                # TODO - BLOCK START
                # TASK#10
                roc_auc = float('nan')
                pr_auc = float('nan')
                f1_sc = float('nan')
                # TODO - BLOCK END

                results.append((step, {"roc_auc": roc_auc, "pr_auc": pr_auc, "f1_score": f1_sc}))

            elif step == 'detect_anomalies':
                if self.clf is None:
                    results.append((step, "Error: Model not trained."))
                    continue

                thresholding = params.get('thresholding', None)

                if self.X_test is None:
                    results.append((step, "Error: Requested split data is not available."))
                    continue

                # TODO - BLOCK START
                # TASK#11
                y_pred = None
                # TODO - BLOCK END

                idx = self.X_test.index.to_numpy()
                anomaly_idx = idx[y_pred.astype(bool)]

                results.append((step, {"indices": anomaly_idx.tolist()}))

            else:
                raise ValueError(f"Unknown step: {step}")

        return results

    @staticmethod
    def example_experiment_1(df, target_column):
        """
        Example of model selection (unsupervised setting with labels available for evaluation):
        - Data split (test_size=0.3, random_state=13, stratify=False)
        - Select best model by ROC AUC among several detectors
          Candidates (use exactly these params):
            * IsolationForest(random_state=13, contamination=0.05)
            * OneClassSVM(kernel='rbf', gamma='scale', nu=0.05)
            * LocalOutlierFactor(n_neighbors=20, contamination=0.05, novelty=True)
            * EllipticEnvelope(contamination=0.05, random_state=13)
        - Run metrics analysis (thresholding: quantile=0.95)

        Returns
        -------
        list[tuple[str, any]]
            Step results for the entire workflow.
        """
        # TODO - BLOCK START
        # TASK#12
        steps = []
        # TODO - BLOCK END
        experiment = Experiment(df, target_column)
        return experiment.run_experiment(steps)

    @staticmethod
    def example_experiment_2(df, target_column):
        """
        Example of a single-detector workflow:
        - Data split with default parameters
        - Train IsolationForest(contamination=0.03, random_state=7)
        - Detect anomalies with auto thresholding

        Returns
        -------
        list[tuple[str, any]]
            Step results for the entire workflow.
        """
        # TODO - BLOCK START
        # TASK#13
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
