import numpy as np

class PrimeNumbersAnalyzer:
    """
    A utility class for analyzing prime numbers from a given list.

    This class provides methods to filter prime numbers,
    calculate their mean and median, and check primality.
    """

    def __init__(self, numbers):
        """
        Initialize the analyzer with a list of numbers.
        """
        # TODO - BLOCK START
        # TASK#3
        pass
        # TODO - BLOCK END

    def filter_primes(self):
        """
        Return the list of prime numbers.

        Returns
        -------
        list of int
            The prime numbers extracted from the numbers.
        """
        # TODO - BLOCK START
        # TASK#4
        pass
        # TODO - BLOCK END

    def mean_of_primes(self):
        """
        Compute the mean of the prime numbers.

        Returns
        -------
        float
            The arithmetic mean of prime numbers,
            or 0 if no prime numbers exist.
        """
        # TODO - BLOCK START
        # TASK#5
        pass
        # TODO - BLOCK END

    def median_of_primes(self):
        """
        Compute the median of the prime numbers.

        Returns
        -------
        float
            The median of prime numbers,
            or 0 if no prime numbers exist.
        """
        # TODO - BLOCK START
        # TASK#6
        pass
        # TODO - BLOCK END

    @staticmethod
    def is_prime(number):
        """
        Check whether a given number is prime.

        Parameters
        ----------
        number : int
            The number to check.

        Returns
        -------
        bool
            True if the number is prime, False otherwise.

        Examples
        --------
        >>> PrimeNumbersAnalyzer.is_prime(7)
        True
        >>> PrimeNumbersAnalyzer.is_prime(10)
        False
        """
        # TODO - BLOCK START
        # TASK#2
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