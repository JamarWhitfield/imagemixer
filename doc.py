from PIL import Image

def compose_images(background, layers, output_path, rotations=None, scales=None):
    """
    Compose an image from multiple PNG layers onto a background image with options to rotate and scale.

    Parameters:
        background (str): File path to the background image (PNG).
        layers (list): List of file paths to the layer images (PNG).
        output_path (str): File path to save the composed image.
        rotations (list, optional): List of rotation angles in degrees for each layer. Default is None.
        scales (list, optional): List of scale factors for each layer. Default is None.

    Usage examples:
        background_image = "background.png"
        layer_images = ["layer1.png", "layer2.png"]
        output_image = "composed_image.png"
        rotations = [0, 45]  # Rotation angles in degrees for each layer
        scales = [1.0, 0.5]  # Scale factors for each layer

        # Compose images with rotations and scales applied
        compose_images(background_image, layer_images, output_image, rotations, scales)

        # Compose images without rotations and scales
        compose_images(background_image, layer_images, output_image)
    """
    base_img = Image.open(background).convert('RGBA')
    composite_img = Image.new('RGBA', base_img.size, (255, 255, 255, 0))
    
    for i, layer in enumerate(layers):
        layer_img = Image.open(layer).convert('RGBA')
        
        if rotations and i < len(rotations):
            layer_img = layer_img.rotate(rotations[i], expand=True)
        
        if scales and i < len(scales):
            layer_img = layer_img.resize((int(layer_img.width * scales[i]), int(layer_img.height * scales[i])), Image.ANTIALIAS)
        
        composite_img = Image.alpha_composite(composite_img, layer_img)
    
    composed_img = Image.alpha_composite(base_img, composite_img)
    composed_img.save(output_path)

# Example usage:
# See docstring above for usage examples.
