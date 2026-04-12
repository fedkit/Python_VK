from process_json import process_json


# 1
keys = set()
process_json(
    '{"a": "x y", "b": "y z"}',
    None,
    ['y'],
    lambda k, t: keys.add(k)
)
assert keys == set()

# 2
json_str = '{"user1": "apple banana", "user2": "banana apple"}'
required_keys = ['user1', 'user2']
tokens = ['apple']
answer = []
process_json(json_str, required_keys, tokens, lambda k, t: answer.append((k, t)))
assert answer == [('user1', 'apple'), ('user2', 'apple')]

# 3
json_str = '{"a": "dog cat dog", "b": "cat dog"}'
required_keys = ['a', 'b']
tokens = ['dog', 'cat']
counter = {}
def counter_pair(k, t):
    if (k, t) in counter:
        counter[(k, t)] += 1
    else:
        counter[(k, t)] = 1
process_json(json_str, required_keys, tokens, counter_pair)
assert counter == {
    ('a', 'dog'): 2,
    ('a', 'cat'): 1,
    ('b', 'cat'): 1,
    ('b', 'dog'): 1
}

# 4
json_str = '{"a": "cat dog", "b": "dog cat"}'
required_keys = []
tokens = ['cat', 'dog']
called = False
def called_func(k, t):
    global called
    called = True
process_json(json_str, required_keys, tokens, called_func)
assert called is False

# 5
json_str = '''
{
    "harry_potter": "Harry Ron Hermione Harry",
    "lord_of_rings": "Frodo Sam Gandalf sauron",
    "game_of_thrones": "Jon Snow Arya Stark tyrion lannister"
}
'''
required_keys = ['harry_potter', 'lord_of_rings', 'game_of_thrones']
tokens = ['harry', 'gandalf', 'sauron', 'frodo', 'arya', 'TYRION']
answer = []
process_json(
    json_str,
    required_keys,
    tokens,
    lambda k, t: answer.append((k, t))
)
assert answer == [
    ('harry_potter', 'harry'),
    ('harry_potter', 'harry'),
    ('lord_of_rings', 'frodo'),
    ('lord_of_rings', 'gandalf'),
    ('lord_of_rings', 'sauron'),
    ('game_of_thrones', 'arya'),
    ('game_of_thrones', 'tyrion'),
]
