import pandas as pd
import numpy as np

# Sample dataset
data = {
    'JobRole': ['Manager', 'Clerk', 'Manager', 'Technician', 'Clerk', 'Technician'],
    'Experience': ['High', 'Low', 'Medium', 'Medium', 'Low', 'High'],
    'Salary': ['High', 'Low', 'Medium', 'Medium', 'Low', 'High'],
    'Approved': ['Yes', 'No', 'Yes', 'Yes', 'No', 'Yes']
}
df = pd.DataFrame(data)

# Entropy calculation
def entropy(column):
    values, counts = np.unique(column, return_counts=True)
    probs = counts / counts.sum()
    return -np.sum([p * np.log2(p) for p in probs if p > 0])

# Information Gain
def info_gain(data, attr, target):
    total_entropy = entropy(data[target])
    values, counts = np.unique(data[attr], return_counts=True)
    weighted_entropy = sum(
        (counts[i]/sum(counts)) * entropy(data[data[attr]==values[i]][target])
        for i in range(len(values))
    )
    return total_entropy - weighted_entropy

# ID3 algorithm
def id3(data, features, target):
    if len(np.unique(data[target])) == 1:
        return np.unique(data[target])[0]
    if len(features) == 0:
        return data[target].mode()[0]

    gains = [info_gain(data, attr, target) for attr in features]
    best_attr = features[np.argmax(gains)]
    tree = {best_attr: {}}

    for val in np.unique(data[best_attr]):
        subset = data[data[best_attr] == val]
        subtree = id3(subset, [f for f in features if f != best_attr], target)
        tree[best_attr][val] = subtree

    return tree

# Run the algorithm
features = list(df.columns)
features.remove('Approved')
tree = id3(df, features, 'Approved')
print("Decision Tree:")
print(tree)
