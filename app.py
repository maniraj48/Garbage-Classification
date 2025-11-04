"""
import os
from flask import Flask, request, render_template, url_for
from werkzeug.utils import secure_filename
import tensorflow as tf
from PIL import Image
import numpy as np

# --- INITIAL SETUP ---
app = Flask(__name__)

# --- 1. Load the trained model ---
# Make sure the model file is in the same directory as this script.
print("Loading the model...")
model = tf.keras.models.load_model('best_waste_classifier.keras')
print("Model loaded successfully.")

# --- 2. Define the class names (must be in the correct order) ---
class_names = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']

# --- 3. Define a function to preprocess the uploaded image ---
def preprocess_image(image_path, target_size=(224, 224)):
    # Loads an image from a file path, resizes it, and prepares it
    # for the model.
    img = Image.open(image_path) # Load image
    img = img.resize(target_size) # Resize
    img_array = np.array(img) # Convert to numpy array
    img_array = np.expand_dims(img_array, axis=0) # Add a batch dimension
    return img_array


# --- 4. Define the routes for the web application ---

# This is the main page
@app.route('/', methods=['GET'])
def index():
    # Just render the initial HTML page
    return render_template('index.html')


# This is where the prediction happens
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    if file:
        # Secure the filename and create a path to save it temporarily
        filename = secure_filename(file.filename)
        upload_folder = os.path.join('static', 'uploads')
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)
        filepath = os.path.join(upload_folder, filename)
        file.save(filepath)

        # Preprocess the image for the model
        processed_image = preprocess_image(filepath)

        # Make a prediction
        prediction = model.predict(processed_image)
        predicted_class_index = np.argmax(prediction)
        predicted_class_name = class_names[predicted_class_index]

        # Render the page again, but this time with the prediction results
        return render_template('index.html', 
                               prediction=predicted_class_name, 
                               image_file=filename)

# --- 5. Run the Flask application ---
if __name__ == '__main__':
    app.run(debug=True) # debug=True is great for development


    """


import os
from flask import Flask, request, render_template, url_for
from werkzeug.utils import secure_filename
import tensorflow as tf
from PIL import Image
import numpy as np

# --- INITIAL SETUP ---
app = Flask(__name__)

# Define the path for uploaded images
UPLOAD_FOLDER = os.path.join('static', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# --- 1. Load the trained model ---
print("Loading the model...")
model = tf.keras.models.load_model('best_waste_classifier.keras')
print("Model loaded successfully.")

# --- 2. Define the class names ---
class_names = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']

# --- 3. Define a function to preprocess the uploaded image ---
def preprocess_image(image_path, target_size=(224, 224)):
    img = Image.open(image_path)
    img = img.resize(target_size)
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# --- 4. Define the routes ---
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    if file:
        filename = secure_filename(file.filename)
        
        # --- THE FIX IS HERE ---
        # Ensure the upload folder exists before trying to save to it
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])
        
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        processed_image = preprocess_image(filepath)
        prediction = model.predict(processed_image)
        predicted_class_index = np.argmax(prediction)
        predicted_class_name = class_names[predicted_class_index]

        # Pass the relative path for the image to the template
        image_path_for_html = os.path.join('uploads', filename)

        return render_template('index.html', 
                               prediction=predicted_class_name, 
                               image_file=image_path_for_html)

# --- 5. Run the Flask application ---
if __name__ == '__main__':
    app.run(debug=True)