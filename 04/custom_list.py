class CustomList(list):
    def __init__(self, iterable=[]):
        super().__init__(iterable)

    def __eq__(self, other):
        return isinstance(other, CustomList) and sum(self) == sum(other)
    
    def __gt__(self, other):
        return isinstance(other, CustomList) and sum(self) > sum(other)

    def __ge__(self, other):
        return isinstance(other, CustomList) and sum(self) >= sum(other)
    
    def __lt__(self, other):
        return isinstance(other, CustomList) and sum(self) < sum(other)

    def __le__(self, other):
        return isinstance(other, CustomList) and sum(self) <= sum(other)

    def __ne__(self, other):
        return isinstance(other, CustomList) and sum(self) != sum(other)

    def __str__(self):
        return f'{list(self)}\nSum:{sum(self)}'
    
    def _append_zeroes(self, a, b):
        if len(a) > len(b):
            b = b + [0] * (len(a) - len(b))
        else:
            a = a + [0] * (len(b) - len(a))
        return a, b

    def __add__(self, other):
        if isinstance(other, int):
            return CustomList([i + other for i in self])

        if isinstance(other, CustomList):
            other = list(other)
        elif isinstance(other, list):
            other = other
        else:
            other = [other]

        a, b = self._append_zeroes(list(self), other)
        answer = []
        for i in range(len(a)):
            answer.append(a[i] + b[i])
        return CustomList(answer)

    def __radd__(self, other):
        if isinstance(other, int):
            return CustomList([other + i for i in self])

        if isinstance(other, CustomList):
            other = list(other)
        elif isinstance(other, list):
            other = other
        else:
            other = [other]

        a, b = self._append_zeroes(other, list(self))
        answer = []
        for i in range(len(a)):
            answer.append(a[i] + b[i])
        return CustomList(answer)

    def __sub__(self, other):
        if isinstance(other, int):
            return CustomList([i - other for i in self])

        if isinstance(other, CustomList):
            other = list(other)
        elif isinstance(other, list):
            other = other
        else:
            other = [other]

        a, b = self._append_zeroes(list(self), other)
        answer = []
        for i in range(len(a)):
            answer.append(a[i] - b[i])
        return CustomList(answer)

    def __rsub__(self, other):
        if isinstance(other, int):
            return CustomList([other - i for i in self])

        if isinstance(other, CustomList):
            other = list(other)
        elif isinstance(other, list):
            other = other
        else:
            other = [other]

        a, b = self._append_zeroes(other, list(self))
        answer = []
        for i in range(len(a)):
            answer.append(a[i] - b[i])
        return CustomList(answer)
