# Import necessary libraries
import os
import glob
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.applications.resnet50 import preprocess_input as pp_i
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename

# Initialize Flask app
app = Flask(__name__)

# Load your trained model (Make sure your model is saved in a .h5 file)
MODEL_PATH = 'dataset.py.h5'
model = load_model(MODEL_PATH)

# Define constants
IMAGE_SIZE = (224, 224)
UPLOAD_FOLDER = 'uploads'

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/scan_image', methods=['POST'])
def scan_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    file = request.files['image']
    
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)
        
        # Load and preprocess the image
        img = load_img(filepath, target_size=IMAGE_SIZE)
        img_array = img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = pp_i(img_array)

        # Predict using the model
        prediction = model.predict(img_array)
        predicted_class = np.argmax(prediction, axis=1)

        # Assuming you have a dictionary of class names
        class_names = {0: 'Class A', 1: 'Class B', 2: 'Class C'}  # Update with your actual classes
        predicted_label = class_names.get(predicted_class[0], 'Unknown')

        return jsonify({'prediction': predicted_label})
    
    return jsonify({'error': 'Invalid image format'}), 400

if __name__ == '__main__':
    app.run(debug=True)
