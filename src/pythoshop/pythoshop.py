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

def transform_image(image_path: str, method: str = 'rotate', direction: str = 'clockwise'):
    """
    Transform Image Function
    This function takes an image path and either rotates or flips the image in a 
    specified direction. 
    
    Parameters:
    -------
    - image_path (str): The path to the input image.
    - method (str, optional): The method to transform the image. ex: rotate, flip
      Options: 'rotate' (default) for rotating in the specified direction (clockwise or counterclockwise),
      'flip' for flipping over the specified axis (horizontal or vertical).
    - direction (str, optional): The direction to transform the image. ex: (clockwise, counterclockwise, 
        vertical, horizontal)
        Options: 'clockwise' and 'counterclockwise' for rotating an image,
        'vertical' or 'horizontal' for the axis to flip the image over.
    
    Returns:
    -------
    None
        The adjusted image is saved as a .png file at the same location as the input with "_trns_img" appended
        to the original filename.
        
    Raises
    ------
    IOError
        If the image file cannot be opened or saved.
    
    ValueError
        If the method and direction are not compatible, ie method = 'flip', direction = 'clockwise',
        or the method or direction are not one of the options.
    
    Example:
    >>> input_path = 'path/to/input_image.jpg'
    >>> adjust_aspect_ratio(input_path, method = 'flip', direction = 'horizontal')
    """
    pass
    
    
