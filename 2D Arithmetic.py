import pandas as pd
import numpy as np
#Use any CSV file as your dataset and Modify them accordingly.
baseball = pd.read_csv(".csv")[['Height', 'Weight', 'Age']].as_matrix().tolist()
n = len(baseball)
updated = np.array(pd.read_csv(".csv", header = None))


# Create np_baseball (3 cols)
np_baseball = np.array(baseball)

# Print out addition of np_baseball and updated
print(np_baseball + updated)

# Create numpy array: conversion
conversion = np.array([0.0254, 0.453592, 1])

# Print out product of np_baseball and conversion
print(np_baseball * conversion)
