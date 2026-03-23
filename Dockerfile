# ---- Student Feedback System Dockerfile ----
# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements first for layer caching
COPY app/requirements.txt /app/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ /app/
COPY templates/ /app/templates/
COPY static/ /app/static/

# Expose Flask port
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Run the application
CMD ["python", "app.py"]
