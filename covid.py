#%%time
import pandas as pd
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go
from datetime import date
import time
s = time.time()
today = date.today()
def load_data():
    start = time.time()
    print('Fetching data')
    df = pd.read_csv('https://covid.ourworldindata.org/data/ecdc/full_data.csv')
    print(f"Fetching complete in {round(time.time()-start, 2)}secs")
    filename = 'data/backups/COVID-19 '+str(today)+' backup.csv'
    df.to_csv(filename, index=False)
    print(f"{filename}, has been saved")
    return df
df = load_data()

df['date'] = pd.to_datetime(df['date'])
df['week'] = df['date'].dt.week

total_cases = df.groupby('location')['total_cases'].max().to_frame().reset_index().sort_values(by='total_cases', ascending=False)[1:26].reset_index(drop=True)
print('Generating Top 25 countries.html')
data = [go.Bar(x=total_cases['location'],
               y=total_cases['total_cases'])]
layout = go.Layout(title=f'Top 25 countries with COVID-19 confirmed cases on {today}',
                  xaxis=dict(title='Countries'),
                  yaxis=dict(title='Confirmed number of Cases'))
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='data/graphs/Top 25 countries.html')


print('Confirmed Cases scatter plot.html')
countries = ['United States', 'Brazil', 'India']
data = [go.Scatter(x=df['date'],
                   y=df[(df['location'] == country)]['total_cases'],
                   name=country,
                   mode='lines+markers') for country in countries]
layout=go.Layout(title=f'Confirmed Cases in {countries}',
                 xaxis=dict(title='Countries'),
                 yaxis=dict(title='Confirmed Cases'))
fig=go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='data/graphs/Confirmed Cases scatter plot.html')





print(f"Completed in {round(time.time()-s, 2)}")
