from __future__ import annotations
from typing import Callable, Dict, List, Tuple
import numpy as np
import skfuzzy as fuzz

from fuzzy_variable import FuzzyVariable


class MamdaniFuzzyRule:
    """
    A single Mamdani-style fuzzy rule.

    Structure
    ---------
    IF antecedent_condition THEN, for each output:
        (output_variable_name, output_membership_label, rule_weight)

    Parameters
    ----------
    antecedent_condition : Condition
        Callable that maps a dict of crisp inputs to a membership degree in [0, 1].
    consequent_triplets : List[Tuple[str, str, float]]
        A list of (output_variable_name, output_membership_label, rule_weight).
        - output_variable_name : str
            Name of the registered fuzzy output variable to affect.
        - output_membership_label : str
            Label of the membership function inside that output variable.
        - rule_weight : float
            Scalar weight (typically in [0, 1]) scaling the firing strength.

    Examples
    --------
    >>> # with FuzzyConditionFactory.atomic(...)
    >>> rule = MamdaniFuzzyRule(
    ...     antecedent_condition=cond_hot,
    ...     consequent_triplets=[("fan_speed", "high", 1.0)]
    ... )
    """
    def __init__(self, antecedent_condition: "Condition",
                 consequent_triplets: List[Tuple[str, str, float]]):
        self.antecedent_condition = antecedent_condition
        self.consequent_triplets = consequent_triplets  # (output_name, label, weight)


class MamdaniFuzzyInferenceModel:
    """
    A lightweight Mamdani fuzzy inference engine that uses:
      - Your FuzzyVariable (with membership_functions_map)
      - Condition callables produced by FuzzyConditionFactory

    Pipeline
    --------
    1) Evaluate each rule antecedent → firing strength in [0, 1].
    2) Implication: apply firing strength to the selected output membership function vector.
    3) Aggregate across rules for each output variable.
    4) Defuzzify each aggregated vector to a crisp value via `skfuzzy.defuzz`.

    Parameters
    ----------
    implication_operator : Callable[[float, np.ndarray], np.ndarray], optional
        Applies firing strength to a membership function vector (default: min).
        Signature: implication_operator(firing_strength, membership_vector) -> vector
    aggregation_operator : Callable[[np.ndarray, np.ndarray], np.ndarray], optional
        Aggregates two membership vectors (default: pointwise maximum).
    defuzzification_method : str, optional
        Any method supported by `skfuzzy.defuzz`, e.g. "centroid", "bisector",
        "mom" (mean of maxima), "som", "lom".
    """

    def __init__(
        self,
        implication_operator: Callable[[float, np.ndarray], np.ndarray] = lambda w, y: np.minimum(w, y),
        aggregation_operator: Callable[[np.ndarray, np.ndarray], np.ndarray] = np.maximum,
        defuzzification_method: str = "centroid"
    ):
        self.input_variables: Dict[str, FuzzyVariable] = {}
        self.output_variables: Dict[str, FuzzyVariable] = {}
        self.rules: List[MamdaniFuzzyRule] = []
        self.implication_operator = implication_operator
        self.aggregation_operator = aggregation_operator
        self.defuzzification_method = defuzzification_method

    def add_input_variable(self, variable: FuzzyVariable) -> None:
        """
        Register a fuzzy input variable (used by antecedent conditions).
        """
        # TODO - BLOCK START
        # TASK#9
        pass
        # TODO - BLOCK END

    def add_output_variable(self, variable: FuzzyVariable) -> None:
        """
        Register a fuzzy output variable (subject to implication, aggregation, defuzzification).
        """
        # TODO - BLOCK START
        # TASK#10
        pass
        # TODO - BLOCK END

    def add_rule(self, rule: MamdaniFuzzyRule) -> None:
        """
        Add a Mamdani rule to the knowledge base.
        """
        # TODO - BLOCK START
        # TASK#11
        pass
        # TODO - BLOCK END

    def compute_outputs(self, crisp_inputs: Dict[str, float]) -> Dict[str, float]:
        """
        Compute crisp outputs for all registered output variables.

        Parameters
        ----------
        crisp_inputs : Dict[str, float]
            Mapping from input variable name to its crisp value,
            e.g. {"temperature": 26.5}.

        Returns
        -------
        Dict[str, float]
            Mapping from output variable name to its crisp value.
        """
        # TODO - BLOCK START
        # TASK#12
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