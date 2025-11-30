class calculator:
    """My calculator class"""

    def __init__(self, vector):
        """Constructor"""
        self.vector = vector

    def __add__(self, object) -> None:
        """Addition"""
        self.vector = [x + object for x in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        """Multiplication"""
        self.vector = [x * object for x in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        """Subtraction"""
        self.vector = [x - object for x in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        """Division"""
        if object == 0:
            print("Error: Division by zero")
            return
        self.vector = [x / object for x in self.vector]
        print(self.vector)
