#per capita income and population of the countries.

import pandas as pd
import plotly.express as px

#reading data from csv files
df= pd.read_csv("data.csv")

#Scatter plot is used to plot data points on a horizontal and a vertical axis in the attempt to show how much one variable is affected by another.
#scatter() method takes parameters such as the data, value for x and y, color and the size for the markers
fig = px.scatter(df, x ='Population'  , y ='Per capita' , color ='Country' , size ='Percentage', size_max= 60 )
fig.show()


#The different color markers show different countries.
#The size depended on the percentage of internet users.
