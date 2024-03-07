"""Bot assistant that works with phone contacts"""
def input_error(func):
    """Error decorator"""
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."

    return inner

def parse_input(user_input):
    """Function analyzes user input and splits the command and arguments"""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    """Function adds new contacts in the contact dictionary"""
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    """Function checks if a contact is in contacts and substitutes the phone number"""
    name, phone = args
    if name in contacts.keys():
        contacts[name] = phone
        return "Contact updated."
    else:
        raise KeyError

@input_error
def show_phone(args, contacts):
    """Function checks if a contact is in contacts and prints user's phone number"""
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        raise KeyError

def show_all(contacts):
    """Function prints all contacts from the dictionary"""
    return contacts

def main():
    """Function communicates with the user and carries out commands"""
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
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

    print(contacts)

if __name__ == "__main__":
    main()
