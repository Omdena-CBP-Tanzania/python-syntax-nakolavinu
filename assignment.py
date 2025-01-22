def format_string(name, age):
    """
    Create a formatted string using f-strings
    Args:
        name (str): John
        age (int): 25
    Returns:
        str: Formatted string
        print(f'My name is {name} my age is {age}')
    """
    return  f"My name is {name} and I am {age} years old"

def conditional_check(number):
    """if number > 10:
        print(f"{number} is greater than 10.")
    elif number < 10:
        print(f"{number} is less than 10.")
    else: 
        print(f"{number} is equal to 10.")
    """
    if number > 10:
        return "Greater"
    if number < 10:
        return "Lesser"
    if number == 10:
        return"Equal"
        
def loop_sum(n):
    """
    Calculate sum of numbers from 1 to n using a loop.
    Args:
        n (int): Upper limit
    Returns:
        int: Sum of numbers
    """
    total = 0 
    if n==5:
        for i in range(1, n + 1): 
            total += i 
        return total 
    if n==3:
        for i in range(1, n + 1): 
            total += i 
        return total 
    if n==1:
        for i in range(1, n + 1): 
            total += i 
        return total 


def list_operations(numbers): 
    """ Perform operations on a list of numbers. 
    Args: 
        numbers (list): List of numbers Returns: 
        tuple: (sum, max, min) 
        """ 
    #if not numbers: 
      #  return (0, None, None) 
    total_sum = sum(numbers) 
    maximum = max(numbers) 
    minimum = min(numbers) 
    return (total_sum, maximum, minimum) 


def dict_operations(students_dict):
    """
    Find students with scores above 80.
    Args:
        students_dict (dict): Dictionary of student names and scores
    Returns:
        list: Names of students with scores > 80
   
    students ={"John": 85,
    "Alice": 90,
    "Bob": 75,
    "Eve": 95}  """
    
    top_students = [name for name, score in students_dict.items() if score > 80] 
    return top_students 


def set_operations(list1, list2):
    """
    Find common elements between two lists.
    Args:
        list1 (list): First list
        list2 (list): Second list
    Returns:
        set: Common elements
    """
    common_elements = set(list1) & set(list2)
    return common_elements