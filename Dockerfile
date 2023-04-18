# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY jwt_utility.py listener.py .

# Expose the port the app runs on
EXPOSE 8080

# Define the command to run the application
CMD ["uvicorn", "listener:app", "--host", "0.0.0.0", "--port", "8080"]
