FROM python:3.12-slim

# ✅ Install system dependencies needed by Pillow and git
RUN apt-get update && \
    apt-get install -y \
    git \
    gcc \
    g++ \
    build-essential \
    libjpeg-dev \
    zlib1g-dev \
    libpng-dev \
    libfreetype6-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app/

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "bot.py"]  # change this if needed
