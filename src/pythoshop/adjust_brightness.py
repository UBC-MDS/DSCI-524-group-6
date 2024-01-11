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
