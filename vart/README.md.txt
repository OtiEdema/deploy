Interactive Virtual Art Studio

https://github.com/OtiEdema/deploy/assets/71005527/4051cddd-6e0a-4299-a898-446261c4a8e2


Overview
The Interactive Virtual Art Studio is an AI-powered application designed to enhance and manipulate digital art through real-time video and image processing. Utilizing computer vision techniques, the application allows users to apply color masking, identify and tag specific colors in live video feeds and uploaded videos, and transform images with various artistic effects.

Features
Real-Time Video Processing: Capture live video from your webcam and apply color masking or identification in real-time.
Color Masking: Display only the selected color in the video or image.
Color Identification: Draw bounding boxes around the selected color in the video or image.
Image Processing: Upload images to convert them into artistic sketches or apply filters like Sepia, Grayscale, and Blur.
Video Processing: Upload videos to apply color masking and identification, similar to live video processing.
Save and Share: Save the processed images and videos for sharing.

Technologies Used
Python
Streamlit
OpenCV
NumPy
Pillow

Installation
Clone the repository:

Create a virtual environment:
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`

Install the required packages:
pip install -r requirements.txt

Usage
Run the Streamlit application:
streamlit run app.py

Access the application:
Open your web browser and go to http://localhost:8501

How to Use
Live Video Capture
Go to the Settings section in the sidebar.
Enable Color Masking or Color Identification as needed.
Adjust the HSV parameters to target the desired color.
Click Start Live Video Capture to begin processing.
To stop, click Stop Live Video Capture.

Video Processing
Go to the Video Processing section in the sidebar.
Upload a video file.
The application will process the video and display the results.
Adjust the HSV parameters for better accuracy.

Image Processing
Go to the Image Processing section in the sidebar.
Upload an image file.
Choose to apply a sketch effect or a filter from the available options.
The processed image will be displayed.

Save and Share
After processing an image, go to the Save and Share section in the sidebar.
Click Save Image to save the processed image to your local machine.

Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes. For major changes, please open an issue first to discuss what you would like to change.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
Thanks to the developers of Streamlit, OpenCV, NumPy, and Pillow for their amazing libraries.

Contact
For questions or suggestions, please contact me using the LinkedIn link at my profile.