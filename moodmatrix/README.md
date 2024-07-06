# Oti AI MoodMatrix

https://github.com/OtiEdema/deploy/assets/71005527/663fb5be-430d-4215-b195-47d4beb446ad


## Overview
Oti AI MoodMatrix is an advanced AI-powered application designed to detect facial landmarks and classify emotions in real-time. Leveraging the power of deep learning and computer vision, this app can identify emotions from live webcam feeds or uploaded images. Oti AI MoodMatrix is ideal for various use cases in businesses, enhancing customer experiences, and more.

## Features
Real-time emotion detection using a webcam
Emotion detection from uploaded images
Interactive and dynamic front-end interface built with Streamlit
Utilizes deep learning models trained with TensorFlow/Keras
Supports a wide range of emotions: Angry, Disgust, Fear, Happy, Sad, Surprise, Neutral
Technologies and Libraries Used
TensorFlow/Keras: For building and training the deep learning model
OpenCV: For real-time face detection and image processing
Streamlit: For creating a dynamic and interactive front-end interface
Python: As the core programming language
Matplotlib: For plotting training history and visualizing results
Pandas and NumPy: For data manipulation and numerical operations
PIL: For handling image files

## Installation
Clone the repository:

Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate # On Windows use `venv\Scripts\activate`

Install the required dependencies


Ensure you have the necessary Haar cascade files for face detection:

mkdir -p haarcascades
cd haarcascades
wget https://github.com/opencv/opencv/raw/master/data/haarcascades/haarcascade_frontalface_default.xml

## Training the Model
To train the model, use the train_emotion_model.py script. This script will train the model on the FER-2013 dataset and save the trained model in the .keras format.
python train_emotion_model.py

## Running the App
To run the Streamlit app, use the emotion_detection_app.py script. This will launch the app in your default web browser.
streamlit run emotion_detection_app.py

## Configuring the App
The app can use a webcam for real-time emotion detection or accept uploaded images for analysis.

## Challenges Faced
Model Training: Achieving a balance between training and validation accuracy was challenging. Various batch sizes, learning rates, and regularization techniques were experimented with to stabilize the model.
Data Augmentation: Effective data augmentation strategies were implemented to improve the model's generalization capabilities.
Model Saving and Loading: Transitioning to the latest TensorFlow SavedModel format while ensuring compatibility and performance was a significant challenge.

## Future Plans
Continue fine-tuning the model for improved accuracy and stability
Implement additional features and enhancements
Gather user feedback for continuous improvement

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License. 

## Contact
For any inquiries, please contact https://www.linkedin.com/in/oti-e-34838485/