from PIL import Image, ImageDraw
import numpy as np
import random

# Function to process images and convert white background to transparent
def process_image(image_path):
    """
    Opens an image and converts the white background to transparent.

    Args:
    image_path (str): The path to the image file.

    Returns:
    Image: The processed image with transparent background.
    """
    img = Image.open(image_path).convert('RGBA')
    img_array = np.array(img)
    # Create a mask for the white background
    white_mask = np.all(img_array[:, :, :3] == [255, 255, 255], axis=-1)
    alpha = np.where(white_mask, 0, 255)
    # Apply the new alpha channel to the image
    img_array[:, :, 3] = alpha
    return Image.fromarray(img_array, 'RGBA')

# Function to add shapes to an image
def add_shapes(img, num_shapes, clustered=False):
    """
    Adds shapes to an image.

    Args:
    img (Image): The image to which shapes will be added.
    num_shapes (int): The number of shapes to add.
    clustered (bool): Whether the shapes should be clustered.

    Returns:
    Image: The image with added shapes.
    """
    draw = ImageDraw.Draw(img)
    width, height = img.size
    for _ in range(num_shapes):
        shape = random.choice(['rectangle', 'circle', 'ellipse', 'triangle', 'square'])
        size = random.randint(1, 5)
        x = random.randint(0, width - size)
        y = random.randint(0, height - size)
        gap = random.randint(0, 2) if not clustered else 0  # Add a gap of 0-2 pixels unless clustered
        if shape == 'rectangle':
            draw.rectangle([x, y, x + size, y + size], fill=(0, 0, 0, 255))
        elif shape == 'circle':
            draw.ellipse([x, y, x + size, y + size], fill=(0, 0, 0, 255))
        elif shape == 'ellipse':
            draw.ellipse([x, y, x + size + gap, y + size], fill=(0, 0, 0, 255))
        elif shape == 'triangle':
            draw.polygon([(x, y), (x + size, y + size), (x - size, y + size)], fill=(0, 0, 0, 255))
        elif shape == 'square':
            draw.rectangle([x, y, x + size, y + size], fill=(0, 0, 0, 255))
    return img

# Main loop to create (n) images
for i in range(20):
    # Create a blank image with a resolution of 1080p 
    img1 = Image.new('RGBA', (1920, 1080), (255, 255, 255, 255))

    # Add more shapes to the first image, some clustered and some not
    img1 = add_shapes(img1, random.randint(200, 250), clustered=random.choice([True, False]))

    # Create a blank image with a resolution of 1080p
    img2 = Image.new('RGBA', (1920, 1080), (255, 255, 255, 255))

    # Add more shapes to the second image, some clustered and some not
    img2 = add_shapes(img2, random.randint(200, 250), clustered=random.choice([True, False]))

    # Resize the second image to match the size of the first image
    resized_img2 = img2.resize(img1.size, Image.BILINEAR)

    # Create a new array for the combined image
    combined_img = np.zeros_like(np.array(img1))

    # Calculate the alpha channel for each image
    alpha1 = np.array(img1)[:, :, 3] / 255.0
    alpha2 = np.array(resized_img2)[:, :, 3] / 255.0

    # Calculate the combined alpha channel
    combined_alpha = alpha1 + alpha2 * (1 - alpha1)

    # Combine the RGB channels
    for j in range(3):
        combined_img[:, :, j] = (np.array(img1)[:, :, j] * alpha1 + np.array(resized_img2)[:, :, j] * alpha2 * (1 - alpha1)) / combined_alpha

    # Combine the alpha channel
    combined_img[:, :, 3] = combined_alpha * 255

    # Create a PIL image from the combined array
    output_img = Image.fromarray(combined_img.astype(np.uint8), 'RGBA')

    # Save the output image with a unique filename
    output_img.save(f'/Users/jamarw/Documents/GitHub/imagemixer/n4/output_{i}.png')