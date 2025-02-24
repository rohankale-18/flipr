# Use an official Python image
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy only requirements first (for caching)
COPY . .

RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Install system dependencies
RUN apt-get update && apt-get install -y wget && \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt-get install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb && \
    apt-get clean

EXPOSE 10000

# Start the Flask app with Gunicorn
CMD ["python3", "app.py"]
