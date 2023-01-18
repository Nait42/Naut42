#!/usr/bin/env python3

ListOfUsers = []
isRunning = True
num = 0
el = 0

class User:
    name = None
    age = int

    def __init__(self, name, age):
        self.name = str(name)
        self.age = int(age)
        print("Пользователь добавлен в список как: ", self.name, "| Age:", self.age, '.')

    def showdata(self):
        print("Пользователь №", el + 1, "-", self.name, "| Возраст:", self.age, '.')


while isRunning:
    print("Для добавления пользователя нажмите клавишу 'enter', для остановки введите 's' ")
    i = input()
    if i != "s":
        try:
            print('Введите ФИО:')
            Name = input("")
            print('Введите возраст:')
            Age = input()
            Spl = Name.split()
            NewPersonName = "".join((str(Spl[1])[0].title() + '.', str(Spl[2])[0].title() + '. ', str(Spl[0]).title()))
            #Строка переделывает ФИО в инициалы + фамилия, а также добавляет заглавные буквы(если пользователь ввёл прописные).
            Person = User(NewPersonName, Age)
            ListOfUsers.append(Person)
            num += 1
        except IndexError:
            print("ОШИБКА! - ФИО должно содержать 3 слова разделённых клавишей 'пробел'.")
        except ValueError:
            print("ОШИБКА! - Возраст необходимо ввести в формате числа, используя цифры.")
    else:
        isRunning = False
        print("Завершаем добавление новых пользователей.\n" )

print("Количество пользователей в списке:", len(ListOfUsers), "\n")

while el < num:
    ListOfUsers[el].showdata()
    el += 1
    print("_______________________________________________________")

print("Конец списка.\n")
print("End of the programme.")
