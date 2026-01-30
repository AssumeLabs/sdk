def predict(pattern):
    """Simple probabilistic prediction"""
    if pattern == "HIGH":
        return {"outcome": "UP", "probability": 0.7}
    return {"outcome": "DOWN", "probability": 0.65}
