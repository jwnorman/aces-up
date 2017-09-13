import collections
import csv
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

data = []
with open('results.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        for word in row:
            data.append(int(word.strip('\s\[\]')))

data_counts = collections.Counter(data)
data_probs = dict()
data_odds = dict()
for data_i, data_count in data_counts.iteritems():
    data_probs[data_i] = float(data_count) / len(data)
    data_odds[data_i] = round(1. / data_probs[data_i], 2)

print data_counts
print ''
print data_probs
print ''
print data_odds

plt.hist(data, normed=1, bins=range(4, 52))
plt.title("Four Million Games of\nIdiot's Delight")
plt.xlabel("Cards Remaining")
plt.ylabel("Proportion of Games")
plt.show()
