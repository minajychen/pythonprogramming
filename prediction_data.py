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
        plt.scatter(self.medinc,self.houseprice)
        plt.title("California medium income vs. housing prices")
        plt.xlabel('Medium income')
        plt.ylabel('Housing prices')
        plt.show()

    def standardize_data(self,data):
        """function that standardizes the data"""
        data=np.array(data)
        return (data-data.mean())/(data.std())
    
    def linear_reg_model1(self):
        """Perform linear regression to compute β in order to attain the linear model: y¯ = βn"""
        stnd_y=np.array(self.standardize_data(self.houseprice))
        stnd_x=np.array(self.standardize_data(self.medinc))
        x_transformed=stnd_x[:,np.newaxis]
        beta, _, _, _ = np.linalg.lstsq(x_transformed, stnd_y,rcond=None)
        plt.plot(x_transformed,stnd_y,'bo')
        plt.plot(x_transformed,beta*x_transformed,'r-')
        plt.show()
        return

    def linear_reg_model2(self):
        """linear regression to fit the moving avg to a linear model y¯ = β0 + β1n."""
        stnd_x=np.array(self.standardize_data())
        x_transformed=np.vstack([stnd_x,np.ones(len(stnd_x))]).T
        stnd_y=np.array(self.standardize_data(self.houseprice))
        beta_1, beta_0 = np.linalg.lstsq(x_transformed,stnd_y,rcond=None)[0]
        plt.plot(x_transformed,stnd_y,'bo')
        plt.plot(x_transformed,beta_1*x_transformed+beta_0,'r-')
        plt.show()
        return 

