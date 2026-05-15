class Node:
    def __init__(self, value=None):
        self.value = value  
        self.previous = None
        self.next = None


class DoubleLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.previous = self.head

    def add(self, node):
        node.previous = self.head
        node.next = self.head.next

        self.head.next.previous = node
        self.head.next = node

    def remove(self, node):
        prev_node = node.previous
        next_node = node.next

        prev_node.next = next_node
        next_node.previous = prev_node

    def pop(self):
        if self.tail.previous == self.head:
            return None

        last_node = self.tail.previous
        self.remove(last_node)
        return last_node


class LRUCache:
    def __init__(self, limit=42):
        self.limit = limit
        self.cache = {}
        self.list = DoubleLinkedList()

    def get(self, key):
        if key not in self.cache:
            return None

        node = self.cache[key]

        self.list.remove(node)
        self.list.add(node)

        return node.value[1] 

    def set(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = (key, value)

            self.list.remove(node)
            self.list.add(node)
        elif len(self.cache) >= self.limit:
            lru_node = self.list.pop()
            del self.cache[lru_node.value[0]]

            new_node = Node((key, value))
            self.cache[key] = new_node
            self.list.add(new_node)
        else:
            new_node = Node((key, value))
            self.cache[key] = new_node
            self.list.add(new_node)
