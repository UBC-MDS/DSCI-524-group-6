import matplotlib.pyplot as plt 

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
    img = plt.imread(image_path)
    plt.imshow(img)

    if method == "crop":
        print("Current dimensions of Image:", img.shape[0], "x", img.shape[1])
        cropped_img = img[:height, :width, :]
        print("Cropped Dimensions:", cropped_img.shape[0], "x", cropped_img.shape[1])
        plt.imshow(cropped_img)
        plt.imsave(f"{image_path}_adj_img.png", cropped_img, origin='lower')
        plt.show()

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

def apply_filter(img_path: str, method: str, degree: float = 0.5):
    """
    Apply filter from a chosen range of colours. 

    This function allows a filter to be applied on the image which can be retrieved from 

    Parameters
    ----------
    image_path : str
        The file path to the image that needs brightness adjustment. The image can be in .jpg or .png format.
    method : str
        Choose from a list of available filters to be applied onto the image. 
    degree : int or float
        Degree to apply the filter on the image. Minimum value is 0 and maximum value is 1. 

    Returns
    -------
    None
        The filtered image is saved as a .png file at the same location as the input with "_filter_img" appended
        to the original filename.  

    Raises
    ------
    IOError
        If the image file cannot be opened or saved.

    ValueError
        If incorrect type of variables are used in parameters. 

    Examples
    --------
    To apply 'sephia' filter on 'photo.jpg' by 30%:
    >>> apply_filter('photo.jpg', 'sephia', 0.3)

    To apply 'aquamarine' filter on 'photo.jpg' by 70%:
    >>> apply_filter('photo.jpg', 'aquamarine', 0.7)
    """
    # Implementation of apply filter function goes here...
    pass


