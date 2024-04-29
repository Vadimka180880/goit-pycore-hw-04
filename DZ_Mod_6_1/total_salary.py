def total_salary(path):
    total_salary = 0
    num_of_developers = 0 
    
    with open(path, 'r') as file: # Відкриваємо файл і зчитуємо рядки
        lines = file.readlines()
        
        for line in lines: # Проходимо крізь кожний рядок 
            try:                
                name, salary_str = line.strip().split(',') # Розділяємо рядок на прізвище та зарплату за комою
            except ValueError:
                print(f"Помилка: Недостатньо даних у рядку '{line.strip()}'")
                continue  # Пропускаємо цей рядок та переходимо до наступного
            
            try:  # Перетворюємо рядок у ціле число
                salary = int(salary_str)
            except ValueError:
                print(f"Помилка: Неправильний формат зарплати для рядка '{line.strip()}'")
                continue # Пропускаємо цей рядок та переходимо до наступного
            
            total_salary += salary # Додаємо зарплату до загальної суми

            num_of_developers += 1  # Збільшуємо лічильник розробників

        average_salary = total_salary / num_of_developers if num_of_developers > 0 else 0 # Розраховуємо середню зарплату

    return total_salary, average_salary

total, average = total_salary('salaries.txt')  # Приклад використання функції  
print(f'Total salary: {total}')
print(f'Average salary: {average}')

# На виході проводимо обрахунки, нівіть якщо у всіх працівників не вказана зарплата.