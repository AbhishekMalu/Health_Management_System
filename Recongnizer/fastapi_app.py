import io
from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from PIL import Image
import tensorflow as tf
import numpy as np
from tensorflow.keras.applications import VGG19

# Load the saved model
vgg_model = tf.keras.models.load_model("C:\\Users\\ShanuPC\\OneDrive\\Desktop\\serverlet\\Patient-Management-System-Or-Pranik-Medical-Services-PMS\\Recongnizer\\6claass.h5")


preparer_model = VGG19(weights = 'imagenet',  include_top = False, input_shape = (180, 180, 3)) 

app = FastAPI()

class InputData(BaseModel):
    input_data: UploadFile

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        prediction = await inference_pipeline(file)
        return {"prediction": prediction}
    except Exception as e:
        return {"error": str(e)}

async def inference_pipeline(image_file: UploadFile) -> str:
    # Read the image file and preprocess it
    contents = await image_file.read()
    img = Image.open(io.BytesIO(contents))

    if img is None:
        return {"error": "Failed to open image"}
    
    img = img.resize((180, 180))  # Resize if necessary
   
    img_array = np.array(img) / 255.0  # Normalize pixel values
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array=preparer_model.predict(img_array)
    
    img_array = img_array.reshape(1, -1)
    #img_array = tf.keras.layers.Flatten()(img_array)  # Flatten the image
   
    
    
    # Make prediction on preprocessed image
    pred = vgg_model.predict(img_array)[0]
    predicted_class_index = np.argmax(pred)
    
    # Define class names
    class_names = ["Acne -> Recommended Doctor = Dr. Pankaj Rao", "Eczema -> Recommended Doctor = Dr. Mamta Parikh", "Atopic -> Recommended Doctor = Dr. Moti Lal Sharma", "Psoriasis -> Recommended Doctor = Dr. Pankaj Rao", "Tinea -> Recommended Doctor = Dr. Mamta Parikh", "Vitiligo -> Recommended Doctor = Dr. Moti Lal Sharma"]
    predicted_class_name = class_names[predicted_class_index]
    
    return predicted_class_name