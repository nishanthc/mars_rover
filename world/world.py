class World:
    """
    Represents a grid-based world.

    Attributes:
    width (int): The width of the world.
    height (int): The height of the world.

    Methods:
    __init__(width, height): Initializes a new instance of the World class with the
     given width and height.
    """

    def __init__(self, width: int, height: int):
        """
        Initializes a new instance of the World class with the given width and height.

        Args:
        width (int): The width of the world.
        height (int): The height of the world.
        """

        # if width or height are not Integers then a TypeError is raised.
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")

        if height < 1:
            raise ValueError("the height of the world cannot be less than 1")

        if width < 1:
            raise ValueError("the width of the world cannot be less than 1")

        self.width: int = width
        self.height: int = height
