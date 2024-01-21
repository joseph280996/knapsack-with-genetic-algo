current_idx = 1


class Box:
    """
    This class represent a box which has weight and value
    Properties:
        id: unique identifier for each boxes
        weight: the weight of the box
        value: the value that the box hold
    """

    def __init__(self, weight: int, value: int):
        global current_idx
        self.id = current_idx
        current_idx += 1
        self.weight = weight
        self.value = value
