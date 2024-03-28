# Description: Dockerfile for FastAPI app

# Use official Python image as a parent image
FROM python:3.12.1

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Set an environment variable for the model path
ENV MODEL_PATH=/app/model.joblib

# Update pip
RUN pip install --upgrade pip

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run main.py (API) when the container launches
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
