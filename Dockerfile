FROM runpod/base:0.4.0-cuda12.1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "-c", "print('RunPod serverless container ready')"]
