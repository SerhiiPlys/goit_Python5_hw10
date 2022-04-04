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

    def __init__(self, phone = None):
        self.phone = phone
        

class Record(Name, Phone):

    def __init__(self, n:Name, p:Phone):
        self.name = n
        self.phone = p
        self.phones = []
        if isinstance(p, Phone) and (p.phone != None):
            self.phones.append(p)
        else:
            print(f"Создайте Phone(телефон) и воспользуйтесь методом add_phone")
        

    def add_phone(self, p:Phone):

        if isinstance(p, Phone) and (p.phone != None):
            self.phones.append(p)
        else:
            print("Создайте номер как объект класса Phone(телефон)")

    def del_phone(self, p:Phone):

        if len(self.phones) >= 1:
            if isinstance(p, Phone) and (p.phone != None):
                for i in self.phones:
                    del_nmb = False           #флаг найденного совпадения
                    if i.phone == p.phone:
                        self.phones.remove(i)
                        del_nmb = True
                        break
                if del_nmb == True:
                    print("Номер удален")
                else:
                    print("Совпадений с заданным номером не найдено")
            else:
                print("Метод принимает объект класса Phone")

        else:
            print("Список номеров пуст")

    def change_phone(self, p:Phone, pn:Phone):

        if (isinstance(p, Phone) and isinstance(pn, Phone) and
           (p.phone != None) and (pn.phone != None)):
            for i in self.phones:
                if i.phone == p.phone:
                    i.phone = pn.phone
                    print("Требуемый номер изменен")
                    break
                else:
                    print("Исходного номера не найдено, добавьте номер через метод add_phone")
        else:
            print("Создайте номер как объект класса Phone")


def main():
    print("ДЗ10")



if __name__ == "__main__":
    main()

"""
ДЗ10
>>> Ivan = Record(Name("Ivan"), Phone("0987776655"))
>>> p = Phone()
>>> p = Phone("0996665544")
>>> Ivan.add_phone(p)
>>> Ivan.phones
[<__main__.Phone object at 0x0000000002E3C610>, <__main__.Phone object at 0x0000000002E7E8E0>]
>>> for i in Ivan.phones:
	print(i.phone)

	
0987776655
0996665544
>>> Ivan.change_phone(Phone("0987776655"), Phone("0664443322"))
Требуемый номер изменен
>>> for i in Ivan.phones:
	print(i.phone)

	
0664443322
0996665544
>>> Ivan.del_phone(Phone("0987654"))
Совпадений с заданным номером не найдено
>>> Ivan.del_phone(Phone("0664443322"))
Номер удален
>>> for i in Ivan.phones:
	print(i.phone)

	
0996665544
>>> tlf = AdressBook()
>>> tlf.add_record(Ivan)
>>> tlf
{'Ivan': <__main__.Record object at 0x0000000002E7E220>}
>>> tlf.del_record(Ivan)
>>> tlf
{}
>>> 
"""
