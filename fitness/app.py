# Import necessary libraries
import streamlit as st
import cv2
import numpy as np
import mediapipe as mp

# Initialize MediaPipe solutions
mp_pose = mp.solutions.pose
mp_hands = mp.solutions.hands
mp_face_mesh = mp.solutions.face_mesh
mp_objectron = mp.solutions.objectron
mp_drawing = mp.solutions.drawing_utils

# Streamlit application layout
st.title("Virtual Fitness Trainer")
st.sidebar.title("Controls")

# Sidebar settings
detection_confidence = st.sidebar.slider("Detection Confidence", 0.0, 1.0, 0.5)
tracking_confidence = st.sidebar.slider("Tracking Confidence", 0.0, 1.0, 0.5)
exercise_type = st.sidebar.selectbox("Exercise Type", ["Squats", "Push-ups", "Lunges", "Boxing"])

# Function to draw landmarks on the frame
def draw_landmarks(image, results_pose, results_hands, results_face):
    if results_pose.pose_landmarks:
        mp_drawing.draw_landmarks(image, results_pose.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    if results_hands.multi_hand_landmarks:
        for hand_landmarks in results_hands.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    if results_face.multi_face_landmarks:
        for face_landmarks in results_face.multi_face_landmarks:
            mp_drawing.draw_landmarks(image, face_landmarks, mp_face_mesh.FACEMESH_TESSELATION)

# Function to draw 3D landmarks on the frame
def draw_3d_landmarks(image, results_objectron):
    if results_objectron.detected_objects:
        for detected_object in results_objectron.detected_objects:
            mp_drawing.draw_landmarks(image, detected_object.landmarks_2d, mp_objectron.BOX_CONNECTIONS)
            mp_drawing.draw_axis(image, detected_object.rotation, detected_object.translation)

# Function to give feedback based on detected landmarks
def give_feedback(landmarks_pose, exercise):
    feedback = ""
    if landmarks_pose:
        if exercise == "Squats":
            hip = [landmarks_pose[mp_pose.PoseLandmark.LEFT_HIP.value].x, landmarks_pose[mp_pose.PoseLandmark.LEFT_HIP.value].y]
            knee = [landmarks_pose[mp_pose.PoseLandmark.LEFT_KNEE.value].x, landmarks_pose[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
            ankle = [landmarks_pose[mp_pose.PoseLandmark.LEFT_ANKLE.value].x, landmarks_pose[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]
            angle = calculate_angle(hip, knee, ankle)
            if angle < 70:
                feedback = "Go deeper in your squat."
            elif angle > 160:
                feedback = "Your squat is too shallow."
            else:
                feedback = "Good squat form!"
    return feedback

# Function to calculate angle between three points
def calculate_angle(a, b, c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)
    if angle > 180.0:
        angle = 360 - angle
    return angle

# Initialize feedback log
feedback_log = []

# Start webcam video feed
run = st.checkbox('Run')
FRAME_WINDOW = st.image([])
feedback_box = st.empty()
feedback_log_box = st.empty()

cap = cv2.VideoCapture(0)

while run:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the BGR image to RGB.
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the image and detect landmarks.
    with mp_pose.Pose(static_image_mode=False, min_detection_confidence=detection_confidence, min_tracking_confidence=tracking_confidence) as pose:
        with mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=detection_confidence, min_tracking_confidence=tracking_confidence) as hands:
            with mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, min_detection_confidence=detection_confidence, min_tracking_confidence=tracking_confidence) as face_mesh:
                with mp_objectron.Objectron(static_image_mode=False, min_detection_confidence=detection_confidence, min_tracking_confidence=tracking_confidence, model_name='Cup') as objectron:
                    results_pose = pose.process(image)
                    results_hands = hands.process(image)
                    results_face = face_mesh.process(image)
                    results_objectron = objectron.process(image)

                    # Draw the pose, hand, and face annotations on the image.
                    draw_landmarks(image, results_pose, results_hands, results_face)
                    draw_3d_landmarks(image, results_objectron)

                    # Give feedback
                    feedback = give_feedback(
                        results_pose.pose_landmarks.landmark if results_pose.pose_landmarks else None,
                        exercise_type
                    )

                    # Update feedback log
                    if feedback:
                        feedback_log.insert(0, feedback)
                        feedback_box.markdown(f"### Real-Time Feedback: {feedback}")
                        feedback_log_box.markdown("### Feedback Log:\n" + "\n".join(feedback_log[:5]))

                    # Display the frame
                    FRAME_WINDOW.image(image)
else:
    cap.release()
