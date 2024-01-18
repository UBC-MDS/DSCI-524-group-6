import unittest
import os
import tempfile
import shutil
import matplotlib.pyplot as plt
import numpy as np
from pythoshop.resize_image import resize_image  # Assuming your function is in a module named 'resize_image'

class TestResizeImageFunction(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for test images
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self):
        # Remove the temporary directory and its contents
        shutil.rmtree(self.temp_dir)

    def test_resize_crop(self):
        # Create a test image with known dimensions
        test_image_path = os.path.join(self.temp_dir, 'test_image_crop.jpg')
        img = np.ones((300, 400, 3), dtype=np.uint8) * 255  # White image
        plt.imsave(test_image_path, img)

        # Resize the image using the 'crop' method
        resize_image(test_image_path, height=200, width=200, method='crop', verbose=False)

        # Check if the resized image has the correct dimensions
        resized_img = plt.imread(os.path.join(self.temp_dir, 'test_image_crop_res_img.png'))
        self.assertEqual(resized_img.shape[0], 200)
        self.assertEqual(resized_img.shape[1], 200)
    
    def test_resize_maintain_aspect_ratio(self):
        # Create a test image with known dimensions
        test_image_path = os.path.join(self.temp_dir, 'test_image_maintain_aspect_ratio.jpg')
        img = np.ones((300, 400, 3), dtype=np.uint8) * 255  # White image
        plt.imsave(test_image_path, img)

        # Resize the image using the 'maintain_aspect_ratio' method
        resize_image(test_image_path, height=200, width=200, method='maintain_aspect_ratio', verbose=False)

        # Check if the resized image has the correct dimensions
        resized_img = plt.imread(os.path.join(self.temp_dir, 'test_image_maintain_aspect_ratio_res_img.png'))
        self.assertEqual(resized_img.shape[0], 200)
        self.assertGreaterEqual(resized_img.shape[1], 200)  # Width can be greater due to maintaining aspect ratio
    
    def test_resize_add_borders(self):
        # Create a test image with known dimensions
        test_image_path = os.path.join(self.temp_dir, 'test_image_add_borders.jpg')
        img = np.ones((1000, 1000, 3), dtype=np.uint8) * 255  # White image
        plt.imsave(test_image_path, img)

        # Resize the image using the 'add_borders' method
        resize_image(test_image_path, height=200, width=200, method='add_borders', verbose=False)

        # Check if the resized image has the correct dimensions
        resized_img = plt.imread(os.path.join(self.temp_dir, 'test_image_add_borders_res_img.png'))
        self.assertEqual(resized_img.shape[0], 200)
        self.assertEqual(resized_img.shape[1], 200)


if __name__ == '__main__':
    unittest.main()