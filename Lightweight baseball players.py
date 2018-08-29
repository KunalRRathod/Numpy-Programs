import pandas as pd
mlb = pd.read_csv("http://s3.amazonaws.com/assets.datacamp.com/course/intro_to_python/baseball.csv")
height = mlb['Height'].tolist()
weight = mlb['Weight'].tolist()

# height and weight are available as a regular lists

# Import numpy
import numpy as np
#Create a boolean numpy array: the element of the array should be True if the corresponding baseball player's BMI is below 21.

# Calculate the BMI: bmi
np_height_m = np.array(height) * 0.0254
np_weight_kg = np.array(weight) * 0.453592
bmi = np_weight_kg / np_height_m ** 2

# Create the light array
#  You can use the < operator for this.
light = bmi < 21
#Print out a numpy array with the BMIs of all baseball players whose BMI is below 21.

# Print out light
print(light)
#  Use light inside square brackets to do a selection on the bmi array
# Print out BMIs of all baseball players whose BMI is below 21
print(bmi[light])