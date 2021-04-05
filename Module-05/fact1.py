
#By using for-loop

from memory_profiler import profile

@profile
def fact(n):
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product

print(fact(4))
# print(%timeit fact(4))
# print(%timeit fact(50))
