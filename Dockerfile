# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set Standard ENv Variables
ENV DEBIAN_FRONTEND noninteractive
ENV container docker
ENV TERM=xterm

# Set Container Labels
LABEL org.opencontainers.image.source="https://github.com/simeononsecurity/docker-rss-display-web"
LABEL org.opencontainers.image.description="This Docker container is designed to fetch and display the latest posts from a specified RSS feed using Python, Flask, and feedparser."
LABEL org.opencontainers.image.authors="simeononsecurity"

# Expose the Default Mapping
EXPOSE 8080:80

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN python -m pip install --upgrade pip && python -m pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV RSS_FEED_URL=https://simeononsecurity.com/rssall.xml

# Run app.py when the container launches
CMD ["python", "app.py"]
