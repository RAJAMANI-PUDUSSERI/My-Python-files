# 1. GENERATING SIMPLE RANDOM DATA

import csv
import random
from datetime import datetime, timedelta
import os # Save in the same directory as the script - see the code below

random.seed(42)

countries = ["Canada", "UK", "UAE", "Germany", "USA"]
plans = ["Free", "Basic", "Pro", "Enterprise"]

def random_signup_date_old():
    start = datetime(2024,1,1)
    end = datetime(2026,1,1)
    delta_days = (end-start).days
    return (start + timedelta(days = random.randint(0, delta_days))).date().isoformat()

rows = []
for i in range(1,1001):
    age = random.randint(18,70)
    country = random.choice(countries)
    plan = random.choice(plans)
    monthly_spend = round(random.uniform(0,500),2)

    rows.append({
        "customer_id": f"CUST{i:05d}",
        "age": age,
        "country": country,
        "plan": plan,
        "monthly_spend":monthly_spend,
        "signup_date": random_signup_date_old()
        })

# Save in the same directory as the script
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "customers.csv")

with open(csv_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader() 
    writer.writerows(rows)

print(f"Successfully saved {csv_path}")

# since the previous code had some issues with saving (fixed with some script), the revised code is pasted below and is workibg fine without all the fuss

import csv
import random
from datetime import datetime, timedelta

random.seed(42)

countries = ["Canada", "UK", "UAE", "Germany", "USA"]
plans = ["Free", "Basic", "Pro", "Enterprise"]

def random_signup_date():
    start = datetime(2024,1,1)
    end = datetime(2026,1,1)
    delta_days = (end-start).days
    return (start + timedelta(days = random.randint(0, delta_days))).date().isoformat()

rows = []
for i in range(1,1001):
    age = random.randint(18,70)
    country = random.choice(countries)
    plan = random.choice(plans)
    monthly_spend = round(random.uniform(0,500),2)

    rows.append({
        "customer_id": f"CUST{i:05d}",
        "age": age,
        "country": country,
        "plan": plan,
        "monthly_spend":monthly_spend,
        "signup_date": random_signup_date()
    })

filename = 'D:/My Python files/customers_new.csv'
with open (filename, "w", newline="",encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader() 
    writer.writerows(rows)

print("Successfully saved customers_new.csv")

# Add controls to the script
import csv
import random

random.seed(42)

plans = ["Free", "Basic", "Pro", "Enterprise"]

def choose_plan():
    roll = random.random()
    if roll < 0.45:
        return "Free"
    if roll < 0.75:
        return "Basic"
    if roll < 0.93:
        return "Pro"
    return "Enterprise"

def generate_spend(age,plan):
    if plan == "Free":
        base = random.uniform(0,10)
    elif plan == "Basic":
        base = random.uniform(10,60)
    elif plan == "Pro":
        base = random.uniform(50,180)
    else:
        base = random.uniform(150,500)
    if age >= 40:
        base *= 1.15
    return round(base,2)

rows = []
for i in range(1,1001):
    age = random.randint(18,70)
    plan = choose_plan()
    spend = generate_spend(age,plan)

    rows.append({
        "customer_id" : f"CUST{i:05d}",
        "age" : age,
        "plan" : plan,
        "monthly_spend" : spend
    })

filename = 'D:/My Python files/controlled_customers.csv'
with open (filename, "w", newline="",encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader() 
    writer.writerows(rows)

print("Successfully saved controlled_customers.csv") 