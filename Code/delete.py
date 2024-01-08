import os
import cv2

folder_path = "Data/Train/C"

for filename in os.listdir(folder_path):
    if not filename.startswith('C'):
        os.remove(os.path.join(folder_path, filename))
