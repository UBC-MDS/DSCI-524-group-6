import unittest
import os
import tempfile
import shutil
import matplotlib.pyplot as plt
import numpy as np
from pythoshop.transform_image import transform_image 

class TestResizeImageFunction(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    def test_rotate_horizontal(self):
        # Create a test image with known dimensions
        test_image_path = os.path.join(self.temp_dir, 'test_rotate.png')
        img = np.ones((300, 400, 3), dtype=np.uint8) * 255 
        plt.imsave(test_image_path, img)

        # Rotate Image
        transform_image(test_image_path, method = 'flip', direction = 'horizontal')

        # Check if the rotated image has the correct dimensions
        rotated_img = plt.imread(os.path.join(self.temp_dir, 'test_image_flip_h_img.png'))
        self.assertEqual(rotated_img.shape[0], 400)
        self.assertEqual(rotated_img.shape[1], 300)

    def test_rotate_horizontal(self):
        # Create a test image with known dimensions
        test_image_path = os.path.join(self.temp_dir, 'test_rotate.png')
        img = np.ones((300, 400, 3), dtype=np.uint8) * 255 
        plt.imsave(test_image_path, img)

        # Rotate Image
        transform_image(test_image_path, method = 'flip', direction = 'horizontal')

        # Check if the rotated image has the correct dimensions
        rotated_img = plt.imread(os.path.join(self.temp_dir, 'test_image_flip_h_img.png'))
        self.assertEqual(rotated_img.shape[0], 400)
        self.assertEqual(rotated_img.shape[1], 300)

    def test_rotate_horizontal(self):
        # Create a test image with known dimensions
        test_image_path = os.path.join(self.temp_dir, 'test_rotate.png')
        img = np.ones((300, 400, 3), dtype=np.uint8)
        plt.imsave(test_image_path, img)

        # Rotate Image
        transform_image(test_image_path, method = 'flip', direction = 'horizontal')

        # Check if the rotated image has the correct dimensions
        rotated_img = plt.imread(os.path.join(self.temp_dir, 'test_image_flip_h_img.png'))
        self.assertEqual(rotated_img.shape[0], 400)
        self.assertEqual(rotated_img.shape[1], 300)

if __name__ == '__main__':
    unittest.main()