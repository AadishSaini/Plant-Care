# Importing Libraries
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import EarlyStopping

from tensorflow.keras.applications import VGG16
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.optimizers import Adam


import warnings
warnings.filterwarnings('ignore')

dataset_path = "house_plant_species"
image_size = (224, 224)
batch_size = 64

datagen = ImageDataGenerator(
    rescale=1./255,  
    validation_split=0.2 
)

# Load training data
train_data = datagen.flow_from_directory(
    dataset_path,
    subset='training',
    batch_size=batch_size,
    class_mode='categorical', 
    target_size=image_size  
)

# Load validation data
validation_data = datagen.flow_from_directory(
    dataset_path,
    subset='validation',
    batch_size=batch_size,
    class_mode='categorical',
    target_size=image_size
)

with tf.device('/GPU:0'):
    base_model = VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

    # Freeze the base model layers
    for layer in base_model.layers:
        layer.trainable = False

    # Add custom top layers for your specific classification task
    x = base_model.output
    x = Flatten()(x)
    x = Dense(256, activation='relu')(x)
    x = Dense(train_data.num_classes, activation='softmax')(x)  # num_classes is the number of categories

    # Create the full model
    model = Model(inputs=base_model.input, outputs=x)

    # Compile the model
    model.compile(optimizer=Adam(learning_rate=1e-4),
                loss='categorical_crossentropy',
                metrics=['accuracy'])

    # Model summary
    model.summary()

    # Define early stopping callback
    early_stopping = EarlyStopping(
        monitor='val_accuracy',  # Metric to monitor
        patience=3,              # Number of epochs to wait for improvement
        restore_best_weights=True # Restore model weights from the epoch with the best value of the monitored metric
    )

    history = model.fit(
        train_data,
        validation_data=validation_data,
        epochs=10,  # Adjust the number of epochs as needed
        verbose=1,
        callbacks=[early_stopping]  # Include the early stopping callback
    )

    model.save('test.h5')



class_labels = train_data.class_indices

class_labels = {v: k for k, v in class_labels.items()}

print(class_labels)

