
from PIL import Image
import numpy as np

# Open the image
img = Image.open('/Users/jamarw/Documents/GitHub/imagemixer/shapes.png').convert('RGBA')

# Create a numpy array from the image
img_array = np.array(img)

# Create a mask for the white background
white_mask = np.all(img_array[:, :, :3] == [255, 255, 255], axis=-1)

# Create a new alpha channel based on the white mask
alpha = np.where(white_mask, 0, 255)

# Apply the new alpha channel to the image
img_array[:, :, 3] = alpha

# Create a new image with the modified alpha channel
new_img = Image.fromarray(img_array, 'RGBA')

# Save the new image
new_img.save('/Users/jamarw/Documents/GitHub/imagemixer/transparent_shapes.png')


# Open the images
img1 = np.array(Image.open('/Users/jamarw/Documents/GitHub/imagemixer/transparent_shapes.png').convert('RGBA'))
img2 = np.array(Image.open('/Users/jamarw/Documents/GitHub/imagemixer/shapes2.png').resize(img1.shape[1::-1], Image.BILINEAR).convert('RGBA'))

# Create a new array for the combined image
combined_img = np.zeros_like(img1)

# Calculate the alpha channel for each image
alpha1 = img1[:, :, 3] / 255.0
alpha2 = img2[:, :, 3] / 255.0

# Calculate the combined alpha channel
combined_alpha = alpha1 + alpha2 * (1 - alpha1)

# Combine the RGB channels
for i in range(3):
    combined_img[:, :, i] = (img1[:, :, i] * alpha1 + img2[:, :, i] * alpha2 * (1 - alpha1)) / combined_alpha

# Combine the alpha channel
combined_img[:, :, 3] = combined_alpha * 255

# Create a PIL image from the combined array
output_img = Image.fromarray(combined_img.astype(np.uint8))

# Save the output image
output_img.save('/Users/jamarw/Documents/GitHub/imagemixer/output2.png')

