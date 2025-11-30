from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Class representing a King"""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize a King character."""
        super().__init__(first_name, is_alive)

    def get_eyes(self):
        """Get the eye color of the King."""
        return self.eyes

    def get_hairs(self):
        """Get the hair color of the King."""
        return self.hairs

    def set_eyes(self, eyes: str):
        """Set the eye color of the King."""
        self.eyes = eyes

    def set_hairs(self, hairs: str):
        """Set the hair color of the King."""
        self.hairs = hairs
