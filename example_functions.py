# All functions taken from "Python Numerical Methods", Kong, Siauw and Bayen 
# https://pythonnumericalmethods.berkeley.edu/notebooks/Index.html

def my_adder(a, b, c):
    """
    Calculate the sum of three numbers.
    This function takes three numbers as input (a,b,c) and returns the the sum.
    
    Args:
        a (int or float): The first number.
        b (int or float): The second number.
        c (int or float): The third number.

    Returns:
         out (int or float): The sum of a, b, and c.
    
    Examples:
       >>> my_adder(1, 2, 3)
       6
       >>> my_adder(1.2, 3.1, 0.5)
       4.9
    """
    
    # Calculate the summation
    out = a + b + c
    
    return out


def my_thermo_stat(temp, desired_temp):
    """
    Adjusts the thermostat status based on the current temperature and desired temperature.

    This function determines the appropriate thermostat status (Heat, AC, or Off)
    based on the temperature and desired temperature settings.

    Args:
        temp (int): The current temperature in degrees Fahrenheit.
        desired_temp (int): The desired temperature in degrees Fahrenheit.

    Returns:
        str: The thermostat status, which can be 'Heat' (if temp is significantly lower
             than desired_temp), 'AC' (if temp is significantly higher than desired_temp),
             or 'Off' (if the current temperature is within 5 degrees of the desired temperature).

    Examples:
        >>> my_thermo_stat(70, 75)
        'Heat'
        >>> my_thermo_stat(80, 75)
        'AC'
        >>> my_thermo_stat(74, 75)
        'Off'
    """
    if temp < desired_temp - 5:
        status = 'Heat'
    elif temp > desired_temp + 5:
        status = 'AC'
    else:
        status = 'Off'
    return status


def have_digits(s):
    """
    This function checks if a string contains digits.

    Args:
        s (str): The input string to check.

    Returns:
           int: 1 if the string contains digits, 0 otherwise.
    
    Examples:
        >>> have_digits("Hello123")
        1
        >>> have_digits("HelloWorld")
        0
    """
    
    out = 0
    
    # Loop through the string
    for c in s:
        # Check if the character is a digit
        if c.isdigit():
            out = 1
            break
            
    return out


 
