FROM python:3.10-slim

WORKDIR /app

RUN pip install --no-cache-dir fastapi uvicorn

COPY handler.py .

CMD ["uvicorn", "handler:app", "--host", "0.0.0.0", "--port", "8000"]
