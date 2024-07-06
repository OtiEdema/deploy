Face and Eye Detection App
![video multi detect](https://github.com/OtiEdema/deploy/assets/71005527/9d1372ba-7f8c-455d-b6cc-c54cd52cd769)


This project is a web application that performs face and eye detection using OpenCV and Streamlit. The app allows users to upload images and videos or use live camera feed for face and eye detection.

Features
Upload Image: Upload an image file (jpg, jpeg, png) and detect faces and eyes within the image.
Upload Video: Upload a video file (mp4, mov, avi) and detect faces and eyes in each frame of the video.
Live Detection: Use the live camera feed to detect faces and eyes in real-time.

Installation
To run this application, you need to have Python installed. Follow the steps below to set up the environment and run the app:

Clone the repository

Create a virtual environment:
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
Install the required packages:

pip install -r requirements.txt

Usage
To start the application, run the following command:

streamlit run app.py
This will open the application in your default web browser.

Application Options
Upload Image: Upload an image and see the detected faces and eyes.
Upload Video: Upload a video and see the detected faces and eyes in each frame.
Live Detection: Use your webcam to detect faces and eyes in real-time.

Additional Information
The face detection uses the Haar cascades provided by OpenCV.
The application has a sidebar with options to select the activity (Image upload, Video upload, Live detection) and to close the application.

Dependencies
OpenCV
Streamlit
NumPy
Pillow

You can install the dependencies using the requirements.txt file:
pip install -r requirements.txt

Acknowledgements
The Haar cascades for face and eye detection are provided by OpenCV.
The application interface is built using Streamlit.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributing
Contributions are welcome! Please open an issue or submit a pull request for any features, bug fixes, or enhancements.

Contact
For any questions or suggestions, feel free to open an issue or contact me directly at linkedin

