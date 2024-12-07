import os
from PIL import Image


for input_file in os.listdir('assets/img'):
    if not input_file.endswith('png') and '_squared' not in input_file:
        continue
    
    img = Image.open(f'assets/img/{input_file}')
    width, height = img.size



    # Determine the new size for a square image
    new_size = max(width, height)

    # Create a new white image
    new_img = Image.new('RGB', (new_size, new_size), (255, 255, 255))

    # Paste the original image onto the new image
    new_img.paste(img, ((new_size - width) // 2, (new_size - height) // 2))

    # Save the new image
    base_name, ext = os.path.splitext(input_file)
    output_file = f"assets/img/{input_file.split('.')[0]}_squared.png"

    # Save the new image
    new_img.save(output_file)


