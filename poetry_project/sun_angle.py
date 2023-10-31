"""sun_angle_compute function"""

def sun_angle_compute(time):
    """Compute the sun angle according to time input
    Args:
    - time: (str): hours:minutes display
    Returns:
    The angle of the sun in the sky (if we are at daytime).
    I don't see the sun otherwise.
    """

    if not isinstance(time,str):
        raise TypeError("Please put a string as an input")

    angle = (int(time[:2])-6)*15 + int(time[3:])*0.25
    if 0 <= angle <= 180:
        return angle
    return "I don't see the sun!"
