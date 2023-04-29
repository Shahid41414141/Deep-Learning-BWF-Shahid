import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import CountVectorizer

# Load the email dataset
emails = pd.read_csv('D:\WORK\VS_CODE\Deep-Learning-BWF-Shahid\Tasks\Task 18\spam_ham_dataset.csv.csv')

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(emails['text'], emails['label'], test_size=0.3, random_state=42)

# Vectorize the email text
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

# Train the Naive Bayes model
clf = GaussianNB()
clf.fit(X_train.toarray(), y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test.toarray())

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
