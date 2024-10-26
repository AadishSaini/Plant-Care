
# # from keras.models import load_model
# # import numpy as np
# # # import cv2 as cv




# # from PIL import Image
# # import numpy
 
 
# # img= Image.open("./testing.jpg")
# # print(img.size)
# # img = img.resize((244, 244))
# # print(img.size)
# # print(img)
# # np_img = numpy.array(img)

# # model = load_model('test.h5')



# # a= model.predict(img)
# # print(a)





# from keras.models import load_model
# import numpy as np
# from PIL import Image


# from tensorflow.keras.preprocessing.image import load_img, img_to_array

# # Load and resize the image
# img = load_img('testing.jpg', target_size=(224, 224))
# img_array = img_to_array(img)

# # Expand dimensions to match batch size
# img_array = img_array.reshape((1, 224, 224, 3))


# model = load_model('test.h5')
# a = model.predict(img_array)

# print(a)


# class_labels = {0: 'African Violet (Saintpaulia ionantha)', 1: 'Aloe Vera', 2: 'Anthurium (Anthurium andraeanum)', 3: 'Areca Palm (Dypsis lutescens)', 4: 'Asparagus Fern (Asparagus setaceus)', 5: 'Begonia (Begonia spp.)', 6: 'Bird of Paradise (Strelitzia reginae)', 7: 'Birds Nest Fern (Asplenium nidus)', 8: 'Boston Fern (Nephrolepis exaltata)', 9: 'Calathea', 10: 'Cast Iron Plant (Aspidistra elatior)', 11: 'Chinese Money Plant (Pilea peperomioides)', 12: 'Chinese evergreen (Aglaonema)', 13: 'Christmas Cactus (Schlumbergera bridgesii)', 14: 'Chrysanthemum', 15: 'Ctenanthe', 16: 'Daffodils (Narcissus spp.)', 17: 'Dracaena', 18: 'Dumb Cane (Dieffenbachia spp.)', 19: 'Elephant Ear (Alocasia spp.)', 20: 'English Ivy (Hedera helix)', 21: 'Hyacinth (Hyacinthus orientalis)', 22: 'Iron Cross begonia (Begonia masoniana)', 23: 'Jade plant (Crassula ovata)', 24: 'Kalanchoe', 25: 'Lilium (Hemerocallis)', 26: 'Lily of the valley (Convallaria majalis)', 27: 'Money Tree (Pachira aquatica)', 28: 'Monstera Deliciosa (Monstera deliciosa)', 29: 'Orchid', 30: 'Parlor Palm (Chamaedorea elegans)', 31: 'Peace lily', 32: 'Poinsettia (Euphorbia pulcherrima)', 33: 'Polka Dot Plant (Hypoestes phyllostachya)', 34: 'Ponytail Palm (Beaucarnea recurvata)', 35: 'Pothos (Ivy arum)', 36: 'Prayer Plant (Maranta leuconeura)', 37: 'Rattlesnake Plant (Calathea lancifolia)', 38: 'Rubber Plant (Ficus elastica)', 39: 'Sago Palm (Cycas revoluta)', 40: 'Schefflera', 41: 'Snake plant (Sanseviera)', 42: 'Tradescantia', 43: 'Tulip', 44: 'Venus Flytrap', 45: 'Yucca', 46: 'ZZ Plant (Zamioculcas zamiifolia)'}


# import tensorflow as tf
# from tensorflow.keras.preprocessing.image import load_img, img_to_array
# import numpy as np
# import os

# # Load the saved model
# model = tf.keras.models.load_model('test.h5')

# # Define image size (should match the size used during training)
# image_size = (224, 224)

# def predict_image(image_path, model):
#     # Load the image and resize it
#     img = load_img(image_path, target_size=image_size)
    
#     # Convert the image to an array and normalize pixel values
#     img_array = img_to_array(img) / 255.0
    
#     # Expand dimensions to match the input shape required by the model (1, 224, 224, 3)
#     img_array = np.expand_dims(img_array, axis=0)

#     # Make predictions
#     predictions = model.predict(img_array)

#     # Get the predicted class index and confidence
#     predicted_class_index = np.argmax(predictions, axis=1)[0]

#     confidence = np.max(predictions)

#     return predicted_class_index, confidence

# # Provide the path to the image you want to predict
# image_path = "areka_palm.jpg"

