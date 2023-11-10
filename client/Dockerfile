# Use an official Python runtime as a parent image
FROM python:3.10.12-slim AS client

# Set the working directory in the container
WORKDIR /usr/src/app

RUN apt-get update && \
    apt-get install -y wget && \
    rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 7860 available to the world outside this container for Gradio
EXPOSE 7860

# Run server.py when the container launches
CMD ["python", "./app.py"]