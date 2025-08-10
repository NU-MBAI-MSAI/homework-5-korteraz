def is_leap_year(year):
    """
    Determine if a year is a leap year.
    
    A leap year is a year that:
    - Is divisible by 4 and not by 100, OR
    - Is divisible by 100 and also divisible by 400
    
    Args:
        year (int): The year to check
        
    Returns:
        bool: True if the year is a leap year, False otherwise
    """
    return (year % 4 == 0 and year % 100 != 0) or \
        (year % 100 == 0 and year % 400 == 0)
