def adjust_aspect_ratio(image_path: str, height: int, width: int, method: str = 'crop') -> str:
    """
    Adjust Aspect Ratio Function

    This function takes an image path and adjusts the image to have a uniform aspect ratio
    based on the specified method.

    Parameters:
    - image_path (str): The path to the input image.
    - height (int): The desired height for the image.
    - width (int): The desired width for the image.
    - method (str, optional): The method to obtain the desired image dimensions. ex: crop, resize
      Options: 'crop' (default) for cropping to the specified dimensions,
      'resize' for resizing/scaling to the specified dimensions.

    Returns:
    - np.ndarray: The modified image as a NumPy array with new aspect ratio.

    Example:
    >>> input_path = "path/to/input_image.jpg"
    >>> adjust_aspect_ratio(input_path, height=200, width=200, method='crop')
    """
    pass
    # Return the modified image as a NumPy array
