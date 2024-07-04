import streamlit as st
import cv2
import numpy as np
from PIL import Image
import time
import tempfile

# Function to apply color mask
def apply_color_mask(frame, lower_bound, upper_bound):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    result = cv2.bitwise_and(frame, frame, mask=mask)
    return result

# Function to identify color areas with bounding boxes
def identify_color_areas(frame, lower_bound, upper_bound):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        if cv2.contourArea(contour) > 500:  # filter out small areas
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    return frame

# Function to convert image to sketch
def sketch_image(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverted_image = cv2.bitwise_not(gray_image)
    blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
    inverted_blur = cv2.bitwise_not(blurred)
    sketch = cv2.divide(gray_image, inverted_blur, scale=256.0)
    return sketch

# Function to apply filter
def apply_filter(image, filter_type):
    if filter_type == 'Sepia':
        kernel = np.array([[0.272, 0.534, 0.131],
                           [0.349, 0.686, 0.168],
                           [0.393, 0.769, 0.189]])
        return cv2.transform(image, kernel)
    elif filter_type == 'Grayscale':
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    elif filter_type == 'Blur':
        return cv2.GaussianBlur(image, (21, 21), 0)
    return image

# Initialize Streamlit session state
if 'video_capture' not in st.session_state:
    st.session_state.video_capture = False

# Streamlit interface
st.title('Interactive Virtual Art Studio')

# Sidebar settings
st.sidebar.header('Settings')

# Video capture settings
enable_color_mask = st.sidebar.checkbox('Enable Color Masking', key='enable_color_mask')
enable_color_identification = st.sidebar.checkbox('Enable Color Identification', key='enable_color_identification')

if enable_color_mask or enable_color_identification:
    color_options = st.sidebar.selectbox('Choose color', ['Red', 'Blue', 'Green', 'Yellow', 'Cyan', 'Magenta'], key='color_options')

    lower_hue = st.sidebar.slider('Lower Hue', 0, 179, 0, key='lower_hue')
    upper_hue = st.sidebar.slider('Upper Hue', 0, 179, 179, key='upper_hue')
    lower_saturation = st.sidebar.slider('Lower Saturation', 0, 255, 100, key='lower_saturation')
    upper_saturation = st.sidebar.slider('Upper Saturation', 0, 255, 255, key='upper_saturation')
    lower_value = st.sidebar.slider('Lower Value', 0, 255, 100, key='lower_value')
    upper_value = st.sidebar.slider('Upper Value', 0, 255, 255, key='upper_value')

    lower_bound = np.array([lower_hue, lower_saturation, lower_value])
    upper_bound = np.array([upper_hue, upper_saturation, upper_value])

if st.sidebar.button('Start Live Video Capture'):
    st.session_state.video_capture = True

if st.sidebar.button('Stop Live Video Capture'):
    st.session_state.video_capture = False

# Live video capture and processing
if st.session_state.video_capture:
    cap = cv2.VideoCapture(0)
    stframe = st.empty()
    fps = 15  # Limiting to 15 frames per second

    while st.session_state.video_capture:
        ret, frame = cap.read()
        if not ret:
            st.warning('No video feed detected.')
            break

        if enable_color_mask:
            frame = apply_color_mask(frame, lower_bound, upper_bound)

        if enable_color_identification:
            frame = identify_color_areas(frame, lower_bound, upper_bound)

        stframe.image(frame, channels="BGR", use_column_width=True)
        time.sleep(1 / fps)  # Control frame rate

    cap.release()

# Video upload and processing
st.sidebar.header('Video Processing')
uploaded_video = st.sidebar.file_uploader("Upload a video", type=["mp4", "mov", "avi"], key='video_uploader')

if uploaded_video is not None:
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_video.read())
    cap = cv2.VideoCapture(tfile.name)
    stframe = st.empty()
    fps = 15  # Limiting to 15 frames per second

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if enable_color_mask:
            frame = apply_color_mask(frame, lower_bound, upper_bound)

        if enable_color_identification:
            frame = identify_color_areas(frame, lower_bound, upper_bound)

        stframe.image(frame, channels="BGR", use_column_width=True)
        time.sleep(1 / fps)  # Control frame rate

    cap.release()

# Image upload and processing
st.sidebar.header('Image Processing')
uploaded_file = st.sidebar.file_uploader("Upload an image", type=["jpg", "jpeg", "png"], key='file_uploader')

if uploaded_file is not None:
    image = np.array(Image.open(uploaded_file))
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Sketch effect
    if st.sidebar.checkbox('Apply Sketch Effect', key='sketch_effect'):
        sketch = sketch_image(image)
        st.image(sketch, caption='Sketch Image', use_column_width=True)

    # Filter effects
    filter_option = st.sidebar.selectbox('Choose a filter', ['None', 'Sepia', 'Grayscale', 'Blur'], key='filter_option')
    if filter_option != 'None':
        filtered_image = apply_filter(image, filter_option)
        st.image(filtered_image, caption=f'{filter_option} Filter', use_column_width=True)

# Save and Share options
st.sidebar.header('Save and Share')
if st.sidebar.button('Save Image', key='save_image'):
    if 'filtered_image' in locals():
        save_path = 'filtered_image.png'
        cv2.imwrite(save_path, cv2.cvtColor(filtered_image, cv2.COLOR_RGB2BGR))
        st.success(f'Image saved as {save_path}')
    else:
        st.warning('No processed image to save.')

# Integration and Conclusion
st.sidebar.header('Integration')
st.sidebar.write("Integrate with social media and cloud storage for sharing (to be implemented).")
