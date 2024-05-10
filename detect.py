import cv2
import numpy as np
from keras.models import load_model

# Load the model
model = load_model("keras_model.h5", compile=False)

# Load the labels
class_names = ["No leaf", "Good", "Bad"]

def process_image(image):
    # Resize the image to fit the model's input shape
    image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

    # Make the image a numpy array and reshape it to the model's input shape
    image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

    # Normalize the image
    image = (image / 127.5) - 1

    # Predict using the model
    prediction = model.predict(image)
    index = np.argmax(prediction)
    class_name = class_names[index]

    return class_name
