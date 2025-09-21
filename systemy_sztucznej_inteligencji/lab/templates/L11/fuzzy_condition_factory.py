from typing import Callable, Dict
import numpy as np

# Type alias for a condition function
Condition = Callable[[Dict[str, float]], float]


class FuzzyConditionFactory:
    """
    Factory class for creating fuzzy antecedent conditions.

    Each method returns a function (Condition) that, given crisp inputs,
    evaluates to a membership degree in [0, 1].
    """

    @staticmethod
    def atomic(variable, membership_label: str) -> Condition:
        """
        Create an atomic condition: μ = degree of membership_label(variable_value).

        Parameters
        ----------
        variable : FuzzyVariable
            The fuzzy variable to test.
        membership_label : str
            Label of the membership function of that variable.

        Returns
        -------
        Condition
            A callable taking crisp_inputs and returning membership degree.
        """

        def _cond(crisp_inputs: Dict[str, float]) -> float:
            # TODO - BLOCK START
            # TASK#5
            pass
            # TODO - BLOCK END

        return _cond

    @staticmethod
    def and_condition(*subconditions: Condition,
                      t_norm: Callable[[float, float], float] = min) -> Condition:
        """
        Create a logical AND condition using a t-norm.

        Parameters
        ----------
        subconditions : Condition
            One or more conditions to combine.
        t_norm : Callable[[float, float], float], default=min
            Function used for conjunction (commonly min or product).

        Returns
        -------
        Condition
        """

        def _cond(crisp_inputs: Dict[str, float]) -> float:
            val = 1.0
            # TODO - BLOCK START
            # TASK#6
            pass
            # TODO - BLOCK END
            return float(np.clip(val, 0.0, 1.0))

        return _cond

    @staticmethod
    def or_condition(*subconditions: Condition,
                     s_norm: Callable[[float, float], float] = max) -> Condition:
        """
        Create a logical OR condition using an s-norm.

        Parameters
        ----------
        subconditions : Condition
            One or more conditions to combine.
        s_norm : Callable[[float, float], float], default=max
            Function used for disjunction (commonly max or algebraic sum).

        Returns
        -------
        Condition
        """

        def _cond(crisp_inputs: Dict[str, float]) -> float:
            val = 0.0
            # TODO - BLOCK START
            # TASK#7
            pass
            # TODO - BLOCK END
            return float(np.clip(val, 0.0, 1.0))

        return _cond

    @staticmethod
    def not_condition(subcondition: Condition,
                      negation: Callable[[float], float] = lambda a: 1.0 - a) -> Condition:
        """
        Create a logical NOT condition using a negation function.

        Parameters
        ----------
        subcondition : Condition
            The condition to negate.
        negation : Callable[[float], float], default=lambda a: 1 - a
            Function used for negation.

        Returns
        -------
        Condition
        """

        def _cond(crisp_inputs: Dict[str, float]) -> float:
            # TODO - BLOCK START
            # TASK#8
            pass
            # TODO - BLOCK END

        return _cond

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