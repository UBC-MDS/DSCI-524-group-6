import os
import pytest
from pythoshop.adjust_brightness import adjust_brightness
import matplotlib.image as mpimg
import numpy as np

@pytest.fixture(scope="class")
def test_data():
    class TestData:
        test_image_path = "tests/test_img_1.png"
        brightness_factor = 0.5  # 50% increase in brightness
        decrease_factor = -0.3   # 30% decrease in brightness
        no_change_factor = 0.0   # No change in brightness
        invalid_factor = "invalid"  # Non-numeric value
    return TestData
@pytest.mark.usefixtures("test_data")
class TestAdjustBrightness:
    def test_brightness_adjustment(self, test_data):
        expected_output_path = os.path.splitext(test_data.test_image_path)[0] + ".png_brightness_changed.png"
        if os.path.exists(expected_output_path):
            os.remove(expected_output_path)
        original_img = mpimg.imread(test_data.test_image_path)
        adjust_brightness(test_data.test_image_path, test_data.brightness_factor)
        adjusted_img = mpimg.imread(expected_output_path)
        assert np.mean(adjusted_img) > np.mean(original_img), "Image is not brighter after adjustment"
        os.remove(expected_output_path)

    def test_max_brightness_adjustment(self, test_data):
        expected_output_path = os.path.splitext(test_data.test_image_path)[0] + ".png_brightness_changed.png"
        if os.path.exists(expected_output_path):
            os.remove(expected_output_path)
        original_img = mpimg.imread(test_data.test_image_path)
        adjust_brightness(test_data.test_image_path, 1.0)
        adjusted_img = mpimg.imread(expected_output_path)
        assert np.all(adjusted_img >= original_img), "Not all pixels are brighter or equal in the max brightness adjusted image"
        os.remove(expected_output_path)

    def test_brightness_decrease(self, test_data):
        expected_output_path = os.path.splitext(test_data.test_image_path)[0] + ".png_brightness_changed.png"
        if os.path.exists(expected_output_path):
            os.remove(expected_output_path)
        original_img = mpimg.imread(test_data.test_image_path)
        adjust_brightness(test_data.test_image_path, test_data.decrease_factor)
        adjusted_img = mpimg.imread(expected_output_path)
        assert np.mean(adjusted_img) < np.mean(original_img), "Image is not dimmer after adjustment"
        os.remove(expected_output_path)

    def test_no_brightness_change(self, test_data):
        expected_output_path = os.path.splitext(test_data.test_image_path)[0] + ".png_brightness_changed.png"
        if os.path.exists(expected_output_path):
            os.remove(expected_output_path)
        original_img = mpimg.imread(test_data.test_image_path)
        adjust_brightness(test_data.test_image_path, test_data.no_change_factor)
        adjusted_img = mpimg.imread(expected_output_path)
        assert np.array_equal(original_img, adjusted_img), "Image should remain unchanged with zero brightness adjustment"
        os.remove(expected_output_path)

    def test_invalid_brightness_factor(self, test_data):
        """Test whether the function throw an ValueError when it get an invalid datatype input"""
        with pytest.raises(ValueError) as excinfo:
            adjust_brightness(test_data.test_image_path, test_data.invalid_factor)
        assert "Brightness factor must be an integer or float" in str(excinfo.value)

    def test_image_file_not_found(self, test_data):
        """Test handling of a non-existent image file."""
        non_existent_image_path = "tests/non_existent_img.png"  # Updated path

        with pytest.raises(FileNotFoundError):  # Expect FileNotFoundError
            adjust_brightness(non_existent_image_path, test_data.brightness_factor)