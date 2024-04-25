def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            total_salary = 0
            for line in lines:
                name, salary = line.strip().split(',')
                total_salary += int(salary)
            average_salary = int(total_salary / len(lines))
            return total_salary, average_salary
    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {e}")

# Приклад використання коду:
total, average = total_salary("MODUL4/HW1/sal.txt")
if total is not None and average is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
