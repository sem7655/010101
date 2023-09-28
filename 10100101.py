binary_number = input("Введите двоичное число: ")# запрашиваем вод

try:
    decimal_number = int(binary_number, 2)
    print("Десятичное представление:", decimal_number)
except ValueError:
    print("Введите корректное двоичное число.")
