from PIL import Image, ImageDraw
import numpy as np
import random

def process_image(image_path):
    img = Image.open(image_path).convert('RGBA')
    img_array = np.array(img)
    white_mask = np.all(img_array[:, :, :3] == [255, 255, 255], axis=-1)
    alpha = np.where(white_mask, 0, 255)
    img_array[:, :, 3] = alpha
    return Image.fromarray(img_array, 'RGBA')

def add_shapes(img, num_shapes):
    draw = ImageDraw.Draw(img)
    width, height = img.size
    for _ in range(num_shapes):
        shape = random.choice(['rectangle', 'circle', 'ellipse', 'triangle', 'square'])
        size = random.randint(1, 5)
        x = random.randint(0, width - size)
        y = random.randint(0, height - size)
        if shape == 'rectangle':
            draw.rectangle([x, y, x + size, y + size], fill=(0, 0, 0, 255))
        elif shape == 'circle':
            draw.ellipse([x, y, x + size, y + size], fill=(0, 0, 0, 255))
        elif shape == 'ellipse':
            draw.ellipse([x, y, x + size + 2, y + size], fill=(0, 0, 0, 255))
        elif shape == 'triangle':
            draw.polygon([(x, y), (x + size, y + size), (x - size, y + size)], fill=(0, 0, 0, 255))
        elif shape == 'square':
            draw.rectangle([x, y, x + size, y + size], fill=(0, 0, 0, 255))
    return img

for i in range(50):
    # Process the first image
    img1 = process_image('/Users/jamarw/Documents/GitHub/imagemixer/shapes.png')

    # Add more shapes to the first image
    img1 = add_shapes(img1, random.randint(200, 300))

    # Process the second image
    img2 = Image.open('/Users/jamarw/Documents/GitHub/imagemixer/shapes2.png').convert('RGBA')

    # Add more shapes to the second image
    img2 = add_shapes(img2, random.randint(200, 300))

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
    output_img.save(f'/Users/jamarw/Documents/GitHub/imagemixer/new/output_{i}.png')