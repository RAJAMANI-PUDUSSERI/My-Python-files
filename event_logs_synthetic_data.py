"""Creating Event Logs:
 Event logs are another useful script style, ideal for product analytics and workflow testing.
 Instead of one row per customer, you create one row per action."""

import csv
import random
from datetime import datetime, timedelta

filename = 'D:/My Python files/event_log.csv'
random.seed(42)

events = ["signup", "login", "view_page", "add_to_cart", "purchase", "logout"]

rows = []
start = datetime(2026, 1, 1)

for user_id in range(1, 201):
    event_count = random.randint(5, 30)
    current_time = start + timedelta(days=random.randint(0, 10))

    for _ in range(event_count):
        event = random.choice(events)

        if event == "purchase" and random.random() < 0.6:
            # round to 2 decimal places
            value = round(random.uniform(10, 300), 2)
        else:
            value = 0.0

        rows.append({
            "User_ID": f"USER{user_id:04d}",
            "Event_Time": current_time.isoformat(),
            "Event_Name": event,
            "Event_Value": value
        })

        current_time += timedelta(minutes=random.randint(1, 180))

with open(filename, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

print("Successfully saved event_log.csv")
