def parse_input(user_input):
    parts = user_input.split()                                                      # Розбиваємо введений рядок на окремі частини    
    cmd = parts[0].lower()                                                          # Перший елемент - команда, переводимо його в нижній регістр
    args = parts[1:]                                                                # Решта елементів - аргументи команди
    return cmd, args

def add_contact(args, contacts):    
    if len(args) != 2:                                                              # Перевіряємо, чи передано два аргументи (ім'я та номер телефону)
        return "Invalid command. Please provide both username and phone number."    
    name, phone = args                                                              # Розділяємо аргументи на ім'я та номер телефону 
    contacts[name] = phone                                                          # Додаємо контакт до словника контактів
    return "Contact added."

def change_contact(args, contacts):    
    if len(args) != 2:                                                              # Перевіряємо, чи передано два аргументи (ім'я та новий номер телефону)
        return "Invalid command. Please provide both username and new phone number."    
    name, phone = args                                                              # Розділяємо аргументи на ім'я та новий номер телефону
    if name in contacts:                                                            # Перевіряємо, чи ім'я контакту є в словнику
        contacts[name] = phone                                                      # Змінюємо номер телефону для існуючого контакту
        return "Contact updated."
    else:
        return f"Contact '{name}' not found."

def get_phone(args, contacts):    
    if len(args) != 1:                                                              # Перевіряємо, чи передано один аргумент (ім'я контакту)
        return "Invalid command. Please provide username."    
    name = args[0]                                                                  # Отримуємо ім'я контакту з аргументів
    if name in contacts:                                                            # Перевіряємо, чи ім'я контакту є в словнику     
        return f"Phone number for {name}: {contacts[name]}"                         # Повертаємо номер телефону для зазначеного контакту
    else:
        return f"Contact '{name}' not found."

def get_all_contacts(contacts):    
    if not contacts:                                                                # Перевіряємо, чи словник контактів не є порожнім
        return "No contacts found."    
    result = "Contacts:\n"                                                          # Формуємо рядок з усіма контактами та їх номерами телефонів
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result

def main():    
    contacts = {}                                                                   # Ініціалізуємо словник контактів
    print("Welcome to the assistant bot!")
    while True:        
        user_input = input("Enter a command: ")                                     # Запитуємо користувача про команду     
        command, args = parse_input(user_input)                                     # Розбираємо введену команду на команду та аргументи
        
        if command in ["close", "exit"]:                                            # Обробляємо команди користувача
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_phone(args, contacts))
        elif command == "all":
            print(get_all_contacts(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

# Завдяки боту-помічнику, vи матимете зручний інструмент для управління нашими контактами. 
# Ми зможете додавати, змінювати та переглядати інформацію про контакти за допомогою простих команд. 
# Це дозволить нам ефективно організувати наш список контактів та швидко знаходити необхідну інформацію.




