# Use official Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy dependencies and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the backend
COPY . .

# Expose Flask port
EXPOSE 5000

# Prevent Python from buffering logs
ENV PYTHONUNBUFFERED=1

# ✅ Run DB initialization first, then start Flask
CMD ["sh", "-c", "python init_db.py && python app.py"]
