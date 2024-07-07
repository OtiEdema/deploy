from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Load the trained model
import joblib
model = joblib.load("student_mark_predictor.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    study_hours = float(request.form['study_hours'])
    if study_hours < 1 or study_hours > 24:
        return render_template('index.html', prediction_text="Please enter a value between 1 and 24 hours.")
    prediction = model.predict([[study_hours]])[0][0].round(2)
    return render_template('index.html', prediction_text=f'Predicted Marks: {prediction}')

if __name__ == "__main__":
  #  app.run(debug=True)
     app.run(host='127.0.0.1', port=5000)
     

