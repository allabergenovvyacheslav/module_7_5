import os
import datetime

# Цель задания:
#
# Освоить работу с файловой системой в Python, используя модуль os.
# Научиться применять методы os.walk, os.path.join, os.path.getmtime, os.path.dirname, os.path.getsize и
# использование модуля time для корректного отображения времени.
#
# Задание:
#
# Создайте новый проект или продолжите работу в текущем проекте.
# Используйте os.walk для обхода каталога, путь к которому указывает переменная directory
# Примените os.path.join для формирования полного пути к файлам.
# Используйте os.path.getmtime и модуль time для получения и отображения времени последнего изменения файла.
# Используйте os.path.getsize для получения размера файла.
# Используйте os.path.dirname для получения родительской директории файла.

print('Текущая дериктория: ', os.getcwd())

# доступ к названиям и путям всех папок и файлов в каталоге (относительный путь)
for root, directories, files in os.walk('.'):
    for name in files:
        print(os.path.join(root, name))


test_path = '.'
# Нумерованный список (абсолютный путь), содержащий имена файлов и директорий в каталоге
result = sorted(os.listdir(test_path))
for i, j in enumerate(result):
    j = os.path.join(test_path, j)
    print(i + 1, j)

test_path = input('Введите адрес: ')
if os.path.exists(test_path):
    if os.path.isfile(test_path):
        print('Файл')
# для преобразования байтов в килобайты делим на 1024 (в мегабайты делим на 1048576)
        print('Размер: ', os.path.getsize(test_path) // 1024, 'Кб')
        print(f'Родительская директория {test_path}: ', os.path.dirname(test_path))
# datetime.fromtimestamp позволяет выводить время в местном формате
        print('Дата создания: ', datetime.datetime.fromtimestamp(
            int(os.path.getctime(test_path))
        ))
        print('Дата последнего открытия:', datetime.datetime.fromtimestamp(
            int(os.path.getatime(test_path))
        ))
        print('Дата последнего изменения:', datetime.datetime.fromtimestamp(
            int(os.path.getmtime(test_path))
        ))
    else:
        print('Объект не найден')


