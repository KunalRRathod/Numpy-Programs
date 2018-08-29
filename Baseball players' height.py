import pandas as pd
#any CSV data file
mlb = pd.read_csv(".csv")
height = mlb['Height'].tolist()

# Import numpy
import numpy as np

# Create a numpy array from height: np_height
np_height = np.array(height)

# Print out np_height
print(np_height)

# Convert np_height to m: np_height_m
#Multiply np_height with 0.0254 to convert all height measurements from inches to meters. Store the new values in a new array
np_height_m = np_height * 0.0254

# Print np_height_m
print(np_height_m)
