# area_and_perimeter.py

def area_of_rectangle(width, height):
    """
    Calculate the area of a rectangle.

    Parameters:
    width (float): The width of the rectangle.
    height (float): The height of the rectangle.

    Returns:
    float: The area of the rectangle.
    
    Example usage:
    --------------
    # Example: Calculate the area of a rectangle with width 5.0 and height 3.0
    area = area_of_rectangle(5.0, 3.0)
    print(f"Area: {area}")  # Output: Area: 15.0
    """
    return width * height

def perimeter_of_rectangle(width, height):
    """
    Calculate the perimeter of a rectangle.

    Parameters:
    width (float): The width of the rectangle.
    height (float): The height of the rectangle.

    Returns:
    float: The perimeter of the rectangle.
    
    Example usage:
    --------------
    # Example: Calculate the perimeter of a rectangle with width 5.0 and height 3.0
    perimeter = perimeter_of_rectangle(5.0, 3.0)
    print(f"Perimeter: {perimeter}")  # Output: Perimeter: 16.0
    """
    return 2 * (width + height)




