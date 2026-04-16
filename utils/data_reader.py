import json

def load_test_data(path="data/test_data.json"):
    with open(path) as f:
        return json.load(f)