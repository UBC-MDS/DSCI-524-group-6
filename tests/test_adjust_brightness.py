import pytest
from pythoshop.adjust_brightness import adjust_brightness
import matplotlib.image as mpimg
import numpy as np

@pytest.fixture(scope="class")
def test_data():
    """
    A pytest fixture that provides test data for the adjust_brightness tests.

    It includes:
    - A test image loaded into a numpy array.
    - Various brightness factors for testing different brightness adjustments.
    """
    class TestData:
        test_image = mpimg.imread("tests/test_img_1.png")
        brightness_factor = 0.5  # 50% increase in brightness
        decrease_factor = -0.3   # 30% decrease in brightness
        no_change_factor = 0.0   # No change in brightness
        invalid_factor = "invalid"  # Non-numeric value
    return TestData

@pytest.mark.usefixtures("test_data")
class TestAdjustBrightness:
    """
    A collection of tests for the `adjust_brightness` function.
    
    These tests cover various scenarios including brightness increases, decreases,
    invalid inputs, and ensuring that no changes occur when the factor is zero.
    """

    def test_brightness_adjustment(self, test_data):
        """Test that brightness increases when a positive factor is provided."""
        original_img = test_data.test_image
        adjusted_img = adjust_brightness(original_img, test_data.brightness_factor)
        assert np.mean(adjusted_img) > np.mean(original_img), "Image is not brighter after adjustment"

    def test_brightness_decrease(self, test_data):
        """Test that brightness decreases when a negative factor is provided."""
        original_img = test_data.test_image
        adjusted_img = adjust_brightness(original_img, test_data.decrease_factor)
        assert np.mean(adjusted_img) < np.mean(original_img), "Image is not dimmer after adjustment"

    def test_no_brightness_change(self, test_data):
        """Test that the image remains unchanged when the factor is zero."""
        original_img = test_data.test_image
        adjusted_img = adjust_brightness(original_img, test_data.no_change_factor)
        assert np.array_equal(original_img, adjusted_img), "Image should remain unchanged with zero brightness adjustment"

    def test_positive_integer_brightness_increase(self, test_data):
        """Test increasing brightness with a positive integer factor."""
        adjusted_img = adjust_brightness(test_data.test_image, 50) 
        assert np.mean(adjusted_img) > np.mean(test_data.test_image), "Image is not brighter after adjustment"

    def test_negative_integer_brightness_decrease(self, test_data):
        """Test decreasing brightness with a negative integer factor."""
        adjusted_img = adjust_brightness(test_data.test_image, -50) 
        assert np.mean(adjusted_img) < np.mean(test_data.test_image), "Image is not dimmer after adjustment"

    def test_invalid_brightness_factor(self, test_data):
        """Test that an error is raised when the brightness factor is not a number."""
        with pytest.raises(ValueError) as excinfo:
            adjust_brightness(test_data.test_image, test_data.invalid_factor)
        assert "Brightness factor must be an integer or float" in str(excinfo.value)
