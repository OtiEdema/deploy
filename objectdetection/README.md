Real-Time Object Detection with YOLOv8


https://github.com/OtiEdema/deploy/assets/71005527/ddd50eb1-25d1-4a14-8116-5b2a2f97b7d6


Overview
This project showcases a real-time object detection application using the state-of-the-art YOLOv8 model. The application is designed to detect objects in video streams with high accuracy and speed. It includes features such as real-time alerts for specific objects, performance metrics display, and logging of detected objects with timestamps.

Features
Real-Time Object Detection: Utilizes YOLOv8 for fast and accurate object detection in live video streams.
Alert System: Triggers real-time alerts for specific objects (e.g., persons, dogs, cats).
Performance Metrics: Displays FPS (Frames Per Second) to monitor the efficiency of the detection process.
Logging: Records detected objects along with their timestamps for further analysis.
Technologies and Libraries
YOLOv8: Cutting-edge object detection model from Ultralytics.
OpenCV: Efficient video processing and manipulation.
NumPy: Advanced numerical operations.
Python: The core programming language for this project.


Installation

Clone the Repository:

Create and Activate a Virtual Environment:
python -m venv yolo_env
source yolo_env/bin/activate  # On Windows: yolo_env\Scripts\activate

Install the Required Libraries:
pip install -r requirements.txt

Create a requirements.txt file with the following content:
opencv-python-headless
numpy
ultralytics

Usage
Ensure Your Camera is Connected:
The application uses the default webcam for video input. Ensure your webcam is properly connected and recognized by your system.

Run the Application:
python yololive.py

Application Workflow:
The application captures frames from the webcam.
YOLOv8 processes each frame to detect objects.
Detected objects are displayed with bounding boxes and labels.
Alerts are triggered for specific objects (e.g., persons, dogs, cats).
The application logs detected objects with timestamps for later analysis.

Project Structure
yololive.py: Main script for running the object detection application.
utils/coco.txt: Contains the class labels for object detection.
weights/yolov8n.pt: Pretrained YOLOv8 model weights (ensure to place the model weights in this directory).

Customization
Modify Alert Classes
You can modify the alert_classes list in yololive.py to trigger alerts for different objects:
alert_classes = ["person", "dog", "cat"]  # Add any class you want to alert for

Change Video Source
To change the video source (e.g., use a video file instead of the webcam), modify the cv2.VideoCapture parameter in yololive.py:
cap = cv2.VideoCapture("path_to_video_file.mp4")

Contributing
Contributions are welcome! If you have suggestions or improvements, please open an issue or create a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
Special thanks to the developers of YOLOv8 and OpenCV for their incredible tools and libraries.

Contact
For any inquiries or discussions, please feel free to reach out on LinkedIn.

