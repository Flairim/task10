from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)

class Name(Field):
    ...

class Phone(Field):
    def __init__(self, value):
        if len(value) == 10 and value.isdigit():
            super().__init__(value) 
        else:
            raise ValueError("Некоректний номер. Номер має містити 10 цифр")
    
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]
        
    def edit_phone(self, phone, new_phone):
        for i, p in enumerate(self.phones):
            if p.value == phone:
                self.phones[i] = Phone(new_phone)
                return None
        raise ValueError("This phone phone does not exist")
          
    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
            else:
                continue

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, contact:Record):
        name_value = contact.name.value
        if name_value not in self.data:
            self.data[name_value] = [contact]
        else:
            self.data[name_value].append(contact)

    def find(self, name:str):
        records = self.data.get(name)
        if records:
            return records[0]
        else:
            return None
        

    def delete(self, name):
        if name in self.data:
            self.data.pop(name)
        else:
            return ValueError(f"{name} is not exist")
