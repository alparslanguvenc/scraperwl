FROM python:3.11-slim

# Install system dependencies
# Playwright needs these to install browsers
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

# Install Playwright browsers (Chromium only to save space)
RUN playwright install --with-deps chromium

# Copy application code
COPY . .

# Expose port
EXPOSE 5000

# Metadata
ENV FLASK_APP=app.py

# Run commands
# Using gunicorn for production
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--timeout", "300", "app:app"]
