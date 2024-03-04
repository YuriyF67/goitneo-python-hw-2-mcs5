from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, name):
        super().__init__(name)


class Phone(Field):
    def __init__(self, number):
        if len(number) == 10 and number.isdigit():
            super().__init__(number)
        else:
            print("Невірний формат номера телефону")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        phone = Phone(phone_number)
        self.phones.append(phone)

    def remove_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                self.phones.remove(phone)
            else:
                print(f"Номер телефону {phone_number} не знайдено.")

    def edit_phone(self, phone_number, new_phone):
        for phone in self.phones:
            if phone.value == phone_number:
                phone.value = new_phone
                return
            else:
                print(f"Номер телефону {phone_number} не знайдено.")

    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone.value

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(str(p) for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone, please."
        except KeyError:
            return "Give me name and phone, please."
        except IndexError:
            return "Give me name and phone, please."

    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_phone(args, contacts):
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return f"Phone number for {name} updated to {new_phone}."
    else:
        return f"Contact {name} not found."


@input_error
def get_phone(args, contacts):
    (name,) = args
    if name in contacts:
        return f"Phone number for {name}: {contacts[name]}"
    else:
        return f"Contact {name} not found."


@input_error
def get_all_contacts(contacts):
    phone_book = "Phone Book:\n"
    for name, phone in contacts.items():
        phone_book += f"{name}: {phone}\n"
    return phone_book


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_phone(args, contacts))
        elif command == "phone":
            print(get_phone(args, contacts))
        elif command == "all":
            print(get_all_contacts(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
