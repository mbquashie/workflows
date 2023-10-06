# area_and_perimeter.py

def area_of_rectangle(width, height):
    """
    Calculate the area of a rectangle.
    
    This function takes two numbers as input (width, height) and returns the area.
    
    Args:
        width (float or int): The width of the rectangle.
        height (float or int): The height of the rectangle.

    Returns:
        float or int: The area of the rectangle.

    Examples:
        >>> area_of_rectangle(3.0, 4.0)
        12.0
        >>> area_of_rectangle(2.5, 6.0)
        15.0
    """
    return width * height


def perimeter_of_rectangle(width, height):
    """
    Calculate the perimeter of a rectangle.
    
    This function takes two numbers as input (width, height) and returns the perimeter.
    
    Args:
        width (float or int): The width of the rectangle.
        height (float or int): The height of the rectangle.

    Returns:
        float or int: The perimeter of the rectangle.

    Examples:
        >>> perimeter_of_rectangle(3.0, 4.0)
        14.0
        >>> perimeter_of_rectangle(2.5, 6.0)
        17.0
    """
    return 2 * (width + height)




