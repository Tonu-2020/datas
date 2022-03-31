import numpy as np
import seaborn as SnS
arr1= np.arange(1,17).reshape(4,4)

print(arr1)
print("element of 1st and 2nd column in 2nd and 3 row\n",arr1[1:3,:2])
print("2nd and 3rd element of 1st row\n",arr1[:1,1:3])