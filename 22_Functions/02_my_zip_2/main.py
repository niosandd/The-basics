def my_zip(*arg):
    arg = list(map(list, arg))
    try:
        yield tuple(map(lambda x : x.pop(0), arg))
        yield from my_zip(*arg)
    except:
        pass
