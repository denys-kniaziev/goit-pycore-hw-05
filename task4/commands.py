from textwrap import dedent

def input_error(func):
    """
    Decorator to handle input errors for bot command functions.
    
    Handles the following exceptions:
    - ValueError: When unpacking arguments fails or invalid values are provided
    - KeyError: When trying to access an item that doesn't exist
    - IndexError: When not enough arguments are provided
    
    Args:
        func: The function to decorate
        
    Returns:
        The decorated function with error handling
    """
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Invalid input. Please check your arguments."
        except KeyError:
            return "Item not found."
        except IndexError:
            return "Not enough arguments provided."
    
    return inner

def parse_input(user_input: str) -> tuple[str, list[str]]:
    """
    Parse user input into command and arguments.
    
    Args:
        user_input (str): The raw input string from the user.
        
    Returns:
        tuple[str, list[str]]: A tuple containing the command and a list of arguments.
    """
    # Handle empty input
    if not user_input.strip():
        return "", []
        
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


@input_error
def add_contact(args: list[str], contacts: dict[str, str]) -> str:
    """
    Add a new contact to the contacts dictionary.
    
    Args:
        args (list[str]): List containing name and phone number.
        contacts (dict[str, str]): Dictionary of contacts with names as keys and phone numbers as values.
        
    Returns:
        str: Status message.
    """
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args: list[str], contacts: dict[str, str]) -> str:
    """
    Change the phone number of an existing contact.
    
    Args:
        args (list[str]): List containing name and new phone number.
        contacts (dict[str, str]): Dictionary of contacts with names as keys and phone numbers as values.
        
    Returns:
        str: Status message.
    """    
    name, phone = args
    _ = contacts[name]  # This will raise KeyError if contact doesn't exist
    contacts[name] = phone
    return "Contact updated."


@input_error
def show_phone(args: list[str], contacts: dict[str, str]) -> str:
    """
    Show the phone number of a specific contact.
    
    Args:
        args (list[str]): List containing the name of the contact.
        contacts (dict[str, str]): Dictionary of contacts with names as keys and phone numbers as values.
        
    Returns:
        str: The phone number or an error message.
    """
    name = args[0]  # This will raise IndexError if args is empty    
    return contacts[name] # This will raise KeyError if contact doesn't exist


@input_error
def show_all(args: list[str], contacts: dict[str, str]) -> str:
    """
    Show all contacts and their phone numbers.
    
    Args:
        args (list[str]): Should be empty.
        contacts (dict[str, str]): Dictionary of contacts with names as keys and phone numbers as values.
        
    Returns:
        str: Formatted string of all contacts or message if no contacts.
    """
    if not contacts:
        return "No contacts saved."
    
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    
    return "\n".join(result)


def show_help() -> str:
    """
    Show help information with all available commands and their usage.
    
    Returns:
        str: Formatted help text with all commands
    """
    help_text = dedent("""
        Available commands:
        hello                    - Greet the bot
        add <name> <phone>       - Add a new contact
        change <name> <phone>    - Change existing contact's phone number
        phone <name>             - Show contact's phone number
        all                      - Show all contacts
        help                     - Show this help message
        exit/close               - Exit the program

        Examples:
        add John 1234567890
        change John 0987654321
        phone John
        all""")
    return help_text.strip()