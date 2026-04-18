import math
from collections import Counter

class Statistics:
    def __init__(self, data):
        self.data = sorted(data)

    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return self.max() - self.min()

    def mean(self):
        return round(self.sum() / self.count())

    def median(self):
        n = self.count()
        mid = n // 2
        if n % 2 == 0:
            return (self.data[mid - 1] + self.data[mid]) / 2
        return self.data[mid]

    def mode(self):
        freq = Counter(self.data)
        max_count = max(freq.values())
        mode_val = [k for k, v in freq.items() if v == max_count][0]
        return {'mode': mode_val, 'count': max_count}

    def var(self):
        m = self.mean()
        return round(sum((x - m) ** 2 for x in self.data) / self.count(), 1)

    def std(self):
        return round(math.sqrt(self.var()), 1)

    def freq_dist(self):
        freq = Counter(self.data)
        n = self.count()
        result = [(round(count / n * 100, 1), val) for val, count in freq.items()]
        return sorted(result, reverse=True)

    def describe(self):
        print(f"Count: {self.count()}")
        print(f"Sum:  {self.sum()}")
        print(f"Min:  {self.min()}")
        print(f"Max:  {self.max()}")
        print(f"Range:  {self.range()}")
        print(f"Mean:  {self.mean()}")
        print(f"Median:  {self.median()}")
        mode = self.mode()
        print(f"Mode:  ({mode['mode']}, {mode['count']})")
        print(f"Variance:  {self.var()}")
        print(f"Standard Deviation:  {self.std()}")
        print(f"Frequency Distribution: {self.freq_dist()}")


ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

data = Statistics(ages)

print('Count:', data.count())
print('Sum: ',  data.sum())
print('Min: ',  data.min())
print('Max: ',  data.max())
print('Range: ', data.range())
print('Mean: ',  data.mean())
print('Median: ', data.median())
print('Mode: ',  data.mode())
print('Standard Deviation: ', data.std())
print('Variance: ', data.var())
print('Frequency Distribution: ', data.freq_dist())

print()
data.describe()
