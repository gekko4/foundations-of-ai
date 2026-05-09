# Import required libraries
import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras

# Load MNIST dataset (handwritten digits 0–9)
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# Normalize pixel values to range [0, 1]
x_train = x_train / 255.0
x_test  = x_test  / 255.0

# Flatten 28x28 images into 784‑dimensional vectors
x_train = x_train.reshape(-1, 784)
x_test  = x_test.reshape(-1, 784)

# Build the neural network
model = keras.Sequential([
    keras.layers.Dense(128, activation='relu', input_shape=(784,)),  # Hidden layer 1
    keras.layers.Dense(64, activation='relu'),                       # Hidden layer 2
    keras.layers.Dense(10, activation='softmax')                     # Output layer (10 classes)
])

# Compile the model with optimizer, loss function, and evaluation metric
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Train the model on the training data
model.fit(
    x_train, y_train,
    epochs=10,
    batch_size=32,
    validation_split=0.1  # Use 10% of training data for validation
)

# Evaluate model performance on the test dataset
loss, accuracy = model.evaluate(x_test, y_test)
print(f"Test Accuracy: {accuracy * 100:.2f}%")

# Generate predictions for the first 10 test images
predictions = model.predict(x_test[:10])

# Plot the images with predicted and true labels
for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(x_test[i].reshape(28, 28), cmap='gray')
    plt.title(f"Pred: {np.argmax(predictions[i])}, True: {y_test[i]}")
    plt.axis('off')

plt.tight_layout()
plt.show()