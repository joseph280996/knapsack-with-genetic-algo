from models.Box import Box


def mapInputToBox(input: str) -> Box:
    values = input.strip('()').split(',')
    if len(values) != 2:
        raise ValueError("Input is in invalid form")

    weight, value = int(values[0]), int(values[1])
    return Box(weight, value)

