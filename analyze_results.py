import csv
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import collections

data = []
with open('results.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter = ',')
    for row in spamreader:
        for word in row:
            data.append(int(word.strip()))

data_counts = collections.Counter(data)
data_probs = dict()
for data_i, data_count in data_counts.iteritems():
    data_probs[data_i] = float(data_count) / len(data)

print data_counts
print ''
print data_probs

plt.hist(data, normed=1, bins=range(4,52))
plt.title("Four Million Games of\nIdiot's Delight")
plt.xlabel("Cards Remaining")
plt.ylabel("Percentage of Time")
plt.show()

