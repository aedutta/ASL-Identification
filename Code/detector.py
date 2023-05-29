import cv2 # Part of OpenCV Library
from cvzone.HandTrackingModule import HandDetector # This is a separate package which will help track gestures and various other hand symbols
from cvzone.ClassificationModule import Classifier # This classifies the hand sign
import numpy as np
import time

# OpenCV video capture from default camera (camera index 0)
capture = cv2.VideoCapture(0)

# This initializes the HandDector object, and we specify that the maximum number of objects to detect is 1
detector = HandDetector(maxHands=1)
clasifier = Classifier("Model/keras_model.h5", "Model/labels.txt")

counter = 0

labels = ["A", "B", "C"]

# This loops a bunch of images to process the video
while True:
    # Read a frame from the video capture
    success, img = capture.read()

    # Detect hands in the frame with HandDetector
    hands, img = detector.findHands(img)

    # If the hand is detected
    if hands:
        hand = hands[0] # Get the only hand (0 index)
        x,y,w,h = hand['bbox'] # Extract the bounding box in terms of x, y coordinates and width (w) and height (h)
        
        # Add an offset to increase the size of the bounding box
        offset = 20
        x = max(0, x - offset)
        y = max(0, y - offset)
        w = min(img.shape[1], w + offset * 2)
        h = min(img.shape[0], h + offset * 2)

        crop = img[y:y+h, x:x+w] # Crop frame according to width and height

        # Calculate the scaling factor based on the larger dimension (width or height)
        scale_factor = max(w, h) / 224
        
        # Calculate the scaled width and height
        scaled_width = int(w / scale_factor)
        scaled_height = int(h / scale_factor)
        
        # Resize the cropped image using the calculated scaling factor, this will act to stop an error in the code where the cropped image is greater than the 224 x 224 size
        crop = cv2.resize(crop, (scaled_width, scaled_height))

        if hand['type'] == 'Left': # If the detected hand is a left hand, rotate the image by 180 degrees
            crop = cv2.flip(crop, flipCode=1) # this is in order to make all images detected the same

        # Create a white background of size 224x224 pixels, this will make all the images the same size
        background = np.zeros((224, 224, 3), dtype=np.uint8) + 255

        # Calculate the position to place the cropped image on the background
        x_offset = (224 - crop.shape[1]) // 2
        y_offset = (224 - crop.shape[0]) // 2
        
        # Place the cropped image on the background
        background[y_offset:y_offset+crop.shape[0], x_offset:x_offset+crop.shape[1]] = crop

        cv2.imshow("Cropped Video", background) # Display the cropped video

    cv2.imshow("Video", img) # Display the original video
