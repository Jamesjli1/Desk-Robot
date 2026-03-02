import json
import os
import random

current_dir= os.path.dirname(__file__)
file_path = os.path.join(current_dir, "speech.json")


with open(file_path) as f:
    data = json.load(f)

speech = random.choice(data["study"])
print(speech)