# Write a Pandas program to compare the elements of the two Pandas Series.
# Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 10]

import pandas as pd

series1 = pd.Series([2, 4, 6, 8, 10])
series2 = pd.Series([1, 3, 5, 7, 10])

print("Equal\n",series1==series2)

print("Greater\n",series1>series2)

print("Less\n",series1<series2)


