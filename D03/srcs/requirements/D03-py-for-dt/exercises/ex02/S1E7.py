from S1E9 import Character


class Baratheon(Character):
    """
    Representing the Baratheon family.
    """

    def __init__(self, first_name, is_alive=True, eyes="brown", hairs="dark"):
        """
        Initializes a Baratheon instance.

        Args:
            first_name (str): The first name of the character.
            is_alive (bool, optional): The living status of the character.
                Defaults to True.
            eyes (str, optional): The eye color of the character.
                Defaults to "brown".
            hairs (str, optional): The hair color of the character.
                Defaults to "dark".
        """
        super().__init__(first_name, is_alive)
        self.family_name = Baratheon.__name__
        self.eyes = eyes
        self.hairs = hairs

    def __str__(self) -> str:
        """
        Returns a string representation of the current instance of class
        Baratheon.

        Returns:
            str: A string representation of the Baratheon instance.
        """
        return f"{self.family_name}, {self.eyes}, {self.hairs}"

    def __repr__(self) -> str:
        """
        Returns a string representation of the current instance of class
        Baratheon.

        Returns:
            str: A string representation of the Baratheon instance.
        """
        return self.__str__()

    def die(self):
        """
        Sets the is_alive attribute to False and kills the current instance
        of class Baratheon.
        """
        self.is_alive = False


class Lannister(Character):
    """
    Representing the Lannister family.
    """
    def __init__(self, first_name, is_alive=True, eyes="blue", hairs="light"):
        """
        Initializes a Lannister instance.

        Args:
            first_name (str): The first name of the character.
            is_alive (bool, optional): The living status of the character.
                Defaults to True.
            eyes (str, optional): The eye color of the character.
                Defaults to "blue".
            hairs (str, optional): The hair color of the character.
                Defaults to "light".
        """
        super().__init__(first_name, is_alive)
        self.family_name = Lannister.__name__
        self.eyes = eyes
        self.hairs = hairs

    def __str__(self) -> str:
        """
        Returns a string representation of the current instance of class
        Lannister.

        Returns:
            str: A string representation of the Lannister instance.
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self) -> str:
        """
        Returns a string representation of the current instance of class
        Lannister.

        Returns:
            str: A string representation of the Lannister instance.
        """
        return self.__str__()

    def die(self):
        """
        Sets the is_alive attribute to False and kills the current instance
        of class Lannister.
        """
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """
        Creates an instance of the Lannister class.

        Args:
            first_name (str): The first name of the character.
            is_alive (bool, optional): The living status of the character.
            Defaults to True.

        Returns:
            Lannister: An instance of the Lannister class.
        """
        return cls(first_name, is_alive)
