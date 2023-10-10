from sun_angle import *

def test_sun_angle():
    assert sun_angle_compute("07:00") == 15
    assert sun_angle_compute("12:15") == 93.75
    assert sun_angle_compute([12:20]) == "Please put a string as an input"