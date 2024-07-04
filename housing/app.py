from flask import Flask, render_template, request, jsonify
import pandas as pd
import pickle
import os
import matplotlib.pyplot as plt
import seaborn as sns
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Load models
model_dir = 'models'
model_names = [
    'LinearRegression', 'RobustRegression', 'RidgeRegression', 'LassoRegression', 'ElasticNet', 
    'PolynomialRegression', 'SGDRegressor', 'ANN', 'RandomForest', 'SVM', 'LGBM', 
    'XGBoost', 'KNN'
]
models = {}
for name in model_names:
    try:
        model_path = os.path.join(model_dir, f'{name}.pkl')
        with open(model_path, 'rb') as f:
            models[name] = pickle.load(f)
    except Exception as e:
        print(f"An error occurred while loading {name}: {e}")

# Load evaluation results
results_df = pd.read_csv('model_evaluation_results.csv')

def get_best_model(results_df):
    best_model = results_df.loc[results_df['R2'].idxmax()]
    return best_model['Model']

best_model = get_best_model(results_df)

@app.route('/')
def index():
    return render_template('index.html', model_names=model_names, best_model=best_model)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        model_name = request.form['model']
        input_data = {
            'Avg. Area Income': float(request.form['Avg. Area Income']),
            'Avg. Area House Age': float(request.form['Avg. Area House Age']),
            'Avg. Area Number of Rooms': float(request.form['Avg. Area Number of Rooms']),
            'Avg. Area Number of Bedrooms': float(request.form['Avg. Area Number of Bedrooms']),
            'Area Population': float(request.form['Area Population'])
        }
        input_df = pd.DataFrame([input_data])
        
        if model_name in models:
            model = models[model_name]
            prediction = model.predict(input_df)[0]
            return render_template('results.html', prediction=prediction, model_name=model_name)
        else:
            return jsonify({'error': 'Model not found'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/results')
def results():
    return render_template('model.html', tables=[results_df.to_html(classes='data')], titles=results_df.columns.values)

@app.route('/comparison')
def comparison():
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='Model', y='R2', data=results_df, ax=ax)
    plt.xticks(rotation=45)
    plt.title('Model Comparison')
    plt.tight_layout()
    comparison_chart = os.path.join('static', 'comparison_chart.png')
    plt.savefig(comparison_chart)
    return render_template('comparison.html', comparison_chart=comparison_chart, best_model=best_model)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join('uploads', filename)
            file.save(file_path)
            data = pd.read_csv(file_path)
            model_name = request.form['model']
            if model_name in models:
                model = models[model_name]
                predictions = model.predict(data)
                data['Predictions'] = predictions
                result_path = os.path.join('uploads', f'predictions_{filename}')
                data.to_csv(result_path, index=False)
                return render_template('upload_result.html', result_path=result_path)
            else:
                return jsonify({'error': 'Model not found'}), 400
    return render_template('upload.html', model_names=model_names)

if __name__ == '__main__':
    app.run(debug=True)
