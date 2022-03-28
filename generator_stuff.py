def gen1():
    yield 1
    yield 2
    yield 3
    return


def take(count: int, iterable):
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item


def no_duplicates(iterable):
    yielded = set()
    for item in iterable:
        if item in yielded:
            continue
        yielded.add(item)
        yield item