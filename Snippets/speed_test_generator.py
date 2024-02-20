'''Generator funtion for a simple speed test'''

from functools import wraps
from time import time

def speed_test(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        start_time = time()
        result = fn(*args,**kwargs)
        end_time = time()
        print(f'Executing {fn.__name__}')
        print(f'Time Elasped {end_time - start_time}')
        return result
    return wrapper

@speed_test
def num_sqaured(n):
    return n*n

print(num_sqaured(5))


