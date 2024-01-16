import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from pythoshop.pythoshop import *
from pythoshop.adjust_brightness import *

adjust_aspect_ratio("test_img_1.png", 800, 700, "crop")
adjust_brightness("test_img_1.png", 0.3)
