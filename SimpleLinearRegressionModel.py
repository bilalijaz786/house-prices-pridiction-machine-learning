import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model

#Creating a instance of linear regression model
model=linear_model.LinearRegression()

#loading the excel data into data frame
df=pd.read_excel("D:\\Python projects\\homeprices.xlsx")

#Creating Scatter Plot
plt.xlabel("Area")
plt.ylabel("Prices")
plt.scatter(df.area,df.price,color="red",marker="+")
plt.show()

X=df.drop(columns="price")

#Training the model
model.fit(X,df.price) 
print(model.predict([[5000]])) #Testing the model