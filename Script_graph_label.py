import scipy.io as sio
import matplotlib.pyplot as plt
import numpy as np

data = sio.loadmat('/media/z3525831/Transcend/UNSW/DATA ADCP/CH100_nostructure.mat')

data_U = data['U']
data_V = data['V']
data_depthV = data['depthV']
data_t = data['t']
data_timeDV = data['timeDV']                      # We must define variables for each list key in the "data"                     
data_u25 = data['u25']                            # dictionary in order to be able to exploit them.
data_u55 = data['u55']
data_u90 = data['u90']
data_v25 = data['v25']
data_v55 = data['v55']
data_v90 = data['v90']


import datetime as dt
def matlab2datetime(matlab_datenum):
    day = dt.datetime.fromordinal(int(matlab_datenum))                       # Conversion of Matlab time data to  
    dayfrac = dt.timedelta(days=matlab_datenum%1) - dt.timedelta(days = 366) #'classic python time data.
    return day + dayfrac

# convert Matlab variable "t" into list of python datetime objects
py_t = [matlab2datetime(tval) for tval in t]


x = data_u25[0,:]
x2 = data_U[5,:]                #Creation of the first graph.
plt.plot(x2)
plt.plot(x)
plt.show()


x = data_u25[0,:]
x2 = data_U[5,:]                              #Creation of the secon graph, with label line.
plt.plot(x2,"r--", linewidth=5,label="U25")  #option for color, thickness, legend_name
plt.plot(x,label="U")
plt.xlabel("U25_velocity (m.s-1)")   # line for y_axi_label
plt.ylabel("Depth")                  # line for x_axi_label
plt.title("CH100 velocity data")     # line for title_label
plt.grid(True)                       # line for creat grid
plt.legend()                         # line for creat legend 
plt.show()




t = data_t[0,:]                #Creation of the third graph.
plt.plot(py_t,x)
plt.xlabel("Time")
plt.ylabel("U25_velocity (m.s-1)")
plt.title("CH100 velocity data")
plt.show()
