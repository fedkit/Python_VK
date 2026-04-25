class ReverseIterator:
    def __init__(self, iterable, step=1):
        self.iterable = [i for i in iterable]
        self.step = step
        self.current_index = len(self.iterable) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index >= 0:
            value = self.iterable[self.current_index]
            self.current_index -= self.step
            return value
        raise StopIteration
