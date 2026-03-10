from eva_data_analysis import text_to_duration, calculate_crew_size
import pytest

def test_text_to_duration_integer():
    """
    test that text_to_duration returns expected integer value when minutes are zero
    """
    assert text_to_duration("10:00") == 10

def test_text_to_duration_float():
    """
    Test that text_to_duration returns expected float value for typical durations with non-zero minute components
    """
    assert abs(text_to_duration("10:20") == pytest.approx(10.3333333))

@pytest.mark.parametrize("input_value, expected_result", [
    ("Bruce Willis;", 1),
    ("Bruce Willis; Bob Thornton;", 2),
    ("Bruce Willis; Bob Thornton; Ben Affleck;", 3),
])
def test_calculate_crew_size(input_value, expected_result):
    """
    test to check the calculate_crew_size function
    """
    actual_result = calculate_crew_size(input_value)
    assert actual_result == expected_result

test_text_to_duration_integer()
test_text_to_duration_float()