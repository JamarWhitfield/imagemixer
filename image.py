from PIL import Image

def compose_images(background, layers, output_path, rotations=None, scales=None):
    # Open the background image
    base_img = Image.open(background).convert('RGBA')
    
    # Initialize a transparent layer to composite all images
    composite_img = Image.new('RGBA', base_img.size, (255, 255, 255, 0))
    
    for i, layer in enumerate(layers):
        # Open the layer image
        layer_img = Image.open(layer).convert('RGBA')
        
        # Rotate if specified
        if rotations and i < len(rotations):
            layer_img = layer_img.rotate(rotations[i], expand=True)
        
        # Scale if specified
        if scales and i < len(scales):
            layer_img = layer_img.resize((int(layer_img.width * scales[i]), int(layer_img.height * scales[i])), Image.ANTIALIAS)
        
        # Composite the layer onto the transparent image
        composite_img = Image.alpha_composite(composite_img, layer_img)
    
    # Composite the transparent image onto the background
    composed_img = Image.alpha_composite(base_img, composite_img)
    
    # Save the composed image
    composed_img.save(output_path)

# Example usage:
background_image = "background.png"
layer_images = ["layer1.png", "layer2.png"]
output_image = "composed_image.png"
rotations = [0, 45]  # Rotation angles in degrees for each layer
scales = [1.0, 0.5]  # Scale factors for each layer

compose_images(background_image, layer_images, output_image, rotations, scales)
