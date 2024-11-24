import streamlit as st
from tensorflow import image
from keras import models
import numpy as np
from PIL import Image


model = models.load_model("model.h5")
pets = ["Cat", "Dog", "Panda"]

def image_classifier(jpg):
    try:
       
        resize = jpg.resize((256, 256))
        img_array = np.expand_dims(np.array(resize) / 255.0, axis=0)  # Normalize pixel values
        pred = model.predict(img_array)  # Get predictions
        arg = np.argmax(pred)  # Find the index of the highest probability
        return pets[arg]
    except Exception as e:
        st.error("Unsupported File Format or Error in Processing.")
        return None

# Streamlit app interface
st.title("Animal Image Classifier 😺🐶🐼")
st.write("Upload an image of a **Cat**, **Dog**, or **Panda** and the model will classify it for you!")

# File uploader for images
uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    try:
       
        img = Image.open(uploaded_file)
        st.image(img, caption="Uploaded Image", use_column_width=True)

        result = image_classifier(img)

        if result:
            st.success(f"Predicted Animal: **{result}**")
    except Exception as e:
        st.error(f"Error processing image: {e}")
