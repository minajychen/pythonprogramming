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
        self.y=(np.loadtxt(file,delimiter=',',skiprows=1,dtype=int,usecols=(2))).tolist()
        plt.title(file)
        plt.xlabel("time")
        plt.ylabel("number of sessions")
        plt.plot(self.x,self.y)
        #plt.plot(self.x,self.moving_average(self.y,3))
        #self.linear_reg_model2()
        #plt.plot(self.x,self.m * self.x + self.c, 'r', label='Fitted Line')
        plt.legend()
        plt.grid(True)
        plt.show()
        #look up how to reformat x axis label

    def moving_average(self,data,window_size=3):
        """function to compuate moving average"""
        #moving avg doesn't seem to work
        ret=np.cumsum(data,dtype=float)
        ret[window_size:]=ret[window_size:]-ret[:-window_size]
        return ret[window_size-1:]/window_size
    
    def linear_reg_model1(self):
        """Perform linear regression to compute β in order to attain the linear model: y¯ = βn"""
        #can you provide some tips on how to execute this using Numpy's linalg.lstsq?
        return

    def linear_reg_model2(self):
        """linear regression to fit the moving avg to a linear model y¯ = β0 + β1n."""
        #this doesn't work
        A=np.vstack([self.x,np.ones(len(self.x))]).T
        self.m, self.c = np.linalg.lstsq(A,self.y,rcond=None)[0]
        return self.m, self.c


t=TimeSeries("libraries wifi.csv")
