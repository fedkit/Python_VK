from LRU import LRUCache


def test1():
    cache = LRUCache(limit=2)

    assert cache.get(1) is None
    assert cache.get('key!!!!!') is None


def test2():
    cache = LRUCache(limit=3)

    cache.set(10, 'vk')
    cache.set('x', 100)
    cache.set((1, 2), 'tuple')

    cache.get(10)
    cache.get('x')

    cache.set(67, [1, 2, 3])
    cache.set('x', 'updated')
    cache.set('new', 3.14)

    assert cache.get('x') == 'updated'
    assert cache.get((1, 2)) in ('tuple', None)
    assert cache.get(67) == [1, 2, 3]
    assert cache.get('new') == 3.14



def test3():
    cache = LRUCache(limit=2)

    cache.set(1, 11111)
    cache.set(2, 22222)

    cache.get(1)      
    cache.set(3, 33333)  

    assert cache.get(1) == 11111
    assert cache.get(2) is None
    assert cache.get(3) == 33333


def test4():
    cache = LRUCache(limit=2)

    cache.set(1, -10)
    cache.set(1, 999) 

    assert cache.get(1) == 999

    cache.set(2, -20)
    cache.set(3, -30)  

    assert cache.get(1) is None
    assert cache.get(2) == -20
    assert cache.get(3) == -30



if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()