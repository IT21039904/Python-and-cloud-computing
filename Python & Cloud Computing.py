import numpy as np
import panda as pd
import sklearn 

from sklearn.datasets import load_boston
df = mload_boston()

df.keys()
print(df.DESCR)

boston =pd.DataFrame(df.data, columns=df.feature_names)
boston.head()

boston ['MEDV']= df.target
boston.head()

boston=pd.Dataframe(df.data, columns=df.feature_names)
boston.head()

boston['MEDV']=df.target
boston.head()

boston.isnull()
boston.isnull.sum()

from sklearn.model_selection import train_test_split
X= boston.drop ('MEDY', axis=1)
Y=boston ['MEDY']
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size = 0.15, random_state=5)

print(X_train.shape)
print(X_test.shape)
print(Y_train.shape)
print(Y_test.shape)

from sklearn. linear_model import LinarRegression
from sklearn.metrices import mean_squared_error

lin_model = LinearRegression()
lin_model.fit(X_train, Y_train)

y_train_predict= lin_model.predict(X_train)
rmse =(np.sqrt(mean_squared_error(Y_train, y_train_predict)))

print("The model performance for training set")
print('RMSE is {}'.format(rmse))
print("\n")

y_test_predict = lin_model.predict(X_test)

rmse= (np.sqrt (mean_squared_error(Y_test, y_test_predict)))

print("The model performance for testing set")
print('RMSE is {}'.format(rmse))

 import requests
#import os
from datetime import datetime

api_key = '87d845b0b6cf29baa1a73cc34b067a95'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')

print("====================================================")


# making a list so that i can print the info to a txt 
txtlist = [temp_city,weather_desc,hmdt,wind_spd,date_time]
#using open() buit-in function to write to a text file
with open("textfile.txt" , mode= 'w' ,encoding= 'utf-8') as f :     
                                     #encoding = utf-8 for linux and cp1252 for win
    f.write("------------------------------------------------------------- \n ")   
    f.write("Weather Stats for - {}  || {}".format(location.upper(), date_time))
    f.write("\n ------------------------------------------------------------- \n")
    f.write("Current temperature is: {:.2f} deg C\n".format(txtlist[0]))
    
    f.write("{},{} \n".format("Current weather desc  :" ,txtlist[1]))
    f.write("{},{},{} \n".format("Current Humidity      :",txtlist[2],"%"))
    f.write("{},{},{} \n".format("Current wind speed    :",txtlist[3],"kmph"))
    f.write("====================================================")