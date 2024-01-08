import os
import cv2

# Folder path containing the original images
input_folder = 'Data/Test/B'

# Folder path that will save images. In this case, I made it the same folder.
output_folder = 'Data/Test/B'

# Desired size for resized images
target_size = (150, 150)

# Loop through all files in the input folder
counter = 1  # Initialize a counter for renaming images
for filename in os.listdir(input_folder):
    # Check if the file is an image (you can customize this check based on your file types)
    if filename.endswith('.jpg'):
        # Load image
        image = cv2.imread(os.path.join(input_folder, filename))

        # Resize image
        resized_image = cv2.resize(image, target_size)

        # Check if the image was resized correctly
        if resized_image.shape[:2] == target_size:
            # Save resized image with a numeric name (e.g., 1.jpg, 2.jpg, etc.)
            output_filename = f'A{counter}.jpg'
            cv2.imwrite(os.path.join(output_folder, output_filename), resized_image)
            counter += 1
        else:
            # Delete the image if it's not resized correctly
            os.remove(os.path.join(input_folder, filename))

print("Images have been renamed and non-resized images have been deleted.")
