FROM python:3.12-slim

# Install git and other build tools
RUN apt-get update && \
    apt-get install -y git gcc g++ build-essential && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app/

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "main.py"]  # Or whatever your main entry point is
