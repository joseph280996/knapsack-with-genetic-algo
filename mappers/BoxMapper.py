from models.Box import Box


def mapInputToBox(input: str) -> Box:
    values = input.strip('()').split(',')
    if len(values) != 2:
        raise ValueError("Input is in invalid form")

    weight, value = int(values[0].strip()), int(values[1].strip())
    return Box(weight, value)

