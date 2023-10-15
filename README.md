# ASL-Identification
My CS Project was to use machine learning/computer vision to classify American Sign Language. ASL is an expressive form of communication predominantly used by the deaf and hard-of-hearing community. This project aimed to bridge the communication gap between the ASL users and the broader population. The project involved collecting a comprehensive dataset of ASL gestures, training a classifier model, and evaluating its performance.

Throughout this project, I had to make several design choices to achieve the best results. I used the mediapipe library to detect if an object was a hand. After that, I wrote a code which would take several pictures from a running video and put it into several labeled datasets. After this, I decided to use tensorflow/keras to train the model. My design was inspired from other projects on YouTube that did similar things. However, I was able to optimize the code to be more efficient and incorporated other features like using Mediapipe and being able to train the data on your own.

Additionally, for the future there are more ways to make this project better (which I am working on right now). For one, ASL is a rich language with several gestures that imply meanings. My current approach uses static images and therefore cannot classify gestures. Additionally, it may be useful to train the computer to try doing this like lipreading which could help determine if some videos are fake on the internet.

