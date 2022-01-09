from itertools import cycle
my_list = [1, 2, 3, 5]
с = 0
for el in cycle(my_list):
    if с > 10:
        break
    print(el)
    с += 1

