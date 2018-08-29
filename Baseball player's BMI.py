import pandas as pd
#any CSV file
mlb = pd.read_csv(".csv")
height = mlb['Height'].tolist()
weight = mlb['Weight'].tolist()

# Import numpy
import numpy as np
#Create a numpy array from the weight list with the correct units.
#  Multiply by 0.453592 to go from pounds to kilograms.
#  Store the resulting numpy array as np_weight_kg

# Create array from height with correct units: np_height_m
np_height_m = np.array(height) * 0.0254

# Create array from weight with correct units: np_weight_kg
np_weight_kg = np.array(weight) * 0.453592

# Calculate the BMI: bmi
bmi = np_weight_kg / np_height_m ** 2

# Print out bmi
print(bmi)
