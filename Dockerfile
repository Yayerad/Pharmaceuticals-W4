# Use the official Python 3.9 base image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy all files from the current directory to the container
COPY . /app

# Install the dependencies listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the API will use
EXPOSE 8000

# Command to start the FastAPI application with Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
