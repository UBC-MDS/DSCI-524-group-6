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
        A value(int) that determines the amount by which to adjust the brightness. Positive values increase 
        brightness, while negative values decrease it. The scale can be considered as a percentage if 
        a float is provided (e.g., 0.2 for a 20% increase) or as a direct addition/subtraction to the pixel
        values if an integer is provided.

    Returns
    -------
    None
        The adjusted image is saved as a .png file at the same location as the input with "_brightened" appended
        to the original filename.

    Raises
    ------
    IOError
        If the image file cannot be opened or saved.

    Examples
    --------
    To increase the brightness of 'photo.jpg' by 30%:
    >>> adjust_brightness('photo.jpg', 0.3)

    To decrease the brightness of 'image.png' by 50 units:
    >>> adjust_brightness('image.png', -50)
    """
    # Implementation of brightness adjustment goes here...
    pass

