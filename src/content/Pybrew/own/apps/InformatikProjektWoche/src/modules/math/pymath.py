from logging import root
from math import sqrt
from typing import Type


class Math:

    def __init__(self) -> None:
        """
        This module provides a lot of methods and constantes for mathematically operations.\n

        There are this methods: \n
        add() -> Add 2 or more numbers and return the result.\n
        subtrate() -> Subtrate 2 or more numbers and return the result. \n
        multiply() -> Multiply 2 or more numbers and return the result. \n
        divide() -> Divide 2 or more numbers and return the result. \n
        sqrt() -> Get the square-root of a positive number n and return the result. \n
        root() -> Get a custom root of a positive number n and return the result. \n
        pythagoras() -> Calculate the length of the hypotenuse using the Pythagorean theorem. \n
        factorial() -> Calculate the factorial of a number. \n

        There these constantes: \n
        pi: float = 3.14159 -> Constant to calculate circles. \n
        c: int = 299792458 -> Speed of light in a vakuum. \n 
        e: float = 2.71828 -> Constant for natural logarithms. \n
        r2: float = 1.4142135623730951 -> Square root of the number 2. \n
        """

    def __repr__(self) -> str:
        return f'A module for mathematical operations.'

    class Constantes:
        
        def __init__(self) -> None:
            """
            This class defines some mathematically constantes.
            """

        def __repr__(self) -> str:
            return f'This Class defines some mathematically constantes.'

        pi: float = 3.14159 
        c: int = 299792458
        e: float = 2.71828
        r2: float = 1.4142135623730951

    class DivisionByZeroError(Exception):
        """Can't divide by zero!"""
        pass

    class MissingValueError(Exception):
        """At least two numbers must be provided!"""
        pass

    class NegativeValueError(Exception):
        """This operation is not defined for negative values!"""
        pass

    class NotANumberError(Exception):
        """This is not a number!"""
        pass

    def add(self, *args: int | float) -> int | float:
        """
        Add multiple numbers.

        Parameters:
        *args (int | float): The numbers to add. At least two numbers must be provided.

        Returns:
        int | float: The sum of the numbers.

        Raises:
        MissingValueError: If fewer than two numbers are provided.
        """
        try:
            if len(args) < 2:
                raise Math.MissingValueError("At least two numbers must be provided!")
            return sum(args)
        except TypeError:
            raise math.NotANumberError("Provided str, expected int!")
    
    def subtract(self, *args: int | float) -> int | float:
        """
        Subtract multiple numbers.

        Parameters:
        *args (int | float): The numbers to subtract. At least two numbers must be provided.

        Returns:
        int | float: The result of subtracting all subsequent numbers from the first number.

        Raises:
        MissingValueError: If fewer than two numbers are provided.
        """
        try:
            if len(args) < 2:
                raise Math.MissingValueError("At least two numbers must be provided!")
            result = args[0]
            for num in args[1:]:
                result -= num
            return result
        except TypeError:
            raise math.NotANumberError("Provided str, expected int!")
    
    def multiply(self, *args: int | float) -> int | float:
        """
        Multiply multiple numbers.

        Parameters:
        *args (int | float): The numbers to multiply. At least two numbers must be provided.

        Returns:
        int | float: The product of the numbers.

        Raises:
        MissingValueError: If fewer than two numbers are provided.
        """
        try:
            if len(args) < 2:
                raise Math.MissingValueError("At least two numbers must be provided!")
            result = args[0]
            for num in args[1:]:
                result *= num
            return result
        except TypeError:
            raise math.NotANumberError("Provided str, expected int!")
    
    def divide(self, *args: int | float) -> int | float:
        """
        Divide multiple numbers.

        Parameters:
        *args (int | float): The numbers to divide. At least two numbers must be provided.

        Returns:
        int | float: The result of dividing the first number by all subsequent numbers.

        Raises:
        MissingValueError: If fewer than two numbers are provided.
        DivisionByZeroError: If attempting to divide by zero.
        """
        try:
            if len(args) < 2:
                raise Math.MissingValueError("At least two numbers must be provided!")
            result = args[0]
            for num in args[1:]:
                if num == 0:
                    raise Math.DivisionByZeroError("Can't divide by zero!")
                result /= num
            return result
        except TypeError:
            raise math.NotANumberError("Provided str, expected int!")
    
    def sqrt(self, x: int | float) -> int | float:
        """
        Calculate the square root of a number.

        Parameters:
        x (int | float): The number to calculate the root of.

        Returns:
        int | float: The square root of the number.

        Raises:
        ValueError: If the number is negative.
        """
        try:
            if x < 0:
                raise math.NegativeValueError("Cannot calculate the square root of a negative number!")
            return x ** (1 / 2)
        except TypeError:
            raise math.NotANumberError("Provided str, expected int!")

    def root(self, x: int | float, n: int = 2) -> int | float:
        """
        Calculate the n-th root of a number.

        Parameters:
        x (int | float): The number to calculate the root of.
        n (int): The degree of the root (default is 2 for square root).

        Returns:
        int | float: The n-th root of the number.

        Raises:
        ValueError: If the number is negative and n is even.
        """
        try:
            if x < 0 and n % 2 == 0:
                raise math.NegativeValueError("Cannot calculate the even root of a negative number!")
            return x ** (1 / n)
        except TypeError:
            raise math.NotANumberError("Provided str, expected int!")

    def pythagoras(self, a: int | float, b: int | float) -> int | float:
        """
        Calculate the length of the hypotenuse using the Pythagorean theorem.

        Parameters:
        a (int | float): The length of one leg of the right triangle.
        b (int | float): The length of the other leg of the right triangle.

        Returns:
        int | float: The length of the hypotenuse.
        """
        try:
            return self.root(a**2 + b**2)
        except TypeError:
            raise math.NotANumberError("Provided str, expected int!")

    def factorial(self, n: int) -> int:
        """
        Calculate the factorial of a number.

        Parameters:
        n (int): The number to calculate the factorial of. Must be a non-negative integer.

        Returns:
        int: The factorial of the number.

        Raises:
        NegativeValueError: If the number is negative.
        """
        try:
            if n < 0:
                raise Math.NegativeValueError("Factorial is not defined for negative values!")
            if n == 0:
                return 1
            result = 1
            for i in range(1, n + 1):
                result *= i
            return result
        except TypeError:
            raise math.NotANumberError("Provided str, expected int!")

if __name__ == '__main__':
    math = Math()
    print(math.add(2, 2))
