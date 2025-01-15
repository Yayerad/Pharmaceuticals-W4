![image](https://github.com/user-attachments/assets/515e68ca-54e1-4575-8cb7-7a4a11eb86d8)
Website link: https://atsoe02z3cz1zhst.vercel.app/ 
Api Deployment link:   https://pharmaceuticals-w4.onrender.com/predict

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

All fields that previously took a,b,c as input in origin have changed to 1,2,3 repectively 

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
