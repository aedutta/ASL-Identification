import os
import cv2

folder_path = "Data/A"

# Loop through all the files in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        # Check if the file is a regular image (not resized)
        if not filename.endswith("_resized.jpg"):
            # Delete the regular image
            os.remove(file_path)
