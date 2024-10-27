from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self,name):
        super().__init__(name)


class Phone(Field):
    def __init__(self, number):   
        super().__init__(self.__is_valid_number(number))
    
    def __is_valid_number(self, number):
        if len(number) != 10 and not number.isdigit():
            raise ValueError("Wrong phone number")
        
        return number
    
    def update_number(self, new_number):
        self.value = self.__is_valid_number(new_number)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


    def add_phone(self,phone):
        self.phones.append(Phone(phone))


    def edit_phone(self, old_phone, new_phone):
        phone = self.find_phone(old_phone)
        if phone:
            phone.update_number(new_phone)
            return
        
        raise ValueError("No such old phone")
    

    def find_phone(self, number):
        for phone in self.phones:
            if phone.value == number:
                return phone
            
        return None

        


class AddressBook(UserDict):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return f"Records {self.data}"

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name):
        if not self.data[name]:
            raise KeyError("Record not found")
        
        return self.data[name]

    def delete(self, name):
        if name not in self.data:
            raise KeyError(f"Record for name '{name}' not found")
        del self.data[name]

    


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

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")

for name, record in book.data.items():
    print(record)