# Get image path and portion size from the user (simple console-based interaction)
image_path = input("Enter the path to the food image: ")
portion_size = int(input("Enter the portion size (in grams): "))

# Recognize the food item and estimate calories
recognized_food, calories = recognize_and_estimate_calories(image_path, portion_size)
print(f"Recognized Food: {recognized_food}, Estimated Calories: {calories} kcal")
