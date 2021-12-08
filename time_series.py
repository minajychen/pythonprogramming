#jiang-ying mina chen
#A Python module with class and function defintions for time series data (data that is tracked over time).

import numpy as np
from datetime import datetime
from matplotlib import pyplot as plt

class TimeSeries():
    def __init__(self,file):
        self.in_dates=(np.loadtxt(file,delimiter=',',skiprows=1,dtype=str,usecols=(0,1))).tolist()
        self.x=[]
        for combo in self.in_dates:
            self.x.append(combo[0]+" "+combo[1])
        self.y=(np.loadtxt(file,delimiter=',',skiprows=1,dtype=str,usecols=(2))).tolist()
        plt.title(file)
        plt.xlabel("time")
        plt.ylabel("number of sessions")
        plt.plot(self.x,self.y)
        plt.show()

        #for item in self.date:
            #d=datetime.strptime(item,'%B %Y')
           # self.x.append(d)
        #need to figure out how to plot timeseries data



t=TimeSeries("libraries wifi.csv")
print(t.date)