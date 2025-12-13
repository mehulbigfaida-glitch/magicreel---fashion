import runpod

def handler(event):
    return {
        "status": "ok",
        "message": "MagicReel serverless base is live"
    }

runpod.serverless.start({"handler": handler})
