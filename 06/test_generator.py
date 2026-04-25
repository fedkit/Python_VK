from generator import chunked


def test1():
    answer = []
    for first, chunk in chunked([1, 2, 3, 4, 5, 6, 7], 2):
        answer.append((first, list(chunk)))

    assert answer == [
        (0, [1, 2]),
        (2, [3, 4]),
        (4, [5, 6]),
        (6, [7])
    ]


def test2():
    answer = []
    for first, chunk in chunked([], 3):
        answer.append((first, list(chunk)))

    assert answer == []


def test3():
    answer = []
    for first, chunk in chunked([j for j in range(11)], 4):
        answer.append((first, list(chunk)))

    assert answer == [
        (0, [0, 1, 2, 3]),
        (4, [4, 5, 6, 7]),
        (8, [8, 9, 10])
    ]


def test4():
    def gen():
        for i in range(5):
            yield i

    answer = []
    for first, chunk in chunked(gen(), 2):
        answer.append((first, list(chunk)))

    assert answer == [
        (0, [0, 1]),
        (2, [2, 3]),
        (4, [4])
    ]


if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    print(b'rewfefver')