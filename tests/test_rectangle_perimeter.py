from poetry_project.rectangle_perimeter import *

def test_rectangle_perimeter():
    assert rectangle_perimeter_compute(5,2) == 14
    assert rectangle_perimeter_compute(0,0) == 0
    #assert rectangle_perimeter_compute(-4,2) == 0