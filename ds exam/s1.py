import matplotlib.pyplot as plt
import numpy as np

plt.title("student mark")
plt.xlabel("total mark")
plt.ylabel("mark obtained")
x = np.array([10,20,30,40,50,60,70,80,90,100])
x1 = [38,62,18,75,38,59,66,92,52,75]
plt.scatter(x,x1, color = 'red', marker="*")

y = [74,44,85,19,88,69,50,33,29,32]

plt.scatter(x,y, marker="^")

plt.legend(["Maths", "English"], loc ="upper right")
plt.show()


 
