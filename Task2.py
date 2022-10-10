# 20.	Задайте список. Напишите программу, которая определит,
# присутствует ли в заданном списке строк некое число.
# x =int(input('Введите некое число = '))
# list = ['efkdmfmlk445', 'jdfid 94i epr0 0i00ii4u8nfjdf', 'fglk38877 098 mekweir3m']

# length = len(list)
# x = str(x)
# Flag = False
# for i in range (length):
#     if list[i].find(x) != -1 :
#         Flag = True
#         break
# print (Flag)

lst = ['efkdmfmlk445', 'jdfid 94i epr0 0i00ii4u8nfjdf', 'fglk38877 098 mekweir3m']
num = int(input('Введите число для проверки: '))
count = 0
for elem in lst:
    if str(num) in elem:
        count += 1
if count > 0:
    print ('Да, присутствует')
else:
    print ('Не присутствует')
    