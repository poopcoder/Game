import json
import random

while True:
    inp = input("> ")
    ints = {}
    with open('intents.json', 'r') as f:
        json.dump(f, ints)
    try:
        if ints[inp].type() == list:
            val = random.choice(ints[inp])
        else:
            val = ints[inp]
        print(val)
    except:
        print("I don't understand.")