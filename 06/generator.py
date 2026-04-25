def make_generator(s):
    for i in s:
        yield i


def chunked(iterable, size):
    iterable = [i for i in iterable]
    index = 0
    gen = None

    while index < len(iterable):
        if gen is not None:
            for _ in gen:
                pass

        start_index = index
        chunk = iterable[index:index + size]
        index += len(chunk)
        answer_gen = make_generator(chunk)
        gen = answer_gen

        yield start_index, answer_gen