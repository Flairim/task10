class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, name):
        super().__init__(name)


class Phone(Field):
    def __init__(self, phone):
        super().__init__(phone)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def delete_phone(self, phone):
        for p in self.phones:
            if str(p) == phone:
                self.phones.remove(p)

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if str(p) == old_phone:
                p.value = new_phone

    def __str__(self):
        return f"Name: {self.name}, Phones: {', '.join(map(str, self.phones))}"


class AddressBook:
    def __init__(self):
        self.data = {}

    def add_record(self, record):
        key = str(record.name)
        if key not in self.data:
            self.data[key] = record

    def find_records(self, keyword):
        result = []
        for key, record in self.data.items():
            if keyword in key:
                result.append(record)
        return result

    def __str__(self):
        return "\n".join(map(str, self.data.values()))

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Invalid command format"

    return wrapper

@input_error
def add_contact(command, address_book):
    parts = command.split()
    name, phone = parts[1], parts[2]
    record = Record(name)
    record.add_phone(phone)
    address_book.add_record(record)
    return f"Added {name} with phone {phone}"

@input_error
def change_phone(command, address_book):
    parts = command.split()
    name, phone = parts[1], parts[2]
    records = address_book.find_records(name)
    if records:
        records[0].edit_phone(records[0].phones[0].value, phone)
        return f"Changed {name}'s phone to {phone}"
    else:
        return f"Contact {name} not found"

@input_error
def get_phone(command, address_book):
    name = command.split()[1]
    records = address_book.find_records(name)
    if records:
        return f"{name}'s phone is {records[0].phones[0].value}"
    else:
        return f"Contact {name} not found"

def show_all_contacts(command, address_book):
    if not address_book.data:
        return "No contacts in the book"
    return str(address_book)

def main():
    address_book = AddressBook()
    print("Bot assistant. Type 'hello' to start.")
    while True:
        user_input = input().strip().lower()
        if user_input in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        elif user_input == "hello":
            print("How can I help you?")
        elif user_input.startswith("add "):
            result = add_contact(user_input, address_book)
            print(result)
        elif user_input.startswith("change "):
            result = change_phone(user_input, address_book)
            print(result)
        elif user_input.startswith("phone "):
            result = get_phone(user_input, address_book)
            print(result)
        elif user_input == "show all":
            result = show_all_contacts(user_input, address_book)
            print(result)
        else:
            print("Invalid command. Type 'hello' to start or 'exit' to close.")

if __name__ == "__main__":
    main()
