from commands import parse_input, show_help, add_contact, change_contact, show_phone, show_all

def main():
    """Main function that runs the assistant bot."""
    contacts = {}
    print("Welcome to the assistant bot!")
    
    try:
        while True:
            user_input = input("Enter a command: ")
            command, args = parse_input(user_input)
            
            match command:
                case "close" | "exit":
                    print("Good bye!")
                    break
                    
                case "hello":
                    print("How can I help you?")
                    
                case "help":
                    print(show_help())
                    
                case "add":
                    print(add_contact(args, contacts))
                    
                case "change":
                    print(change_contact(args, contacts))
                    
                case "phone":
                    print(show_phone(args, contacts))
                    
                case "all":
                    print(show_all(args, contacts))
                    
                case "":
                    continue  # Skip empty inputs
                    
                case _:
                    print("Invalid command. Type 'help' for available commands.")
    
    except KeyboardInterrupt:
        print("\nGood bye!")

if __name__ == "__main__":
    main()
