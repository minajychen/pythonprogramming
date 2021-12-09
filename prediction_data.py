#jiang-ying mina chen
#A Python module with class and function definitions for tabular data. 
# Each row is a sample and each column is a feature. Features are used to predict a target column
import numpy as np
from matplotlib import pyplot as plt
import scipy.stats as stats

class PredictionData():
    def __init__(self,file):
        self.medinc=(np.loadtxt(file,delimiter=',',skiprows=1,dtype=float,usecols=(0))).tolist()
        self.houseprice=(np.loadtxt(file,delimiter=',',skiprows=1,dtype=float,usecols=(8))).tolist()
        plt.scatter(self.houseprice,self.medinc)
        plt.title("California house prices vs. medium income")
        plt.xlabel('Housing prices')
        plt.ylabel('Medium income')
        plt.show()

    def standardize_data(self,data):
        #how do I standardize the target?
        return stats.zscore(data)

p=PredictionData("california house prices.csv")