#  Food Recognition and Calorie Estimation System
## Objective:-
The aim of this project is to develop a system that can accurately recognize food items from images and estimate their calorie content. This system helps users track their dietary intake and make informed food choices by using image recognition techniques and simple calorie estimation algorithms. 
#
## System Components:
### Image Preprocessing and Feature Extraction:-
* OpenCV is used to load and resize food images into a standard format.
* Features such as color histograms are extracted from the images to capture color distribution, which serves as a simplified representation of the food items.

### Food Classification:
* Using scikit-learn, the system leverages a traditional machine learning classifier, specifically a Support Vector Machine (SVM). The classifier is trained to recognize different food items based on the extracted image features.
* LabelEncoder is used to convert the food labels into numerical format for training, and the SVM model classifies new food images into one of the predefined categories.
  
### Calorie Estimation:
* After recognizing the food item, the system estimates the calorie content based on a simple dictionary of common food items and their average calorie values (per 100g or per portion).
* Users can input the portion size (in grams) to get a more accurate calorie estimate based on the recognized food item.
#
## Technologies Used:
* OpenCV: For image loading, resizing, and feature extraction (color histograms).
* NumPy: For array manipulation and handling image data.
* scikit-learn: For machine learning, including training the SVM classifier, label encoding, and model evaluation.
#
## Conclusion:
This project demonstrates a simple yet effective approach to food recognition and calorie estimation using machine learning and image processing techniques. It is a lightweight alternative to deep learning-based systems and can be further enhanced with more sophisticated feature extraction methods and classifiers. The system can be deployed in mobile or web applications, helping users easily track their dietary intake by simply taking pictures of their meals.






