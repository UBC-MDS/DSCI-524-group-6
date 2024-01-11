# Pythoshop

Pythoshop is a Python package designed to provide a set of handy image processing functions for simple yet effective adjustments to images. Whether you need to tweak brightness, adjust aspect ratios, transform images, or apply filters, Pythoshop has you covered.

## Functions

- **adjust_brightness(img_path, brightness_factor):**
  Adjusts the brightness of an image specified by the given image path. The `brightness_factor` parameter allows fine-tuning the brightness level.

- **adjust_aspect_ratio(img_path, height, width, method):**
  Modifies the aspect ratio of an image specified by the given image path. The function supports two methods: "crop" and "resize," providing flexibility in achieving the desired dimensions.

- **transform_image(img_path, method, direction):**
  Transforms an image based on the specified method and direction. Options include "rotate" or "flip", allowing users to orient images as needed.

- **apply_filter(img_path, method, degree):**
  Applies a filter to an image specified by the given image path. Users can choose from filter methods and adjust the degree of filtering to achieve the desired visual effect.


## Python Ecosystem Integration

Pythoshop complements existing image processing libraries in the Python ecosystem, offering a lightweight solution for common image adjustments. While other comprehensive libraries like Pillow and OpenCV provide extensive functionalities, Pythoshop focuses on simplicity and ease of use. If you need quick and straightforward image processing without the overhead of more extensive libraries, Pythoshop is the ideal choice.

### Related Packages:

- [Pillow](https://python-pillow.org/): A powerful image processing library in Python, providing comprehensive features for image manipulation and editing.

- [OpenCV](https://opencv.org/): An open-source computer vision and machine learning library, suitable for complex image processing tasks and computer vision applications.


## Installation

```bash
$ pip install pythoshop
```

## Usage

- TODO

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.


## Contributors

Salva Umar, Jenny Lee, Ella Hein, Runtian (Rachel) Li.

## License

`pythoshop` was created by Salva Umar, Jenny Lee, Ella Hein, Rachel Li. It is licensed under the terms of the MIT license.

## Credits

`pythoshop` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
