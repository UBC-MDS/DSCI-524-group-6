import matplotlib.pyplot as plt
import numpy as np

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
    - IOError: If the image file cannot be opened or saved.

    Example:
    >>> input_path = "path/to/input_image.jpg"
    >>> resize_image(input_path, height=200, width=200, method='crop')
    """
    img = plt.imread(image_path)
    if verbose:
        print(f"Initial image dimensions: {img.shape}")

    if method == 'maintain_aspect_ratio':
        aspect_ratio = img.shape[1] / img.shape[0]
        new_width = int(height * aspect_ratio)
        new_img = plt.imshow(img, extent=(0, new_width, 0, height), aspect='auto')
    elif method == 'crop':
        new_img = plt.imshow(img[:height, :width], extent=(0, width, 0, height), aspect='auto')
    elif method == 'add_borders':
        aspect_ratio = img.shape[1] / img.shape[0]
        new_width = int(height * aspect_ratio)
        img = plt.resize(img, (new_width, height))

        # Initialize image with white background
        new_img = np.ones((height, width, img.shape[2])) * 255
        x_offset = (width - img.shape[1]) // 2
        y_offset = (height - img.shape[0]) // 2
        new_img[y_offset:y_offset+img.shape[0], x_offset:x_offset+img.shape[1], :] = img
        new_img = plt.imshow(new_img, extent=(0, width, 0, height), aspect='auto')
    else:
        raise ValueError("Invalid resize method. Supported methods: 'maintain_aspect_ratio', 'crop', 'add_borders'.")

    plt.axis('off')
    plt.savefig(f'{image_path[:-4]}_res_img.png')  # Save the resized image as a PNG file

    if verbose:
        print(f"Resized image saved as: {image_path[:-4]}_res_img.png")

    plt.show()  # Display the resized image
