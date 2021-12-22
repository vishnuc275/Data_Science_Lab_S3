import matplotlib.pyplot as plt
import numpy as np


x = np.array(['MON','TUE','WED','THU','FRI'])
y = np.array([300,450,150,400,650])

plt.subplot(1, 2, 1)
plt.xlabel("days of week")
plt.ylabel("sales of drink")
plt.title("Sales Data1",loc='right')
plt.plot(x,y,':',color='c',marker='h',mfc='m',mec='b')


x = np.array(['MON','TUE','WED','THU','FRI'])
y = np.array([400,500,350,300,500])

plt.subplot(1, 2, 2)
plt.xlabel("days of week")
plt.ylabel("sales of food")
plt.title("Sales Data2",loc='center')
plt.plot(x,y,'--',color='y',marker='d',mfc='g',mec='r')

plt.show()
