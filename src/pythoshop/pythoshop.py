def adjust_aspect_ratio(image_path: str, height: int, width: int, method: str = 'crop'):
    """
    Adjust Aspect Ratio Function

    This function takes an image path and adjusts the image to have a uniform aspect ratio
    based on the specified method.

    Parameters:
    -------
    - image_path (str): The path to the input image.
    - height (int): The desired height for the image.
    - width (int): The desired width for the image.
    - method (str, optional): The method to obtain the desired image dimensions. ex: crop, resize
      Options: 'crop' (default) for cropping to the specified dimensions,
      'resize' for resizing/scaling to the specified dimensions.

    Returns:
    -------
    None
        The adjusted image is saved as a .png file at the same location as the input with "_adj_img" appended
        to the original filename.
    Raises
    ------
    IOError
        If the image file cannot be opened or saved.

    Example:
    >>> input_path = "path/to/input_image.jpg"
    >>> adjust_aspect_ratio(input_path, height=200, width=200, method='crop')
    """
    pass
    # Return the modified image as a NumPy array
