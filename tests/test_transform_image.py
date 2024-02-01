import matplotlib.image as img
import numpy as np
from pythoshop.transform_image import *
import unittest

class TestTransformImage(unittest.TestCase):
      '''
      Tests function transform_image.py
      '''
      def setUp(self):
            self.test_image = np.ones((300, 400, 3), dtype=np.uint8) * 255
            self.height, self.width = self.test_image.shape[:2]
      
      def test_rotate(self):
            created_image = transform_image(image = self.test_image)
            transform_height, transform_width = created_image.shape[:2]
            self.assertEqual(self.height, transform_width)
            self.assertEqual(self.width, transform_height)
      
            created_image = transform_image(image = self.test_image, direction = "counterclockwise")
            transform_height, transform_width = created_image.shape[:2]
            self.assertEqual(self.height, transform_width)
            self.assertEqual(self.width, transform_height)

      def test_flip(self):
            created_image = transform_image(image = self.test_image, method = "flip", direction = "vertical")
            transform_height, transform_width = created_image.shape[:2]
            self.assertEqual(self.height, transform_height)
            self.assertEqual(self.width, transform_width)
      
            created_image = transform_image(image = self.test_image, method = "flip", direction = "horizontal")
            transform_height, transform_width = created_image.shape[:2]
            self.assertEqual(self.height, transform_height)
            self.assertEqual(self.width, transform_width)
     
      def test_transform_raises_value_error(self):
            with self.assertRaises(ValueError):
                  transform_image(image = self.test_image, method = "flip", direction = "clockwise")
                  transform_image(image = self.test_image, method = "flip", direction = "counterclockwise")
                  transform_image(image = self.test_image, method = "rotate", direction = "vertical")
                  transform_image(image = self.test_image, method = "rotate", direction = "horizontal")
      

if __name__ == '__main__':
    unittest.main()
