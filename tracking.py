# Part of OpenCV Library
import cv2
# This is a separate package which will help track gestures and various other hand symbols
from cvzone.HandTrackingModule import HandDetector

# OpenCV video capture from default camera (camera index 0)
capture = cv2.VideoCapture(0)

# This initializes the HandDector object, and we specify that the maximum number of objects to detect is 1
detector = HandDetector(maxHands=1)

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
        crop = img[y:y+h, x:x+w] # Crop frame according to width and height
        cv2.imshow("Cropped Video", crop) # Display the cropped video

    cv2.imshow("Video", img) # Display the original video
    cv2.waitKey(1) # Wait for a key event with a 1 ms delay