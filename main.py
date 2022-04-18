import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import pandas as pd
import csv

df=pd.read_csv("reading_time.csv")
data=df["reading_time"].tolist()
fig=ff.create_distplot([data],["reading time"],show_hist=False)
fig.show()

mean=statistics.mean(data)
std_deviation=statistics.stdev(data)
print("mean of population: ",mean)
print("standardDeviation of population: ",std_deviation)