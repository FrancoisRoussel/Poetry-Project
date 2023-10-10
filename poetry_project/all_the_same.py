def all_the_same_compute(elements):
    if type(elements) != list:
        return False
    if len(elements) == 0 or len(elements) == 1:
        return True
    if elements[-1] == elements[-2]:
        return all_the_same_compute(elements[:-2])
    else:
        return False

