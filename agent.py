class Agent:
    def __init__(self, name):
        self.name = name

    def analyze(self, signal):
        pattern = "HIGH" if signal > 50 else "LOW"
        return {
            "agent": self.name,
            "signal": signal,
            "pattern": pattern
        }
