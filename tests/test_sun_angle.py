from poetry_project.sun_angle import *

def test_sun_angle():
    assert sun_angle_compute("07:00") == 15
    assert sun_angle_compute("00:00") == "I don't see the sun!"
