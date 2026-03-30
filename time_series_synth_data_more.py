import csv
import random
from datetime import datetime, timedelta

filename = 'D:/My Python files/visits_timeseries_1.csv'
random.seed(42)
  
def apply_time_of_day_effects(base:int, hour:int):
    if 8 <= hour <= 11:          # Morning peak
        base += 60
    elif 12 <= hour <= 14:       # Lunch dip This subtracts 20 visits during lunch hours.
        base -= 20
    elif 18 <= hour <= 21:       # Evening bump
        base += 40
    elif 0 <= hour <= 5:         # Late-night lull
        base -= 30
    return base

def apply_weekend_effect(base:int, weekday:int):
    if weekday >= 5:             # Saturday, Sunday
        base = 80
    return base

def apply_seasonal_effects(base:int, ts):
    month = ts.month
    if month in [11, 12, 1, 2]:  # Winter boost
        base += 30
    elif month in [6, 7, 8]:     # Summer dip
        base -= 25
    return base

def apply_custom_patterns(base, hour, patterns):
    for p in patterns.values():
        start, end = p["range"]
        if start <= hour <= end:
            base += p["adjust"]
    return base

def compute_base(ts, custom_patterns=None):
    weekday = ts.weekday()
    hour = ts.hour
    base = 120
    base = apply_weekend_effect(base, weekday)
    base = apply_time_of_day_effects(base, hour)
    base = apply_seasonal_effects(base, ts)

    if custom_patterns:
        base = apply_custom_patterns(base, hour, custom_patterns)

    return base

start = datetime(2026,1,1,0,0)
hours = 24*30
custom_patterns = {
    "early_morning": {"range": (5, 7), "adjust": +15},
    "late_night": {"range": (22, 23), "adjust": -20},
    "lunch_dip": {"range": (12, 14), "adjust": -25},
}
rows = []

for i in range(hours):
    ts = start + timedelta(hours=i)
    visits = max(0, int(random.gauss(compute_base(ts),15))) # (mu: float = 0, sigma: float = 1) -> float, Gaussian distribution. mu is the mean, and sigma is the standard deviation. This is slightly faster than the normalvariate() function
    rows.append({
        "Time Stamp" : ts.isoformat(),
        "Visits" : visits
    })

with open(filename, "w", newline="", encoding = "utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["Time Stamp","Visits"]) # fieldnames=rows[0].keys()
    writer.writeheader()
    writer.writerows(rows)

print("Successfully saved visits_timeseries_1.csv ")