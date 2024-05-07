from add_entry import add_entry
import os

balance = 0


def main():
    print("1. Показать баланс")
    print("2. Добавить запись")
    print("3. Редактировать запись")
    print("4. Поиск по записям")
    choice = int(input("Выберите действие: "))

    match choice:
        case 1:
            print(f"\nВаш баланс: {balance}\n")
        case 2:
            add_entry()
        case 3:
            print("fr")
        case 4:
            print("wefre")


main()


def clear_cmd():
    os.system('cls' if os.name == 'nt' else 'clear')
