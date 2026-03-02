import json
import os
import random

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "joke.json")


with open(file_path) as f:
    data = json.load(f)

laugh = random.choice(data["funny_jokes"])
print(laugh)

