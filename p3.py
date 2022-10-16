# Задача 3. Создайте скрипт бота, который находит ответы на фразы по ключу в словаре. Бот должен, как минимум, отвечать на фразы «привет», «как тебя зовут». Если фраза ему неизвестна, он выводит соответствующую фразу.
# «как тебя зовут?» –> меня зовут Анатолий


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
f.close()



# while user != 'qwe':
#     f = open('text/bot_v0.1.txt','r+', encoding='utf-8')
#     if dictionary == {}:
#         dictionary2 = {"как тебя зовут": "меня зовут Анатолий", "привет": "Привет",}
#         for key, value in dictionary2.items():
#             f.writelines(f'{key}, {value}\n')
   
#     botstr = 'Бот: '

#     if user in dictionary:
#         print(botstr, dictionary[user])
#     elif user not in dictionary:
#         print(f'{botstr} Я не знаю что такое "{user}" Как мне на это ответить ?(Чтобы отклонить нажмите "=" ')
#         K = user.lower()
#         V = str(input().lower())
#         if V != "=":
#             if len(V) < 100 and len(V) != 0: f.writelines(f'{K},{V}\n')  
#     else:
#         print(botstr + "незнаю")
    
#     user = str(input('Вы: ').lower())
# print(dictionary)
