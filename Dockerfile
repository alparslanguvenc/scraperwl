# Use official Playwright image (includes Python, Browsers, System Dependencies)
# This is much more stable than installing on top of python:slim
FROM mcr.microsoft.com/playwright/python:v1.40.0-jammy

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
# Note: playwright is already in the image, but requirements might have specific version
# We install others (flask, beautifulsoup4, gunicorn)
RUN pip install --no-cache-dir -r requirements.txt

# Ensure browsers are installed (The base image has them, but good to be sure for Chromium)
# Browsers are already in the base image for 1.40.0
# RUN playwright install chromium

# Copy application code
COPY . .

# Expose port (Documentation only, real binding happens via CMD)
EXPOSE 5000

# Metadata
ENV FLASK_APP=app.py

# Run commands
# Using gunicorn for production
# Important: Bind to 0.0.0.0:[PORT]
CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:$PORT --timeout 300 app:app"]
