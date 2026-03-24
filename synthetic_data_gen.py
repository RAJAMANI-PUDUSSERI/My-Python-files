# import csv
# import random
# from datetime import datetime, timedelta
# import os # Save in the same directory as the script - see the code below

# random.seed(42)

# countries = ["Canada", "UK", "UAE", "Germany", "USA"]
# plans = ["Free", "Basic", "Pro", "Enterprise"]

# def random_signup_date():
#     start = datetime(2024,1,1)
#     end = datetime(2026,1,1)
#     delta_days = (end-start).days
#     return (start + timedelta(days = random.randint(0, delta_days))).date().isoformat()

# rows = []
# for i in range(1,1001):
#     age = random.randint(18,70)
#     country = random.choice(countries)
#     plan = random.choice(plans)
#     monthly_spend = round(random.uniform(0,500),2)

#     rows.append({
#         "customer_id": f"CUST{i:05d}",
#         "age": age,
#         "country": country,
#         "plan": plan,
#         "monthly_spend":monthly_spend,
#         "signup_date": random_signup_date()
#         })

# # Save in the same directory as the script
# script_dir = os.path.dirname(os.path.abspath(__file__))
# csv_path = os.path.join(script_dir, "customers.csv")

# with open(csv_path, "w", newline="", encoding="utf-8") as f:
#     writer = csv.DictWriter(f, fieldnames=rows[0].keys())
#     writer.writeheader() 
#     writer.writerows(rows)

# print(f"Saved {csv_path}")

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

print("Saved customers_new.csv")