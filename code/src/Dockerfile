# Use a lightweight Python image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI app files
COPY . .

# Expose the Cloud Run required port
EXPOSE 8080

# Start FastAPI using Gunicorn with Uvicorn workers
ENV PORT=8080
CMD ["gunicorn", "-w", "2", "-t", "600", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:8080", "main:app"]
