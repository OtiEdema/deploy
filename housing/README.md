# House Price Prediction App

This project is a web application for predicting house prices using various regression models. The application is built using Flask for the backend and Bootstrap for the frontend. It supports individual house price predictions, model comparisons, and batch predictions from CSV files.

## Features

- **Individual House Price Prediction**: Select a model and input house features to predict the price.
- **Model Comparison**: Visualize the performance of different regression models.
- **Batch Prediction**: Upload a CSV file with multiple house entries to predict prices in bulk.
- **Best Model Highlight**: Automatically identifies and highlights the best model based on R-squared value.

## Demo

![](demo.mp4)

## Installation

1. **Clone the repository**:
   
2. Create and activate a virtual environment:

python -m venv venv 
venv\Scripts\activate # On Windows
source venv/bin/activate # On macOS/Linux

Install the required packages:

pip install -r requirements.txt

Prepare the dataset:
Place the USA_Housing.csv file in the root directory of the project.

Usage
Train the models:
python model.py

Run the Flask application:
python app.py

Access the application:
Open your web browser and go to http://127.0.0.1:5000/.

File Structure
house-price-prediction-app/
│
├── models/                     # Directory to save trained model files
├── uploads/                    # Directory to save uploaded CSV files for batch prediction
├── templates/                  # HTML templates for the Flask app
│   ├── index.html
│   ├── results.html
│   ├── comparison.html
│   ├── upload.html
│   └── upload_result.html
├── USA_Housing.csv             # Dataset file
├── app.py                      # Flask application file
├── model.py                    # Model training and evaluation script
├── requirements.txt            # Python packages requirements
└── README.md                   # This README file

Instructions
Predict House Price
Select a model from the dropdown menu.
Enter the required features for the house.
Click "Predict" to see the estimated house price.

Compare Models
Click on "Compare Models" in the navigation bar.
View the comparison chart of different models based on R-squared value.

Batch Prediction
Click on "Batch Prediction" in the navigation bar.
Select a model and upload a CSV file with the required features for multiple houses.
Click "Upload and Predict" to get predictions for all entries in the file.

Contributing
Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.

License
This project is licensed under the MIT License.

Acknowledgments
The dataset used in this project is the USA_Housing.csv file.
This project uses various machine learning models from the scikit-learn, lightgbm, and xgboost libraries.

Contact
For any questions or feedback, please contact me on LinkedIn.