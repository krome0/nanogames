import numpy as np

testarray = np.arange(16).reshape(4,4)

print(testarray)

testarray = np.rot90(testarray)

print(testarray)

testarray = np.rot90(testarray, -1)

print(testarray)