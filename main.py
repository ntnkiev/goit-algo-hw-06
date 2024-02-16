from collections import UserDict
import re

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        if not re.findall(r"\d{10}", value): #перевірка формату номеру телефону
            raise(Exception("Invalid phone number"))
        
class Record:
    def __init__(self, name):
        self.record = Name(name)
        self.name = Name(name) 
        self.phones = []
        # self.emails = []

    def add_phone(self, phone):
        try:
            self.phones.append(Phone(phone)) #додавання номера
        except Exception as e:
            print(e)

    def find_in_list(self, phone) -> int:
        for i in range(len(self.phones)):
            if self.phones[i].value == phone: #пошук номера в списку контакту та повертання його індексу
                return i
        return None

    def remove_phone(self, phone):
        i = self.find_in_list(phone)
        if i != None:
            del self.phones[i]
            print(f'Phone number {phone} was delated from {self.name.value} contact.')
        else:
            print(f"Phone {phone} not found in {self.name} contact")
        
    def edit_phone(self, old_phone, new_phone):
        i = self.find_in_list(old_phone)
        if i != None:
            self.phones[i].value = new_phone
            print(f"Phone number {old_phone} was changed to {new_phone}")
        else:
            print(f"Phone {old_phone} not found in {self.name} contact")

    def find_phone(self, phone):
        i = self.find_in_list(phone)
        if i != None:
            return phone   
        else: 
            print(f"Phone {phone} not found in {self.name} contact")

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record #додавання запису

    def find(self, name):
        if name in self.data: #пошук запису
            return self.data[name]
    
    def del_record(self, name):
        del self.data[name.name.value] #видалення запису
        print(f'The entry {name.name.value} was deleted')

if __name__ == "__main__":
		

    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    john_record.remove_phone("5555555555")
    # book.del_record(jane_record)

    for name, record in book.data.items():
        print(record)

    jane_record.find_phone('9876543210')

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    # book.delete("Jane")