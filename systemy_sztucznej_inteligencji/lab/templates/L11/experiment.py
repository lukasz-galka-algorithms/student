from __future__ import annotations
import numpy as np

from fuzzy_condition_factory import FuzzyConditionFactory
from fuzzy_variable import FuzzyVariable
from takagi_sugeno_model import TakagiSugenoFuzzyInferenceModel, TakagiSugenoFuzzyRule
from mamdani_model import MamdaniFuzzyInferenceModel, MamdaniFuzzyRule


class Experiment:
    """
    Container for ready-made example fuzzy inference models.
    Each method builds and returns a configured model.
    """

    @staticmethod
    def example_experiment_mamdani() -> MamdaniFuzzyInferenceModel:
        """
        Build a Mamdani fuzzy inference model for controlling fan speed
        depending on the current temperature.

        Task description
        ----------------
        We want to design a fuzzy controller for a fan.
        The input variable is **temperature** (0–50 °C).
        The output variable is **fan_speed** (0–100 %).

        1) Define input fuzzy variable: temperature
           - Universe of discourse: from 0 to 50, sampled densely (e.g. np.linspace(0, 50, 501)).
           - Membership functions:
               * "cold"   – triangular, parameters (0, 0, 20)
                 (maximum membership at 0 °C, decreases linearly to 20 °C).
               * "medium" – triangular, parameters (15, 25, 35)
                 (peak at 25 °C, overlapping with "cold" and "hot").
               * "hot"    – triangular, parameters (30, 50, 50)
                 (starts rising around 30 °C, full membership from 50 °C).

        2) Define output fuzzy variable: fan_speed
           - Universe of discourse: from 0 to 100, sampled densely (e.g. np.linspace(0, 100, 1001)).
           - Membership functions:
               * "low"    – triangular, parameters (0, 0, 40)
                 (fan is off at 0 %, linearly rises up to 40 %).
               * "medium" – triangular, parameters (30, 50, 70)
                 (peak at 50 %, overlap with "low" and "high").
               * "high"   – triangular, parameters (60, 100, 100)
                 (starts rising at 60 %, maximum from 100 %).

        3) Build fuzzy rules:
           - Rule 1: IF temperature IS cold   THEN fan_speed IS low
           - Rule 2: IF temperature IS medium THEN fan_speed IS medium
           - Rule 3: IF temperature IS hot    THEN fan_speed IS high

        4) Inference mechanism:
           - Use Mamdani inference.
           - For implication and aggregation use standard min/max operators.
           - For defuzzification use the centroid method.

        Expected outcome
        ----------------
        The model should return:
          * low fan speeds (close to 0 %) when the temperature is cold (e.g. 10 °C),
          * medium fan speeds (around 50 %) when the temperature is moderate (e.g. 25 °C),
          * high fan speeds (close to 100 %) when the temperature is hot (e.g. 40 °C).

        Returns
        -------
        MamdaniFuzzyInferenceModel
            A fully configured Mamdani model.
        """
        # TODO - BLOCK START
        # TASK#16
        pass
        # TODO - BLOCK END

    @staticmethod
    def example_experiment_takagi_sugeno() -> TakagiSugenoFuzzyInferenceModel:
        """
        Build a Takagi–Sugeno (first-order) fuzzy inference model
        for computing a final exam grade from exam performance and attendance.
        The model uses only two labels per input (low/high and poor/good).

        Task description
        ----------------
        We want to design a fuzzy grader for a course.
        The input variables are **exam_score** (0–100 %) and **attendance** (0–100 %).
        The output variable is **final_grade** on the Polish scale (2.0–5.0).

        1) Define input fuzzy variable: exam_score
           - Universe of discourse: from 0 to 100, sampled densely (e.g., np.linspace(0, 100, 101)).
           - Membership functions (two labels for simplicity):
               * "low"  – trapezoidal,  parameters (0, 0, 35, 55)
                 (full membership for very low scores; fades out around midrange)
               * "high" – trapezoidal,  parameters (45, 65, 100, 100)
                 (starts around midrange, saturates toward the maximum)
             The overlap (35–65) ensures smooth transitions.

        2) Define input fuzzy variable: attendance
           - Universe of discourse: from 0 to 100, sampled densely (e.g., np.linspace(0, 100, 101)).
           - Membership functions (two labels for simplicity):
               * "poor" – trapezoidal, parameters (0, 0, 30, 60)
               * "good" – trapezoidal, parameters (40, 70, 100, 100)
             The overlap (40–70) allows gradual switching between poor and good.

        3) Register numeric Takagi–Sugeno output channel (no output membership functions):
           - Output name: "final_grade"
           - Clip the final crisp value to the valid range [2.0, 5.0].

        4) Build fuzzy rules (first-order TS; linear consequents)
           Let s = exam_score, a = attendance (both in [0, 100]).
           The four rules cover all combinations:

           - Rule 1: IF exam_score IS low  AND attendance IS poor
                     THEN final_grade = 1.9 + 0.004*s + 0.001*a
                     (very conservative baseline; small gains even if one factor improves)

           - Rule 2: IF exam_score IS low  AND attendance IS good
                     THEN final_grade = 2.2 + 0.006*s + 0.004*a
                     (good attendance partially compensates a low score)

           - Rule 3: IF exam_score IS high AND attendance IS poor
                     THEN final_grade = 2.8 + 0.012*s + 0.001*a
                     (strong score drives the grade; weak attendance limits the maximum)

           - Rule 4: IF exam_score IS high AND attendance IS good
                     THEN final_grade = 3.0 + 0.014*s + 0.004*a
                     (both good → tends toward 5.0)

        Returns
        -------
        TakagiSugenoFuzzyInferenceModel
            A fully configured Takagi–Sugeno model for exam grading.
        """
        # TODO - BLOCK START
        # TASK#17
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