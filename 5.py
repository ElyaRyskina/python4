from functools import reduce
def my_func(el, el2):
    return(el * el2)

print(reduce(my_func, [el for el in range(100, 1001) if el%2==0]))
