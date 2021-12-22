import matplotlib.pyplot as plt
import numpy as np
  

x = np.array([2001,2002,2003,2004,2005,2006,2007])
y = np.array([24000,22500,19700,17500,14500,10000,5700])
  
plt.plot(x, y,'-.',marker='*', mfc='g',mec='g', ms=20, color='r')
plt.xlabel("year")
plt.ylabel("car value")
plt.title("Value Depreciation",loc='left')
plt.show()