# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy requirements file and install dependencies
# COPY requirements.txt .
# RUN pip install -r requirements.txt

# Copy application code
COPY . .

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

# Expose the port Flask will run on
EXPOSE 5000

# Run the Flask app
CMD ["flask", "run"]
