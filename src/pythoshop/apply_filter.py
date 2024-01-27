import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import os
import matplotlib

matplotlib.use('Agg') 

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
      FileNotFoundError
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
       
      try:
            img = mpimg.imread(image_path)
      except:
            raise FileNotFoundError("Your image is not found in the specified directory.")

      new_image = img.copy()

      if degree < 0.5:
            raise Exception("Degree of filter shouldn't be smaller than 0.5.")

      if method == "sepia":
            new_image[::, ::, 0] = (img[::, ::, 0] * 0.786 * degree) + (img[::, ::, 1] * 0.769) + (img[::, ::, 2] * 0.189)
            new_image[::, ::, 1] = (img[::, ::, 0] * 0.349 * degree) + (img[::, ::, 1] * 0.686) + (img[::, ::, 2] * 0.168)
            new_image[::, ::, 2] = (img[::, ::, 0] * 0.272 * degree) + (img[::, ::, 1] * 0.534) + (img[::, ::, 2] * 0.131)
      elif method == "blue":
            new_image[:, :, 0] = img[:, :, 0] * (1-degree)
            new_image[:, :, 1] = img[:, :, 1] * (1-degree)
            new_image[:, :, 2] = (img[:, :, 2] * (1 * degree if degree is not None else 0))
      elif method == "gray":
            new_image[:, :, 0] = (img[::, ::, 0] * (1-degree)) 
            new_image[:, :, 1] = (img[::, ::, 1] * (1-degree))
            new_image[:, :, 2] = (img[::, ::, 2] * (1-degree))
      elif method == "red":
            new_image[:, :, 0] = (img[:, :, 0] * (1 * degree if degree is not None else 0))
            new_image[:, :, 1] = img[:, :, 1] * (1-degree)
            new_image[:, :, 2] = img[:, :, 2] * (1-degree)
      elif method == "green":
            new_image[:, :, 0] = img[:, :, 0] * (1-degree)
            new_image[:, :, 1] = (img[:, :, 1] * (1 * degree if degree is not None else 0))
            new_image[:, :, 2] = img[:, :, 2] * (1-degree)
      else:
            raise ValueError("Method is not an accepted type.")

      new_image = np.clip(new_image, 0, 1)
      plt.imshow(new_image)
      plt.show()

      mpimg.imsave(f"{image_path}_filter_img.png", new_image)