import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from pythoshop.pythoshop import *

adjust_aspect_ratio("mds_logo.png", 100, 100, "crop")

