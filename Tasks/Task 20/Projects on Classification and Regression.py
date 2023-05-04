import numpy as np
from sklearn.datasets import load_iris
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical

# Load the iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Convert the target variable to categorical
y = to_categorical(y)

# Split the dataset into training and testing sets
train_X = X[:100]
train_y = y[:100]
test_X = X[100:]
test_y = y[100:]

# Define the model architecture
model = Sequential()
model.add(Dense(10, input_dim=4, activation='relu'))
model.add(Dense(3, activation='softmax'))

# Compile the model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(train_X, train_y, epochs=100, batch_size=10)

# Evaluate the model on the test set
loss, accuracy = model.evaluate(test_X, test_y)
print('Accuracy:', accuracy)
