# 27.	Задайте строку из набора чисел. Напишите программу, 
# которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.

x = '1 3 5 7 9 15'
lst = [int(i) for i in x.split()]
Min = lst[0]
Max = lst[0]
for i in lst:
    if Min > i:
        Min = i
    for j in lst:
        if Max < j:
            Max = j
print(f'Минимальное число =  {Min}')
print(f'Максимальное число = {Max}')        
        
    


# print(len(lst))
# print(type(lst))      
 