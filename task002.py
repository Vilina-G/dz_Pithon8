print("""Задача 2.
Документ «article.txt» содержит следующий текст:
Вечерело
Жужжали мухи
Светил фонарик
Кипела вода в чайнике
Венера зажглась на небе
Деревья шумели
Тучи разошлись
Листва зеленела
Требуется реализовать функцию longest_words(file), которая выводит слово, имеющее максимальную длину
(или список слов, если таковых несколько).""")


def longest_words(file):
    with open(file, 'r', encoding='utf-8') as file:
        text = set(file.read().split())
        text = list(sorted(text, key=len, reverse=True))
        print(text[0])
        for i in range(1, len(text)):
            if len(text[0]) == len(text[i]):
                print(text[i])
            else:
                break


file = input('Введите имя файла: ')  # article.txt
longest_words(file)
