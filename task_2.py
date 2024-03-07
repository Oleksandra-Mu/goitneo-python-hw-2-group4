"""Module supplying classes for manipulating dictionaries"""
from collections import UserDict
class Field:
    "Parent class"
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    """class Name works with the contact name"""
    def __init__(self, name):
        super().__init__(name)
class Phone(Field):
    """class Phone works with the contact phone"""
    def __init__(self, phone):
        if len(phone) == 10:
            super().__init__(phone)
        else:
            print("Wrong phone number")
class Record:
    """class Record manipulates the contact phone number info"""
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    def add_phone(self, phone):
        """function adds contact's phone number to the list"""
        phone = Phone(phone)
        self.phones.append(phone)
    def remove_phone(self, check_phone):
        """function removes contact's phone number to the list"""
        for p in self.phones:
            if p.value == check_phone:
                self.phones.remove(p)
    def edit_phone(self, p, new_phone):
        """function edits contact's phone number in the list"""
        for p in self.phones:
            if p.value == new_phone:
                return "No need to edit"
            else:
                self.phones.append(new_phone)
                self.phones.remove(p)
    def find_phone(self, search_phone):
        """function searched and returns contact's phone number in the list"""
        for p in self.phones:
            if p == search_phone:
                return p
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    """class AddressBook works with the contact records"""
    def add_record(self, record):
        """function adds the record into the dictionary"""
        self.data[record.name.value] = record
    def find(self, name):
        """function searches the record in the dictionary"""
        for name in self.data:
            return self.data.get(name)
    def delete(self, name):
        """function deletes the record from the dictionary"""
        if name in self.data.keys():
            self.data.pop(name)
        else:
            return "Error"
        