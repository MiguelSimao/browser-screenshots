FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./screenshot.py /app
COPY ./requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run screenshot.py when the container launches
CMD ["python", "-u", "screenshot.py", "https://www.google.com", "screenshots/google", "--wait-time", "2"]
