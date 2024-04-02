# Use the official Python image as base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY order_processing.py .

# Command to run the application
CMD ["python", "order_processing.py"]
