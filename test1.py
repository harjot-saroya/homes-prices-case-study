import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
train_file_path = 'C:\\Users\\harjo\\Desktop\\Personal Projects\\Home prices\\train.csv'
train_data = pd.read_csv(train_file_path)
print(list(train_data))
#Show Histogram
#sns.distplot(train_data['SalePrice'])
#plt.show()


#Check linear relationship between general living area and SalePrice
#var = 'GrLivArea'
#data = pd.concat([train_data['SalePrice'],train_data[var]],axis = 1)
#data.plot.scatter(x=var, y='SalePrice', ylim=(0,800000))
#plt.show()
#From observing the plot above we can clearly see a linear relationship between these two variables

#Check linear relationhip between salesprice and total basement square foot
#var = 'TotalBsmtSF'
#data =  pd.concat([train_data['SalePrice'],train_data[var]],axis = 1)
#data.plot.scatter(x=var,y='SalePrice',ylim = (0,800000))
#plt.show()
#From observation, we can see that there is a linear relationship between these two variables, however when we have a
#Basement square foor of 0, we can see that the price goes up which could mean that sale price is affected by other
#Factors

#Set up correlation matrix heatmap
corr = train_data.corr()
sns.heatmap(corr, xticklabels=corr.columns.values,
            yticklabels=corr.columns.values)
#plt.show()
#Strong correlation between saleprice and overallQual, YearBuilt,GarageArea,GarageCars,GrLivArea,1stFlrSF,TotalBsmtSF

print(corr.SalePrice)