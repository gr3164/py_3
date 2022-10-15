# Задача 1. Создайте файл. Запишите в него N первых элементов последовательности Фибоначчи.
# 6 –> 1 1 2 3 5 8

date = open('text/p1.txt', 'w', encoding='utf-8')

def fib(N):
    n1 = 1
    n2 = 1
    str1 = "1 1"
    while (N-2) > 0:
        n_sum = n1 + n2
        n1 = n2
        n2 = n_sum
        str1 += (" " + str(n2))
        N-=1
    return str1

# N = int(input())
N = 6
date.write(str(N) + ' -> '+ fib(N))
date.close()