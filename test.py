from huggingface_hub import hf_hub_download
from tensorflow import keras

# Download the model from Hugging Face
model_file = hf_hub_download(repo_id="Saksham4106/Plant-Detection", filename="test.h5")

# Load the model
model = keras.models.load_model(model_file)

# Now you can use your model to make predictions
# predictions = model.predict(your_input_data)