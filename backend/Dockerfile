FROM python:3.10-slim

# Install Pandoc
RUN apt-get update \
    && apt-get install -y pandoc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY cli ./cli
ENTRYPOINT ["python", "cli/anonymize.py"]
