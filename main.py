from agent import Agent
from signal import live_signal
from predictor import predict
from tracker import AccuracyTracker
import random

agents = [
    Agent("Agent-Alpha"),
    Agent("Agent-Beta")
]

tracker = AccuracyTracker()

for signal in live_signal():
    print(f"\n📡 Incoming Signal: {signal:.2f}")

    for agent in agents:
        analysis = agent.analyze(signal)
        prediction = predict(analysis["pattern"])

        # Simulated actual outcome
        actual = random.choice(["UP", "DOWN"])
        tracker.update(prediction["outcome"], actual)

        print(
            f"🤖 {agent.name} | "
            f"Pattern: {analysis['pattern']} | "
            f"Predict: {prediction['outcome']} "
            f"({prediction['probability']}) | "
            f"Actual: {actual}"
        )

    print(f"📊 Accuracy: {tracker.accuracy() * 100}%")
