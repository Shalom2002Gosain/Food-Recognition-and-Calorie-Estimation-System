import cv2           
import numpy as np




# Function to extract color histogram features using OpenCV
def extract_color_histogram(image):
    # Calculate color histogram for each image
    hist = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    cv2.normalize(hist, hist)  # Normalize histogram values
    return hist.flatten()      # Flatten the histogram array for machine learning input

# Extract features for all images
features = np.array([extract_color_histogram(image) for image in images])
print(f"Extracted {features.shape[1]} features from each image")
