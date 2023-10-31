"""test_sun_angle python file"""

from poetry_project.sun_angle import sun_angle_compute

def test_sun_angle():
    """Define the function to test the sun angle function"""
    assert sun_angle_compute("07:00") == 15
    assert sun_angle_compute("00:00") == "I don't see the sun!"
    assert sun_angle_compute(12) == "TypeError: Please put a string as an input"
