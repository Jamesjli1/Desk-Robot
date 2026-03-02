import json
import os
import random

current_dir= os.path.dirname(__file__)
file_path = os.path.join(current_dir, "speech.json")


with open(file_path) as f:
    data = json.load(f)



emotions_inquiry = input("How are you feeling (sad/happpy/confident)?: ").lower()

if emotions_inquiry == "happy":
    print(random.choice(data["Happiness"]))
elif emotions_inquiry == "sad":
    print(random.choice(data["Sadness"]))
elif emotions_inquiry == "confident": 
    print(random.choice(data["Confidence"]))
else:
    print("I didn't quite understand that boi")