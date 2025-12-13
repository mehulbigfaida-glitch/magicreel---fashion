FROM python:3.10-slim

WORKDIR /app

RUN pip install --no-cache-dir runpod

COPY handler.py .

CMD ["python", "-u", "-m", "runpod.serverless", "handler"]
