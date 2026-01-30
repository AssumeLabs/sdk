import random
import time

def live_signal():
    """Simulate live incoming signals"""
    while True:
        yield random.uniform(0, 100)
        time.sleep(1)
