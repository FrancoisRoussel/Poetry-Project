from poetry_project.all_the_same import *

def test_all_the_same():
    assert all_the_same_compute([1, 1, 1]) == True
    assert all_the_same_compute([1, 2, 1]) == False
    assert all_the_same_compute([1, "a", 1]) == False
    assert all_the_same_compute([]) == True
    assert all_the_same_compute([1]) == True
    assert all_the_same_compute('not a list') == False