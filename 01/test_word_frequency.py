from word_frequency import top_k_words

assert top_k_words("apple apple apple", 1) == [('apple', 3)]
assert top_k_words("a b c d a b c a", 3) == [('a', 3), ('c', 2), ('b', 2)]
assert top_k_words("red blue green red blue red", 2) == [('red', 3), ('blue', 2)]

test_text = """
В лесу родилась елочка,
В лесу она росла,
Зимой и летом стройная,
Зеленая была.
"""
assert top_k_words(test_text, 3) == [('лесу', 2), ('в', 2), ('стройная,', 1)]
