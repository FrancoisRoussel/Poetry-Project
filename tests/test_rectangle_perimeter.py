"""test_rectangle_perimeter function"""

from poetry_project.rectangle_perimeter import rectangle_perimeter_compute

def test_rectangle_perimeter():
    """Define the function to test rectangle_perimeter function"""
    assert rectangle_perimeter_compute(5,2) == 14
    assert rectangle_perimeter_compute(0,0) == 0
    assert rectangle_perimeter_compute(-4,2) == "ValueError: Length and width must be positive integers"
    