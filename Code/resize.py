import os
import cv2

# Folder path containing the original images
input_folder = 'Data/C'

# Folder path that will save images. In this case, I made it the same folder. 
output_folder = 'Data/C'

# Desired size for resized images
target_size = (224, 224)

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    # Check if the file is an image (you can customize this check based on your file types)
    if filename.endswith('.jpg'):
        # Load image
        image = cv2.imread(os.path.join(input_folder, filename))

        # Resize image
        resized_image = cv2.resize(image, target_size)

        # Save resized image
        output_filename = os.path.splitext(filename)[0] + '_resized.jpg'  # Example: image.jpg -> image_resized.jpg
        cv2.imwrite(os.path.join(output_folder, output_filename), resized_image)