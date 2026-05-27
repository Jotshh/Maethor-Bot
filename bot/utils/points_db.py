import json
import os

DB_PATH = 'data/points.json'

def load_points():
    if not os.path.exists(DB_PATH):
        return {}
    with open(DB_PATH, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def save_points(data):
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    with open(DB_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def add_points(user_id: int, amount: int):
    data = load_points()
    user_id_str = str(user_id)
    if user_id_str not in data:
        data[user_id_str] = 0
    data[user_id_str] += amount
    save_points(data)
    return data[user_id_str]

def remove_points(user_id: int, amount: int):
    data = load_points()
    user_id_str = str(user_id)
    if user_id_str not in data:
        data[user_id_str] = 0
    data[user_id_str] -= amount
    if data[user_id_str] < 0:
        data[user_id_str] = 0
    save_points(data)
    return data[user_id_str]

def get_points(user_id: int):
    data = load_points()
    user_id_str = str(user_id)
    return data.get(user_id_str, 0)
