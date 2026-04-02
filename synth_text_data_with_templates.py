"""Generating Synthetic Text Data with Templates
 Synthetic data is also valuable for natural language processing (NLP).
 You do not always need an LLM to start; you can build effective text datasets using templates and controlled variation.
 For example, you can create support ticket training data:
"""
import json
import random

random.seed(42)
filename = 'D:/My Python files/support_tickets.jsonl'

issues = [("billing", "I was charged twice for my subscription"),
          ("loging", "I cannot log into my account"),
          ("shippint", "My order has not arrived yet"),
          ("refund", "I want to request for a refund"),
          ]

tones = ["Please help", "This is urgent", "Can you check this", "I need support"]

records = []

for _ in range(100):
    label, message = random.choice(issues)
    tone = random.choice(tones)

    text = f"{tone}, {message}."
    records.append({
        "Text" : text,
        "Label" : label
    })

with open(filename, "w", encoding="utf-8") as f:
    for item in records:
        f.write(json.dumps(item) + "\n")
print("Successfully saved support_tickets.jsonl")
