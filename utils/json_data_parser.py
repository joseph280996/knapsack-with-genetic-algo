import json
from models.Box import Box

def parse(file: str):
    with open(file, 'r') as f:
        data = json.load(f)

    boxes = []
    for box in data["boxes"]:
        box_instance = Box(box['weight'], box['value'])
        boxes.append(box_instance)

    return boxes

