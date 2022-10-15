# Задача 1. Создайте файл. Запишите в него N первых элементов последовательности Фибоначчи.
# 6 –> 1 1 2 3 5 8

def fibanachi():
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

fibanachi()

# ==========================================================================================================================================================
# Задача 2. В файле находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву.
# а –> абрикос, авокадо, апельсин, айва.

def task2():
    date = open('text/p2.txt', 'r', encoding='utf-8')
    str1 = date.readlines()
    date.close()

    leeter = str(input("Напишите букву: "))

    def compare():
        str2 = []
        mylist = []

        for i in str1: str2.append(i.rstrip('\n'))

        for i in str2:
            if i[0].lower() == leeter.lower(): 
                mylist.append(i.lower())
            
        result = ', '.join(mylist)

        if mylist == [] or len(leeter) > 1:
            print("Ошибка!")
        else:
            print(leeter + " -> " , result)
    compare()

# task2()

# ==========================================================================================================================================================
# Задача 3. Создайте скрипт бота, который находит ответы на фразы по ключу в словаре. Бот должен, как минимум, отвечать на фразы «привет», «как тебя зовут». Если фраза ему неизвестна, он выводит соответствующую фразу.
# «как тебя зовут?» –> меня зовут Анатолий

def bot():
    print("Bot v0.1")
    print("Для выхода наберите: 'qwe'")

    user = str(input('Вы: ').lower())
    str2 = []
    dictionary = {}
    botstr = 'Бот: '

    while user != 'qwe':

        f = open('text/bot.txt','r+', encoding='utf-8')
        str1 = f.readlines()
    
        for i in str1: str2.append(i.rstrip('\n').split(','))
        for i in str2: dictionary[i[0]] = i[1]

        if user in dictionary: print(botstr, dictionary[user])
        elif user not in dictionary:
            print(f'{botstr} Я не знаю что такое "{user}" Как мне на это ответить ?(Чтобы отклонить нажмите "=" ')

            K = user.lower()
            V = str(input().lower())
            if V != "=":
                if len(V) < 100 and len(V) != 0: f.writelines(f'\n{K},{V}')  

        else: print(botstr + "незнаю")
        
        user = str(input('Вы: ').lower())

# bot()