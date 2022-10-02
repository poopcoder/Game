import json

while True:
    inp = input("> ")
    ints = {}
    with open('intents.json', 'r') as f:
        json.dump(f, ints)
    
    print()