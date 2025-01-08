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

