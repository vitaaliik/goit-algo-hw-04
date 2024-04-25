def parse_input(user_input):
    parts = user_input.split()
    cmd = parts[0].strip().lower()
    args = parts[1:]
    return cmd, args

def add_contact(args, contacts):
    name, phone = args
    sss = input("Ви новий користувач? (yes/no): ").lower()
    for i in contacts:
        if name in contacts:
            name+='1'
    else:
        pass    
    if sss == "yes":
        contacts[name] = phone
        return "Contact added."
    elif sss == "no":
        if name not in contacts:
            return "Contact not found."
        else:
            print(change_contact(args, contacts))
    else:
        return "Invalid input."

    
    

def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact changed."
    

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "he":
            print("How can I help you?")    
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "all":
            for name, phone in contacts.items():
                print(f"{name}: {phone}")  
        elif command == "aaa":
            print(contacts)        
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()