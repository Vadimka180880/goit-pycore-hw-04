def get_cats_info(path):
    cats_info = []                                                                # Створюємо порожній список для збереження інформації про котів

    try:                                                                          # Відкриваємо файл для читання        
        with open(path, 'r') as file:                                             # Проходимо через кожен рядок у файлі           
            for line in file:                                                     # Розділяємо рядок за комою                
                cat_data = line.strip().split(',')

                if len(cat_data) != 3:                                            # Перевіряємо, чи в рядку є всі необхідні дані
                    print(f"Помилка: неправильний формат рядка '{line.strip()}'")
                    continue                                                      # Пропускаємо цей рядок і переходимо до наступного
               
                try:                                                              # Спробуємо перетворити вік кота у число з плаваючою точкою
                    age = float(cat_data[2])
                    if age <= 0:
                        raise ValueError
                except ValueError:
                    print(f"Помилка: неправильне значення віку для кота у рядку '{line.strip()}'")
                    continue                                                      # Пропускаємо цей рядок і переходимо до наступного
                
                cat_info = {                                                      # Створюємо словник з інформацією про кота
                    'id': cat_data[0],
                    'name': cat_data[1],
                    'age': age
                }
                
                cats_info.append(cat_info)                                        # Додаємо словник до списку котів

    except FileNotFoundError:
        print(f"Помилка: файл '{path}' не знайдено")

    return cats_info

cats = get_cats_info('cats.txt')                                                 # Приклад використання функції
for cat in cats:
    print(cat)
# У прикладі бачимо повідомлення Помилка: неправильне значення віку для кота у рядку '60b90c1c13067a15887e1ae1,Tayson,-0.3', тому що вік кота не може бути від'ємним