"""all_the_same function"""

def all_the_same_compute(elements):
    """Check if all the elements of a list are the same
    Args:
    elements: (list) list of integers.
    Returns: (bool) True or False.
    """
    
    if type(elements) != list:
        return False
    if len(elements) == 0 or len(elements) == 1:
        return True
    if elements[-1] == elements[-2]:
        return all_the_same_compute(elements[:-2])
    else:
        return False
