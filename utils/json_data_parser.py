import json
from models.Box import Box

def parse(file: str) -> list[Box]:
    """
    This function will parse a json file for input data.

    Argument:
        file: The path to file for parsing.

    Return:
        The list of boxes from the input file.
    """
    with open(file, 'r') as f:
        data = json.load(f)

    boxes = []
    for box in data["boxes"]:
        box_instance = Box(box['weight'], box['value'])
        boxes.append(box_instance)

    return boxes

