import streamlit as st
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image

# Load the re-saved emotion detection model
emotion_model = load_model('emotion_model.keras')

# Define the emotion labels
emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

# Function to detect faces and predict emotions
def detect_emotions(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)
        if np.sum([roi_gray]) != 0:
            roi = roi_gray.astype('float') / 255.0
            roi = img_to_array(roi)
            roi = np.expand_dims(roi, axis=0)
            preds = emotion_model.predict(roi)[0]
            label = emotion_labels[preds.argmax()]
            label_position = (x, y - 10)  # Adjust label position above the face
            cv2.putText(frame, label, label_position, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return frame

# Load the Haar cascades for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Streamlit app
st.set_page_config(
    page_title="Oti AI MoodMatrix",
    page_icon=":smiley:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Display the header image
header_image_path = 'c:/projects/emdect/header_image.png'
header_image = Image.open(header_image_path)
st.image(header_image, use_column_width=True, caption="Oti AI MoodMatrix")

# Apply custom CSS for styling
st.markdown("""
    <style>
    .reportview-container {
        background: #f0f2f6;
        color: #000000;
    }
    .sidebar .sidebar-content {
        background: #f0f2f6;
        color: #000000;
    }
    .stTextInput, .stFileUploader, .stCheckbox, .stSelectbox, .stButton {
        background: #f0f2f6;
        color: #000000;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Oti AI MoodMatrix")
st.markdown("""
    <style>
    .reportview-container {
        background: linear-gradient(to right, #000428, #004e92);
        color: white;
    }
    .sidebar .sidebar-content {
        background: linear-gradient(to top, #000428, #004e92);
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# Option to use webcam or upload image
option = st.sidebar.selectbox("Select Input Source", ("Webcam", "Upload Image"))

if option == "Webcam":
    st.write("**Webcam Live Feed**")
    run = st.checkbox('Run')
    FRAME_WINDOW = st.image([])
    camera = cv2.VideoCapture(0)
    while run:
        _, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = detect_emotions(frame)
        FRAME_WINDOW.image(frame)
    else:
        st.write('Stopped')
else:
    st.write("**Upload an Image**")
    uploaded_file = st.file_uploader("Choose an image...", type="jpg")
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        img_array = np.array(image)
        frame = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
        frame = detect_emotions(frame)
        st.image(frame, use_column_width=True)

st.sidebar.markdown("### About")
st.sidebar.info(
    """
    Unlocking the future of emotional intelligence with Oti AI Mood Matrix where cutting-edge machine learning and AI meets the art of feeling, transforming data into empathy.
    """
)
