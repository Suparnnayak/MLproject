from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# Initialize Flask application
application = Flask(__name__)
app = application

# Home route
@app.route('/')
def index():
    return render_template('home.html')

# Prediction route
@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')

    try:
        # Extract form data
        input_data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('reading_score')),
            writing_score=float(request.form.get('writing_score'))
        )

        # Convert to DataFrame
        data_df = input_data.get_data_as_data_frame()
        print("Input DataFrame:\n", data_df)

        # Make prediction
        pipeline = PredictPipeline()
        prediction = pipeline.predict(data_df)
        print("Prediction Result:", prediction)

        return render_template('home.html', results=prediction[0])
    
    except Exception as e:
        print("Error during prediction:", str(e))
        return render_template('home.html', results="⚠️ Prediction failed. Check your input or try again later.")

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
