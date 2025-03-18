import time


def time_it(func):

    def wrapper(*kargs, **kwargs):
        begin = time.time_ns()
        func(*kargs, **kwargs)
        elapse = (time.time_ns() - begin) // 1000
        print(f"func {func.__name__} took {elapse} ms to finish")

    return wrapper
