import runpod

def handler(event):
    return {"status": "magicreel serverless alive"}

runpod.serverless.start({"handler": handler})
