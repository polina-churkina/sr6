#Найти количество элементов в заданном массиве ARRAY, отличающихся от минимального на DELTA

n = int(input('Введите целое десятичное число, которое будет определять размер массива : '))
k = 0
ARRAY = []
for i in range(n):
    ARRAY.append(int(input('Введите следующий член массива: ')))
DELTA = int(input('Введите целое десятичное число DELTA: '))
minimum = ARRAY[1] 
for i in range(n):
    if (ARRAY[i] <= minimum):
        minimum = ARRAY[i]
a = minimum + DELTA
for i in range(n):
    if (ARRAY[i] == a):
        k = k+1
print(k)

   
