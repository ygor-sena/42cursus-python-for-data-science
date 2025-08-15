import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """
    Generates a random 15-character string ID.

    Returns:
        str: A random string of 15 lowercase ASCII characters.
    """
    return "".join(random.choices(string.ascii_lowercase, k=15))


def generate_login(name: str, surname: str) -> str:
    """
    Generates a login string based on the first letter of the name and
    the surname.

    Args:
        name (str): The first name of the student.
        surname (str): The surname of the student.

    Returns:
        str: A login string in the format 'Nsurname', where 'N' is the
        capitalized first letter of the name.
    """
    return (name[0].upper() + surname).capitalize()


@dataclass
class Student:
    """
    Represents a student with a name, surname, active status, login, and ID.

    Attributes:
        name (str):    The first name of the student.
        surname (str): The surname of the student.
        active (bool): The active status of the student. Defaults to True.
        login (str):   The login string for the student, generated based on
                       the name and surname.
        id (str):      The unique ID for the student, generated randomly.
    """
    name: str
    surname: str
    active: bool = field(default=True)
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self):
        """
        Initializes the login attribute after the dataclass is instantiated.
        """
        self.login = generate_login(self.name, self.surname)
