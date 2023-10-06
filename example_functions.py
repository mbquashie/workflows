# All functions taken from "Python Numerical Methods", Kong, Siauw and Bayen 
# https://pythonnumericalmethods.berkeley.edu/notebooks/Index.html

def my_adder(a, b, c):
    """
    Calculate the sum of three numbers.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.
    c (int or float): The third number.

    Returns:
    int or float: The sum of a, b, and c.
    
    Example usage:
    --------------
    # Example: Calculate the sum of 1, 2, and 3
    result = my_adder(1, 2, 3)
    print(f"Sum: {result}")  # Output: Sum: 6
    """
    
    # Calculate the summation
    out = a + b + c
    
    return out


def my_thermo_stat(temp, desired_temp):
    """
    Determine the thermostat status based on the current temperature and desired temperature.

    Parameters:
    temp (int): The current temperature.
    desired_temp (int): The desired temperature.

    Returns:
    str: The thermostat status, which can be 'Heat', 'AC', or 'off'.
    
    Example usage:
    --------------
    # Example 1: It's colder than desired_temp - 5, so the status is 'Heat'
    status = my_thermo_stat(65, 70)
    print(f"Thermostat Status: {status}")  # Output: Thermostat Status: Heat

    # Example 2: It's hotter than desired_temp + 5, so the status is 'AC'
    status = my_thermo_stat(80, 72)
    print(f"Thermostat Status: {status}")  # Output: Thermostat Status: AC

    # Example 3: It's within the desired temperature range, so the status is 'off'
    status = my_thermo_stat(72, 72)
    print(f"Thermostat Status: {status}")  # Output: Thermostat Status: off
    """
    
    if temp < desired_temp - 5:
        status = 'Heat'
    elif temp > desired_temp + 5:
        status = 'AC'
    else:
        status = 'off'
    
    return status


def have_digits(s):
    """
    Check if a string contains digits.

    Parameters:
    s (str): The input string to check.

    Returns:
    int: 1 if the string contains digits, 0 otherwise.
    
    Example usage:
    --------------
    # Example 1: Check if the string contains digits
    contains_digits = have_digits("Hello123")
    print(f"Contains Digits: {contains_digits}")  # Output: Contains Digits: 1

    # Example 2: Check if the string contains digits (no digits in this case)
    contains_digits = have_digits("HelloWorld")
    print(f"Contains Digits: {contains_digits}")  # Output: Contains Digits: 0
    """
    
    out = 0
    
    # Loop through the string
    for c in s:
        # Check if the character is a digit
        if c.isdigit():
            out = 1
            break
            
    return out

 
