import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

# Constants
IMG_HEIGHT, IMG_WIDTH = 128, 128

def preprocess_frame(frame):
    """Preprocess the video frame for model input."""
    frame_resized = cv2.resize(frame, (IMG_HEIGHT, IMG_WIDTH))
    frame_normalized = frame_resized / 255.0
    frame_expanded = np.expand_dims(frame_normalized, axis=0)
    return frame_expanded

def load_models(gesture_model_path, emotion_model_path):
    """Load the trained gesture and emotion detection models."""
    gesture_model = load_model(gesture_model_path)
    emotion_model = load_model(emotion_model_path)
    return gesture_model, emotion_model

def predict(model, frame):
    """Make predictions using the provided model."""
    predictions = model.predict(frame)
    predicted_class = np.argmax(predictions, axis=1)[0]
    confidence = np.max(predictions)
    return predicted_class, confidence

def main():
    # Load the models
    gesture_model_path = "gesture_cnn_model.keras"
    emotion_model_path = "emotion_cnn_model.keras"

    gesture_model, emotion_model = load_models(gesture_model_path, emotion_model_path)

    # Class names
    gesture_classes = ['Hello', 'I Love You', 'No', 'Thanks', 'Yes']  # Update with gesture class names
    emotion_classes = ['happy', 'sad', 'angry', 'neutral', 'disgust', 'surprise', 'fear']  # Update with emotion class names

    # Start video capture
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    print("Starting real-time detection...")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame.")
            break

        # Preprocess frame
        preprocessed_frame = preprocess_frame(frame)

        # Gesture detection
        gesture_pred, gesture_conf = predict(gesture_model, preprocessed_frame)
        gesture_label = f"Gesture: {gesture_classes[gesture_pred]} ({gesture_conf:.2f})"

        # Emotion detection
        emotion_pred, emotion_conf = predict(emotion_model, preprocessed_frame)
        emotion_label = f"Emotion: {emotion_classes[emotion_pred]} ({emotion_conf:.2f})"

        # Display results
        cv2.putText(frame, gesture_label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.putText(frame, emotion_label, (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

        cv2.imshow('Real-Time Detection', frame)

        # Break loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
