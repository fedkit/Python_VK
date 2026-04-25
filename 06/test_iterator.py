from iterator import ReverseIterator

def test1():
    answer = []
    for i in ReverseIterator('python'):
        answer.append(i)
    assert answer == ['n', 'o', 'h', 't', 'y', 'p']

def test2():
    answer = []
    for i in ReverseIterator([]):
        answer.append(i)
    assert answer == []

def test3():
    answer = []
    for i in ReverseIterator([j for j in range(11)], 4):
        answer.append(i)
    assert answer == [10, 6, 2]

def test4():
    def gen():
        for i in range(5):
            yield i

    answer = []
    for i in ReverseIterator(gen(), step=2):
        answer.append(i)

    assert answer == [4, 2, 0]


if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
