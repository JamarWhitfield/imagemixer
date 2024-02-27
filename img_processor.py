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
    