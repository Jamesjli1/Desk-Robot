<<<<<<< HEAD
import json
import os
import time

with open("timing.json") as f:
    data = json.load(f)

choice = input("Choose timer (pomodor/short_break/lng_break): ").lower()

if choice in data:
    seconds = data[choice]
    print(f"Starting {choice} timer ...")
    time.sleep(seconds)
    print("Time's up!")
else:
    print("Invalid choice.")

=======
def timer():
    print("Timer function is not implemented yet.")
>>>>>>> a86452c79f9394bf5ad745bd74251fc2cabda737
