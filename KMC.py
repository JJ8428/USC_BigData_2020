import numpy as np
import matplotlib.pyplot as plt


def distance(arr1, arr2):
    ret = 0
    for i in range(0, arr1.__len__()):
        ret += (arr1[i] - arr2[i]) ** 2
    ret **= .5
    return ret


# Harvest the given 311 centroids, and given patient data
chemicals = []
patients = []
r0 = open('Chemicals.csv', 'r')
for data in r0.readlines():
    data = data.replace('\n', '').replace('^M,', '').split(',')
    for a in range(0, data.__len__()):
        data[a] = int(data[a])
    chemicals.append(data)
r0.close()
r1 = open('CaseCompetitionPatientData.csv', 'r')
limit = 1000
for data in r1.readlines():
    data = data.replace('\n', '').replace('^M,', '').split(',')
    for a in range(0, data.__len__()):
        data[a] = int(data[a])
    patients.append(data)
    limit -= 1
    if limit == 0:
        break
r1.close()
print('Data harvested')

# Classify each point with what point it is closest too
classification = []
for a in range(0, patients.__len__()):
    chemicals_responsible = []    # An array of point if multiple chemicals are in the same distance
    diff = -1
    for b in range(0, 311):
        new_diff = distance(chemicals[b], patients[a])
        if diff == -1 or diff > new_diff:
            diff = new_diff
            chemicals_responsible.append(b)
    classification.append(chemicals_responsible)
print('Data classified')

# Find out the frequency of each chemical
frequency = np.zeros(311, int)
for a in range(0, patients.__len__()):
    if isinstance(classification[a], int):
        frequency[classification[a]] += 1
    else:
        for b in range(0, classification[a].__len__()):
            frequency[classification[a][b]] += 1
print('Frequency recorded')

plt.plot(frequency)
plt.show()
print('Histogram generated')
