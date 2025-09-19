from __future__ import annotations

from typing import Dict, Tuple, List
import numpy as np
import skfuzzy as fuzz

class FuzzyVariable:
    """
    Represents a fuzzy (linguistic) variable: its name, a discretized universe,
    and a dictionary of named membership functions.

    Attributes
    ----------
    variable_name : str
        Human-readable name of the variable (e.g., "temperature", "fan_speed").
    universe_values : np.ndarray
        One-dimensional grid (x-axis) representing the variable's universe,
        e.g., np.linspace(0, 50, 501).
    membership_functions_map : Dict[str, Tuple[np.ndarray, np.ndarray]]
        Mapping: label -> (x_vector, membership_values). The x_vector is
        typically `universe_values`, while membership_values are the evaluated
        membership function values over that grid.

    Notes
    -----
    - Membership function shapes are built using scikit-fuzzy:
      `fuzz.trimf`, `fuzz.trapmf`, `fuzz.gaussmf`.
    - The membership degree for a crisp value is computed with
      `fuzz.interp_membership` (linear interpolation).
    """

    def __init__(self, variable_name: str, universe_values: np.ndarray):
        """
        Parameters
        ----------
        variable_name : str
            The name of the linguistic variable.
        universe_values : np.ndarray
            One-dimensional array defining the universe grid.

        Examples
        --------
        >>> FuzzyVariable("temperature", np.linspace(0, 50, 501))
        """
        # Store the variable name
        self.variable_name = variable_name

        # Ensure the universe is a float array (consistent with scikit-fuzzy)
        self.universe_values = np.asarray(universe_values, dtype=float)

        # Container for membership functions:
        #   label -> (x_axis, membership_values)
        self.membership_functions_map: Dict[str, Tuple[np.ndarray, np.ndarray]] = {}

    def add_triangular_membership_function(self, label: str, a: float, b: float, c: float) -> None:
        """
        Register a triangular membership function with vertices (a, b, c).

        Parameters
        ----------
        label : str
            Unique label for the membership function (e.g., "cold", "medium").
        a, b, c : float
            Triangle parameters with a <= b <= c. Values outside [a, c] map to 0.
            At b the function reaches its maximum (1) when a != b and b != c.

        Raises
        ------
        ValueError
            If the label already exists or the parameters are invalid.

        Examples
        --------
        >>> variable.add_triangular_membership_function("low", 0, 0, 40)
        """
        # TODO - BLOCK START
        # TASK#6
        pass
        # TODO - BLOCK END

    def add_trapezoidal_membership_function(self, label: str, a: float, b: float, c: float, d: float) -> None:
        """
        Register a trapezoidal membership function with breakpoints (a, b, c, d).

        Parameters
        ----------
        label : str
            Unique label for the membership function.
        a, b, c, d : float
            Trapezoid parameters with a <= b <= c <= d. Over [b, c] the function
            equals 1; on [a, b] and [c, d] it rises/falls linearly.

        Raises
        ------
        ValueError
            If the label already exists or the parameters are invalid.

        Examples
        --------
        >>> variable.add_trapezoidal_membership_function("medium", 30, 50, 70, 90)
        """
        # TODO - BLOCK START
        # TASK#7
        pass
        # TODO - BLOCK END

    def add_gaussian_membership_function(self, label: str, mean: float, sigma: float) -> None:
        """
        Register a Gaussian membership function parameterized by (mean, sigma).

        Parameters
        ----------
        label : str
            Unique label for the membership function.
        mean : float
            Center (x-value at which the function is maximal).
        sigma : float
            Standard deviation (> 0). Larger values produce a wider bell curve.

        Raises
        ------
        ValueError
            If the label already exists or sigma <= 0.

        Examples
        --------
        >>> variable.add_gaussian_membership_function("hot", 40.0, 5.0)
        """
        # TODO - BLOCK START
        # TASK#8
        pass
        # TODO - BLOCK END

    def get_membership_degree(self, label: str, crisp_value: float) -> float:
        """
        Compute the membership degree μ ∈ [0, 1] for a given crisp input value,
        using linear interpolation (`fuzz.interp_membership`).

        Parameters
        ----------
        label : str
            Label of a previously registered membership function.
        crisp_value : float
            Numeric value (e.g., temperature=23.7) for which to compute μ.

        Returns
        -------
        float
            The membership degree in [0, 1].

        Raises
        ------
        KeyError
            If no membership function with the given label exists.

        Examples
        --------
        >>> variable.get_membership_degree("medium", 25.0)
        1.0
        """
        if label not in self.membership_functions_map:
            raise KeyError(f"Unknown membership function label: '{label}'")

        x_axis, membership_values = self.membership_functions_map[label]
        value = fuzz.interp_membership(x_axis, membership_values, crisp_value)
        return float(np.clip(value, 0.0, 1.0))

    def list_membership_function_labels(self) -> List[str]:
        """
        Return the list of available membership function labels.

        Returns
        -------
        List[str]
            Labels of all registered membership functions.

        Examples
        --------
        >>> variable.list_membership_function_labels()
        ['cold', 'medium', 'hot']
        """
        return list(self.membership_functions_map.keys())

    def get_membership_function_vectors(self, label: str) -> Tuple[np.ndarray, np.ndarray]:
        """
        Return the (x_axis, membership_values) vectors for a given membership function.
        Useful for plotting or external analysis.

        Parameters
        ----------
        label : str
            Label of the membership function.

        Returns
        -------
        Tuple[np.ndarray, np.ndarray]
            (x_axis, membership_values).

        Raises
        ------
        KeyError
            If no membership function with the given label exists.

        Examples
        --------
        >>> x_axis, mu = variable.get_membership_function_vectors("medium")
        >>> x_axis.shape, mu.shape
        ((501,), (501,))
        """
        if label not in self.membership_functions_map:
            raise KeyError(f"Unknown membership function label: '{label}'")
        return self.membership_functions_map[label]

    def remove_membership_function(self, label: str) -> None:
        """
        Remove a registered membership function by its label.

        Parameters
        ----------
        label : str
            The label of the membership function to remove.

        Raises
        ------
        KeyError
            If no membership function with the given label exists.

        Examples
        --------
        >>> variable.remove_membership_function("medium")
        """
        if label not in self.membership_functions_map:
            raise KeyError(f"Unknown membership function label: '{label}'")
        del self.membership_functions_map[label]

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