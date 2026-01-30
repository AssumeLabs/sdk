class AccuracyTracker:
    def __init__(self):
        self.total = 0
        self.correct = 0

    def update(self, prediction, actual):
        self.total += 1
        if prediction == actual:
            self.correct += 1

    def accuracy(self):
        if self.total == 0:
            return 0
        return round(self.correct / self.total, 2)
