import cv2           # OpenCV for image handling
import numpy as np    # NumPy for data manipulation
import os            # OS for file directory management

# Path to your dataset
DATASET_PATH = 'C:\\Users\\shalo\\Downloads\\archive (3)\\Fruits_Vegetables_Dataset(12000)\\Vegetables\\RottenCarrot'

# Define constants
IMAGE_SIZE = (128, 128)

# Function to load and preprocess images using OpenCV
def load_images_and_labels(dataset_path):
    images = []
    labels = []
    
    for category in os.listdir(dataset_path):  # Loop through each food category
        category_path = os.path.join(dataset_path, category)
        if os.path.isdir(category_path):
            for file_name in os.listdir(category_path):
                image_path = os.path.join(category_path, file_name)
                img = cv2.imread(image_path)   # Load image with OpenCV
                if img is not None:
                    img_resized = cv2.resize(img, IMAGE_SIZE)  # Resize image to uniform size
                    images.append(img_resized)   # Append image to the list
                    labels.append(category)      # Append label (food category) to the list
    
    return np.array(images), np.array(labels)   # Return images and labels as NumPy arrays

# Load images and labels
images, labels = load_images_and_labels(DATASET_PATH)
print(f"Loaded {len(images)} images from {DATASET_PATH}")
