import pytest
from msf_2024.add import add

def test_add():
    # Test case 1: Positive numbers
    result = add(2, 3)
    assert result == 5, "Addition of positive numbers failed"

    # Test case 2: Negative numbers
    result = add(-5, -7)
    assert result == -12, "Addition of negative numbers failed"

    # Test case 3: Zero
    result = add(0, 0)
    assert result == 0, "Addition of zero failed"

    # Test case 4: Decimal numbers
    result = add(3.14, 2.86)
    assert result == pytest.approx(6.0), "Addition of decimal numbers failed"

    # Test case 5: Large numbers
    result = add(10**9, 10**9)
    assert result == 2 * (10**9), "Addition of large numbers failed"