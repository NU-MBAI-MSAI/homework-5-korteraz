def date_format(date_string):
    """
    Convert a date from MM/DD/YYYY format to YYYY-MM-DD format.
    
    Args:
        date_string (str): Date in MM/DD/YYYY format
        
    Returns:
        str: Date in YYYY-MM-DD format
    """
    # Split the date string by '/'
    parts = date_string.split('/')
    
    # Extract month, day, and year
    month = parts[0]
    day = parts[1]
    year = parts[2]
    
    # Return in YYYY-MM-DD format
    return f"{year}-{month}-{day}"
