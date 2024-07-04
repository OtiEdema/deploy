import streamlit as st
import cv2
import mediapipe as mp

# Initialize MediaPipe
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

# Streamlit UI setup
st.title("Virtual Fitness Trainer")
st.sidebar.title("Controls")

# Sidebar settings
detection_confidence = st.sidebar.slider("Detection Confidence", 0.0, 1.0, 0.5)
tracking_confidence = st.sidebar.slider("Tracking Confidence", 0.0, 1.0, 0.5)
exercise_type = st.sidebar.selectbox("Exercise Type", ["Squats", "Push-ups", "Lunges", "Boxing"])

# Placeholder for feedback
feedback = st.empty()

# Start webcam feed
run = st.checkbox('Start Webcam')
FRAME_WINDOW = st.image([])

cap = None

if run:
    cap = cv2.VideoCapture(0)
else:
    if cap:
        cap.release()

while run:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convert the frame to RGB
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process the image and detect landmarks
    with mp_pose.Pose(min_detection_confidence=detection_confidence, min_tracking_confidence=tracking_confidence) as pose:
        results = pose.process(image)
        
        # Draw landmarks on the frame
        if results.pose_landmarks:
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        
        # Convert back to BGR for OpenCV
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        FRAME_WINDOW.image(image)
        
        # Generate dummy feedback for demonstration
        if results.pose_landmarks:
            feedback.markdown("### Feedback: Good form!")
        else:
            feedback.markdown("### Feedback: Adjust your position.")
else:
    if cap:
        cap.release()
