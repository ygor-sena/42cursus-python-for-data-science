class calculator:
    """
    A simple calculator class to perform vector operations. All the methods
    are static because they do not require any class attributes. Moreover,
    the methods assume that the input vectors are of the same length.
    """

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        Calculates the dot product of two vectors.

        Args:
            V1 (list[float]): The first vector.
            V2 (list[float]): The second vector.
        """
        result = sum([V1[i] * V2[i] for i in range(len(V1))])
        print(f"Dot product is: {result:.1f}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        Adds two vectors element-wise.

        Args:
            V1 (list[float]): The first vector.
            V2 (list[float]): The second vector.
        """
        result = [float(V1[i] + V2[i]) for i in range(len(V1))]
        print(f"Add Vector is : {result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        Subtracts the second vector from the first vector element-wise.

        Args:
            V1 (list[float]): The first vector.
            V2 (list[float]): The second vector.
        """
        result = [float(V1[i] - V2[i]) for i in range(len(V1))]
        print(f"Sous Vector is: {result}")
