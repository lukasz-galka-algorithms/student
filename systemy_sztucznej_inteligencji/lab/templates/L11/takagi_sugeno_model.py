from __future__ import annotations
from typing import Callable, Dict, List
import numpy as np

from fuzzy_variable import FuzzyVariable


class TakagiSugenoFuzzyRule:
    """
    A single Takagi–Sugeno fuzzy rule.

    Structure
    ---------
    IF antecedent_condition THEN, for each output_name:
        output_value = consequent_function(crisp_inputs)

    Unlike Mamdani, the consequent is a numeric function of inputs
    (constant, linear, or any callable), not a membership function label.

    Parameters
    ----------
    antecedent_condition : Condition
        Callable that evaluates to a membership degree in [0, 1] using crisp inputs.
    consequent_functions_by_output_name : Dict[str, Callable[[Dict[str, float]], float]]
        Mapping from output name to a callable that returns the consequent value
        for those crisp inputs (e.g., lambda d: 1.2*d["temperature"] - 10).
    rule_weight : float, default=1.0
        Scales the firing strength of the rule.

    Examples
    --------
    >>> rule = TakagiSugenoFuzzyRule(
    ...     antecedent_condition=cond_hot,
    ...     consequent_functions_by_output_name={"fan_speed": lambda d: 2.5*d["temperature"] - 30.0},
    ...     rule_weight=1.0
    ... )
    """
    def __init__(
        self,
        antecedent_condition: "Condition",
        consequent_functions_by_output_name: Dict[str, Callable[[Dict[str, float]], float]],
        rule_weight: float = 1.0
    ):
        self.antecedent_condition = antecedent_condition
        self.consequent_functions_by_output_name = dict(consequent_functions_by_output_name)
        self.rule_weight = float(rule_weight)


class TakagiSugenoFuzzyInferenceModel:
    """
    A lightweight Takagi–Sugeno fuzzy inference engine.

    Pipeline
    --------
    For each output:
      - Evaluate all rules:
          firing_strength_r = transform( antecedent_condition(crisp_inputs) * rule_weight )
          z_r = consequent_function_r(crisp_inputs)
      - Combine via weighted average:
          output = sum_r( firing_strength_r * z_r ) / sum_r( firing_strength_r )

    Parameters
    ----------
    firing_strength_transform : Callable[[float], float], optional
        Post-processing of raw firing strength (e.g., identity, power, etc.).
        Default: identity (lambda a: a).
    output_value_clipping_ranges : Dict[str, (float, float)], optional
        Optional min/max clipping for each named output.

    Notes
    -----
    - This engine does not require output membership functions or defuzzification.
    - It works with the same Condition callables produced by your FuzzyConditionFactory.
    """

    def __init__(
        self,
        firing_strength_transform: Callable[[float], float] = lambda a: a,
        output_value_clipping_ranges: Dict[str, tuple[float, float]] | None = None
    ):
        self.input_variables: Dict[str, FuzzyVariable] = {}
        self.output_names: Dict[str, None] = {}  # acts as a set of output names
        self.rules: List[TakagiSugenoFuzzyRule] = []
        self.firing_strength_transform = firing_strength_transform
        self.output_value_clipping_ranges = output_value_clipping_ranges or {}

    def add_input_variable(self, variable: FuzzyVariable) -> None:
        """
        Register a fuzzy input variable (used by antecedent conditions).
        """
        # TODO - BLOCK START
        # TASK#13
        pass
        # TODO - BLOCK END

    def add_output_name(self, output_name: str, clip_range: tuple[float, float] | None = None) -> None:
        """
        Register a named output for this model.

        Parameters
        ----------
        output_name : str
            The name of the output channel (e.g., "fan_speed").
        clip_range : (float, float), optional
            Optional numeric (min, max) range to clip the final output value.
        """
        self.output_names[output_name] = None
        if clip_range is not None:
            self.output_value_clipping_ranges[output_name] = clip_range

    def add_rule(self, rule: TakagiSugenoFuzzyRule) -> None:
        """
        Add a Takagi–Sugeno rule to the knowledge base.
        """
        # TODO - BLOCK START
        # TASK#14
        pass
        # TODO - BLOCK END

    def compute_outputs(self, crisp_inputs: Dict[str, float]) -> Dict[str, float]:
        """
        Compute crisp outputs for all registered output names.

        Parameters
        ----------
        crisp_inputs : Dict[str, float]
            Mapping from input variable name to its crisp value,
            e.g. {"temperature": 26.5}.

        Returns
        -------
        Dict[str, float]
            Mapping from output name to its crisp value.
        """
        # TODO - BLOCK START
        # TASK#15
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