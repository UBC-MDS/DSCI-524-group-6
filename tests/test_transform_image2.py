import matplotlib.image as img
import numpy as np
from pythoshop import pythoshop
from pythoshop.transform_image import *
import unittest
import os

class TestTransformImage(unittest.TestCase):
    def setUp(self):
        self.test_path = "/tests/mds_logo.png"
        self.test_image = img.imread(os.getcwd() + self.test_path)
        self.expected_path = "/tests/mds_logo_trns_img.png"
        self.height, self.width = self.test_image.shape[:2]       

    def test_rotate(self):
            transform_image(image_path = self.test_path)
            try:
                  created_image = img.imread(os.getcwd() + self.expected_path)
                  transform_height, transform_width = created_image.shape[:2]
            except:
                  raise Exception("Image not saved to expected path.")

            self.assertEqual(self.height, transform_width)
            self.assertEqual(self.width, transform_height)
            
            os.remove(os.getcwd() + self.expected_path)
    
    def test_flip(self):
            transform_image(image_path = self.test_path, method = "flip", direction = "vertical")
            try:
                  created_image = img.imread(os.getcwd() + self.expected_path)
                  transform_height, transform_width = created_image.shape[:2]
            except:
                  raise Exception("Image not saved to expected path.")

            self.assertEqual(self.height, transform_height)
            self.assertEqual(self.width, transform_width)

            os.remove(os.getcwd() + self.expected_path)

if __name__ == '__main__':
    unittest.main()
