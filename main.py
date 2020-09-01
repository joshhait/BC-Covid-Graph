import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from collections import Counter, OrderedDict
import datetime as dt
import io
import requests
import mplcursors

# get the csv data from the BC CDC website
url = 'http://www.bccdc.ca/Health-Info-Site/Documents/BCCDC_COVID19_Dashboard_Case_Details.csv'
s = requests.get(url).content
df = pd.read_csv(io.StringIO(s.decode('utf-8')))

#df = pd.read_csv("BCCovid.csv")

count = Counter([date for date in df['Reported_Date'].values])

ordered = OrderedDict(sorted(dict(count).items(), key=lambda t:t[0]))

dates = list(ordered.keys())

num_cases = list(ordered.values())

x_values = [dt.datetime.strptime(d, '%Y-%m-%d').date() for d in dates]

fig, ax = plt.subplots()
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=30))
bars = ax.bar(x_values ,num_cases)
plt.ylabel("Number of Cases per Day")
plt.title("Covid-19 cases in BC over time")
plt.grid(True, axis='y', linewidth=0.5)
plt.gcf().autofmt_xdate()

# Add hovering
cursor = mplcursors.cursor(hover=True)
mplcursors.cursor(bars)

plt.show()