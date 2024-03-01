'''
from PIL import Image, ImageDraw
import numpy as np
import random

# Function to add shapes to an image
def add_shapes(img, num_shapes):
    """
    Adds shapes to an image.

    Args:
    img (Image): The image to which shapes will be added.
    num_shapes (int): The number of shapes to add.

    Returns:
    Image: The image with added shapes.
    """
    draw = ImageDraw.Draw(img)
    width, height = img.size
    # Simple loop construct that creates a color and random number of shapes
    for _ in range(num_shapes):
        # Generate random grayscale color
        color = random.randint(0, 255)
        
        # Choose a random shape from triangle, circle, and square
        shape = random.choice(['triangle', 'circle', 'square'])
        
        size = random.randint(20, 30)
        x = random.randint(0, width - size)
        y = random.randint(0, height - size)
        
        if shape == 'triangle':
            draw.polygon([(x, y), (x + size, y + size), (x - size, y + size)], fill=(color, color, color, 255))
        elif shape == 'circle':
            draw.ellipse([x, y, x + size, y + size], fill=(color, color, color, 255))
        elif shape == 'square':
            draw.rectangle([x, y, x + size, y + size], fill=(color, color, color, 255))
    return img

# Main loop to create (n) images
for i in range(20):

    # Create a blank image with a resolution of 1080p 
    img = Image.new('RGBA', (1920, 1080), (255, 255, 255, 255))

    # Add more shapes to the image
    img = add_shapes(img, random.randint(50, 100))

    # Save the output image with a unique filename
    img.save(f'/Users/jwhitf/Documents/GitHub/imagemixer/lm/output_{i}.png')
'''

from PIL import Image, ImageDraw
import numpy as np
import random
import os

# Function to add shapes to an image with random grayscale color
def add_grayscale_shapes(img, num_shapes):
    """
    Adds shapes with random grayscale colors to an image.

    Args:
    img (Image): The image to which shapes will be added.
    num_shapes (int): The number of shapes to add.

    Returns:
    Image: The image with added shapes in random grayscale colors.
    """
    draw = ImageDraw.Draw(img)
    width, height = img.size
    for _ in range(num_shapes):
        # Generate random grayscale color
        color = random.randint(0, 255)
        
        # Choose a random shape from triangle, circle, and square
        shape = random.choice(['triangle', 'circle', 'square'])
        
        size = random.randint(20, 30)
        x = random.randint(0, width - size)
        y = random.randint(0, height - size)
        
        if shape == 'triangle':
            draw.polygon([(x, y), (x + size, y + size), (x - size, y + size)], fill=(color, color, color, 255))
        elif shape == 'circle':
            draw.ellipse([x, y, x + size, y + size], fill=(color, color, color, 255))
        elif shape == 'square':
            draw.rectangle([x, y, x + size, y + size], fill=(color, color, color, 255))
    return img

# Function to create colored version of an image with random RGB colors
def add_colored_version(grayscale_img):
    """
    Creates a colored version of a grayscale image by replicating its shapes with random RGB colors.

    Args:
    grayscale_img (Image): The grayscale image.

    Returns:
    Image: The colored version of the grayscale image with random RGB colors.
    """
    colored_img = grayscale_img.copy()
    draw = ImageDraw.Draw(colored_img)
    for x in range(colored_img.width):
        for y in range(colored_img.height):
            r, g, b, _ = grayscale_img.getpixel((x, y))
            color = random.randint(0, 255)
            draw.point((x, y), color)
    return colored_img

# Main loop to create (n) images
grayscale_output_folder = "/Users/jwhitf/Documents/GitHub/imagemixer/grayscale"  # Specify the grayscale folder path
#colored_output_folder = "/Users/jwhitf/Documents/GitHub/imagemixer/color"  # Specify the colored folder path
os.makedirs(grayscale_output_folder, exist_ok=True)  # Ensure the grayscale output folder exists
#os.makedirs(colored_output_folder, exist_ok=True)  # Ensure the colored output folder exists

for i in range(20):  # Generate 20 images
    # Create a blank grayscale image with a resolution of 1920x1080 pixels
    grayscale_img = Image.new('RGBA', (1920, 1080), (255, 255, 255, 255))

    # Add grayscale shapes to the image
    grayscale_img = add_grayscale_shapes(grayscale_img, random.randint(50, 100))

    # Save the output grayscale image with a unique filename in the grayscale folder
    grayscale_img.save(os.path.join(grayscale_output_folder, f'grayscale_output_{i}.png'))

    # Create a colored version of the grayscale image
    colored_img = add_colored_version(grayscale_img)

    # Save the output colored image with a unique filename in the colored folder
    colored_img.save(os.path.join(colored_output_folder, f'colored_output_{i}.png'))