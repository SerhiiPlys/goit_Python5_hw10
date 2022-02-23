""" ДЗ10

"""
import os
from collections import UserDict

class AdressBook(UserDict):

    def add_record(self, contact, rec):
        self.data.update({contact:rec})
    
class Field():  
    pass

class Name(Field):
    
    def __init__(self, name):
        self.name = name

class Phone(Field):
    
    def __init__(self, phone):
        self.phone = phone

class Record(Name, Phone):

    def __init__(self, name, phone=''):
        self.name = Name(name)
        self.phone = []
        self.phone.append(Phone(phone))

    def add_phone(self, phone):
        self.phone.append(Phone(phone))

    def del_phone(self, phone):
        if len(self.phone) > 1:
            self.phone.pop()
            print("Номер удален")
        else:
            print("Список номеров пуст")

    def change_phone(self, phone):
        if len(self.phone) > 1:
            self.phone[-1] = phone # редактируем последний номер в списке
            print("Номер изменен")
        else:
            print("Список номеров пуст")
        

      
          


def main():
    print("ДЗ10")



if __name__ == "__main__":
    main()
