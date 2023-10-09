#!/usr/bin/python3
"""
class MyInt inherit from built-in int class
"""


class MyInt(int):
    """initialising the super class"""
    def __init__(self, num):
        """Initializes MyInt
        Args:
            num (int): int that's passed through
        """

        self.num = num

    def __eq__(self, value):
        """Inverts == to !=
            Returns:
                bool: true or false
        """

        if not isinstance(value, MyInt):
            return False

    def __ne__(self, value):
        """Inverts != to ==
            Returns:
                bool: true or false
        """

        if not isinstance(value, MyInt):
            return True