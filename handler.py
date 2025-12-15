import runpod

def handler(event):
    return {
        "status": "magicreel server alive",
        "input": event
    }

runpod.serverless.start({"handler": handler})
