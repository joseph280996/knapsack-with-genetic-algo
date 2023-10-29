from models.Box import Box

class Bag():
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
        if self.current_weight + box.weight > self.max_weight:
            raise ValueError("This box exceed the max weight permitted")

        self.items.append(box)
        self._current_weight += box.weight
        self._total_value += box.value
