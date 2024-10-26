class calculator:
    """
    A simple calculator class to perform basic arithmetic
    operations on a vector.
    """

    def __init__(self, vector) -> None:
        """
        Initializes the calculator with a vector.

        Args:
            vector (list): A list of numbers to perform operations on.
        """
        self.vector = vector

    def __add__(self, object) -> None:
        """
        Adds a number to each element of the vector.

        Args:
            object (int or float): The number to add to each
            element of the vector.
        """
        self.vector = [i + object for i in self.vector]
        print([x for x in self.vector])

    def __mul__(self, object) -> None:
        """
        Multiplies each element of the vector by a number.

        Args:
            object (int or float): The number to multiply
            each element of the vector by.
        """
        self.vector = [i * object for i in self.vector]
        print([x for x in self.vector])

    def __sub__(self, object) -> None:
        """
        Subtracts a number from each element of the vector.

        Args:
            object (int or float): The number to subtract from
            each element of the vector.
        """
        self.vector = [i - object for i in self.vector]
        print([x for x in self.vector])

    def __truediv__(self, object) -> None:
        """
        Divides each element of the vector by a number.

        Args:
            object (int or float): The number to divide each
            element of the vector by.
        """
        self.vector = [i / object for i in self.vector]
        print([x for x in self.vector])
