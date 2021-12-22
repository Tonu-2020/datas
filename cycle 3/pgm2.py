import numpy as np
import matplotlib.pyplot as plt

#plot1
x= np.array(['mon','tue','wed','thur','fri'])
y = np.array([300,450,150,400,600])
plt.subplot(2,1,1)
plt.plot(x,y,color ='cyan', linestyle='dotted',marker ='h' ,ms=20, mec="black", mfc ='m')
plt.grid(color ='green', linestyle='dotted')
plt.title("sales data 1",loc="right")
plt.xlabel("days of week")
plt.ylabel("drinks")

#plot2
x= np.array(['mon','tue','wed','thur','fri'])

y = np.array([400,500,350,300,500])
plt.subplot(2,1,2)
plt.plot(x,y,'.-y',marker = 'd',ms=20,mec='r',mfc='g')
plt.grid(color ='green', linestyle='dotted')
plt.title("sales data2",loc="right")
plt.xlabel("days of week")
plt.ylabel("foods")
plt.subplots_adjust(top=2.5,
                    bottom=1.5,
                    wspace=0.4,
                   hspace=0.4 )