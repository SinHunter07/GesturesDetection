import os
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping

# Constants
BATCH_SIZE = 32
IMG_HEIGHT, IMG_WIDTH = 128, 128
EPOCHS = 20

# Step 1: Data Preparation
def create_data_generators(train_dir, test_dir):
    """Creates training and testing data generators."""
    train_datagen = ImageDataGenerator(
        rescale=1.0/255,
        rotation_range=20,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')

    test_datagen = ImageDataGenerator(rescale=1.0/255)

    train_generator = train_datagen.flow_from_directory(
        train_dir,
        target_size=(IMG_HEIGHT, IMG_WIDTH),
        batch_size=BATCH_SIZE,
        class_mode='categorical')

    test_generator = test_datagen.flow_from_directory(
        test_dir,
        target_size=(IMG_HEIGHT, IMG_WIDTH),
        batch_size=BATCH_SIZE,
        class_mode='categorical',
        shuffle=False)

    return train_generator, test_generator

# Step 2: Model Creation
def create_cnn_model(num_classes):
    """Creates a CNN model for classification."""
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(IMG_HEIGHT, IMG_WIDTH, 3)),
        MaxPooling2D(pool_size=(2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D(pool_size=(2, 2)),
        Conv2D(128, (3, 3), activation='relu'),
        MaxPooling2D(pool_size=(2, 2)),
        Flatten(),
        Dense(128, activation='relu'),
        Dropout(0.5),
        Dense(num_classes, activation='softmax')
    ])
    return model

# Step 3: Model Training
def train_and_save_model(train_dir, test_dir, num_classes, model_name):
    """Trains the CNN model and saves the best model to disk."""
    train_gen, test_gen = create_data_generators(train_dir, test_dir)

    model = create_cnn_model(num_classes)
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    checkpoint = ModelCheckpoint(
        f'{model_name}.keras',  # Save model with the provided name
        save_best_only=True,
        monitor='val_accuracy',
        mode='max'
    )

    early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

    model.fit(
        train_gen,
        validation_data=test_gen,
        epochs=EPOCHS,
        callbacks=[checkpoint, early_stopping]
    )

    return model

if __name__ == "__main__":
    # Paths to datasets
    base_dir = r"C:\\Users\\user\\OneDrive\\Desktop\\minorproject\\gesture\\dataset"

    # Gesture Dataset Paths
    gesture_train_dir = os.path.join(base_dir, 'gesture_train')
    gesture_test_dir = os.path.join(base_dir, 'gesture_test')

    # Emotion Dataset Paths
    emotion_train_dir = os.path.join(base_dir, 'emotion_train')
    emotion_test_dir = os.path.join(base_dir, 'emotion_test')

    # Gesture Model Training
    gesture_classes = ['Hello', 'I love you', 'No', 'Thanks', 'Yes']  # Gesture class names
    print("Training Gesture Model...")
    train_and_save_model(gesture_train_dir, gesture_test_dir, len(gesture_classes), "gesture_cnn_model")

    # Emotion Model Training
    emotion_classes = ['happy', 'sad', 'angry', 'neutral', 'disgust', 'surprise', 'fear']  # Emotion class names
    print("Training Emotion Model...")
    train_and_save_model(emotion_train_dir, emotion_test_dir, len(emotion_classes), "emotion_cnn_model")
