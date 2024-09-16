def add_everything_up(a, b):
    try:
        # Проверяем, что оба аргумента числа
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a + b
        # Проверяем, что оба аргумента строки
        elif isinstance(a, str) and isinstance(b, str):
            return a + b
        else:
            # Если типы разные, пытаемся привести к строке
            return str(a) + str(b)
    except Exception as e:
        # Обрабатываем любые другие исключения и выводим сообщение об ошибке
        return f"Произошла ошибка: {e}"

# Примеры использования функции
print(add_everything_up(123.456, 'строка'))  # Вывод: 123.456строка
print(add_everything_up('яблоко', 4215))     # Вывод: яблоко4215
print(add_everything_up(123.456, 7))          # Вывод: 130.456
print(add_everything_up([1, 2], (3, 4)))      # Вывод: [1, 2](3, 4) (разные типы)
