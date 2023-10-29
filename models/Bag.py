from models.Box import Box

class Bag():
    """
    The class representation of the Bag that holds the boxes
    Properties:
        max_weight: The maximum weight that the bag can hold
        current_weight: The current weight of all the boxes in the bag
        total_value: The values of all the boxes in the bag
    """
    def __init__(self, max_weight: int):
        self.max_weight = max_weight
        self._current_weight = 0
        self._total_value = 0
        self.items = []

    @property
    def total_value(self):
        return self._total_value

    @property
    def current_weight(self):
        return self._total_value

    def add(self, box: Box):
        """
        Add a box into the bag and update the total weight and value of the bag

        Args:
            box: The box to add to the bag
        """
        if self.current_weight + box.weight > self.max_weight:
            raise ValueError("This box exceed the max weight permitted")

        self.items.append(box)
        self._current_weight += box.weight
        self._total_value += box.value
