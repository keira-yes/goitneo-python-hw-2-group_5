from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        if not (value.isdigit() and len(value) == 10):
            raise ValueError("Phone number must contain 10 digits")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, number):
        self.phones.append(Phone(number))

    def remove_phone(self, number):
        self.phones = [existing_phone for existing_phone in self.phones if existing_phone.value != number]

    def edit_phone(self, prev_phone, new_phone):
        for index, phone in enumerate(self.phones):
            if phone.value == prev_phone:
                self.phones[index] = Phone(new_phone)
                return
        return "No phone was found, add correct number please"

    def find_phone(self, number):
        for phone in self.phones:
            if phone.value == number:
                return phone.value
        return "No phone was found"

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        self.data.pop(name, None)