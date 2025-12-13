FROM runpod/serverless:python3.10-cuda12.1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "-c", "print('RunPod serverless container ready')"]
