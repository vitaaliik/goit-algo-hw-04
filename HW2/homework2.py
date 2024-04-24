def get_cats_info(path):
    cats_info = []  
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                cat_data = line.strip().split(',')  
                cat_info = {
                    "id": cat_data[0],
                    "name": cat_data[1],
                    "age": cat_data[2]
                }
                cats_info.append(cat_info)  
        return cats_info
    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
        return None 
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return None  

# Приклад використання:
cats_info = get_cats_info("HW2/cats.txt")
if cats_info is not None:
    print(cats_info)
