"""Generating Time Series Synthetic Data :
Synthetic data is not just limited to static tables.
Many systems produce sequences over time, such as app traffic, sensor readings, orders per hour, or server response times.
Here is a simple time series generator for hourly website visits with weekday patterns."""

import csv
import random
from datetime import datetime, timedelta
import math

filename = 'D:/My Python files/visits_timeseries.csv'
random.seed(42)

start = datetime(2026,1,1,0,0) 
hours = 24*30 # that many number of hours in 30 days
rows = []

for i in range(hours):
    time_series = start + timedelta(hours=i)
    weekday = time_series.weekday()

    base_visits = 120
    if weekday >= 5:
        base_visits = 80

    hour = time_series.hour
    if 8<= hour <=11: # if hour >= 8 and hour <= 11: # Morning peak
        base_visits += 60
    elif 12<= hour <=14: # Lunch dip This subtracts 20 visits during lunch hours.
        base_visits -= 20 
    elif 18<= hour <=21: # Evening bump
        base_visits +=40
    elif 0<= hour <=5: # Late-night lull
        base_visits -= 30

    seasonal = 20 * math.sin(2 * math.pi * (time_series.timetuple().tm_yday / 365)) # Smooth yearly seasonality- you can use a smooth sinusoidal pattern:This creates a natural up‑and‑down curve across the year.
    base_visits += seasonal
    
    visits = max(0, int(random.gauss(base_visits,15))) # (mu: float = 0, sigma: float = 1) -> float, Gaussian distribution. mu is the mean, and sigma is the standard deviation. This is slightly faster than the normalvariate() function

    rows.append({
        "Time Stamp" : time_series.isoformat(),
        "Visits" : visits
    })

with open(filename, "w", newline="", encoding = "utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["Time Stamp","Visits"]) # fieldnames=rows[0].keys()
    writer.writeheader()
    writer.writerows(rows)

print("Successfully saved visits_timeseries.csv ")

