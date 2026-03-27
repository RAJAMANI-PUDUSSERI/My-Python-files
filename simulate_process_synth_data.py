import csv
import random
from datetime import datetime, timedelta

filename = 'D:/My Python files/warehouse_sim.csv'

random.seed(42)

inventory = {
    "A" : 120,
    "B" : 80,
    "C" : 50
}

rows = []
current_time = datetime(2026,1,1)

for day in range(30):
    for product in inventory:
        daily_number_of_orders = random.randint(0,12)

        for _ in range(daily_number_of_orders):
            qty_ordered = random.randint(1,5)
            stock_before = inventory[product]

            if inventory[product] >= qty_ordered:
                inventory[product] -= qty_ordered
                status = "Order fulfilled"
            else:
                status = "Order not fulfilled"

            rows.append({
                "Time" : current_time.isoformat(),
                "Product" : product,
                "Stock_before" : stock_before,
                "Quantity" : qty_ordered,
                "Stock_after" : inventory[product],
                "Status" : status
            })

        if inventory[product] <20:
            restock = random.randint(30,80)
            inventory[product] += restock
            rows.append({
                "Time" : current_time.isoformat(),
                "Product" : product,
                "Stock_before" : inventory[product] - restock,
                "Quantity" : restock,
                "Stock_after" : inventory[product],
                "Status" : "Quantity restocked"
            })

    current_time += timedelta(days=1)

with open(filename, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

print("Successfully saved warehouse_sim.csv")