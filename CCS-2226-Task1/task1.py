# CCS 2226 - Foundations of AI (2026)
# Task One: MNIST Digit Recognition (0-9)

import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras

# Load and preprocess data
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

x_train = x_train / 255.0
x_test  = x_test  / 255.0
x_train = x_train.reshape(-1, 784)
x_test  = x_test.reshape(-1, 784)

# Build and train model
model = keras.Sequential([
    keras.layers.Dense(128, activation='relu', input_shape=(784,)),
    keras.layers.Dense(64,  activation='relu'),
    keras.layers.Dense(10,  activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=10, batch_size=32, validation_split=0.1)

# Evaluate
loss, accuracy = model.evaluate(x_test, y_test)
print(f"Test Accuracy: {accuracy * 100:.2f}%")

# Show predictions on a few test images
predictions = model.predict(x_test[:10])

for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(x_test[i].reshape(28, 28), cmap='gray')
    plt.title(f"Pred: {np.argmax(predictions[i])}, True: {y_test[i]}")
    plt.axis('off')

plt.tight_layout()
plt.show()