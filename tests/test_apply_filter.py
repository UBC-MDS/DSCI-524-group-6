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
            tolerance = 0.5
            test_image_opened = mpimg.imread(test_image)
      return TestData

@pytest.mark.usefixtures("test_data")
class TestApplyFilter:
      def test_apply_filter_red(self, test_data):
            
            created_image = apply_filter(image=test_data.test_image_opened, method="red", degree=test_data.test_degree)
            
            assert np.allclose(created_image[:,:,0], (test_data.test_image_opened[:, :, 0] * test_data.test_degree), atol=test_data.tolerance)
            assert np.allclose(created_image[:,:,1], (test_data.test_image_opened[:, :, 1] * (1-test_data.test_degree)), atol=test_data.tolerance)
            assert np.allclose(created_image[:,:,2], (test_data.test_image_opened[:, :, 2] * (1-test_data.test_degree)), atol=test_data.tolerance)

      def test_apply_filter_blue(self, test_data):
            created_image = apply_filter(image=test_data.test_image_opened, method="blue", degree=test_data.test_degree)
            
            assert np.allclose(created_image[:,:,0], (test_data.test_image_opened[:, :, 0] * (1-test_data.test_degree)), atol=test_data.tolerance)
            assert np.allclose(created_image[:,:,1], (test_data.test_image_opened[:, :, 1] * (1-test_data.test_degree)), atol=test_data.tolerance)
            assert np.allclose(created_image[:,:,2], (test_data.test_image_opened[:, :, 2] * test_data.test_degree), atol=test_data.tolerance)

      def test_apply_filter_green(self, test_data):
            created_image = apply_filter(image=test_data.test_image_opened, method="green", degree=test_data.test_degree)
            
            assert np.allclose(created_image[:,:,0], (test_data.test_image_opened[:, :, 0] * (1-test_data.test_degree)), atol=test_data.tolerance)
            assert np.allclose(created_image[:,:,1], (test_data.test_image_opened[:, :, 1] * test_data.test_degree), atol=test_data.tolerance)
            assert np.allclose(created_image[:,:,2], (test_data.test_image_opened[:, :, 2] * (1-test_data.test_degree)), atol=test_data.tolerance)

      def test_apply_filter_sepia(self, test_data):
            created_image = apply_filter(image=test_data.test_image_opened, method="sepia", degree=test_data.test_degree)
            
            assert np.allclose(created_image[::,::,0], ((test_data.test_image_opened[::, ::, 0] * 0.786 * test_data.test_degree) + (test_data.test_image_opened[::, ::, 1] * 0.769) + (test_data.test_image_opened[::, ::, 2] * 0.189)), atol=test_data.tolerance)
            assert np.allclose(created_image[::,::,1], ((test_data.test_image_opened[::, ::, 0] * 0.349 * test_data.test_degree) + (test_data.test_image_opened[::, ::, 1] * 0.686) + (test_data.test_image_opened[::, ::, 2] * 0.168)), atol=test_data.tolerance)
            assert np.allclose(created_image[::,::,2], ((test_data.test_image_opened[::, ::, 0] * 0.272 * test_data.test_degree) + (test_data.test_image_opened[::, ::, 1] * 0.534) + (test_data.test_image_opened[::, ::, 2] * 0.131)), atol=test_data.tolerance)

      def test_apply_filter_gray(self, test_data):
            created_image = apply_filter(image=test_data.test_image_opened, method="gray", degree=test_data.test_degree)
            
            assert np.allclose(created_image[:,:,0], (test_data.test_image_opened[:, :, 0] * (1-test_data.test_degree)), atol=test_data.tolerance)
            assert np.allclose(created_image[:,:,1], (test_data.test_image_opened[:, :, 1] * (1-test_data.test_degree)), atol=test_data.tolerance)
            assert np.allclose(created_image[:,:,2], (test_data.test_image_opened[:, :, 2] * (1-test_data.test_degree)), atol=test_data.tolerance)

      def test_apply_filter_raise_exception(self, test_data):
            with pytest.raises(Exception, match="Degree of filter shouldn't be smaller than 0.5."):
                  apply_filter(test_data.test_image_opened, "green", 0.3)

      def test_apply_filter_raise_valueerror(self, test_data):
            with pytest.raises(ValueError, match="Method is not an accepted type."):
                  apply_filter(test_data.test_image_opened, "violet")