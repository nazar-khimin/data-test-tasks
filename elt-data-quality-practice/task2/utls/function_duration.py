import time


def timeit(func):
    """
    Decorator to measure execution time of functions.
    """

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start_time
        print(f"{func.__name__} executed in {elapsed:.4f} seconds")
        return result

    return wrapper
