import matplotlib.pyplot as plt
import numpy as np
z=np.array(['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec'])
x = np.array([173,153,195,147,120,144,148,109,174,130,172,131])
plt.scatter(z,x,color="pink")

plt.xlabel("month of year",fontsize="18")
plt.ylabel("sales of segment")
plt.title(("sales data"))


z=np.array(['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec'])
y = np.array([189,189,105,112,173,109,151,197,174,145,177,161])
plt.scatter(z, y,color="y")

q=np.array(['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec'])
z = np.array([185,185,126,134,196,153,112,133,200,145,167,110])
plt.scatter(q,z,color="b")