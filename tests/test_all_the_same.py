"""Testing the all_the_same function"""

from poetry_project.all_the_same import all_the_same_compute

def test_all_the_same():
    """Define the test function
    Args: None
    Returns: None"""
    assert all_the_same_compute([1, 1, 1]) is True
    assert all_the_same_compute([1, 2, 1]) is False
    assert all_the_same_compute([1, "a", 1]) is False
    assert all_the_same_compute([]) is True
    assert all_the_same_compute([1]) is True
    assert all_the_same_compute('not a list') is False
