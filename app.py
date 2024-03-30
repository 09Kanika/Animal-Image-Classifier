import gradio as gr
from tensorflow import image
from keras import models
import numpy as np
from PIL import Image
import pandas as pd

# st.title("Animal Image :violet[Classifier] 🐶😺🐼")

model = models.load_model("model.h5")
pets = ["Cat", "Dog", "Panda"]

def image_classifier(jpg):
    try:
        resize= image.resize(jpg,(256,256)) 
        dim= np.expand_dims(resize, axis=0)
        pred= model.predict(dim) #[0.23, 0.987,0.546]
        arg= np.argmax(pred)  # finds the maximum value and returns the index  
        return pets[arg]
    except:
        return "Unsupported File Format"


app = gr.Interface(title="Animal Image Classifier 😺🐶🐼",fn=image_classifier, inputs="image", outputs="label")
app.launch()