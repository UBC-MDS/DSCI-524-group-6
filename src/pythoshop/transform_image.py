import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

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
    img = mpimg.imread(image_path)

    new_image = img.copy()

    direction_options = {'flip': ['vertical', 'hrorizontal'], 'rotate': ['clockwise', 'counterclockwise']}

    if direction not in direction_options.method.value:
          raise ValueError("Please enter a compatable direction option. For rotating these are: clockwise or counterclockwise. For flipping these are: horizontal or vertical")
                
                
                

   
    
    
    
    new_image = np.clip(new_image, 0, 1)
    plt.imshow(new_image)
    plt.show()
    mpimg.imsave(f"{image_path}_filter_img.png", new_image)


def apply_filter(image_path, method, degree=0.7):
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
            Default is set as 0.7. 
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

      img = mpimg.imread(image_path)

      new_image = img.copy()

      if degree < 0.5:
            raise Exception("Degree of filter shouldn't be smaller than 0.5.")

      if method == "sepia":
            new_image[::, ::, 0] = (img[::, ::, 0] * 0.786 * degree) + (img[::, ::, 1] * 0.769) + (img[::, ::, 2] * 0.189)
            new_image[::, ::, 1] = (img[::, ::, 0] * 0.349 * degree) + (img[::, ::, 1] * 0.686) + (img[::, ::, 2] * 0.168)
            new_image[::, ::, 2] = (img[::, ::, 0] * 0.272 * degree) + (img[::, ::, 1] * 0.534) + (img[::, ::, 2] * 0.131)
      elif method == "blue":
            new_image[:, :, 0] = new_image[:, :, 0] * (1-degree)
            new_image[:, :, 1] = new_image[:, :, 1] * (1-degree)
            new_image[:, :, 2] = (img[:, :, 2] * (1 * degree if degree is not None else 0))
      elif method == "gray":
            new_image[:, :, 0] = (img[::, ::, 0] * (1-degree)) 
            new_image[:, :, 1] = (img[::, ::, 1] * (1-degree))
            new_image[:, :, 2] = (img[::, ::, 2] * (1-degree))
      elif method == "red":
            new_image[:, :, 0] = (img[:, :, 0] * (1 * degree if degree is not None else 0))
            new_image[:, :, 1] = new_image[:, :, 1] * (1-degree)
            new_image[:, :, 2] = new_image[:, :, 2] * (1-degree)
      elif method == "green":
            new_image[:, :, 0] = new_image[:, :, 0] * (1-degree)
            new_image[:, :, 1] = (img[:, :, 1] * (1 * degree if degree is not None else 0))
            new_image[:, :, 2] = new_image[:, :, 2] * (1-degree)
      else:
            raise ValueError("Method is not an accepted type.")

      new_image = np.clip(new_image, 0, 1)
      plt.imshow(new_image)
      plt.show()

      mpimg.imsave(f"{image_path}_filter_img.png", new_image)