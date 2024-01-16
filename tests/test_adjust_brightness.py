import os
import pytest
from pythoshop.adjust_brightness import adjust_brightness
import matplotlib.image as mpimg
import numpy as np

# Test for correct brightness adjustment
def test_brightness_adjustment():
    """Test if the brightness adjustment is correct."""
    test_image_path = "tests/test_img_1.png"
    brightness_factor = 0.5  # 50% increase in brightness
    expected_output_path = os.path.splitext(test_image_path)[0] + "_brightened.png"

    # Ensure the output file doesn't exist before testing
    if os.path.exists(expected_output_path):
        os.remove(expected_output_path)

    original_img = mpimg.imread(test_image_path)
    adjust_brightness(test_image_path, brightness_factor)
    adjusted_img = mpimg.imread(expected_output_path)

    # Assert that the adjusted image is brighter than the original
    assert np.mean(adjusted_img) > np.mean(original_img), "Image is not brighter after adjustment"

    # Cleanup
    os.remove(expected_output_path)

# Test for error handling with invalid brightness_factor
def test_invalid_brightness_factor():
    """Test handling of invalid brightness_factor input."""
    test_image_path = "tests/test_img_1.png"
    invalid_factor = "invalid"  # Non-numeric value

    with pytest.raises(ValueError) as excinfo:
        adjust_brightness(test_image_path, invalid_factor)

    assert "Brightness factor must be an integer or float" in str(excinfo.value)

# Run the tests with pytest from the command line:
# $ pytest tests/
