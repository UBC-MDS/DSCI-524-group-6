import os
import pytest
from pythoshop.apply_filter import apply_filter
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

test_image = "tests/test_img_1.png"
wrong_image = "tests/test_img_1_non.png"

def test_apply_filter():
      test_degree = 0.6
      test_method = "red"
      test_image_opened = mpimg.imread(test_image)

      expected_image_path = f"{test_image}_filter_img.png"

      apply_filter(image_path=test_image, method=test_method, degree=test_degree)

      try:
            created_image = mpimg.imread(expected_image_path)
            plt.imshow(created_image)
            plt.show()
      except:
            raise Exception("Filter applied image is not saved at the right path.")
      
      print(created_image[:,:,0])
      print(test_image_opened[:, :, 0] * (1-test_degree))

      tolerance = 0.5
      
      assert np.allclose(created_image[:,:,0], (test_image_opened[:, :, 0] * (1-test_degree)), atol=tolerance)
      assert np.allclose(created_image[:,:,1], (test_image_opened[:, :, 1] * (1-test_degree)), atol=tolerance)
      assert np.allclose(created_image[:,:,2], (test_image_opened[:, :, 2] * test_degree), atol=tolerance)

      os.remove(expected_image_path)

def test_apply_filter_raise_exception():
      with pytest.raises(Exception, match="Degree of filter shouldn't be smaller than 0.5."):
            apply_filter(test_image, "green", 0.3)

def test_apply_filter_raise_valueerror():
      with pytest.raises(ValueError, match="Method is not an accepted type."):
            apply_filter(test_image, "violet")

def test_apply_filter_raise_filenotfounderror():
      with pytest.raises(FileNotFoundError, match="Your image is not found in the specified directory."):
            apply_filter(wrong_image, "violet")