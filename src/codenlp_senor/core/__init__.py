from functools import wraps
import time


def timeit(f):
    @wraps(f)
    def wrap(*args, **kw):
        t0 = time.perf_counter()
        result = f(*args, **kw)
        t1 = time.perf_counter()
        print(f"func:{f.__name__} took: {t1-t0:2.4f} sec")
        return result
    return wrap