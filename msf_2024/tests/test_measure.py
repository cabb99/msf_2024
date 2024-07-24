import msf_2024
import numpy as np


def test_calculate_angle():
    r1 = np.array([0, 0, -1])
    r2 = np.array([0, 0, 0])
    r3 = np.array([1, 0, 0])

    expected_value = 90
    calculated_angle = msf_2024.calculate_angle(r1, r2, r3, degrees=True)
    assert calculated_angle == expected_value, "The calculated angle was wrong"
    calculated_angle = msf_2024.calculate_angle(r1, r2, r3, degrees=False)
    assert calculated_angle != expected_value, "The calculated angle was wrong"
