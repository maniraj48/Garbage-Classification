# Automated Waste Classification using Convolutional Neural Networks

This project provides an end-to-end solution for automatically classifying waste into different categories using a Convolutional Neural Network (CNN) built from scratch. The trained model is deployed in a simple, interactive web application built with Flask.

## Demo

![Demo of the Waste Classifier Web App](./demo.png)
![Demo of the Waste Classifier Web App](./demo1.png)

## 1. Project Overview

### The Problem
Effective waste management is critical for environmental sustainability, but manual sorting is inefficient, costly, and error-prone. This inefficiency leads to lower recycling rates and increased landfill usage. There is a clear need for an automated, accurate, and scalable solution to distinguish between different types of waste.

### The Solution
This project addresses the challenge by developing an intelligent system that can automatically classify different types of waste from an uploaded image. By leveraging computer vision and deep learning, this project serves as a proof-of-concept for automating the waste sorting process.

### The Objective
The primary objective was to build, train, and deploy a deep learning model to:
- **Develop a CNN from scratch** to identify and differentiate waste items.
- **Train the model** to classify images into six categories: `cardboard`, `glass`, `metal`, `paper`, `plastic`, and `trash`.
- **Deploy the trained model** into a user-friendly web application for real-world demonstration.

## 2. Model Performance

The model was built from scratch using TensorFlow and Keras. The training process was a comprehensive journey of iterative improvement, which involved:
- **Initial Training:** Identifying and diagnosing overfitting.
- **Debugging:** Solving critical data loading and model instability issues.
- **Optimization:** Implementing a robust training methodology using **Data Augmentation**, **Batch Normalization**, **Dropout**, and **Callbacks** (`EarlyStopping` and `ModelCheckpoint`) to ensure the model's peak performance was captured.

After this rigorous process, the final model achieved:

- **Final Test Accuracy:** **58.20%**

This accuracy was achieved by evaluating the best-performing version of the model on a completely unseen test set.

## 3. Technologies Used

- **Backend:** Python, Flask
- **Deep Learning:** TensorFlow, Keras
- **Image Processing:** Pillow
- **Frontend:** HTML, CSS

## 4. How to Run This Project

### Prerequisites
- Python 3.8+
- A virtual environment (recommended for managing dependencies)

### Step 1: Clone the Repository
```bash
git clone https://github.com/maniraj48/Garbage-Classification.git
cd Garbage-Classification
```

### Step 2: Download the Trained Model
The trained model file (589 MB) is too large for GitHub. You must download it manually from the link below and place the `best_waste_classifier.keras` file in the main project directory (the same folder as `app.py`).

**➡️ ([[Download the model here](https://drive.google.com/file/d/1Ztovs_CaC_qHLDtBIWIeq9aO3aIOtpS2/view?usp=sharing)])**

### Step 3: Set Up and Activate a Virtual Environment
```bash
# Create a virtual environment named 'venv'
python -m venv venv

# Activate the environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 4: Install Dependencies
Install all the required Python libraries using the `requirements.txt` file.
```bash
pip install -r requirements.txt
```

### Step 5: Run the Web Application
```bash
python app.py
```
The application will start a local development server. Open your web browser and navigate to `http://127.0.0.1:5000` to use the classifier.

## 5. Project Structure

The project is organized with a clean and scalable structure:

```
.
├── app.py                      # The main Flask application script
├── best_waste_classifier.keras   # The final, trained model file - download it from given link
├── requirements.txt            # A list of all project dependencies
├── README.md                   # This documentation file
│
├── templates/
│   └── index.html              # The HTML template for the user interface
│
└── static/
    └── uploads/                # A directory for storing user-uploaded images
```
