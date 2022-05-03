from functools import lru_cache     # last recent used
import time


@lru_cache(maxsize=None)
def fibo(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


start = time.time()
print(fibo(5))
end = time.time() - start
print(f'{end} seconds')
