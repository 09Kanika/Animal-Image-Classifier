# Animal Image Classifier Using CNN

This project is an Animal Image Classifier that uses a Convolutional Neural Network (CNN) to classify images of dogs, cats, and pandas. The frontend of the application is built using Streamlit, making it easy to upload images and see the classification results.

![image (1)](https://github.com/user-attachments/assets/e174ebf8-772a-4a5a-9eb9-4c744652e8e0)


## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Requirements](#requirements)
- [Usage](#usage)
- [Model Training](#model-training)
- [Contributing](#contributing)

## Overview

The Animal Image Classifier is designed to identify and classify images of three different animals: dogs, cats, and pandas. The model is built using TensorFlow and Keras, and the frontend interface allows users to upload images and get predictions in real-time.

## Features

- Classifies images into three categories: Dog, Cat, Panda
- User-friendly frontend interface built with Streamlit
- Real-time image classification
- Display of prediction probabilities for each class

## Installation

To run this project, you need to have Python version 3.10 or higher. Follow the steps below to set up the project:

1. Clone the repository:
    ```bash
    git clone https://github.com/09Kanika/Animal-Image-Classifier.git
    cd Animal-Image-Classifier
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
    
## Requirements
The following packages are required to run the project:
```bash
Python version >= 3.10
pandas==2.2.2
numpy==1.26.4
matplotlib==3.8.0
tensorflow==2.17.1
keras==3.5.0
streamlit==1.40.1
```

## Usage

To run the Streamlit app, use the following command:
```bash
streamlit run app.py
```
- This will start the Streamlit server, and you can interact with the app via your web browser.
![image](https://github.com/user-attachments/assets/a4e69c4e-7865-4669-b4fb-81cb0ed19c65)

- Upload image.
![image](https://github.com/user-attachments/assets/78944f38-d7c4-4639-bc03-ba015bb01211)


## Model Training
The model is trained using a Convolutional Neural Network (CNN) with TensorFlow and Keras.

Model Summary:
![image](https://github.com/user-attachments/assets/d75a1612-e346-4c64-80b5-8f960c938230)
![image](https://github.com/user-attachments/assets/b25b162f-7fec-4ad6-9c66-c6685206547a)

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request or open an issue to discuss any changes or improvements.
