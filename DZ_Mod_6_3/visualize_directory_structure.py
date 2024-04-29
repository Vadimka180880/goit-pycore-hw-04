import sys
from pathlib import Path
from colorama import init, Fore, Style

init()                                                                           # Ініціалізуємо colorama

def visualize_directory_structure(directory):    
    if not directory.is_dir():                                                   # Перевіряємо, чи існує директорія
        print(f"{Fore.RED}Error:{Style.RESET_ALL} Directory does not exist.")
        return   
    
    print(f"{Fore.BLUE}Directory: {directory}{Style.RESET_ALL}")                 # Виводимо назву директорії
        
    for item in directory.iterdir():                                             # Переглядаємо файли та піддиректорії в даній директорії
        if item.is_dir():
            print(f"{Fore.GREEN}Directory: {item.name}{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}File: {item.name}{Style.RESET_ALL}")

if __name__ == "__main__":     
    if len(sys.argv) != 2:                                                       # Перевіряємо, чи був переданий аргумент командного рядка
        print(f"{Fore.RED}Usage:{Style.RESET_ALL} python visualize_directory_structure.py <directory>")
    else:        
        directory_path = Path(sys.argv[1])                                       # Отримуємо шлях до директорії з аргументу командного рядка
        visualize_directory_structure(directory_path)
