from abc import ABC, abstractmethod


class Character(ABC):
    """
    Abstract class that defines a character and its method die().
    """

    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """
        Initializes a character.

        Args:
            first_name (str): The first name of the character.
            is_alive (bool, optional): The status of the character.
            Defaults to True.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die() -> None:
        """
        Abstract method to be implemented by subclasses to handle
        character death.
        """
        pass


class Stark(Character):
    """
    Class that implements a character called Stark, which inherits
    from Character.
    """

    def __init__(self, first_name, is_alive=True):
        """
        Initializes a Stark character.

        Args:
            first_name (str): The first name of the Stark character.
            is_alive (bool, optional): The status of the Stark character.
            Defaults to True.
        """
        super().__init__(first_name, is_alive)

    def die(self) -> None:
        """
        Handles the death of the Stark character.
        """
        self.is_alive = False
