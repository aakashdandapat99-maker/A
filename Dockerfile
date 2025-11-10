# ---------- VishalMusic Render Dockerfile ----------
FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg git curl build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app

# Install python dependencies
RUN pip install --no-cache-dir --upgrade pip setuptools wheel
RUN if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi

# Expose port (optional for health check webapp)
ENV PORT=8080
EXPOSE 8080

# Default start command for Render
CMD ["python3", "-m", "VISHALMUSIC"]
