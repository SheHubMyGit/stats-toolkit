from stats_tools import mean, median, std_dev

class Scores:
    def __init__(self, values):
        if len(values)==0:
            raise ValueError("Scores need at least 1 number")
        self.values = values.copy()

    def mean(self):
        return mean(self.values)

    def median(self):
        return median(self.values)

    def std_dev(self):
        return std_dev(self.values)

    def report(self):
        return f"Mean: {self.mean():.2f}\nMedian: {self.median():.2f}\nStd dev: {self.std_dev():.2f}"

