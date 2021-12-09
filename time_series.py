#jiang-ying mina chen
#A Python module with class and function defintions for time series data (data that is tracked over time).

import numpy as np
from datetime import datetime
from matplotlib import pyplot as plt

class TimeSeries():
    def __init__(self,file):
        self.file=file
        self.in_dates=(np.loadtxt(file,delimiter=',',skiprows=1,dtype=str,usecols=(0,1))).tolist()
        self.x=[]
        for combo in self.in_dates:
            self.x.append(combo[0]+" "+combo[1])
        self.y=(np.loadtxt(file,delimiter=',',skiprows=1,dtype=int,usecols=(2))).tolist()
        plt.title(file)
        plt.xlabel("time")
        plt.ylabel("number of sessions")
        plt.plot(self.x,self.y)
        plt.grid(True)
        plt.show()
        #look up how to reformat x axis label

    def moving_average(self,y,m):
        """function to compuate moving average"""
        k=m//2
        i=k
        moving_averages=[]
        while i<len(y)-k-1:
            window=y[i-k:i+k+1]
            window_avg=sum(window)/m
            moving_averages.append(int(window_avg))
            i+=1
        return moving_averages
    
    def moving_average_plot(self,m):
        self.x_placeholder=self.x[m//2:-m//2+1]
        plt.title(self.file)
        plt.xlabel("time")
        plt.ylabel("number of sessions")
        plt.plot(self.x,self.y)
        plt.plot(self.x_placeholder,self.moving_average(self.y,m))
        plt.grid(True)
        plt.show()
        return

    def linear_reg_model1(self):
        """Perform linear regression to compute β in order to attain the linear model: y¯ = βn"""
        self.ordinal_x=[]
        for date in self.x:
            date=datetime.strptime(date,'%B %Y')
            self.ordinal_x.append(date.toordinal())
        self.ordinal_x=np.array(self.ordinal_x)
        x_transformed=self.ordinal_x[:np.newaxis]
        print(x_transformed)
        beta, _, _, _ = np.linalg.lstsq([x_transformed], np.array(self.y))
        plt.plot(self.x,self.y,'b_0')
        plt.plot(self.x,beta*self.ordinal_x,'r-')
        plt.show()
        return

    def linear_reg_model2(self):
        """linear regression to fit the moving avg to a linear model y¯ = β0 + β1n."""
        x_transformed=np.vstack([self.ordinal_x,np.ones(len(self.ordinal_x))]).T
        beta_1, beta_0 = np.linalg.lstsq(x_transformed,self.y,rcond=None)[0]
        plt.plot(self.x,self.y,'b_0')
        plt.plot(self.x,beta_1*self.ordinal_x+beta_0,'r-')
        plt.show()
        return 


t=TimeSeries("libraries wifi.csv")
