from abc import ABC, abstractmethod


class Character(ABC):
    """
    Abstract base class representing a character.
    """

    @abstractmethod
    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Initialize a character with a first name and is_alive status.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """
        Change the character's is_alive from true to false.
        """
        self.is_alive = False


class Stark(Character):
    """
    Class Stark
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Initialize a Stark character.
        """
        super().__init__(first_name, is_alive)
