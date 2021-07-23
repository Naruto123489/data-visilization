#Use line graph to compare the growth of per capita income in different countries

#library for data manipulation and analysis
import pandas as pd

#library for data visualization
import plotly.express as px


#use a read_csv method provided by pandas to read the csv file and store the data in the df variable.
df = pd.read_csv("line_chart.csv")

#Line charts are often used to see how the value of one parameter (y) changes compared to another parameter (x).
# one value which varies independently is called an independent variable (x)
#The other value which varies as the independent variable changes is called the dependent variable(y)

fig = px.line(df, x = 'Year' , y ='Per capita income', color = 'Country', title = 'Per Capita Income')
fig.show()

#The lines show drop and growth over the years indicating growth or drop in per capita income of the countries.
#Different colors indicate different countries
#On the x axis there are years plotted and on y axis we have the per capita income.
