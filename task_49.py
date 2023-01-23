# Задача 49.
# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи (Например имя или фамилию человека)
# 4. Использование функций. Ваша прогрмма не должна быть линейной

# data = open('tel.txt','r+')
# data.writelines('Hello world' + '\n')
# print(data.readline())
# data.close()

import re
fileName = 'tel.txt'

def writeFile(file_name):
    with open(file_name, 'a+') as data:
        data.writelines("Hello world" + '\n')

def readFile(file_name):
    result = []
    with open(file_name, 'r+') as data:
        for line in data:
            result.append(line.split())
        return result

def findUsers(userList):
    name = 'Ivan,'
    for user in userList:
        if user[1] == name: 
            print(user[3])



with open('tel.txt') as data:
    lines = data.readlines()
pattern = re.compile(re.escape('Ivan'))
with open('tel.txt', 'w') as data:
    for line in lines:
        result = pattern.search(line)
        if result is None:
            data.write(line)



# writeFile(fileName)
# print(type(readFile(fileName)))
print(readFile(fileName))
findUsers(readFile(fileName))

