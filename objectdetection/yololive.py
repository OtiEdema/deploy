import random
import cv2
import numpy as np
from ultralytics import YOLO
import time

# Load class labels
class_file_path = r"C:\Class\yolo\utils\coco.txt"
with open(class_file_path, "r") as my_file:
    class_list = my_file.read().split("\n")

# Generate random colors for each class
detection_colors = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in class_list]

# Load a pretrained YOLOv8n model
model = YOLO("weights/yolov8n.pt", "v8")

# Initialize video capture from webcam
cap = cv2.VideoCapture(0)  # Use 0 for default webcam

# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Cannot open camera")
    exit()

# Define frame dimensions for resizing
frame_width, frame_height = 640, 480

# Set up logging for detected objects
log_file = open("detection_log.txt", "w")

# Alert for specific classes
alert_classes = ["person", "dog", "cat"]  # Add any class you want to alert for

while True:
    start_time = time.time()
    
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Resize the frame
    frame = cv2.resize(frame, (frame_width, frame_height))

    # Predict objects in the frame
    detect_params = model.predict(source=[frame], conf=0.45, save=False)
    DP = detect_params[0].numpy()
    
    # Process detections
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
                print(f"ALERT: {class_list[int(clsID)]} detected!")

    # Calculate and display FPS
    end_time = time.time()
    # Display the resulting frame
    cv2.imshow("AI Live Detector", frame)

    # Break loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
log_file.close()
cv2.destroyAllWindows()
