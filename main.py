from drugs import *
from client import *

k = 0
print("Введите пароль: ")
password = input()
if password == "1234":
    print("Доступ разрешен.")
    while k != 7:
            choise = int(input("Что хотите сделать?\n1.Добавить препарат\n2.Вывести список препаратов\n3.Продать препарат\n4.Добавить клиента в базу данных\n5.Найти информацию о клиенте\n6.Вывод всех клиентов\n7.Выход\n"))
            if choise == 1:
                print("Введите название препарата: ")
                name = input()
                print("Введите описание препарата: ")
                description = input()
                print("По рецепту?: ")
                prescription = input()
                print("Введите количество препарата: ")
                quantity = int(input())
                print("Введите цену препарата: ")
                price = int(input())

                pharmacy.add_medicine(name, description, prescription, quantity, price)

            elif choise == 2:
                print("Список препаратов:")
                pharmacy.get_all_medicines()

            elif choise == 3:
                print("Введите название препарата: ")
                name = input()
                print("Введите количество препарата: ")
                quantity = int(input())
                pharmacy.purchase_medicine(name, quantity)

            elif choise == 4:
                print("Введите фамилию клиента: ")
                surname = input()
                print("Введите номер клиента: ")
                phone_number = input()
                db.add_client(Client(surname, phone_number))

            elif choise == 5:
                print("Введите номер клиента: ")
                phone_number = input()
                # Поиск клиента по номеру телефона
                client = db.find_client_by_phone(phone_number)
                if client:
                    print(client)  # Выведет информацию о клиенте
                else:
                    print("Клиент не найден")

            elif choise == 6:
                # Вывод всех клиентов
                print("Все клиенты:")
                for c in db.get_all_clients():
                    print(c)


            elif choise == 7:
                k = 7
