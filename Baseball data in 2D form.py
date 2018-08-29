import pandas as pd
#Use any CSV file here
baseball = pd.read_csv(".csv")[['Height', 'Weight']].as_matrix().tolist()
# Import numpy package
import numpy as np

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the shape of np_baseball
print(np_baseball.shape)
