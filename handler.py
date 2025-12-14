import runpod

def handler(event):
    """
    Minimal handshake-safe handler.
    This MUST return JSON-serializable output.
    """
    return {
        "status": "ok",
        "input": event.get("input", {})
    }

runpod.serverless.start({
    "handler": handler
})
