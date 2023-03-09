print("""Задача 3.
ДОП ЗАДАЧА.
Классическая задача про бассейн, который заполняется через 3 трубы, слишком проста. У нас труб будет больше.
Бассейн можно заполнить из N труб. В файле pipes.txt записаны времена заполнения всего бассейна только одной
данной работающей трубой (в часах). Затем после пустой строки перечислены трубы, которые будут заполнять бассейн.
Сколько минут на это потребуется?
Номер трубы соответствует номеру строки, в которой записана ее производительность.
Результат запишите в файл time.txt
Пример
Ввод
1
2
3
(пустая строка)
1 2 3
Вывод
32.72727272727273 """)


def pipes_task():
    with open('pipes.txt', encoding='utf-8') as file:
        time = file.read().split('\n')
    while all(time) is False:
        time.remove('')
    pipes = list(map(int, time[-1].split()))
    time.remove(time[-1])
    pipes = list(map(lambda x: x - 1, pipes))
    time = [time[pipe] for pipe in pipes]
    with open('time.txt', 'w', encoding='utf-8') as answer:
        answer.write(str(60 / sum(map(lambda x: 1 / float(x), time))))

    # f = open('pipes.txt', 'r')
    # f2 = open("time.txt", "w")
    # s = [line.rstrip() for line in f]
    # d = []
    # d1 = []
    # flag = 0
    # for i in s:
    #     if flag == 0:
    #         if i != '':
    #             d.append(eval(i))
    #         else:
    #             flag += 1
    #     else:
    #         s1 = i.split()
    #         for j in s1:
    #             d1.append(d[int(j) - 1])
    # f2.write(str(60 / sum([1 / i for i in d1])))
    # f2.close()
    # f.close()


pipes_task()
