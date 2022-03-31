""" ДЗ10

"""
from collections import UserDict

class AdressBook(UserDict):

    def add_record(self,  rec):
        if isinstance(rec, Record):
            self.data.update({rec.name.value:rec})
        else:
            print("Добавить можно только объект класса Record")

    def del_record(self, rec):

            if isinstance(rec, Record):
                l1 = self.data.keys() # получили список ключей
                if rec.name.value in l1: # если такой есть то удаляем
                    self.data.pop(rec.name.value)
                else:
                    print("Нет записи с таким именем")
            else:
                print("Метод принимает только объект класса Record")

    
class Field():  
    pass

class Name(Field):

    def __init__(self, name):
        self.value = name

class Phone(Field):

    def __init__(self, phone):
        self.phone = phone
        

class Record():

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):

        if isinstance(phone, Phone) and phone is not None:
            self.phones.append(phone)
        else:
            print("Создайте номер как объект класса Phone")

    def del_phone(self):

        if len(self.phones) >= 1:
            self.phones.pop()       # удаляем последний объект с номером
            print("Номер удален")
        else:
            print("Список номеров пуст")

    def change_phone(self, phone):

        if isinstance(phone, Phone) and phone is not None:
            if len(self.phones) >= 1:
                self.phones[-1] = phone # редактируем последний объект с номером
                print("Номер изменен")
            else:
                print("Список номеров пуст")
        else:
            print("Создайте номер как объект класса Phone")


def main():
    print("ДЗ10")



if __name__ == "__main__":
    main()

"""
>>> Ivan = Record("Ivan")
>>> mob_Ivan = "0976875463"
>>> Ivan.add_phone(mob_Ivan)
Создайте номер как объект класса Phone
>>> mob_Ivan = Phone("0976758476")
>>> Ivan.add_phone(mob_Ivan)
>>> dom_Ivan = Phone("0445554433")
>>> Ivan.add_phone(dom_Ivan)
>>> Ivan.phones
[<__main__.Phone object at 0x0000000002E92850>, <__main__.Phone object at 0x0000000002E92940>]
>>> Ivan.phones[0].phone
'0976758476'
>>> Ivan.phones[1].phone
'0445554433'
>>> Ivan.del_phone()
Номер удален
>>> Ivan.phones
[<__main__.Phone object at 0x0000000002E92850>]
>>> mob1_Ivan = Phone("0987776655")
>>> Ivan.change_phone(mob1_Ivan)
Номер изменен
>>> Ivan.phones[0].phone
'0987776655'
>>> Tel_Book = AdressBook()
>>> Tel_Book.add_record(Ivan)
>>> Tel_Book
{'Ivan': <__main__.Record object at 0x0000000002E4F1F0>}
>>> Tel_Book.del_record(Ivan)
>>> Tel_Book
{}
>>> Tel_Book.add_record(Ivan)
>>> Tel_Book
{'Ivan': <__main__.Record object at 0x0000000002E4F1F0>}
"""
