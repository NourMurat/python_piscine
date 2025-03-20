# python_piscine/ex04/whatis.py
import sys


if __name__ == "__main__":
    # Проверяем количество аргументов (sys.argv[0] — имя скрипта)
    if len(sys.argv) == 1:
        exit()  # Ничего не выводим, если аргументов нет
    elif len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        exit()

    # Проверяем, является ли аргумент целым числом
    arg = sys.argv[1]
    try:
        num = int(arg)
    except ValueError:
        print("AssertionError: argument is not an integer")
        exit()

    # Проверяем чётность
    if num % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


