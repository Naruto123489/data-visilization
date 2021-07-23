#Bar Graph

#library for data manipulation and analysis
import pandas as pd

#library for data visualization
import plotly.express as px


#use a read_csv method provided by pandas to read the csv file and store the data in the df variable.
df = pd.read_csv("data.csv")

#Bar charts are a type of graph that are used to display and compare the number, frequency or other measure for different categories of data

fig = px.bar(df, x = 'Country' , y ='InternetUsers')
fig.show()

#The bar chart here shows number of internet users in each country
#China has mthe most number of internet users