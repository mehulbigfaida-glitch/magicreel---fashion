from fastapi import FastAPI
import uvicorn
import os

app = FastAPI()

@app.get("/")
def root():
    return {"status": "magicreel server alive"}

@app.get("/health")
def health():
    return {"ok": True}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
