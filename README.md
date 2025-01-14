Sales Prediction using LSTM

Overview

This project implements a Long Short-Term Memory (LSTM) model for predicting future sales based on historical sales data. The data includes information about sales, stores, and test data without sales, which are used to train and evaluate the model. The repository demonstrates end-to-end time series forecasting, from data preparation to model evaluation.

Files in the Repository

train.csv: Historical data including sales.

test.csv: Historical data excluding sales (for prediction).

store.csv: Supplemental information about the stores.

sample_submission.csv: A sample submission file in the required format.

Steps to Build the LSTM Model

1. Prepare the Time Series Data

1.1 Isolate Time Series Data:

Focused on the Sales column and treated it as a time series indexed by Date.

1.2 Stationarity Check:

Applied the Augmented Dickey-Fuller (ADF) test to determine if the time series is stationary.

1.3 Differencing:

Differenced the data to make it stationary if necessary.

1.4 Autocorrelation Analysis:

Visualized the Autocorrelation Function (ACF) and Partial Autocorrelation Function (PACF). 

Sales Prediction API
This repository contains a Sales Prediction API built using FastAPI. The model predicts sales for a given store based on multiple input features such as store type, competition distance, promotional activities, and more. This API is deployed and can be accessed for making predictions.

Features
Predicts sales based on various store features.
Built using FastAPI and scikit-learn for sales prediction using a pre-trained model.
Dockerized for easy deployment.
Hosted online for real-time predictions.
API Endpoint
POST /predict
This endpoint allows you to send input data and get predicted sales values.
Request Body
The request body should be in the following JSON format:

json
Copy code
{
  "Store": 1,
  "DayOfWeek": 5,
  "Promo": 1,
  "StateHoliday": "0",
  "SchoolHoliday": 0,
  "Assortment": 2,
  "StoreType": 3,
  "CompetitionDistance": 300.5,
  "Promo2SinceWeek": 10,
  "Promo2SinceYear": 2018,
  "CompetitionOpenSinceMonth": 4,
  "Year": 2025,
  "Month": 1,
  "Day": 14,
  "IsWeekend": 0,
  "IsMonthStart": 0,
  "IsMonthEnd": 0
}
Response
The API will return a prediction of sales in the following format:

json
Copy code
{
  "predicted_sales": 12345.67
}
Example Request (using curl):
bash
Copy code
curl -X 'POST' \
  'https://pharmaceuticals-w4.onrender.com/predict' \
  -H 'Content-Type: application/json' \
  -d '{
  "Store": 1,
  "DayOfWeek": 5,
  "Promo": 1,
  "StateHoliday": "0",
  "SchoolHoliday": 0,
  "Assortment": 2,
  "StoreType": 3,
  "CompetitionDistance": 300.5,
  "Promo2SinceWeek": 10,
  "Promo2SinceYear": 2018,
  "CompetitionOpenSinceMonth": 4,
  "Year": 2025,
  "Month": 1,
  "Day": 14,
  "IsWeekend": 0,
  "IsMonthStart": 0,
  "IsMonthEnd": 0
}'
Example Response:
json
Copy code
{
  "predicted_sales": 12345.67
}
Docker Support
To deploy the application with Docker, follow these steps:

1. Build Docker Image
First, build the Docker image using the provided Dockerfile:

bash
Copy code
docker build -t sales-prediction-api .
2. Run Docker Container
Once the image is built, run the Docker container:

bash
Copy code
docker run -d -p 8000:8000 sales-prediction-api
The API will be available at http://localhost:8000.

3. Docker Compose (Optional)
If you have multiple services, or if you want to simplify the Docker workflow, you can use Docker Compose. Ensure that you have a docker-compose.yml file and then run:

bash
Copy code
docker-compose up --build
This will automatically build the images and run the application in a container.

Local Development
1. Clone the Repository
bash
Copy code
git clone https://github.com/yourusername/sales-prediction-api.git
cd sales-prediction-api
2. Install Dependencies
Make sure you have all dependencies installed. If you're using a virtual environment, activate it, then run:

bash
Copy code
pip install -r requirements.txt
3. Run the Application
To run the application locally, simply execute:

bash
Copy code
uvicorn app:app --reload
This will start the API on http://localhost:8000, and you can test it locally using tools like Postman or cURL.

Dockerfile
Here's a basic Dockerfile that you can use to deploy the FastAPI app with Docker:

dockerfile
Copy code
# Use official Python image as the base
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the application code to the container
COPY . /app

# Install required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the API port
EXPOSE 8000

# Run the FastAPI app with Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
Technologies Used
FastAPI: Web framework for building APIs quickly.
scikit-learn: Machine learning library used for the predictive model.
Docker: Containerization to easily deploy and run the app anywhere.
Uvicorn: ASGI server to serve FastAPI applications.
License
This project is licensed under the MIT License.

2. Data Preparation for Supervised Learning

Transformed the time series data into a supervised learning format by creating lagged features.

3. Data Scaling

Scaled the features using MinMaxScaler to improve model performance.

4. Build the LSTM Model

Built a sequential LSTM model with the following architecture:

Two LSTM layers.

Dropout for regularization.

Dense output layer for prediction.

5. Train the Model

Trained the model with the scaled data over multiple epochs and with a batch size of 32.

6. Make Predictions

Used the trained model to make predictions on the test data and inverse-transformed the scaled predictions to obtain actual sales values.

7. Visualize Results

Plotted the predicted sales against the actual sales for visualization.

8. Evaluate the Model

Calculated the Mean Absolute Error (MAE) to evaluate model performance.

Prerequisites

Python 3.7 or higher

Required libraries:

pandas

numpy

matplotlib

tensorflow

scikit-learn

statsmodels

Install the required libraries using:

pip install pandas numpy matplotlib tensorflow scikit-learn statsmodels

How to Use

Clone the repository:

git clone <repository_url>

Navigate to the repository:

cd <repository_folder>

Place the train.csv, test.csv, store.csv, and sample_submission.csv files in the repository.

Run the notebook or script containing the LSTM implementation:

python lstm_sales_prediction.py

Check the output plots and evaluation metrics.

Project Highlights

Stationarity Analysis: Ensured the time series data was stationary for effective modeling.

LSTM Implementation: Built a robust LSTM architecture to capture sequential dependencies in the sales data.

Evaluation: Achieved meaningful predictions and evaluated using Mean Absolute Error (MAE).

Future Improvements

Automate the process for multiple stores in the dataset.

Incorporate additional features from the store.csv file into the model.

Experiment with other deep learning models for better performance.

Author

Yayerad Mekonnen

Feel free to contribute to the project by submitting pull requests or raising issues!

