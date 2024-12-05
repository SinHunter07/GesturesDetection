import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
import streamlit as st


IMG_HEIGHT, IMG_WIDTH = 128, 128

@st.cache_resource
def load_models(gesture_model_path, emotion_model_path):
    """Load the trained gesture and emotion detection models."""
    gesture_model = load_model(gesture_model_path)
    emotion_model = load_model(emotion_model_path)
    return gesture_model, emotion_model

def preprocess_frame(frame):
    """Preprocess the video frame for model input."""
    frame_resized = cv2.resize(frame, (IMG_HEIGHT, IMG_WIDTH))
    frame_normalized = frame_resized / 255.0
    frame_expanded = np.expand_dims(frame_normalized, axis=0)
    return frame_expanded

def predict(model, frame):
    """Make predictions using the provided model."""
    predictions = model.predict(frame)
    predicted_class = np.argmax(predictions, axis=1)[0]
    confidence = np.max(predictions)
    return predicted_class, confidence


def main():
    st.title("Real-Time Gesture and Emotion Detection")
    
    st.info("""
    **How It Works**:
    - This app uses two deep learning models:
      1. A gesture detection model to recognize hand gestures.
      2. An emotion detection model to analyze facial expressions.
    - You can start the detection by clicking the **Start Detection** button. 
    - Stop it anytime using **Stop Detection** and reset the app using **Reset**.
    """)
    
    # models
    gesture_model_path = "gesture_cnn_model.keras"
    emotion_model_path = "emotion_cnn_model.keras"
    gesture_model, emotion_model = load_models(gesture_model_path, emotion_model_path)

    
    gesture_classes = ['Hello', 'I Love You', 'No', 'Thanks', 'Yes'] 
    emotion_classes = ['happy', 'sad', 'angry', 'neutral', 'disgust', 'surprise', 'fear']  

    # webcam
    st.write("### Control Panel")
    st.text("Use the buttons below to start, stop, or reset the detection process.")
    start_button = st.button("Start Detection")
    stop_button = st.button("Stop Detection")
    reset_button = st.button("Reset")

    # Placeholder for video feed
    st.write("### Live Detection Output")
    video_placeholder = st.empty()
    status_placeholder = st.empty()

    # Webcam handling
    cap = None

    # Start detection
    if start_button:
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            status_placeholder.error("Error: Could not access webcam.")
        else:
            status_placeholder.info("Detection started... Press 'Stop Detection' to stop.")

    if cap and cap.isOpened():
        while not stop_button:
            ret, frame = cap.read()
            if not ret:
                status_placeholder.error("Error: Failed to capture frame.")
                break

            
            preprocessed_frame = preprocess_frame(frame)

            # Gesture prediction
            gesture_pred, gesture_conf = predict(gesture_model, preprocessed_frame)
            gesture_label = f"Gesture: {gesture_classes[gesture_pred]} ({gesture_conf:.2f})"

            # Emotion prediction
            emotion_pred, emotion_conf = predict(emotion_model, preprocessed_frame)
            emotion_label = f"Emotion: {emotion_classes[emotion_pred]} ({emotion_conf:.2f})"

            # Annotate the frame
            cv2.putText(frame, gesture_label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.putText(frame, emotion_label, (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

            
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            video_placeholder.image(frame_rgb, channels="RGB")

        if stop_button:
            cap.release()
            video_placeholder.empty()
            status_placeholder.warning("Detection stopped.")

   

if __name__ == "__main__":
    main()
