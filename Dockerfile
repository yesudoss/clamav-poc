# Dockerfile
FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Copy FastAPI app code and dependencies
COPY app /app
COPY requirements.txt /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port FastAPI runs on
EXPOSE 8000

# Command to start FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
