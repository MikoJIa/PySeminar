# 19.	Реализуйте алгоритм задания случайных чисел без использования 
# встроенного генератора псевдослучайных чисел.
#from time import time

#x = f'Введите число = {int(time() % 1 * 100)}')



# C = 9
# A = 2
# B = 3
# x = 1
# m = 10
# list = []
# for i in range(C):
#     x = (A * (i - 1) + B) % m
#     list.append(x)
# print(list)    
    
    
import time


def Random_Set(start = 0,end = 1):
    seconds = time.time()
    Next = True
    while Next:
        Rand = end * (seconds % 1)
        if Rand >= start or Rand > end: Next = False
        
    
    return int(Rand)

print(Random_Set(1,1000))
    