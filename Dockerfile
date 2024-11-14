# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the necessary Python dependencies
RUN pip install --no-cache-dir -r requirement.txt

# Expose the port the app runs on
EXPOSE 5000

# Define the environment variable for Mongo URI (optional if you want it dynamic in the container)
ENV MONGO_URI=mongodb://mongo:27017/mydb

# Run the Flask app
CMD ["python", "main.py"]
