def handler(event):
    return {
        "status": "ok",
        "message": "MagicReel Dockerfile serverless is alive",
        "input": event.get("input", {})
    }
