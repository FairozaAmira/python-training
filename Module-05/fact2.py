
from memory_profiler import profile

#By using if-else statement
@profile
def fact2 (n):
    if n == 0:
        return 1
    else:
        return n * fact2(n-1)

print(fact2(4))
# %timeit fact2(4)
# %timeit fact2(50)
