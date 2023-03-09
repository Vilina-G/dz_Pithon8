print("""Задача 1. 
Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и выводить на печать
построчно последние строки в количестве lines (на всякий случай проверим, что задано положительное целое число).
Протестируем функцию на файле «article.txt» со следующим содержимым:
Вечерело
Жужжали мухи
Светил фонарик
Кипела вода в чайнике
Венера зажглась на небе
Деревья шумели
Тучи разошлись
Листва зеленела""")


def read_last(value_1: int, value_2: str):
    with open(value_2, 'r', encoding='utf-8') as file:
        text = file.read().splitlines()
        max = len(text)
        if value_1 > max:
            min = 0
            print('Не верно указано количество последних строк\n'
                  f'Будет выведен максимум в {max} строк\n'
                  )
        else:
            min = len(text) - value_1
        for e in range(min, max):
            print(text[e])
        print('\n')


file = input('Введите имя файла(article.txt): ')
lines = int(input('Сколько последних строк вывести: '))
if lines > 0 and file == 'article.txt':
    read_last(lines, file)
else:
    print('Неверно указаны последние строки')
