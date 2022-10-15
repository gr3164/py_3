# Задача 2. В файле находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву.
# а –> абрикос, авокадо, апельсин, айва.

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