# # Call the prediction function
# predicted_class, confidence = predict_image(image_path, model)

# # Print the result
# # print(f"Predicted Class: {predicted_class}, Confidence: {confidence:.2f}")
# # class_labels = train_data.class_indices  # Get class indices
# # class_labels = {v: k for k, v in class_labels.items()}  # Invert to map index to label

# # Print the predicted class name
# # print(f"Predicted Class: {class_labels[predicted_class]}, Confidence: {confidence:.2f}")
# print(predicted_class)
# print(f"Predicted Class: {class_labels[predicted_class]}, Confidence: {confidence:.2f}")





# Import necessary libraries
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from huggingface_hub import hf_hub_download
import numpy as np
import os


model_file = hf_hub_download(repo_id="Saksham4106/Plant-Detection", filename="test.h5")

# Load the model
model1 = tf.keras.models.load_model(model_file)
# model1 = tf.keras.models.load_model('test.h5')

image_size = (224, 224)

# dataset_path = "house_plant_species"
# class_labels = sorted(os.listdir(dataset_path))
class_labels = {0: 'African Violet (Saintpaulia ionantha)', 1: 'Aloe Vera', 2: 'Anthurium (Anthurium andraeanum)', 3: 'Areca Palm (Dypsis lutescens)', 4: 'Asparagus Fern (Asparagus setaceus)', 5: 'Begonia (Begonia spp.)', 6: 'Bird of Paradise (Strelitzia reginae)', 7: 'Birds Nest Fern (Asplenium nidus)', 8: 'Boston Fern (Nephrolepis exaltata)', 9: 'Calathea', 10: 'Cast Iron Plant (Aspidistra elatior)', 11: 'Chinese Money Plant (Pilea peperomioides)', 12: 'Chinese evergreen (Aglaonema)', 13: 'Christmas Cactus (Schlumbergera bridgesii)', 14: 'Chrysanthemum', 15: 'Ctenanthe', 16: 'Daffodils (Narcissus spp.)', 17: 'Dracaena', 18: 'Dumb Cane (Dieffenbachia spp.)', 19: 'Elephant Ear (Alocasia spp.)', 20: 'English Ivy (Hedera helix)', 21: 'Hyacinth (Hyacinthus orientalis)', 22: 'Iron Cross begonia (Begonia masoniana)', 23: 'Jade plant (Crassula ovata)', 24: 'Kalanchoe', 25: 'Lilium (Hemerocallis)', 26: 'Lily of the valley (Convallaria majalis)', 27: 'Money Tree (Pachira aquatica)', 28: 'Monstera Deliciosa (Monstera deliciosa)', 29: 'Orchid', 30: 'Parlor Palm (Chamaedorea elegans)', 31: 'Peace lily', 32: 'Poinsettia (Euphorbia pulcherrima)', 33: 'Polka Dot Plant (Hypoestes phyllostachya)', 34: 'Ponytail Palm (Beaucarnea recurvata)', 35: 'Pothos (Ivy arum)', 36: 'Prayer Plant (Maranta leuconeura)', 37: 'Rattlesnake Plant (Calathea lancifolia)', 38: 'Rubber Plant (Ficus elastica)', 39: 'Sago Palm (Cycas revoluta)', 40: 'Schefflera', 41: 'Snake plant (Sanseviera)', 42: 'Tradescantia', 43: 'Tulip', 44: 'Venus Flytrap', 45: 'Yucca', 46: 'ZZ Plant (Zamioculcas zamiifolia)'}  

def predict_top_k(image_path, model=model1, k=1):
    img = load_img(image_path, target_size=image_size)
    img_array = img_to_array(img) / 255.0  
    img_array = np.expand_dims(img_array, axis=0)  

    predictions = model.predict(img_array)[0]  

    top_k_indices = np.argsort(predictions)[-k:][::-1]  
    top_k_confidences = predictions[top_k_indices]

    top_k_predictions = [(class_labels[i], top_k_confidences[idx]) 
                         for idx, i in enumerate(top_k_indices)]

    return top_k_predictions

# image_path = "meriphoto.jpg"

# top_3_predictions = predict_top_k(image_path, model, k=3)

# print("Top 3 Predictions:")
# for label, confidence in top_3_predictions:
#     print(f"{label}: {confidence:.2f}")
