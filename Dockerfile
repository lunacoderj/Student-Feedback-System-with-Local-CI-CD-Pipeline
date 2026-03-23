# ---- Student Feedback System Dockerfile ----
# Base image
FROM python:3.10-slim

# Set working directory to mirror local project structure
WORKDIR /project

# Copy requirements first for layer caching
COPY app/requirements.txt /project/app/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r app/requirements.txt

# Copy application code (same layout as local)
COPY app/ /project/app/
COPY templates/ /project/templates/
COPY static/ /project/static/

# Ensure write permissions for SQLite database
RUN chmod -R 777 /project/app

# Expose Flask port
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=app/app.py
ENV FLASK_ENV=production

# Run the application
CMD ["python", "app/app.py"]
