from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """
    All hail the supreme ruler of Westeros!
    """
    def __init__(self, first_name, is_alive=True):
        """
        Initializes a King instance.

        Args:
            first_name (str): The first name of the character.
            is_alive (bool, optional): The living status of the character.
            Defaults to True.
        """
        super().__init__(first_name, is_alive)

    def get_eyes(self) -> str:
        """
        Returns the value of the eyes attribute.

        Returns:
            str: The eye color of the character.
        """
        return self.eyes

    def get_hairs(self) -> str:
        """
        Returns the value of the hairs attribute.

        Returns:
            str: The hair color of the character.
        """
        return self.hairs

    def set_eyes(self, eyes):
        """
        Sets the value of the eyes attribute.

        Args:
            eyes (str): The new eye color of the character.
        """
        self.eyes = eyes

    def set_hairs(self, hairs):
        """
        Sets the value of the hairs attribute.

        Args:
            hairs (str): The new hair color of the character.
        """
        self.hairs = hairs
