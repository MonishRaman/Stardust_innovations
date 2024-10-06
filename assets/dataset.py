# Import necessary libraries
import os
import glob
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import RandomFlip, RandomRotation, Dense, Dropout, Input
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.applications.resnet50 import preprocess_input as pp_i
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Define dataset path
images_dir = "assets/planate dataset"  # Replace with the actual path to dataset

# Load and label image names
image_names = [file for file in glob.glob(os.path.join(images_dir, '*', '*.jpg'))]
labels = [os.path.basename(os.path.dirname(name)) for name in image_names]

# Encode labels into integers for classification
unique_labels = list(set(labels))
label_dict = {name: idx for idx, name in enumerate(unique_labels)}
def label_encoder(label):
    return label_dict.get(label)

# Load images and encode labels
features = []
labels_encoded = []
IMAGE_SIZE = (224, 224)

for name in image_names:
    label = os.path.basename(os.path.dirname(name))
    label_encoded = label_encoder(label)
    if label_encoded is not None:
        img = load_img(name, target_size=IMAGE_SIZE)
        img_array = img_to_array(img)
        img_array = pp_i(img_array)
        features.append(img_array)
        labels_encoded.append(label_encoded)

# Convert features and labels to numpy arrays
features_array = np.array(features)
labels_array = np.array(labels_encoded)

# One-hot encode labels
label_one_hot = pd.get_dummies(labels_array).values

# Split data into train, validation, and test sets
x_train, x_test, y_train, y_test = train_test_split(features_array, label_one_hot, test_size=0.2, random_state=42)
x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, test_size=0.2, random_state=42)

# Data augmentation and model definition
data_augmentation = Sequential([RandomFlip("horizontal_and_vertical"), RandomRotation(0.2)])
resnet_model = ResNet50(include_top=False, pooling='avg', weights='imagenet')
resnet_model.trainable = False

# Build model
inputs = Input(shape=(224, 224, 3))
x = data_augmentation(inputs)
x = resnet_model(x, training=False)
x = Dropout(0.2)(x)
outputs = Dense(len(unique_labels), activation='softmax')(x)
model = tf.keras.Model(inputs, outputs)

# Compile model
model.compile(optimizer=tf.keras.optimizers.Adam(), loss='categorical_crossentropy', metrics=['accuracy'])

# Train model
model_history = model.fit(x_train, y_train, validation_data=(x_val, y_val), epochs=10)

# Plot accuracy and loss
epochs_range = range(10)
plt.figure(figsize=(15, 6))

plt.subplot(1, 2, 1)
plt.plot(epochs_range, model_history.history['accuracy'], label='Training Accuracy')
plt.plot(epochs_range, model_history.history['val_accuracy'], label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(1, 2, 2)
plt.plot(epochs_range, model_history.history['loss'], label='Training Loss')
plt.plot(epochs_range, model_history.history['val_loss'], label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')

plt.show()

# Evaluate model
model.evaluate(x_test, y_test)

# Prediction example
y_pred = model.predict(x_test)
y_pred
