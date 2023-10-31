"""rectangle_perimeter_compute function"""

def rectangle_perimeter_compute(length: int, width: int) -> int:
    """Compute the perimeter of a rectangle:
    Args:
    - length: (int) length of the rectangle;
    - width: (int) width of the rectangle.
    Return: (int) perimeter of the rectangle.
    """
    if isinstance(length,int) and isinstance(width,int):
        return 2*length + 2*width
    raise ValueError("Length&width must be positive integers")
