def format_string(name, age):
<<<<<<< HEAD
    #Create a formatted string using f-strings.
    
    format_string = f"Name: {name}, Age: {age}"
    print(format_string)
    
name = 'Aziz'
age = 39
format_string(name, age)

pass

def conditional_check():
    number = float(input("Please enter a number: "))
    if number > 10:
        print(f"{number} is greater than 10.")
    elif number < 10:
        print(f"{number} is less than 10.")
    else:
        print(f"{number} is equal to 10.")
conditional_check()
pass


n=int(input("Please enter the upper limit (n): ")) 
=======
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
        
        
>>>>>>> ffe4072 (revised assignment)
def loop_sum(n):
    """
    Calculate sum of numbers from 1 to n using a loop.
    Args:
        n (int): Upper limit
    Returns:
        int: Sum of numbers
    """
    total = 0 
<<<<<<< HEAD
    for i in range(1, n + 1): 
        total += i 
    return total 

result = loop_sum(n) 
print(f"The sum of all numbers between 0 and {n} is: {result}")
pass

=======
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
>>>>>>> ffe4072 (revised assignment)


def list_operations(numbers): 
    """ Perform operations on a list of numbers. 
    Args: 
        numbers (list): List of numbers Returns: 
        tuple: (sum, max, min) 
        """ 
<<<<<<< HEAD
    if not numbers: 
        return (0, None, None) 
=======
    #if not numbers: 
      #  return (0, None, None) 
>>>>>>> ffe4072 (revised assignment)
    total_sum = sum(numbers) 
    maximum = max(numbers) 
    minimum = min(numbers) 
    return (total_sum, maximum, minimum) 
<<<<<<< HEAD


numbers = [2, 4, 6, 8, 10] 
result = list_operations(numbers) 
print(result) 
pass

=======
>>>>>>> ffe4072 (revised assignment)


def dict_operations(students_dict):
    """
    Find students with scores above 80.
    Args:
        students_dict (dict): Dictionary of student names and scores
    Returns:
        list: Names of students with scores > 80
<<<<<<< HEAD
    """
    top_students = [name for name, score in students_dict.items() if score > 80] 
    return top_students 
#the names are just asumed
students_dict = { "Amina": 75, "Ali": 82, "Suzane": 90, "Angel": 68, "Aysha": 85, "Omar": 34 } 
top_students =  dict_operations(students_dict) 
print(top_students)
pass
=======
   
    students ={"John": 85,
    "Alice": 90,
    "Bob": 75,
    "Eve": 95}  """
    
    top_students = [name for name, score in students_dict.items() if score > 80] 
    return top_students 
>>>>>>> ffe4072 (revised assignment)


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
<<<<<<< HEAD


list1 = [2,4,6,8,10,12,14,16,18]
list2 = [1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17]
common_elements = set_operations(list1, list2)
print(common_elements)

pass

def arithmetic_ops(a, b):
    """
    Perform arithmetic operations.
    Args:
        a (float): First number
        b (float): Second number
    Returns:
        dict: Results of arithmetic operations
    """
    a = float(input("Please enter the first number: "))
    b = float(input("Please enter the second number: "))
    results = {
        'sum': a + b,
        'difference': a - b,
        'product': a * b,
    }
    return results

# Example usage
a = 10
b = 5
result = arithmetic_ops(a, b)
print(result)

pass

def logical_ops(x, y):
    """
    Perform logical operations.
    Args:
        x (bool): First boolean
        y (bool): Second boolean
    Returns:
        dict: Results of logical operations
    """
    results = {
    'AND': x and y,
    'OR': x or y,
    'NOT x': not x,
    'NOT y': not y,
    'XOR': x ^ y,
    'x == y': x == y,
    'x != y': x != y
}
    return results

# Example usage
x = True
y = False
result = logical_ops(x, y)
print(result)
pass

def bitwise_ops(a, b):
    """
    Perform bitwise operations.
    Args:
        a (int): First integer
        b (int): Second integer
    Returns:
        dict: Results of bitwise operations
    """
    a = int(input("Please enter the first number: "))
    b = int(input("Please enter the second number: "))
    results = {
        'AND': a & b,
        'OR': a | b,
        'XOR': a ^ b,
        'NOT a': ~a,
        'NOT b': ~b,
        'Left shift a by b': a << b,
        'Right shift a by b': a >> b
    }
    return results

result = bitwise_ops(a, b)
print(result)
pass
=======


>>>>>>> ffe4072 (revised assignment)
