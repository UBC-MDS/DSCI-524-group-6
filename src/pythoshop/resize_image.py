import matplotlib.pyplot as plt
import numpy as np
import os

def resize_image(image_path: str, height: int, width: int, method: str = 'crop', verbose: bool = True):
    """
    Image Resizing Function

    This function takes an image path and adjusts the image to have
    the inputted dimensions using the selected method.

    Parameters:
    - image_path (str): The path to the input image.
    - height (int): The desired height for the image.
    - width (int): The desired width for the image.
    - method (str, optional): The method to obtain the desired image dimensions.
      Options: 'maintain_aspect_ratio' (default) for maintaining the aspect ratio,
               'crop' for cropping to the specified dimensions,
               'add_borders' for adding borders to maintain the aspect ratio.
    - verbose (bool, optional): If True, print verbose information.

    Returns:
    - None
    The resized image is saved as a .png file at the same location as the input with "_res_img.png" appended
    to the original filename.

    Raises:

    - FileNotFoundError: If the specified file does not exist.
    - ValueError: If a method outside the available options is added

    Example:
    >>> input_path = "path/to/input_image.jpg"
    >>> resize_image(input_path, height=200, width=200, method='crop')
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"The file '{image_path}' does not exist.")
    
    img = plt.imread(image_path)
    if verbose:
        print(f"Initial image dimensions: {img.shape}")

    if method == 'maintain_aspect_ratio':
        aspect_ratio = img.shape[1] / img.shape[0]
        new_width = int(height * aspect_ratio)
        img = np.resize(img, (height, new_width, img.shape[2]))
    elif method == 'crop':
        img = img[:height, :width, :]
    elif method == 'add_borders':
        aspect_ratio = img.shape[1] / img.shape[0]
        new_width = int(height * aspect_ratio)
        img = np.resize(img, (height, new_width, img.shape[2]))

        # Initialize image with white background
        new_img = np.ones((height, width, img.shape[2])) * 255
        x_offset = (width - img.shape[1]) // 2
        y_offset = (height - img.shape[0]) // 2
        new_img[y_offset:y_offset+img.shape[0], x_offset:x_offset+img.shape[1], :] = img
        # Normalize the image values to the range [0, 1]
        new_img = new_img / 255.0
        img = new_img
    else:
        raise ValueError("Invalid resize method. Supported methods: 'maintain_aspect_ratio', 'crop', 'add_borders'.")

    plt.axis('off')
    save_img = img[:, :, :3] if img.shape[2] == 4 else img  # If the image has an alpha channel, discard it
    plt.imsave(f'{image_path[:-4]}_res_img.png', save_img, format='png')  # Save the resized image with higher resolution and tighter bounding box

    if verbose:
        print(f"Resized image saved as: {image_path[:-4]}_res_img.png")
        resized_img = plt.imread(f"{image_path[:-4]}_res_img.png")
        print("Resize Image Dimensions: ", resized_img.shape)
        
        if verbose:
            plt.imshow(img)  # Display the resized image
            plt.show()

