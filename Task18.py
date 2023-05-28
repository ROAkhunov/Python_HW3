# Задача 18: Требуется найти в массиве A[1..N] самый близкий по 
# величине элемент к заданному числу X. Пользователь в первой 
# строке вводит натуральное число N – количество элементов в 
# массиве. В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X
print('Введите количество элементов массива: ')
N=int(input())
x=6
A= list ()
for i in range(N):
    A.append(i+1)
print(*A)
print(x)
number=N
for i in range(len(A)):
    if A[i]>x:
        help=A[i]-x
    else:
        help=x-A[i]
    if help<number:
        number=A[i]
print(number)
