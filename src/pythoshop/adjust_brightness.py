import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import os

def adjust_brightness(image_path, brightness_factor):
    """
    Adjust the brightness of an image and save the result.

    This function changes the brightness of an input image by a specified factor. The factor can be 
    positive to increase brightness or negative to decrease it. The brightness change is applied 
    uniformly to all pixels of the image.

    Parameters
    ----------
    image_path : str
        The file path to the image that needs brightness adjustment. The image can be in .jpg or .png format.
    brightness_factor : int or float
        A value that determines the amount by which to adjust the brightness. Positive values increase 
        brightness, while negative values decrease it.

    Returns
    -------
    None
        The adjusted image is saved as a .png file at the same location as the input with "_brightened" appended
        to the original filename.

    Raises
    ------
    IOError
        If the image file cannot be opened or saved.
    """
    if not isinstance(brightness_factor, (int, float)):
        raise ValueError("Brightness factor must be an integer or float")

    try:
        # Read the image file using matplotlib
        img = mpimg.imread(image_path)

        # Check if brightness_factor is integer or float and adjust brightness accordingly
        if isinstance(brightness_factor, int):
            # Adjust brightness for integer factor
            adjusted_img = np.clip(img.astype(np.int16) + brightness_factor, 0, 255).astype(np.uint8)
        elif isinstance(brightness_factor, float):
            # Adjust brightness for float factor
            adjusted_img = np.clip(img.astype(np.float32) * (1 + brightness_factor), 0, 1)

        # Save the adjusted image
        new_image_path = os.path.splitext(image_path)[0] + "_brightness_changed.png"
        mpimg.imsave(new_image_path, adjusted_img)

    except FileNotFoundError as fnf_error:
        raise FileNotFoundError(fnf_error)
    except Exception as e:
        raise IOError(f"Error processing the image: {e}")

# Example usage:
# Note: You can use this function by providing a valid image path and a brightness factor.
# adjust_brightness('path/to/image.jpg', 0.3)  # Increase brightness by 30%
# adjust_brightness('path/to/image.png', -50)  # Decrease brightness by 50 units