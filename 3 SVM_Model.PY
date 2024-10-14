from sklearn.model_selection import train_test_split   # For splitting the data into train and test sets
from sklearn.preprocessing import LabelEncoder         # For encoding labels (food categories)
from sklearn.svm import SVC                            # Support Vector Machine model
from sklearn.metrics import accuracy_score             # For accuracy calculation

# Encode labels to integers using LabelEncoder from scikit-learn
le = LabelEncoder()
labels_encoded = le.fit_transform(labels)  # Convert text labels to numerical format

# Split data into training and testing sets using scikit-learn
X_train, X_test, y_train, y_test = train_test_split(features, labels_encoded, test_size=0.2, random_state=42)

# Train an SVM classifier using scikit-learn
svm_model = SVC(kernel='linear', probability=True)  # SVM with a linear kernel
svm_model.fit(X_train, y_train)  # Train the model

# Predict on the test set and evaluate the model
y_pred = svm_model.predict(X_test)

# Calculate and print accuracy score using scikit-learn's accuracy_score
accuracy = accuracy_score(y_test, y_pred)
print(f"Test Accuracy: {accuracy * 100:.2f}%")
