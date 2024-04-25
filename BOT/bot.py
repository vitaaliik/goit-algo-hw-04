# Декоратор для обробки помилок вводу користувача
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Invalid input format."

    return inner


# Функція для обробки вводу користувача та розбору команд
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


# Функція для додавання контакту
@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


# Функція для зміни контакту
@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact changed."
    else:
        return "Contact not found."


# Функція для отримання номеру телефону
@input_error
def your_number(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found." 
    

# Функція головного циклу бота
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
            print(change_contact(args, contacts))
        elif command == "all":
            for name, phone in contacts.items():
                print(f"{name}: {phone}")  
        elif command == "phone":
            print(your_number(args,contacts))              
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()