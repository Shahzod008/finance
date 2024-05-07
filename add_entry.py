import uuid
from datetime import datetime

DATA_FILE = 'finance_data.json'


def add_entry_income(icnome):
    while True:
        try:
            cur = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            add_amount = int(input("Введите сумму: "))
            description = input("Введите описание: ")

            new_entry = (f"Дата и время: {cur}"
                         f"\nКатегория: {icnome}"
                         f"\nСумма: {add_amount}"
                         f"\nОписание: {description}")
            print(f"\nЗапись была добавлена успешно!\n\n{new_entry}")
            return new_entry
        except ValueError:
            print("Ошибка: Введено не число. Попробуйте снова. Введите только число.")
            add_entry()
            break


def add_entry():
    print("1. Доход")
    print("2. Расход")
    while True:
        try:
            choice = int(input("Выберите категорию (1/2): "))
            if choice == 1:
                add_entry_income("Доход")
            elif choice == 2:
                add_entry_income("Расход")
            break
        except ValueError:
            print("Некорректный ввод. Пожалуйста, выберите 1 или 2.")
