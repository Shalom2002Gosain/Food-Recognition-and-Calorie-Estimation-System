
# Dictionary mapping food items to calorie content (per 100g or per portion)
food_calorie_data = {
    'apple': 52,   # calories per 100g
    'banana': 89,
    'pizza': 266,  # per slice
    'pasta': 131,  # per cup cooked
}

# Function to estimate calories based on recognized food and portion size
def estimate_calories(recognized_food, portion_size):
    # Get calorie value for the recognized food item
    calories_per_100g = food_calorie_data.get(recognized_food, 0)
    # Estimate calories for the given portion size
    return (calories_per_100g * portion_size) / 100

# Predict the class of a new image and estimate calories
def recognize_and_estimate_calories(image_path, portion_size=100):
    img = cv2.imread(image_path)   # Read image with OpenCV
    img_resized = cv2.resize(img, IMAGE_SIZE)  # Resize image to 128x128
    img_features = extract_color_histogram(img_resized).reshape(1, -1)  # Extract features
    
    # Predict food class using the trained SVM model
    predicted_class_idx = svm_model.predict(img_features)[0]
    predicted_food = le.inverse_transform([predicted_class_idx])[0]  # Convert index back to food name
    
    # Estimate calories based on the recognized food item
    estimated_calories = estimate_calories(predicted_food, portion_size)
    
    return predicted_food, estimated_calories

# Example usage
image_path = 'path_to_test_image.jpg'  # Path to test image
recognized_food, calories = recognize_and_estimate_calories(image_path, portion_size=150)
print(f"Recognized Food: {recognized_food}, Estimated Calories: {calories} kcal")
