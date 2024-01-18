import os
import pytest
from pythoshop.apply_filter import apply_filter
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

@pytest.fixture(scope="class")
def test_data():
      class TestData:
            test_image = "tests/test_img_1.png"
            wrong_image = "tests/test_img_1_non.png"
            test_degree = 0.6
            test_method = "red"
      return TestData

@pytest.mark.usefixtures("test_data")
class TestApplyFilter:
      def test_apply_filter(self, test_data):

            test_image_opened = mpimg.imread(test_data.test_image)

            expected_image_path = f"{test_data.test_image}_filter_img.png"

            apply_filter(image_path=test_data.test_image, method=test_data.test_method, degree=test_data.test_degree)

            try:
                  created_image = mpimg.imread(expected_image_path)
            except:
                  raise Exception("Filter applied image is not saved at the right path.")

            tolerance = 0.5
            
            assert np.allclose(created_image[:,:,0], (test_image_opened[:, :, 0] * (1-test_data.test_degree)), atol=tolerance)
            assert np.allclose(created_image[:,:,1], (test_image_opened[:, :, 1] * (1-test_data.test_degree)), atol=tolerance)
            assert np.allclose(created_image[:,:,2], (test_image_opened[:, :, 2] * test_data.test_degree), atol=tolerance)

            os.remove(expected_image_path)

      def test_apply_filter_raise_exception(self, test_data):
            with pytest.raises(Exception, match="Degree of filter shouldn't be smaller than 0.5."):
                  apply_filter(test_data.test_image, "green", 0.3)

      def test_apply_filter_raise_valueerror(self, test_data):
            with pytest.raises(ValueError, match="Method is not an accepted type."):
                  apply_filter(test_data.test_image, "violet")

      def test_apply_filter_raise_filenotfounderror(self, test_data):
            with pytest.raises(FileNotFoundError, match="Your image is not found in the specified directory."):
                  apply_filter(test_data.wrong_image, "violet")