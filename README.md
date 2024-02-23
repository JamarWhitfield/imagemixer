## Image Mixer

This Python script generates synthetic images by adding random shapes to blank images. The purpose of this script is to create a dataset for testing computer vision algorithms or generating training data for machine learning models.

### How It Works

The script utilizes the Python Imaging Library (PIL) to create blank images and add shapes such as triangles, circles, and squares to them. Each shape is randomly positioned within the image, and its color is chosen randomly from a grayscale spectrum. The number of shapes added to each image is also randomized.

### Functionality

The script contains the following functionality:

- **add_shapes**: This function takes an image and adds a specified number of random shapes to it. Shapes can be triangles, circles, or squares, each filled with a randomly chosen grayscale color.

- **Main loop**: The main loop of the script iterates a specified number of times to create multiple synthetic images. For each iteration, a blank image is created, shapes are added to it using the `add_shapes` function, and the resulting image is saved with a unique filename.

### Usage

To use this script, follow these steps:

1. Ensure you have Python installed on your system.
2. Install the required Python libraries by running:
   ```bash
   pip install Pillow numpy
   ```
3. Download the script (`img_processor.py`) to your local machine.
4. Customize the script as needed:
   - **Adjusting Resolution**: You can adjust the resolution of the output images by modifying the parameters passed to `Image.new('RGBA', (1920, 1080), (255, 255, 255, 255))`. Change the `(1920, 1080)` values to your desired width and height.
   - **Number of Images**: Change the number of images produced by modifying the range in the main loop. For example, to create 30 images, change `range(20)` to `range(30)`.
5. Run the script using Python:
   ```bash
   python img_processor.py
   ```
6. Synthetic images will be generated and saved in the specified directory.

### Output

The script saves the generated images in PNG format with filenames in the format `output_{i}.png`, where `{i}` is a unique identifier for each image.
