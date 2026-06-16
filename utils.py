import json
import pandas as pd


def load_inventory():
    with open("data/inventory.json", "r") as f:
        data = json.load(f)
    return pd.DataFrame(data)


def load_trends():
    with open("data/trends.json", "r") as f:
        data = json.load(f)
    return pd.DataFrame(data)