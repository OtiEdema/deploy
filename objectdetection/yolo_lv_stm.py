import streamlit as st
import cv2
import numpy as np
from ultralytics import YOLO
import random
import threading
import time

# Load class labels
class_file_path = r"C:\Class\yolo\utils\coco.txt"
with open(class_file_path, "r") as my_file:
    class_list = my_file.read().split("\n")

# Generate random colors for each class
detection_colors = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in class_list]

# Load a pretrained YOLOv8n model
model = YOLO("weights/yolov8n.pt", "v8")

# Define frame dimensions for resizing
frame_width, frame_height = 640, 480

# Alert for specific classes
alert_classes = ["person", "dog", "cat"]  # Add any class you want to alert for

# Initialize video capture from webcam
cap = cv2.VideoCapture(0)  # Use 0 for default webcam

# Global state
state = {
    "is_running": False,
    "frame": None,
    "alert": ""
}

# Function to run detection
def run_detection():
    global state, cap
    log_file = open("detection_log.txt", "w")
    while state["is_running"]:
        start_time = time.time()
        
        # Capture frame-by-frame
        ret, frame = cap.read()
        
        if not ret:
            st.error("Can't receive frame (stream end?). Exiting ...")
            break

        # Resize the frame
        frame = cv2.resize(frame, (frame_width, frame_height))

        # Predict objects in the frame
        detect_params = model.predict(source=[frame], conf=0.45, save=False)
        DP = detect_params[0].numpy()
        
        # Process detections
        alert_triggered = False
        if len(DP) != 0:
            for i in range(len(detect_params[0])):
                boxes = detect_params[0].boxes
                box = boxes[i]
                clsID = box.cls.numpy()[0]
                conf = box.conf.numpy()[0]
                bb = box.xyxy.numpy()[0]

                # Draw bounding box and label
                cv2.rectangle(frame, (int(bb[0]), int(bb[1])), (int(bb[2]), int(bb[3])), detection_colors[int(clsID)], 3)
                cv2.putText(frame, f"{class_list[int(clsID)]} {round(conf, 3)}%", (int(bb[0]), int(bb[1]) - 10),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

                # Log detections
                log_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Detected {class_list[int(clsID)]} with confidence {round(conf, 3)}%\n")

                # Alert mechanism
                if class_list[int(clsID)] in alert_classes:
                    alert_triggered = True

        # Calculate and display FPS
        end_time = time.time()
        fps = 1 / (end_time - start_time)
        cv2.putText(frame, f"FPS: {int(fps)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Convert BGR to RGB for displaying in Streamlit
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Update state
        state["frame"] = frame
        state["alert"] = "ALERT: Detected specific object!" if alert_triggered else ""

        # Display the resulting frame in Streamlit
        st.session_state.frame = frame

    # Release resources
    cap.release()
    log_file.close()
    cv2.destroyAllWindows()
    state["is_running"] = False

# Initialize session state variables
if "frame" not in st.session_state:
    st.session_state.frame = None

# Streamlit app layout
st.title("Futuristic AI Live Detector")
st.subheader("Real-time Object Detection with YOLOv8")

start_button = st.button("Start Detection")
stop_button = st.button("Stop Detection")

if start_button and not state["is_running"]:
    state["is_running"] = True
    threading.Thread(target=run_detection).start()

if stop_button and state["is_running"]:
    state["is_running"] = False

if st.session_state.frame is not None:
    st.image(st.session_state.frame, channels="RGB")

if state["alert"]:
    st.warning(state["alert"])
