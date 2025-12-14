FROM python:3.10-slim

WORKDIR /app

RUN pip install --no-cache-dir runpod fastapi uvicorn

COPY handler.py .

CMD ["python", "handler.py"]
